from decimal import Decimal
import random
from typing import List


def get_list_of_decimals(
    lower_bound: float, upper_bound: float, quantity: int
) -> List[Decimal]:
    result = []

    for _ in range(quantity):
        result.append(Decimal(random.uniform(lower_bound, upper_bound)))

    return result
