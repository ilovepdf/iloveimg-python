"""iloveimg package initialization."""

__version__ = "1.0.0"

from . import exceptions
from .compress_task import CompressTask
from .convert_task import ConvertTask
from .crop_task import CropTask
from .file import File
from .iloveimg_api import Iloveimg
from .removebackground_task import RemoveBackgroundTask
from .resize_task import ResizeTask
from .rotate_task import RotateTask
from .task import Task
from .upscale_task import UpScaleTask
from .watermark_task import WatermarkElement, WatermarkTask

__all__ = [
    "Iloveimg",
    "File",
    "Task",
    "CompressTask",
    "CropTask",
    "RemoveBackgroundTask",
    "UpScaleTask",
    "RotateTask",
    "ConvertTask",
    "ResizeTask",
    "WatermarkTask",
    "WatermarkElement",
    "exceptions",
]
