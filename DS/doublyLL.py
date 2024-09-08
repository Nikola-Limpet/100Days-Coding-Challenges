# Doubly Linked Lists 

class DoublyNode:
  def __init__(self, val, next=None, prev=None):
    self.val = val
    self.next = next 
    self.prev = prev

  def __str__(self) -> str:
    return str(self.val)


head = tail = DoublyNode(1)

# print(tail)

# display -O(n)

def display(head):
  curr = head
  elements = []
  while curr:
    elements.append(str(curr.val))
    curr = curr.next

  print(' <-> '.join(elements))
display(head) # tail 1 head 1

def insert_at_beginning(head, tail, val):
  new_node = DoublyNode(val, next=head)  # new_node become head and new_node pointer(next) point to old head
  head.prev = new_node # old head pointer(prev) to new_node

  return new_node, tail  # return new_node at the beginnning and the tail stay the same

head, tail = insert_at_beginning(head, tail, 3)
display(head) # 3 <-> 1
  

# Insert at the end O(1)

def insert_at_end(head, tail, val):
  new_node = DoublyNode(val, prev=tail) # new_node pointer(prev) point to the old tail node
  tail.next = new_node # old tail node pointer(next) point to the new_node that become the tail node
  return new_node, head # return tail node(new_node) and the head still the same

head, tail = insert_at_end(head, tail, 7)
display(tail) # 3 <-> 1 <-> 7

