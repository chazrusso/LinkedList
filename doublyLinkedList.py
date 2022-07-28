#Node class creation: create a node with a set value. Previous and Next nodes default to 'None'
class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
#Set the 'next node' in the list to a new node    
  def set_next_node(self, next_node):
    self.next_node = next_node
#Return the value of the next node in the list    
  def get_next_node(self):
    return self.next_node
#Set the 'previous node' in the list to a new node
  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
#Return the value of the previous node    
  def get_prev_node(self):
    return self.prev_node
#Return the value of the current node  
  def get_value(self):
    return self.value
#Creation of a doubly linked list
class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
#Add to the head of the list  
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node

    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)

    self.head_node = new_head

    if self.tail_node == None:
      self.tail_node = new_head
#Add to the tail of the list
  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)

    self.tail_node = new_tail

    if self.head_node == None:
      self.head_node = new_tail
#Remove the head of the list
  def remove_head(self):
    removed_head = self.head_node

    if removed_head == None:
      return None

    self.head_node = removed_head.get_next_node()

    if self.head_node != None:
      self.head_node.set_prev_node(None)

    if removed_head == self.tail_node:
      self.remove_tail()

    return removed_head.get_value()
#Remove the tail of the list
  def remove_tail(self):
    removed_tail = self.tail_node

    if removed_tail == None:
      return None

    self.tail_node = removed_tail.get_prev_node()

    if self.tail_node != None:
      self.tail_node.set_next_node(None)

    if removed_tail == self.head_node:
      self.remove_head()

    return removed_tail.get_value()
#Remove a node from the list by value
  def remove_by_value(self, value_to_remove):
    node_to_remove = None
    current_node = self.head_node

    while current_node != None:
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
        break

      current_node = current_node.get_next_node()

    if node_to_remove == None:
      return None

    if node_to_remove == self.head_node:
      self.remove_head()
    elif node_to_remove == self.tail_node:
      self.remove_tail()
    else:
      next_node = node_to_remove.get_next_node()
      prev_node = node_to_remove.get_prev_node()
      next_node.set_prev_node(prev_node)
      prev_node.set_next_node(next_node)

    return node_to_remove
#Create a printable version of the list
  def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list  


#Testing

subway = DoublyLinkedList()

subway.add_to_head("Times Square")
subway.add_to_head("Grand Central")
subway.add_to_head("Central Park")

print(subway.stringify_list())

subway.add_to_tail("Penn Station")
subway.add_to_tail("Wall Street")
subway.add_to_tail("Brooklyn Bridge")

print(subway.stringify_list())

subway.remove_head()
subway.remove_tail()

print(subway.stringify_list())

subway.remove_by_value("Times Square")

print(subway.stringify_list())
