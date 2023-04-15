from uno_Card import *

class Player: # player 클래스 생성
    playerName = '' # 플레이어 이름
    isUser = True # user인가 bot인가 확인
    handCardList = [] # 들고 있는 카드
    

    def __init__(self, player_name, is_user): # player 클래스 생성자
        self.playerName = player_name
        self.isUser = is_user
        self.handCardList = []

    def __del__(self): # player class 소멸자
        if self.handCardList != []: # handCardList의 Card instance들을 모두 del 합니다.
            for i in self.handCardList:
                del i
            self.handCardList = []

    def draw(self, game, num): # game의 DeckList에서 카드를 뽑아 패로 가져옵니다.
        
        if (len(game.deckList.cardList) == 0) and (len(game.openCard.cardList) == 1):
            print("섞을 카드가 없어요")
        else:
            if len(game.deckList.cardList) < num: # 뽑을 카드 부족하면
                print('뽑을 카드가 없으므로 openCard를 가져오겠습니다.')
                top = game.openCard.takeTopCard() # 맨 위 카드 하나 빼놓고
                game.deckList + game.openCard.cardList # 나머지는 합쳐서
                game.deckList.shuffle() # 셔플
                game.openCard + [top] # 빼둔 카드 openCard에 둠
            
        
            for i in range(0, num): # num 만큼 반복
                result = self.drawOneCard(game)
                if result == 0:
                    print('뽑을 카드가 없어요')
                    break
            
    def drawOneCard(self, game):
        if len(game.deckList.cardList) != 0:
            self.handCardList.append(game.deckList.takeTopCard())
            return 1
        else:
            return 0
    
     
        

    def allHand(self): # hand의 모든 카드에 대한 텍스트를 반환합니다.
        tempList = []
        handCardList = self.handCardList
        for i in range(0, len(handCardList)):
            tempList.append(handCardList[i].info())

        return tempList

    def delCard(self, index): # player의 카드를 삭제합니다. i : 삭제할 인덱스
        
        result = self.handCardList[index]
        del self.handCardList[index]
        
        return result
    
    def canUseIdx(self, game): # 낼 수 있는 카드의 인덱스 리스트를 반환합니다.
        chkList = []
        tpHand = self.handCardList
        
        for i in range(0, len(tpHand)):
            if tpHand[i].canUse(game) == True:
                chkList.append(i)
        
        return chkList
        
    def delIndex(self, i, color): # 삭제할 카드의 인덱스를 찾습니다. i : 삭제할 숫자, color : 삭제할 색깔
        for c in self.handCardList:
            #c.cardNumber = 3
            #c.cardColor = green
            if c.number == i: # 이 부분이 수행 안됨
                #print(c.cardNumber)
                if c.color == color: # 이 부분이 수행 안됨
                    return player.handCardList.index(c) # c의 인덱스 값 리턴

    def printCurSta(self): # 현재 Player 카드 리스트
        print(self.playerName + ": ", self.allHand(), "\n")
        
    def data(self): # Front에서 card instance의 정보를 dictionary로 확인하기 위한 메서드
        name = self.playerName
        isUser = self.isUser
        handList = self.handCardList
        
        result = {'playerName': name, 'isUser': isUser, 'handCardList': handList}
        
        return result
