"""
LowKernels: A Python toolkit for creating low-level operating systems.

Modules:
- project: Functions to create and manage OS projects.
- builder: Functions to compile and build bootable OS images.
"""

from .project import create_project
from .builder import build_os

__all__ = ["create_project", "build_os"]

__version__ = "0.1.0"
__author__ = "LowKernels"
__license__ = "MIT"
