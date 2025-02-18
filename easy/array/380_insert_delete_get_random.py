class RandomizedSet:
    def __init__(self):
        self.num_to_index = {}  # Stores value -> index mapping
        self.nums = []          # Stores actual values
    
    def insert(self, val: int) -> bool:
        if val in self.num_to_index:
            return False  # Value already exists
        self.num_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.num_to_index:
            return False  # Value not found
        
        # Get index of the element to remove
        index_to_remove = self.num_to_index[val]
        last_element = self.nums[-1]  # Last element in list

        # Swap the element to remove with the last one
        self.nums[index_to_remove] = last_element
        self.num_to_index[last_element] = index_to_remove  # Update index of last element

        # Remove the last element
        self.nums.pop()
        del self.num_to_index[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)