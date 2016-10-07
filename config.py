import os

try:
    import local_settings
except ImportError:
    local_settings = object


def get_config(key):
    return os.environ.get(key) if os.environ.get(key) is not None else getattr(
        local_settings, key, globals().get(key))
