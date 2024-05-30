class Node():
  def __init__(self, value, parent = None):
    self.value = value
    self.parent = parent

  def __str__(self) -> str:
    return f"Node({self.value})->{self.parent}"

def main():
  SIZE = 10

  node = Node(0)
  for i in range(1, SIZE):
   node = Node(i, node)

  print(node)

if __name__ == "__main__":
  main()