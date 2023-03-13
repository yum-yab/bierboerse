from typing import TypeVar, Generic, List, Optional


T = TypeVar('T')


class CircularQueue(Generic[T]):

    def __init__(self, max_size: int, initial_values: Optional[List[T]] = None) -> None:
        
        if initial_values is None:
            initial_values = []
        elif len(initial_values) > max_size:
            initial_values = initial_values[:max_size]
        

        self.queue: List[T] = initial_values
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
