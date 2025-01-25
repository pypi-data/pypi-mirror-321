from typing import Union, Optional, List

from .aws import (
    s3_write,
    s3_read,
    s3_read_to_string,
    s3_copy,
    s3_list_objects,
    s3_delete_objects
)

__version__ = "0.1.0"

__all__ = [
    "s3_write",
    "s3_read",
    "s3_read_to_string",
    "s3_copy", 
    "s3_list_objects",
    "s3_delete_objects"
]