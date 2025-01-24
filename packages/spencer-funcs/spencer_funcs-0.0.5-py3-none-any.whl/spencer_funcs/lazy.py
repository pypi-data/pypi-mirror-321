from typing import Callable, Any


def lazy_init(cls, *args, **kwargs):
    def f():
        return cls(*args, **kwargs)
    return LazyObject(f)


class LazyObject(object):
    def __init__(self, func: Callable[[], Any]):
        self._asdfghjkl_func = func
        self._asdfghjkl_data = None

    def _asdfghjkl_ensure_initd(self):
        if self._asdfghjkl_data is None:
            self._asdfghjkl_data = self._asdfghjkl_func()
        return self._asdfghjkl_data

    def __getattr__(self, item):
        if item.startswith("_asdfghjkl_"):
            return object.__getattribute__(self, item)
        self._asdfghjkl_ensure_initd()
        return object.__getattribute__(self._asdfghjkl_data, item)

    def __setattr__(self, key, value):
        if key.startswith("_asdfghjkl_"):
            object.__setattr__(self, key, value)
            return

        object.__setattr__(self._asdfghjkl_data, key, value)

    def __getitem__(self, item):
        self._asdfghjkl_ensure_initd()
        return self._asdfghjkl_data[item]

    def __call__(self, *args, **kwargs):
        self._asdfghjkl_ensure_initd()
        return self._asdfghjkl_data(*args, **kwargs)

    def __str__(self):
        self._asdfghjkl_ensure_initd()
        return self._asdfghjkl_data.__str__()

def raw_from_lazy(lazy: LazyObject):
    if lazy._asdfghjkl_data is None:
        return lazy._asdfghjkl_func()
    return lazy._asdfghjkl_data

