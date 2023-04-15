from uno_Player import * # Player Class

class PlayerList:
    
    playerList = [] # 플레이어 리스트
    turnIdx = -1
    direction = 1
    nextIdx = 0
    prevIdx = -1
    applySkip = False
    
    def __init__(self, player_list): # playerList class 생성자
        self.playerList = player_list.copy()
        self.turnIdx = (len(self.playerList)-1)%self.size()
        self.direction = 1
        self.nextIdx = (len(self.playerList))%self.size()
        self.prevIdx = (len(self.playerList)-2)%self.size()
        self.applySkip = False
        
        self.it = 0
        
    def __del__(self): # playerList class 소멸자
        if self.playerList != []: # playerList의 player instance들을 모두 del 합니다.
            for i in self.playerList:
                del i
            self.playerList = []
    

    def size(self): # 리스트 사이즈 반환
        return len(self.playerList)
    
    def nextTurn(self): # 턴을 넘긴다
        self.prevIdx = self.turnIdx
        self.turnIdx = self.nextIdx
        self.nextIdx = (self.turnIdx+self.direction)%self.size()
        self.applySkip = False
        
    def skip(self): # 스킵 효과 적용
        self.nextIdx = (self.nextIdx+self.direction)%self.size()
    
    def reverse(self): # 리버스 효과 적용
        self.direction *= -1
        if self.applySkip == False:
            self.nextIdx = (self.nextIdx + 2*self.direction)%self.size()
            self.applySkip = True
    
    def turnPlayer(self): # 현재 플레이어 반환
        return self.playerList[self.turnIdx]
    
    def prevPlayer(self): # 이전 플레이어 반환
        return self.playerList[self.prevIdx]
    
    def nextPlayer(self): # 다음 플레이어 반환
        return self.playerList[self.nextIdx]
    
    def idxPlayer(self, idx): # 인덱스 플레이어 반환
        return self.playerList[idx]
    
    def lst(self): # 플레이어 리스트 반환
        result = self.playerList.copy()
        return result
    
    
    
