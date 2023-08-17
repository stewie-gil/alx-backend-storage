#!/usr/bin/env python3
"""This module contains the get_page function."""


import requests
import redis
from functools import wraps
from typing import Callable


def cache_result(method: Callable) -> Callable:
    """Decorator to cache results with expiration time."""
    @wraps(method)
    def wrapper(url):
        cached_result = cache.get(url)
        if cached_result is not None:
            return cached_result.decode()

        result = method(url)
        cache.setex(url, 10, result)
        cache.incr(f"count:{url}")

        return result
    return wrapper


def get_page(url: str) -> str:
    """Fetch HTML content from a URL using requests."""
    response = requests.get(url)
    return response.text


# Connect to the Redis server
cache = redis.Redis(host='localhost', port=6379, db=0)


if __name__ == "__main__":
    slow_url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://example.com"

    cached_get_page = cache_result(get_page)
    content = cached_get_page(slow_url)
    print(content)
