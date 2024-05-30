def main():
  
  print("Classic Fibonacci resolution: ")
  print(*fibonacci(10))

  print("\nRecursive Fibonnaci resolution: ")
  print(*fibonacci2(10))

  print("\nPythonic Fibonacci resolution: ")
  print(*fibonacci3(10))


""" Classic Fibonacci resolution """
def fibonacci(n):
  fib = [1, 1]
  for i in range(2, n):
    fib.append(fib[i-2] + fib[i-1])  
  return fib


""" Recursive Fibonnaci resolution """
def fibonacci2(n):
  fib = []
  for i in range(1, n+1):
    fib.append(fibonacci_recursive(i))
  return fib

def fibonacci_recursive(n):
  if n > 1:
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
  return n


""" Pythonic Fibonacci resolution """
def fibonacci3(n): 
  a, b = 1, 1
  for _ in range(n):
    yield a
    a, b = b, a + b
  

if __name__ == "__main__":
  main()