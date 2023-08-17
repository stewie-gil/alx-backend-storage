#!/usr/bin/env python3
"""This module contains the class cache"""

import redis
import uuid
from functools import wraps
from typing import Callable

def call_history(method: Callable) -> Callable:
    """Decorator that stores input and output history"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        
        self._redis.rpush(input_key, str(args))
        
        result = method(self, *args, **kwargs)
        
        self._redis.rpush(output_key, result)
        
        return result
    return wrapper

def replay(method: Callable):
    """ Replay the calls of a specific method """
    m_name = method.__qualname__
    inputs = f"{m_name}:inputs"
    outputs = f"{m_name}:outputs"
    r = redis.Redis()

    data = r.get(m_name).decode("utf-8")
    inputs_list = r.lrange(inputs, 0, -1)
    outputs_list = r.lrange(outputs, 0, -1)

    print(f"{m_name} was called {data} times:")

    for k, v in zip(inputs_list, outputs_list):
        print(f"{m_name}(*{k.decode('utf-8')}) -> {v.decode('utf-8')}")

class Cache:
    """The cache class"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
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

