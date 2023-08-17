#!/usr/bin/env python3
"""This module contains the class cache"""

import redis
import uuid
from functools import wraps
from typing import Callable, Optional


class Cache:
    """ The cache class"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str):
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str):
        return self.get(key, fn=int)


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        method_name = method.__qualname__
        self._redis.incr(method_name)
        return method(self, *args, **kwargs)
    return wrapper


Cache.store = count_calls(Cache.store)

cache = Cache()
