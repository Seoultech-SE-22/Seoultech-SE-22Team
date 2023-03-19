import random
from queue import Queue

class game: # game 클래스 생성
    deckList = Queue() # 남은 덱
    openCard = [] # 공개된 카드
    playerList = [] # 플레이어 목록
    turnPlayer = 0 # 현재 턴 플레이어
    attackCard = 0 # 공격 카드 매수

    def __init__(self, player_list): # game 클래스 생성자
        self.playerList = player_list
        self.deckList = Queue() # 초기화
        self.openCard = []

    def __del__(self): # game class 소멸자
        pass

    def ready(self): #게임을 준비하는 메서드
        deck = self.setDeck() # 사전에 정의한 덱 리스트
        random.shuffle(deck) # 셔플

        for i in range(0, len(deck)): # 섞은 덱을 Queue에 넣습니다.
            self.deckList.put(deck[i])

        for i in range(0, len(self.playerList)): # 각 플레이어들에게 카드를 나눠줍니다.
            self.playerList[i].draw(self, 5) # 나눠줄 카드의 개수 : 임의로 5로 설정했음
            print(self.playerList[i].playerName + ": ", self.playerList[i].allHand(),"\n")

        self.placeOpenCardZone(self.deckList.get()) # 덱 맨 위에서 카드를 1장 오픈합니다.
        print("TopCard" +": " + self.openCard[len(self.openCard)-1].info()+"\n")

    def placeOpenCardZone(self, card): #OpenCardList에 카드를 놓습니다.
        self.openCard.append(card)
        card.cardEffect()

    def deckShuffle(self): # OpenCardList의 마지막(맨 위) 카드만 남기고 deckList에 넣어 셔플합니다.
        if len(self.openCard) > 1:
            tempList = []
            topCard = self.openCard[-1]
            del self.openCard[-1]

            for i in range(0, self.deckList.qsize()): # 남은 덱 temp에 넣고
                tempList.append(self.deckList.get())

            for i in range(0, len(self.openCard)): # TopCard 뺀 openCard도 temp에 넣습니다.
                tempList.append(self.openCard)

            random.shuffle(tempList)

            for i in range(0, len(tempList)): # 섞은 덱을 Queue에 넣습니다.
                self.deckList.put(tempList[i])

            self.openCard.append(topCard)

    def setDeck(self): # 게임에 사용할 덱의 CardList를 반환합니다.
        tempList = []
        for i in range(0, 4): # 0~9까지의 4색 카드를 임시 리스트에 넣습니다.
            for j in range(0, 10):
                tempList.append(card(i, j))

        return tempList

    def checkCardCondition(self, card): # 카드를 낼 수 있는지 체크하는 메서드

        TopCard_N, TopCard_C = (self.openCard[-1].cardNumber, self.openCard[-1].cardColor)
        ChkCard_N, ChkCard_C = (card.cardNumber.cardNumber, card.cardNumber.cardColor)
        TopCard_CC = self.openCard[-1].changedColor

        if (TopCard_N == ChkCard_N) and (TopCard_N > 0): # 숫자 같으면 낼 수 있음
            return True

        if (TopCard_C == ChkCard_C) and (TopCard_C > 1): # 색깔 같아도 낼 수 있음
            return True

        if (TopCard_C == -1) and (TopCard_CC == ChkCard_N): # 바뀐 색이 같아도 낼 수 있음.
            return True

        if (ChkCard_C == -1): # 색이 없는 카드는 언제든 낼 수 있음.
            return True

        return False # 이상의 조건을 통과하지 못했다면 내지 못함.

class player: # player 클래스 생성
    playerName = '' # 플레이어 이름
    isUser = True # user인가 bot인가 확인
    handCardList = [] # 들고 있는 카드

    def __init__(self, player_name, is_user): # player 클래스 생성자
        self.playerName = player_name
        self.isUser = player
        self.handCardList = []

    def __del__(self): # player class 소멸자
        pass

    def draw(self, game, num): # game의 DeckList에서 카드를 뽑아 패로 가져옵니다.
        for i in range(0, num):
            self.handCardList.append(game.deckList.get())

    def allHand(self): # hand의 모든 카드에 대한 텍스트를 반환합니다.
        tempList = []
        handCardList = self.handCardList
        for i in range(0, len(handCardList)):
            tempList.append(handCardList[i].info())

        return tempList


    def addCard(self, game, num): # player의 카드를 추가 합니다. num 은 덱으로부터 가져올 카드 갯수
        for _ in range(0, num):
            self.handCardList.append(game.deckList.get())

    def delCard(self, index): # player의 카드를 삭제합니다. i : 삭제할 인덱스
        del self.handCardList[index]


    def delIndex(self, i, color): # 삭제할 카드의 인덱스를 찾습니다. i : 삭제할 숫자, color : 삭제할 색깔
        for c in player.handCardList:
            if c.cardNumber == i: # 이 부분이 수행 안됨
                if c.cardColor == color: # 이 부분이 수행 안됨
                    return player.handCardList.index(c) # c의 인덱스 값 리턴

    def printCurSta(self): # 현재 Player 카드 리스트
        print(self.playerName + ": ", self.allHand(), "\n")

class card: # 카드 클래스 생성
    cardColor = -1 # 0: red, 1: green, 2: yellow, 3: blue, -1: none_color_card
    cardNumber = -1 # -1: special_card
    changedColor = -1 # 카드의 색이 바뀌었을 경우에 바뀐 색을 표기함

    def __init__(self, color, number): # card 클래스 생성자
        self.cardColor = color
        self.cardNumber = number

    def __del__(self): # card class 소멸자
        pass

    def cardEffect(self): # 특수 카드의 효과를 처리하기 위한 메서드.
        ## 임시 코드
        if self.cardNumber == -1:
            print("+2 공격이 시행되었어요")
        else:
            print(self.info() + "가 놓여졌어요")

    def info(self): # 카드 정보 표시
        colorDict = {-1:'None', 0:'red', 1:'green', 2:'yellow', 3:'blue'}
        return colorDict[self.cardColor] + ' ' + str(self.cardNumber)

## 테스트용 ##
user1 = player('USER', True)
pc1 = player('PC1', False)
pc2 = player('PC2', False)
pc3 = player('PC3', False)

gamePlayerList = [user1, pc1, pc2, pc3]
g = game(gamePlayerList)
g.ready()

c = card(0, -1)
g.placeOpenCardZone(c)

g.deckShuffle()

player.printCurSta(pc1)

print("낼 카드 번호와 색을 입력하세요")
delCardNum, delCardCol = map(str, input().split())
delCardNum = int(delCardNum)

pc1.delCard(1) # 임의로 인덱스 1의 숫자카드를 삭제함
print("해당 카드(임의로 : 인덱스 1)가 삭제되었습니다.")
player.printCurSta(pc1)

pc1.addCard(g, 1) # 임의로 1개의 카드를 덱으로부터 가져옴
print("카드 1개가 추가되었습니다.")
player.printCurSta(pc1)

print(g.deckList.get())