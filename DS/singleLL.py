class SinglyNode:
  def __init__(self, val, next=None):
    self.val = val
    self.next = None

  def __str__(self) -> str:
    return str(self.val)
  
  
head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

# print(head)


# connect each node 
head.next = A
A.next = B
B.next = C


# Traverse the list - O(n)
# current = head
# while current:
#   print(current)
#   current = current.next

# Display Linked List -O(n)

def display(head):
  current = head
  elements = []
  
  while current:
    elements.append(str(current.val))
    current = current.next
  
  print(" -> ".join(elements))

# display(head)

# Search For a node value -O(n)


def search(head, val):
  current = head 
  while current:
    if val == current.val:
       return True
    else:
      current = current.next  
  return False

print(search(head, 2))






class SinglyLinkedList:
  """ 
    implement:
    get_size()
    find(data)
    add_Front(data) O(1)
    add_node_at_position()
    remove(data)
  """
  def __init__(self):
    pass
