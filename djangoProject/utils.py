def str_to_bool(value: str) -> bool:
    if value is None:
        return None
    return value.strip().lower() in ("1", "true", "yes", "on")