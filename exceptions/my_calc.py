from beartype import beartype
from typing import Union
@beartype
def sqrt(n: Union([float, int])):
    if n <= 0:
        raise ValueError(f"sqrt cannot recieve a negative"
                         f" number, and you sent {x}")
    x = n
    y = 1

    eps = 0.0000001
    while (x - y > eps):
        x = (x + y) / 2
        y = n / x

    return x
