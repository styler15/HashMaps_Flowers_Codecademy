from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]
  
  def hash(self, key):
    self.key = key.encode()
    key_hash_code = sum(self.key)
    return key_hash_code
  
  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    
    for items in list_at_array:
      if items[0] == key:
        items[1] == value
        return
    list_at_array.insert(payload)

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    
    for items in list_at_index:
      if items[0] == key:
        return items[1]
      else:
        return None

    #if list_at_index != None:
      #self.array[array_index] = [key, value]
      #return
    #if list_at_index[0] == key:
      #return payload[1]
    #if list_at_index is None:
      #return None
blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])
print(blossom.retrieve('daisy'))
    