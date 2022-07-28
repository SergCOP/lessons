from typing import Generator
  
def my_range(stop: float, start = 0.0, step = 1.0) -> Generator:
    while start < stop:
        yield start
        start += step

print(list(0, 0.5, 0.1))