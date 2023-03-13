from utils.FixedLengthQueue import CircularQueue

from typing import List, Optional

class Stock:
    """A stock represents one traced thing"""

    def __init__(self, name: str, history_length: int, initial_values: Optional[List[float]] = None) -> None:
        
        self.queue = CircularQueue(max_size=history_length, initial_values=initial_values)
        
        self.name = name


        

