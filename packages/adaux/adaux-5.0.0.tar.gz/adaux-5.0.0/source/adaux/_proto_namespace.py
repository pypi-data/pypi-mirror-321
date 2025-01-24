# Copyright (c) 2021-2025 Mario S. Könz; License: MIT
import collections
import typing as tp

# py38 workaround
if tp.TYPE_CHECKING:
    # we use OrderedDict explicitly for readability
    # and we use move_to_end
    OrderedDict = tp.OrderedDict[str, tp.Any]
else:
    OrderedDict = collections.OrderedDict


class _ProtoNamespace(OrderedDict):  # pylint: disable=too-many-instance-attributes
    def __setattr__(self, key: str, val: tp.Any) -> None:
        if key in ["data"]:
            return super().__setattr__(key, val)

        return self.__setitem__(key, val)

    def __getattr__(self, key: str) -> tp.Any:
        if key.startswith("__"):
            raise AttributeError(key)
        return self.__getitem__(key)

    def __delattr__(self, key: str) -> tp.Any:
        return self.__delitem__(key)

    def __repr__(self) -> str:
        res = []
        for key, val in self.items():
            res.append(f"{repr(key)}: {repr(val)}")
        return "{" + ", ".join(res) + "}"

    def insert_after(self, prev_key: str, key: str, val: tp.Any) -> None:
        self[key] = val
        keys = list(self.keys())
        idx = keys.index(prev_key)
        for move_key in keys[idx + 1 : -1]:
            self.move_to_end(move_key)
