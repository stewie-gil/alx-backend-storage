#!/usr/bin/env python3
"""This module contains the class Cache"""

import redis
import uuid
from functools import wraps
from typing import Callable, Optional, Any, Union, List

def call_history(method: Callable) -> Callable:
    """Decorator that stores input and output history"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function for call_history decorator"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        
        self._redis.rpush(input_key, str(args))
        
        result = method(self, *args, **kwargs)
        
        self._redis.rpush(output_key, result)
        
        return result
    return wrapper

def replay(func: Callable) -> None:
    """Replay the history of calls for a given function"""
    method_name = func.__qualname__
    inputs = cache._redis.lrange(f"{method_name}:inputs", 0, -1)
    outputs = cache._redis.lrange(f"{method_name}:outputs", 0, -1)
    
    print(f"{method_name} was called {len(inputs)} times:")
    for input_args, output in zip(inputs, outputs):
        print(f"{method_name}{input_args.decode()} -> {output.decode()}")

class Cache:
    """The Cache class"""

    def __init__(self) -> None:
        """Initialize the Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data and return a key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Any]] = None) -> Any:
        """Retrieve data by key and optionally apply conversion function"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Retrieve data as a string"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieve data as an integer"""
        return self.get(key, fn=int)
