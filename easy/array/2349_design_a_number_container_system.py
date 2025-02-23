import heapq 

class NumberContainers:
    def __init__(self):
        self.indexMap = {}
        self.numberMap = {} 

    def change(self, index:int, number:int)-> None:
        if index in self.indexMap:
            old_number = self.indexMap[index]
            if old_number != number:
                self.numberMap[old_number].discard(index)
        
        self.indexMap[index] = number 

        if number not in self.numberMap:
            self.numberMap[number] = set() 
        self.numberMap[number].add(index) 

    
    def find(self, number:int) ->int:
        if number in self.numberMap and self.numberMap[number]:
            return min(self.numberMap[number])
        
        return - 1 
    
nc = NumberContainers()
print(nc.find(10))  # -1
nc.change(2, 10)
nc.change(1, 10)
nc.change(3, 10)
nc.change(5, 10)
print(nc.find(10))  # 1
nc.change(1, 20)
print(nc.find(10))