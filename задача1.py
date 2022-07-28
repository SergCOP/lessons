from typing import List

def my_range(stop: float, start=0.0, step=1.0) -> List[float]:
    result = []
    while start <= stop:
        result.append(start)
        start += step
    return result

print(my_range(stop=0.5, step=0.1))