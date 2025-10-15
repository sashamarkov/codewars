def lazy(n):
    def decorator(func):
        count = 0
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            should_run = (count - 1) % n == 0 if n > 0 else count % (-n) != 0
            return func(*args, **kwargs) if should_run else None
        return wrapper
    return decorator