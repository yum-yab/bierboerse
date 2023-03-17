from typing import TypeVar, Generic, List, Optional


T = TypeVar("T")


class CircularQueue(Generic[T]):
    def __init__(self, max_size: int, *initial_values: T) -> None:
        init_vals = list(initial_values)

        if len(init_vals) > max_size:
            init_vals = init_vals[:max_size]

        self.queue: List[T] = init_vals
        self.max_size: int = max_size

    def __dequeue(self) -> None:
        self.queue.pop(0)

    def put(self, obj: T) -> None:
        if len(self.queue) > self.max_size:
            self.__dequeue()

        self.queue.append(obj)

    def get(self) -> Optional[T]:
        """Get latest value"""

        if len(self.queue) > 0:
            return self.queue[-1]
        else:
            return None

    def get_content(self) -> List[T]:
        return self.queue
