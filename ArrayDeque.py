from deque import Deque


class ArrayDeque(Deque):
    def __init__(self):
        self.items = [None] * 8  # Start with an array of 8 elements
        self.front = 0  # Points to the front element
        self.back = 0   # Points to the next empty slot at the back
        self.capacity = 8
        self._size = 0
    
    def _resize(self, new_capacity):
        """Resize the underlying array to the new capacity."""
        old_items = self.items
        self.items = [None] * new_capacity
        
        # Realign elements from old array to new one
        for i in range(self._size):
            self.items[i] = old_items[(self.front + i) % self.capacity]
        
        # Reset front and back pointers
        self.front = 0
        self.back = self._size
        self.capacity = new_capacity
    
    def add_first(self, value):
        if self._size == self.capacity:
            self._resize(2 * self.capacity)  # Double the size if full
        
        self.front = (self.front - 1) % self.capacity
        self.items[self.front] = value
        self._size += 1
    
    def add_last(self, value):
        if self._size == self.capacity:
            self._resize(2 * self.capacity)  # Double the size if full
        
        self.items[self.back] = value
        self.back = (self.back + 1) % self.capacity
        self._size += 1
    
    def remove_first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        value = self.items[self.front]
        self.items[self.front] = None  # Optional: Clear the slot
        self.front = (self.front + 1) % self.capacity
        self._size -= 1
        
        if 0 < self._size < self.capacity // 4:
            self._resize(self.capacity // 2)  # Shrink if too empty
        
        return value
    
    def remove_last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        self.back = (self.back - 1) % self.capacity
        value = self.items[self.back]
        self.items[self.back] = None  # Optional: Clear the slot
        self._size -= 1
        
        if 0 < self._size < self.capacity // 4:
            self._resize(self.capacity // 2)  # Shrink if too empty
        
        return value
    
    def is_empty(self):
        return self._size == 0
    
    def size(self):
        return self._size