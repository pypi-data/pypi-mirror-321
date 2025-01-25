import sys

from django33_ninja.constants import NOT_SET

__all__ = ["asynccontextmanager", "NOT_SET_TYPE"]

from contextlib import asynccontextmanager as asynccontextmanager

try:
    from django33_ninja.constants import NOT_SET_TYPE
except Exception:  # pragma: no cover
    NOT_SET_TYPE = type(NOT_SET)
