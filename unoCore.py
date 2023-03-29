import random
from uno_Const import * # const
import uno_ChkCon # Check Condition

from queue import Queue

class game: # game 클래스 생성
    deckList = [] # 남은 덱
    openCard = [] # 공개된 카드
    playerList = [] # 플레이어 목록
    turnPlayer = 0 # 현재 턴 플레이어
    attackCard = 0 # 공격 카드 매수
    jumpNumber = 1 # 턴 종료시, 플레이어를 넘기는 정도
    state = NORM
    botCompeteList = []

    def __init__(self, player_list): # game 클래스 생성자
        self.playerList = player_list
        self.deckList = pile()
        self.openCard = pile()
        state = NORM
        botCompeteList = []

    def __del__(self): # game class 소멸자
        pass

    def ready(self): #게임을 준비하는 메서드
        deckPreset = self.setDeck() # 사전에 정의한 덱 리스트
        
        self.deckList + deckPreset # 덱에 deckPreset을 넣는다.
        self.deckList.shuffle()
        
        for i in range(0, len(self.playerList)): # 각 플레이어들에게 카드를 나눠줍니다.
            self.playerList[i].draw(self, 5) # 나눠줄 카드의 개수 : 임의로 5로 설정했음
            print(self.playerList[i].playerName + ": ", self.playerList[i].allHand(),"\n")
            
        self.placeOpenCardZone(self.deckList.takeTopCard()) # 덱 맨 위에서 카드를 1장 오픈합니다.
        print("TopCard" +": " + self.openCard.cardList[-1].info()+"\n")
        
        

    def placeOpenCardZone(self, card): #OpenCardList에 카드를 놓습니다.
        lst = []
        lst.append(card)
    
        self.openCard + lst
        card.cardEffect(self)

    def setDeck(self): # 게임에 사용할 덱의 CardList를 반환합니다.
        tempList = []
        for i in range(0, 4): # 0~9까지의 4색 카드를 임시 리스트에 넣습니다.
            for j in range(0, 10):
                tempList.append(card(i, j))

        return tempList
    
    def executeTurn(self): # 하나의 턴을 실행합니다.
        
        if self.playerList[self.turnPlayer].isUser == True: # 턴 플레이어가 유저
                self.mainPhase()
                #print("User",self.playerList[self.turnPlayer].playerName, "의 턴")
        else: # 턴 플레이어가 봇
            self.unoBot()
        
        result = self.endPhase()
        return result # 게임이 끝났는지, 승자는 누구인지
    
    def mainPhase(self):
        if self.attackCard > 0: # 공격 처리
            self.playerList[self.turnPlayer].draw(self, self.attackCard)
            self.attackCard = 0 # attactCard 리셋
        
        cond = True
        while cond:
            print("TopCard" +": " + self.openCard.cardList[-1].info()+"\n")
            print(self.playerList[self.turnPlayer].playerName + ": ", self.playerList[self.turnPlayer].allHand())
            print("카드 내기: p, 카드 뽑기: d")
            input_act = input()
            if input_act == 'p':
                print("낼 카드의 인덱스를 입력하세요")
                input_num = int(input())
                if self.playerList[self.turnPlayer].handCardList[input_num].canUse(self):
                    useCard = self.playerList[self.turnPlayer].delCard(input_num)
                    self.placeOpenCardZone(useCard)
                    cond = False
                else:
                    print("그 카드는 낼 수 없습니다.")
            if input_act == 'd':
                print("카드를 1장 뽑습니다.")
                self.playerList[self.turnPlayer].draw(self, 1)
                cond = False
            else:
                pass
            
            print(self.playerList[self.turnPlayer].playerName + ": ", self.playerList[self.turnPlayer].allHand())
        
        print()
    
    def actList(self): # 현재 활성화야햐하는 버튼의 딕셔너리를 반환
        result = {'drawBtn': True,'unoBtn': True} # 'drawBtn': 드로우 버튼, 'unoBtn': 우노 버튼
        if (self.playerList[self.turnPlayer].isUser == False):
            result['drawBtn'] = False
            
        if (self.state == NORM):
            result['unoBtn'] = False
            
        return result
    
    def eventCardBtn(self, idx): # 카드 클릭시 이벤트
        if self.playerList[self.turnPlayer].isUser == True:
            if self.playerList[self.turnPlayer].handCardList[idx].canUse(self) == True:
                useCard = self.playerList[self.turnPlayer].delCard(idx)
                self.placeOpenCardZone(useCard)
            else:
                print("그 카드는 낼 수 없어요")
        else:
            print("아직 당신의 턴이 아니에요")
        
        if len(self.playerList[self.turnPlayer].handCardList) == 1:
            pass # 봇간 우노 경쟁 메서드
        
        self.endPhase()
    
    def eventDrawBtn(self): # 드로우 버튼 클릭시 이벤트
        self.playerList[self.turnPlayer].draw(self, 1)
        self.endPhase()
    
    def eventUnoBtn(self): # 우노 버튼 클릭시 이벤트
        self.state == NORM
        if self.playerList[self.turnPlayer-1].isUser == True: # 나의 우노가
            pass # 저지당하지 않았다.
        else: # 다른 사람의 우노를
            self.playerList[self.turnPlayer-1].draw(self, 1) # 저지했다.
      
    
    def endPhase(self): # endPhase를 실행
        
        if (len(self.playerList[self.turnPlayer].handCardList) == 0):
            return True
        
        self.turnPlayer = (self.turnPlayer+self.jumpNumber)%len(self.playerList) # 점프 처리
        self.jumpNumber = 1 # jumpNumber 리셋
        
        # time 오브젝트의 시간을 초기화
        
        return False
    
    def unoBot(self): # 봇의 턴
        
        chkList = self.playerList[self.turnPlayer].canUseIdx(self)
        
        if chkList != []: # 낼 수 있는 카드가 있다면
            randIdx = random.choice(chkList) # 무작위의 카드를 내고
            useCard = self.playerList[self.turnPlayer].delCard(randIdx)
            self.placeOpenCardZone(useCard)
            print( useCard.info() + "를 냅니다.")
        else:             # 낼 수 있는 카드가 없다면
            self.playerList[self.turnPlayer].draw(self, 1) # 카드를 뽑고
            print("낼 카드가 없어서 1장 뽑습니다.")
        
        print(self.playerList[self.turnPlayer].playerName + ": ", self.playerList[self.turnPlayer].allHand())
        print()
        print()
        self.endPhase()
        
    def processUno(self, idx): # 누군가 우노를 외쳤을 때, 게임에서 실질적으로 바뀌는 부분에 대한 처리
        if self.state == UNO:
            self.state = NORM
            
            if self.turnPlayer-1 == idx: # (턴 플레이어 -1) = 전 턴의 플레이어 = 우노 상태를 만든 당사자
                print(self.playerList[idx].playerName,'가 UNO 우노를 외쳤습니다.')
            else: # 그 외의 플레이어
                print(self.playerList[idx].playerName,'가', self.playerList[self.turnPlayer-1].playerName,' 의 UNO 우노를 저지했습니다.')
                self.playerList[self.turnPlayer-1].draw(self, 1)
        else:
            print('state == UNO에서만 이 메서드가 동작합니다.')
    
    def searchUserIdx(self): # 하나의 user만 있을 때 동작합니다.
        result = -1
        for i in range(0, len(self.playerList)):
            if self.playerList[i].isUser == True:
                result = i
                break
        
        return result
        
    
    def userHand(self): # 유저의 패 리스트를 반환합니다.
        result = self.playerList[self.searchUserIdx()].handCardList
        
        return result
    
    def playerTurnTable(self): # 플레이어의 턴 순서를 표시하기 위한 정보를 반환합니다.
        result = []
        for i in range(0, len(self.playerList)):
            idx = (i+self.turnPlayer)%len(self.playerList)
            result.append(self.playerList[idx])
        return result
 
class pile: # pile 클래스 생성
    cardList = []

    def __init__(self, cardList = []): # player 클래스 생성자
        self.cardList = cardList.copy()

    def __del__(self): # player class 소멸자
        pass
    
    def shuffle(self): # pile의 카드를 섞습니다.
        random.shuffle(self.cardList)
        
    def takeTopCard(self): # 가장 위의 카드를 가져옵니다.
        result = self.cardList.pop()
        
        return result
    
    def __add__(self, op_2): # pile_2의 카드를 전부 옮깁니다.
        for i in op_2:
            self.cardList.append(i)
        op_2.clear() # 카드 옮겼으니 전부 지움
        
    def printlist(self):
        lst = [x.info() for x in self.cardList]
        return lst
        
class player: # player 클래스 생성
    playerName = '' # 플레이어 이름
    isUser = True # user인가 bot인가 확인
    handCardList = [] # 들고 있는 카드

    def __init__(self, player_name, is_user): # player 클래스 생성자
        self.playerName = player_name
        self.isUser = is_user
        self.handCardList = []

    def __del__(self): # player class 소멸자
        pass

    def draw(self, game, num): # game의 DeckList에서 카드를 뽑아 패로 가져옵니다.
        
        if len(game.deckList.cardList) < num: # 뽑을 카드 부족하면
            top = game.openCard.takeTopCard() # 맨 위 카드 하나 빼놓고
            game.deckList + game.openCard.cardList # 나머지는 합쳐서
            game.deckList.shuffle() # 셔플
            game.openCard + [top] # 빼둔 카드 openCard에 둠
        
        for i in range(0, num): # num 만큼 반복
            self.handCardList.append(game.deckList.takeTopCard())

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

class card: # 카드 클래스 생성
    color = -1 # 0: red, 1: green, 2: yellow, 3: blue, -1: none_color_card
    number = -1 # -1: special_card
    attack = -1 # 1 : +2 효과 기능, -1 : none
    changeSequence = -1 # 1 : 순서 변경 기능,-1 : none
    changeNumber = -1 # 1 : 숫자 변경 기능, -1 : none
    turnPass = -1 # 1 : 턴 넘기기 기능, -1 : none
    changeDeck = -1 # 1 : 덱 변경 기능, -1 : none
    changeColor = -1 # 1 : 컬러 변경 기능, -1 : none
    applyNumber = -1
    applyColor = -1
    
    def __init__(self, color, number, attack = -1, changeSequence = -1, changeNumber = -1, turnPass = -1, changeDeck = -1, changeColor = -1): # card 클래스 생성자

        # 특수 카드 생성시에는 인자로 기능들을 구분해야 하나 ?
        self.color = color
        self.number = number
        self.attack = attack
        self.changeSequence = changeSequence
        self.changeNumber = changeNumber
        self.turnPass = turnPass
        self.changeDeck = changeDeck
        self.changeColor = changeColor
        self.applyNumber = self.number # applyNumber 는 cardNumber 로 초기값 설정
        self.applyColor = self.color # applyColor 는 cardColor 로 초기값 설정

    def __del__(self): # card class 소멸자
        pass

    def cardEffect(self, game): # 특수 카드의 효과를 처리하기 위한 메서드.
    
        if self.attack == 1:
            game.attackCard += 2
        if self.changeSequence == 1:
            # game.playerList.reverse()
            tp = game.turnPlayer
            tmp_Lst = []

            for _ in range(len(game.playerList)):
                tp -= 1
                tmp_Lst.append(game.playerList[tp])

        if self.changeNumber == 1:
            applyNumber = int(input())

        if self.turnPass == 1:
            # turn pass turn flow 에서 넘겨야하나 ?
            game.jumpNumber += 1

        if self.changeDeck == 1:
            # change deck 가장 낮은 리스트 개수와 변경
            lstNum = []
            for p in game.playerList:
                lstNum.append(len(p.handCardList))

            MAX = lstNum.index(max(lstNum))
            MIN = lstNum.index(min(lstNum))

            game.playerList[MAX].handCardList, game.playerList[MIN].handCardList  = game.playerList[MIN].handCardList, game.playerList[MAX].handCardList

        if self.changeColor == 1:
            applyColor = int(input())


    def attack(self):
        player.draw()
        
    def canUse(self, game):
        top = game.openCard.cardList[-1]
        result = uno_ChkCon.canUse(top.number, top.color, top.applyColor, top.applyNumber, self.number, self.color)

        return result

    def info(self): # 카드 정보 표시
        colorDict = {NONE_COLOR:'None', RED:'red', GREEN:'green', YELLOW:'yellow', BLUE:'blue'}
        return colorDict[self.color] + ' ' + str(self.number)

## 테스트용 ##

user1 = player('USER', True)
pc1 = player('PC1', False)
pc2 = player('PC2', False)
pc3 = player('PC3', False)

gamePlayerList = [user1, pc1, pc2, pc3]
g = game(gamePlayerList)

g.ready()