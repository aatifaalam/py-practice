# Question - Write a program to print the following pattern:
# *
# **
# ***
# ****
# *****
# n = 5
# for i in range(1, n+1):
#     print(i * "*")
# Question - Write a program to print the following pattern:
# *****
# ****
# ***
# **
# *

# n = 5
# for i in range(n, 0, -1):
#     print(i * "*")

# Question - Write a program to print the following pattern:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# n = 5
# for i in range(1, n + 1):
#     print(i * "*")
# for i in range(n - 1, 0, -1):
#     print(i * "*")

# Question - Write a program to print the following pattern:
#   *
#  ***
# *****
#  ***
#   *

# n = 5
# for i in range(1, n + 1, 2):
#     print((n - i) // 2 * " " + i * "*")
# for i in range(n - 2, 0, -2):
#     print((n - i) // 2 * " " + i * "*")

# Question - Write a program to print the following pattern:
#     *
#    ***
#   *****
#   *****
#    ***
#     *

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def deleteSpecificNode(head, nodeToDelete):
  if head == nodeToDelete:
    return head.next

  currentNode = head
  while currentNode.next and currentNode.next != nodeToDelete:
    currentNode = currentNode.next

  if currentNode.next is None:
    return head

  currentNode.next = currentNode.next.next

  return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
traverseAndPrint(node1)

# Delete node4
node1 = deleteSpecificNode(node1, node4)

print("\nAfter deletion:")
traverseAndPrint(node1)