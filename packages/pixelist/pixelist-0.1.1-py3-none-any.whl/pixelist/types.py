from typing import Callable, List, Tuple, Union, Any, Optional
from typing_extensions import Annotated
from pydantic import BaseModel, PlainValidator, field_validator
from annotated_types import MinLen
from enum import Enum
from functools import wraps
import numpy as np
import inspect
from .features import check_feature


# Type definitions with runtime validation
NumpyArray = Annotated[
    np.ndarray,
    PlainValidator(lambda x: isinstance(x, np.ndarray) or ValueError("Must be numpy array"))
]

ValidImageList = Annotated[
    List[NumpyArray],
    PlainValidator(lambda x: len(x) > 0 or ValueError("Image list cannot be empty"))
]

ValidName = Annotated[
    str,
    PlainValidator(lambda x: len(x) > 0 or ValueError("Name cannot be empty"))
]

class ProcessingStatus(str, Enum):
    INTERMEDIATE = "intermediate"
    FINAL = "final"

class Filter:
    """
    Represents an image processing filter.
    
    Attributes:
        func (Callable): The actual filter function
        name (str): Name of the filter
        description (str, optional): Description of what the filter does
    """
    def __init__(self, func: Callable, name: Optional[str] = None, description: Optional[str] = None):
        self.func = func
        self.name = name or func.__name__
        self.description = description
        # Preserve the function's metadata
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

def filter_decorator(name: Optional[str] = None, description: Optional[str] = None):
    """
    Decorator for creating Filter objects from functions.
    """
    def decorator(func: Callable) -> Filter:
        if func.__name__ == '<lambda>' and not name:
            # Try to get the variable name it was assigned to
            frame = inspect.currentframe().f_back
            if frame:
                for var_name, var_val in frame.f_locals.items():
                    if var_val is func:
                        return Filter(func, name=var_name, description=description)
                return Filter(func, name=f"unknown_filter_{id(func)}", description=description)
        return Filter(func, name=name, description=description)
    return decorator

# Update type definitions
FilterType = Union[Filter, List[Filter], Tuple[Filter, ...]]

class ImageBatch(BaseModel):
    """
    A container for a batch of images and their processing history.

    Attributes:
        images (ValidImageList): List of numpy arrays representing images
        history (List[Filter]): List of filter functions applied to the images
    """
    images: ValidImageList
    history: List[Filter] = []

    class Config:
        arbitrary_types_allowed = True

class ImageSuperposition(BaseModel):
    """
    A collection of multiple ImageBatches representing parallel processing branches.

    Attributes:
        batches (List[ImageBatch]): List of image batches from different processing paths
    """
    batches: Annotated[
        List[ImageBatch],
        PlainValidator(lambda x: len(x) > 0 or ValueError("Must have at least one batch"))
    ]

class ProcessingResult(BaseModel):
    """
    Represents the result of a processing step in the pipeline.

    Attributes:
        step_name (ValidName): Name of the processing step
        result (Union[ImageBatch, ImageSuperposition]): Output of the processing step
        status (ProcessingStatus): Indicates if the result is intermediate or final
    """
    step_name: ValidName
    result: Union[ImageBatch, ImageSuperposition]
    status: ProcessingStatus

    class Config:
        arbitrary_types_allowed = True

def _filter_history_to_string(history: List[Filter]) -> str:
    """Convert a list of filters to a string representation."""
    return "\n".join(str(f) for f in history)

class ImagePipeline:
    """
    A pipeline for processing images through a sequence of filters.

    The pipeline supports sequential and parallel processing of images through
    various filter combinations using both single filters and filter groups.

    Attributes:
        filters (List): Collection of filter functions or filter groups
        results (List[ProcessingResult]): Results from processing steps
    """

    def __init__(self, filters: Optional[FilterType] = None):
        """
        Initialize the pipeline with optional filters.

        Args:
            filters (Optional[FilterType]): Initial filters to add
        """
        self.filters = []
        self.results: List[ProcessingResult] = []
        if filters:
            if not isinstance(filters, (list, tuple)):
                filters = [filters]
            self.filters.extend(filters)

    def add_filter(self, filter_or_sequence: FilterType):
        self.filters.append(filter_or_sequence)
        return self

    def _process_batch(self, batch: ImageBatch, filter_obj: Filter) -> ImageBatch:
        """
        Process a single batch of images through a filter function.

        Args:
            batch (ImageBatch): Batch of images to process
            filter_obj (Filter): Filter function to apply

        Returns:
            ImageBatch: Processed batch with updated history
        """
        processed_images = [filter_obj(img) for img in batch.images]
        return ImageBatch(
            images=processed_images,
            history=batch.history + [filter_obj]
        )

    def _process_step(self,
                     current: Union[ImageBatch, ImageSuperposition],
                     step: FilterType,
                     is_final: bool = False) -> Union[ImageBatch, ImageSuperposition]:
        """
        Process a single step in the pipeline, handling both sequential and parallel processing.

        Args:
            current (Union[ImageBatch, ImageSuperposition]): Current state of images
            step (FilterType): Processing step to apply
            is_final (bool): Whether this is the final processing step

        Returns:
            Union[ImageBatch, ImageSuperposition]: Processed results
        """
        if isinstance(step, (list, tuple)):
            # For parallel processing, create multiple branches
            if isinstance(step, tuple):
                results = []
                for filter_obj in step:
                    if isinstance(current, ImageBatch):
                        result = self._process_batch(current, filter_obj)
                    else:  # ImageSuperposition
                        result = ImageSuperposition(
                            batches=[self._process_batch(batch, filter_obj)
                                   for batch in current.batches]
                        )
                    results.append(result)

                # Combine results into a superposition
                if all(isinstance(r, ImageBatch) for r in results):
                    return ImageSuperposition(batches=results)
                else:
                    return ImageSuperposition(
                        batches=[batch for result in results
                                for batch in result.batches]
                    )

            # For sequential processing, process each step in sequence
            else:  # list
                for substep in step:
                    current = self._process_step(current, substep)
                return current

        elif isinstance(step, Filter):
            if isinstance(current, ImageBatch):
                return self._process_batch(current, step)
            else:  # ImageSuperposition
                return ImageSuperposition(
                    batches=[self._process_batch(batch, step)
                            for batch in current.batches]
                )

        else:
            raise ValueError(f"Invalid step type: {type(step)}")

    def run(self, images: Union[np.ndarray, List[np.ndarray]],
            store_intermediate: bool = True,
            show: bool = False) -> List[ProcessingResult]:
        """
        Run the pipeline with optional display of results.
        """
        if isinstance(images, np.ndarray):
            images = [images]
        initial_batch = ImageBatch(images=images, history=[])

        self.results = [
            ProcessingResult(
                step_name='"input"',
                result=initial_batch,
                status=ProcessingStatus.INTERMEDIATE
            )
        ]

        current = initial_batch
        for i, step in enumerate(self.filters):
            is_final = i == len(self.filters) - 1
            result = self._process_step(current, step, is_final)

            if isinstance(result, ImageBatch):
                step_name = _filter_history_to_string(result.history)
            else:  # ImageSuperposition
                paths = [_filter_history_to_string(batch.history) for batch in result.batches]
                quoted_paths = [f'"{paths[0]}"'] + paths[1:]  # Quote first branch
                step_name = " | ".join(quoted_paths)

            if store_intermediate or is_final:
                self.results.append(
                    ProcessingResult(
                        step_name=step_name,
                        result=result,
                        status=ProcessingStatus.FINAL if is_final
                               else ProcessingStatus.INTERMEDIATE
                    )
                )

            current = result

        if show:
            display_dict = _convert_results_to_display_dict(self.results)
            display_images(display_dict)

        return self.results

    @classmethod
    def make(cls,
             images: Union[np.ndarray, List[np.ndarray]],
             filters: FilterType,
             show: bool = True,
             store_intermediate: bool = True) -> List[ProcessingResult]:
        """
        One-line convenience method to create pipeline, process images and optionally display results.

        Args:
            images (Union[np.ndarray, List[np.ndarray]]): Images to process
            filters (FilterType): Filters to apply
            show (bool): Whether to display the results
            store_intermediate (bool): Whether to store intermediate results

        Returns:
            List[ProcessingResult]: List of processing results
        """
        pipeline = cls(filters)
        return pipeline.run(images, store_intermediate=store_intermediate, show=show)

def _convert_results_to_display_dict(results: List[ProcessingResult]) -> dict:
    """
    Convert processing results to a format suitable for display.

    Args:
        results (List[ProcessingResult]): List of processing results

    Returns:
        dict: Dictionary mapping step names to their corresponding images
    """
    display_dict = {}
    for result in results:
        if isinstance(result.result, ImageBatch):
            key = _filter_history_to_string(result.result.history) if result.result.history else 'input'
            display_dict[key] = result.result.images
        else:  # ImageSuperposition
            for i, batch in enumerate(result.result.batches):
                path = _filter_history_to_string(batch.history) if batch.history else "input"
                key = f'{path}' if i == 0 else path  # First branch gets quotes
                display_dict[key] = batch.images
    return display_dict

@check_feature("display", ["matplotlib", "cv2"])
def display_images(image_dict):
    """
    Display multiple images in a grid layout with proper labeling.

    Args:
        image_dict (dict): Dictionary where keys are image labels and values are lists of images.
            Images should be numpy arrays in either BGR or grayscale format.
    """

    import matplotlib.pyplot as plt
    import cv2

    num_rows = len(image_dict)
    num_cols = len(list(image_dict.values())[0])
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, num_rows * 3))
    fig.suptitle('Image Processing Results', fontsize=16)

    if num_rows == 1:
        axes = axes.reshape(1, -1)

    row_index = 0
    for image_type, images in image_dict.items():
        for col_index, img in enumerate(images):
            if len(img.shape) == 3:
                axes[row_index, col_index].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            else:
                axes[row_index, col_index].imshow(img, cmap='gray')
            # Add more vertical space for multiline labels
            axes[row_index, col_index].set_title(f'{image_type}', pad=15)
            axes[row_index, col_index].axis('off')
        row_index += 1

    # Add more spacing between subplots for the multiline labels
    plt.tight_layout(h_pad=2.0)
    plt.show()

