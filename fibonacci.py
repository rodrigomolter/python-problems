from typing import Iterator

def main():
  SIZE = 10

  print("Classic Fibonacci resolution: ")
  print(*fibonacci(SIZE))

  print("\nRecursive Fibonnaci resolution: ")
  print(*fibonacci2(SIZE))

  print("\nPythonic Fibonacci resolution: ")
  print(*fibonacci3(SIZE))


""" Classic Fibonacci resolution """
def fibonacci(n: int) -> list:
  fib = [1, 1]
  for i in range(2, n):
    fib.append(fib[i-2] + fib[i-1])  
  return fib


""" Recursive Fibonnaci resolution """
def fibonacci2(n: int) -> list:
  fib = []
  for i in range(1, n+1):
    fib.append(fibonacci_recursive(i))
  return fib

def fibonacci_recursive(n: int) -> int:
  if n > 1:
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
  return n


""" Pythonic Fibonacci resolution """
def fibonacci3(n: int) -> Iterator[int]:
  a, b = 1, 1
  for _ in range(n):
    yield a
    a, b = b, a + b
  

if __name__ == "__main__":
  main()