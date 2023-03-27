#массив

from typing import Any

class Array:
    def __init__(self, n: int, dtype: Any):
        self.vals = [None] * n
        self.dtype = dtype

    def get(self, i: int) -> Any:
        return self.vals[i]

    def put(self, i: int, val: Any) -> None:
        if not isinstance(val, self.dtype):
            raise ValueError(f"val явл {type(val)}; должно быть {self.dtype}")
        self.vals[i] = val

arr = Array(10, str)
for i in range(10):
    arr.put(i,"ad")

for i in range(10):
    print(arr.get(i)) 
