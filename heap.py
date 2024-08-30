class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def _left_child(self, index):
        return 2 * index + 1 
    
    def _right_child(self, index):
        return  2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, val):
        self.heap.append(val)
        index = len(self.heap) - 1
        parent = self._parent(index)
        while index != 0 and self.heap[index] > self.heap[parent]:
            self._swap(parent, index)
            index = parent
            parent = self._parent(index)
        return True
    
    def remove(self, val):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        else:
            max_val = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._sink_down(0)

            return max_val

    def _sink_down(self, index):    
        max_index = 0     
        while(True):
            left = self._left_child[index]
            right = self._right_child[index]
            
            if right < len(self.heap) and self.heap[left] > self.heap[index]:
                max_index = left 
            if left < len(self.heap) and self.heap[right] > self.heap[index]: 
                max_index = right
            if max_index !=  index:
                self._swap(index, max_index)
                index = max_index
            else:
                return