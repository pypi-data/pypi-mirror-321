from __future__ import annotations

import functools
import inspect
from typing import Callable, Dict, Optional, Tuple


class Task:
    """The representation of a function within a Pipeline."""

    __slots__ = (
        "func",
        "branch",
        "join",
        "workers",
        "throttle",
        "multiprocess",
        "is_async",
        "is_gen"
    )

    def __init__(
            self,
            func: Callable,
            branch: bool = False,
            join: bool = False,
            workers: int = 1,
            throttle: int = 0,
            multiprocess: bool = False,
            bind: Optional[Tuple[Tuple, Dict]] = None):
        if not isinstance(workers, int):
            raise TypeError("workers must be an integer")
        if workers < 1:
            raise ValueError("workers cannot be less than 1")
        if not isinstance(throttle, int):
            raise TypeError("throttle must be an integer")
        if throttle < 0:
            raise ValueError("throttle cannot be less than 0")
        if not callable(func):
            raise TypeError("A task function must be a callable object")
        
        self.is_gen = inspect.isgeneratorfunction(func) \
            or inspect.isasyncgenfunction(func) \
            or inspect.isgeneratorfunction(func.__call__) \
            or inspect.isasyncgenfunction(func.__call__)
        self.is_async = inspect.iscoroutinefunction(func) \
            or inspect.isasyncgenfunction(func) \
            or inspect.iscoroutinefunction(func.__call__) \
            or inspect.isasyncgenfunction(func.__call__)
        
        if multiprocess:
            # Asynchronous functions cannot be multiprocessed
            if self.is_async:
                raise ValueError("multiprocess cannot be True for an async task")
            
            # The function needs to be globally accessible to be multiprocessed
            # This excludes objects like lambdas and closures
            # We capture these cases to throw a clear error message
            module = inspect.getmodule(func)
            if module is None or getattr(module, func.__name__, None) is not func:
                raise RuntimeError(f"{func} cannot be multiprocessed because it is not globally accessible"
                                   f" -- it must be a globally defined object accessible by the name {func.__name__}")
            
        self.func = func if bind is None else functools.partial(func, *bind[0], **bind[1])
        self.branch = branch
        self.join = join
        self.workers = workers
        self.throttle = throttle
        self.multiprocess = multiprocess
