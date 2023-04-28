class CardHolder:
    def __init__(self, capacity):
        self.nowIdx = 0
        self.capacity = capacity
        
        self.userHand = []

    def __del__(self):
        pass
    
    def update(self, cardList):
        self.userHand = cardList
    
    def realIdx(self, num):
        page = (self.nowIdx) // self.capacity
        return (page * self.capacity) + num
    
    def show(self):
        result = []
        page = (self.nowIdx) // self.capacity
        for i in range(page*self.capacity, ((page+1)*self.capacity)):
            if len(self.userHand)-1 - i>= 0:
                result.append(self.userHand[i])
        
        return result
    
    def pageUp(self):
        page = (self.nowIdx) // self.capacity
        maxPage = len(self.userHand) // self.capacity
        if maxPage > page:
            if (len(self.userHand)) != (page+1)*self.capacity:    
                self.nowIdx = (page+1) * self.capacity
        
    def pageDown(self):
        page = (self.nowIdx) // self.capacity
        if self.nowIdx+1 > self.capacity:
            self.nowIdx = (page) * self.capacity -1
    
    def incIdx(self):
        if len(self.userHand)-1 > self.nowIdx:
            self.nowIdx += 1
            
    def decIdx(self):
        if self.nowIdx > 0:
            self.nowIdx -= 1