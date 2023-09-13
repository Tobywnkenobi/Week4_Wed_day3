from Node import Node

class LinkedList:

  def __init__(self, head_value):
    self.head = Node(head_value)

  def __repr__(self):
    return f'<LinkedList: {self.head.value}>'
  
  def __iter__(self):
    current_node = self.head
    while current_node.right:
      yield current_node
      current_node = current_node.right
    yield current_node
  
  def append_node(self, value):
    current_node = self.head
    while current_node.right:
      current_node = current_node.right
    current_node.right = Node(value)

  def search(self, value):
    for node in self:
      if node.value == value:
        return node
    return False
  
  def get_tail(self):
    for node in self:
      pass
    return node

  def insert(self, neighbor, value):
    for node in self:
      if node.value == neighbor:
        next_node = node.right
        node.right = Node(value)
        node.right.right = next_node
        return
    print(f'{neighbor} not in LinkedList')

  def update_head(self, value):
      new_head = Node(value)
      new_head.right = self.head
      self.head = new_head
      

  def remove(self, value):
        # if self.head and self.head.value == value:
        #   self.head = self.head.right
        #   return
        
        for node in self:
          if node.right and node.right.value == value:
            node.right = node.right.right
            return

linkedlist = LinkedList('Monday')

linkedlist.append_node('Tuesday')
linkedlist.append_node('Wednesday')
linkedlist.append_node('Friday')

# print(linkedlist.search('Monday'))
# print(linkedlist.search('Friday'))

# print(linkedlist.head.right)

linkedlist.insert('Wednesday', 'Thursday')
linkedlist.insert('Saturday', 'Sunday')

for node in linkedlist:
  # print(node)
  print(linkedlist.search(node.value))

# print(linkedlist.get_tail())