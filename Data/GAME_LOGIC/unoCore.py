import random
from Data.GAME_LOGIC.Timer import Timer
from Data.GAME_LOGIC.uno_Const import * # const
from Data.GAME_LOGIC.uno_Pile import * # Pile Class
from Data.GAME_LOGIC.uno_PlayerList import * # PlayerList Class
from Data.GAME_LOGIC.uno_Card import * # Card Class
from Data.GAME_LOGIC.uno_Bot import * # Bot Class

class Game: # game 클래스 생성
    deckList = [] # 남은 덱
    openCard = [] # 공개된 카드
    playerList = None
    state = NORM
    botCompeteList = []
    winner = None
    GameMode = MODE_NORMAL # 게임의 모드
    
    is_selectColor = False
    is_selectNumber = False
    
    other_Uno = False
    use_effect = False

    # timer #
    is_effctTime = False
    timer = Timer(15)
    effectTimer = Timer(0)

    def __init__(self, player_list, mode): # game 클래스 생성자
        self.playerList = PlayerList(player_list)
        self.deckList = Pile()
        self.openCard = Pile()
        self.state = NORM
        self.botCompeteList = []
        self.winner = None
        self.GameMode = mode
        
        self.other_Uno = False
        self.use_effect = False
        
        self.is_selectColor = False
        self.is_selectNumber = False
        
        self.is_effctTime = False
        self.timer = Timer(15)
        self.effectTimer = Timer(0)
        
        self.turn = 0
        
    def __del__(self): # game class 소멸자
        del self.deckList
        del self.openCard
        del self.playerList
        
    def ready(self, screen_size): #게임을 준비하는 메서드
        deckPreset = self.setDeck(screen_size) # 사전에 정의한 덱 리스트
        
        
        self.deckList + deckPreset # 덱에 deckPreset을 넣는다.
        self.deckList.shuffle()
        top = self.deckList.takeTopCard()
        
        distribution(self, self.GameMode) # 카드 분배
            
        self.placeOpenCardZone(top) # 덱 맨 위에서 카드를 1장 오픈합니다.
        print("TopCard" +": " + self.openCard.cardList[-1].info()+"\n")
        
        self.playerList.nextTurn()
        
        if self.playerList.turnPlayer().isUser == True:
            self.timer.reset(USER_TIME)
        else:
            self.timer.reset(BOT_TIME)
        

    def placeOpenCardZone(self, card): #OpenCardList에 카드를 놓습니다.
        lst = []
        lst.append(card)
        self.openCard + lst
    
        # self.openCard.cardList.append(Card)
        card.cardEffect(self)

    def setDeck(self, screen_size): # 게임에 사용할 덱의 CardList를 반환합니다.
        tempList = []
        for i in range(0, 4): # 0~9까지의 4색 카드를 임시 리스트에 넣습니다.
            for j in range(0, 10):
                card = Card(i, j, NO_EFFECT)
                card.default_image = pygame.transform.smoothscale(pygame.image.load(CARD_PATH + f"{Card.imgColor(card)}_{Card.imgValue(card)}.png"), (screen_size[0] / 12.5, screen_size[0] / 8.333))
                tempList.append(card)

        for i in range(0, 4): # 색상이 필요한 특수 카드
            for j in [EFFECT_DRAW, EFFECT_SKIP, EFFECT_REVERSE]:
                if j == 0B10 :
                    card = Card(i, NO_NUMBER, j , attackNumber=2)
                else :
                    card = Card(i, NO_NUMBER, j)
                card.default_image = pygame.transform.smoothscale(pygame.image.load(CARD_PATH + f"{Card.imgColor(card)}_{Card.imgValue(card)}.png"), (screen_size[0] / 12.5, screen_size[0] / 8.333))
                tempList.append(card)
        
        for i in range(2): #+4 드로우 카드
            card = Card(NO_COLOR, NO_NUMBER, EFFECT_DRAW+EFFECT_COLOR , attackNumber=4)
            tempList.append(card)
        
        for i in range(4): # 색깔 있는 +4 카드
            card = Card(i, NO_NUMBER, EFFECT_DRAW, attackNumber=4)
            tempList.append(card)
            
        for i in range(4): # 색깔 있는 +2 리버스 카드
            card = Card(i, NO_NUMBER, EFFECT_DRAW+EFFECT_REVERSE, attackNumber=2)
            tempList.append(card)

        for _ in range(0, 2): # 색상이 불필요한 특수카드
            for j in [EFFECT_COLOR]:
                card = Card(NO_COLOR, NO_NUMBER, j)
                card.default_image = pygame.transform.smoothscale(pygame.image.load(CARD_PATH + f"{Card.imgColor(card)}_{Card.imgValue(card)}.png"), (screen_size[0] / 12.5, screen_size[0] / 8.333))
                tempList.append(card)

        return tempList
    
    def actList(self): # 현재 활성화야햐하는 버튼의 딕셔너리를 반환
        result = {'drawBtn': True,'unoBtn': True, 'colorBtn': True, 'numberBtn': True}
        if (self.playerList.turnPlayer().isUser == False):
            result['drawBtn'] = False
            
        if (self.state == NORM):
            result['unoBtn'] = False
        
        if (self.is_effctTime == True):
            result['unoBtn'] = False
        
        result['colorBtn'] = self.is_selectColor
        result['numberBtn'] = self.is_selectNumber
            
        return result
    
    def actList_M(self, uid):
        idx = self.playerList.uti(uid)
        if idx == None:
            print('그런 uid를 가진 플레이어는 존재하지 않는다.')
            return None
        else:
            result = {'drawBtn': True,'unoBtn': True, 'colorBtn': True, 'numberBtn': True}
            if (self.playerList.turnIdx().uid == uid):
                result['drawBtn'] = False
            
            if (self.state == NORM):
                result['unoBtn'] = False
        
            if (self.is_effctTime == True):
                result['unoBtn'] = False
        
                result['colorBtn'] = self.is_selectColor
                result['numberBtn'] = self.is_selectNumber
            
            return result
    
    def eventCardBtn_M(self, idx, uid): # 카드 클릭시 이벤트
        pidx = self.playerList.uti(uid)
        if pidx != None:
            if self.is_effctTime == False:
                if self.playerList.turnPlayer().uid == uid:
                    if self.playerList.turnPlayer().handCardList[idx].canUse(self) == True:
                        useCard = self.playerList.turnPlayer().delCard(idx)
                        self.placeOpenCardZone(useCard)
                        
                        self.playerList.turnPlayer().UnoAndWinnerChecker(self)
                        
                        self.endPhase()
                        return True
                    else:
                        print(self.playerList.turnPlayer().handCardList[idx].info()+"는 낼 수 없어요")
                        return False
                    
            else:
                print("아직 당신의 턴이 아니에요")
                return False
            
        else:
            print('해당 uid를 가진 플레이어는 존재하지 않습니다.')
            return False
            
    def uidHand(self, uid): # 유저의 패 리스트를 반환합니다.
        idx = self.playerList.uti(uid)
        if idx != None:
            result = self.playerList.idxPlayer(idx).handCardList
            return result
        else:
            return None
        
    def eventUnoBtn_M(self, uid): # 우노 버튼 클릭시 이벤트
        idx = self.playerList.uti(uid)
        if idx != None:
            if self.state == UNO:
                self.processUno(idx)
        else:
            print('해당 uid를 가진 플레이어는 존재하지 않습니다.')
            
    def eventColorBtn(self, color): # 색상 변경 버튼
        self.effectTimer.reset(1)
        self.openCard.cardList[-1].applyColor = color
        self.is_selectColor = False
        self.is_effctTime = False
    
    def eventCardBtn(self, idx): # 카드 클릭시 이벤트
        if self.is_effctTime == False:
            if self.playerList.turnPlayer().isUser == True:
                if self.playerList.turnPlayer().handCardList[idx].canUse(self) == True:
                    useCard = self.playerList.turnPlayer().delCard(idx)
                    self.placeOpenCardZone(useCard)
                    
                    eCode = useCard.effectCode # eCode를 통해 어떤 종류인지 판단

                    if eCode & EFFECT_SKIP == EFFECT_SKIP:  # 다음 플레이어를 스킵하는 효과
                        self.use_effect = True
                    if eCode & EFFECT_REVERSE == EFFECT_REVERSE:  # 턴의 진행 방향을 반대로 바꾸는 효과
                        self.use_effect = True
                    if eCode & EFFECT_DRAW == EFFECT_DRAW:  # 다음 상대에게 카드를 주는 효과
                        self.use_effect = True
                    if eCode & EFFECT_COLOR == EFFECT_COLOR:  # 카드의 색을 바꾸는 효과
                        self.use_effect = True
                    if eCode & EFFECT_NUMBER == EFFECT_NUMBER:  # 카드의 숫자를 바꾸는 효과
                        self.use_effect = True
                    self.playerList.turnPlayer().UnoAndWinnerChecker(self)
                    
                    self.endPhase()
                    return True
                else:
                    print(self.playerList.turnPlayer().handCardList[idx].info()+"는 낼 수 없어요")
                    return False
                
        else:
            print("아직 당신의 턴이 아니에요")
            return False
        
        
    
    def eventDrawBtn(self): # 드로우 버튼 클릭시 이벤트
        self.playerList.turnPlayer().draw(self, 1)
        self.endPhase()
    
    def eventUnoBtn(self): # 우노 버튼 클릭시 이벤트
        if self.state == UNO:
            self.processUno(self.searchUserIdx())
    
    def eventNumberBtn(self, number): # 숫자 변경 버튼
        self.openCard.cardList[-1].applyNumber = number
        self.effectTimer.reset(EFFECT_TIME)

    def endPhase(self): # endPhase를 실행
        self.turn += 1
        self.playerList.nextTurn()
        
        endEvent(self, self.GameMode)
        if self.playerList.turnPlayer().isUser == True:
            self.timer.reset(USER_TIME)
        else:
            self.timer.reset(BOT_TIME)
    
    def update(self): # timer, effectimer 갱신용
        if (self.is_effctTime == False): # 기본 타이머
            self.timer.update()
            self.timeEvent()
        else: # 기술 카드 효과 적용시 타이머
            self.effectTimer.update()
            self.effectTimeEvent()
            
    def timeEvent(self): # 특정 시간이 되었다면, 특정 함수를 실행함.
        ## 우노 경쟁
        if self.state == UNO:
            remainTime = -1
            if self.playerList.turnPlayer().isUser == True:
                remainTime = USER_TIME
            else:
                remainTime = BOT_TIME      
            n = remainTime-min(self.botCompeteList)
            if self.timer.time <= n:
                self.processUno(self.botCompeteList.index(min(self.botCompeteList)))
        
        ## timeOver
        if self.timer.time <= 0:
             if self.playerList.turnPlayer().isUser == True: # user의 턴
                 self.eventDrawBtn()
             else: # bot의 턴
                 self.unoBot()
                 
    def effectTimeEvent(self):
        if self.effectTimer.time <= 0:
            if self.is_selectColor:
                self.is_selectColor = False
                self.eventColorBtn(random.randrange(0,4))
                
            self.is_selectNumber = False
            self.is_effctTime = False          
                
    def unoBot(self): # 봇의 턴    
        strategy(self, self.GameMode)
        self.endPhase()
        
    def processUno(self, idx): # 누군가 우노를 외쳤을 때, 게임에서 실질적으로 바뀌는 부분에 대한 처리
        if self.state == UNO:
            self.state = NORM
            idx_ = idx%self.playerList.size()
            if self.playerList.turnPlayer().isUser == True:
                if self.playerList.prevIdx == idx_:
                    print(self.playerList.prevPlayer().playerName,'가 UNO 우노를 외쳤습니다.(이전 턴에 카드를 내서 1개가 되었습니다.)')
                else: # 그 외의 플레이어
                    print(self.playerList.idxPlayer(idx).playerName,'가', self.playerList.prevPlayer().playerName,' 의 UNO 우노를 저지했습니다.')
                    self.playerList.prevPlayer().draw(self, 1)
                    self.other_Uno = True
            else:
                if self.playerList.prevIdx == idx_:
                    print(self.playerList.prevPlayer().playerName,'가 UNO 우노를 외쳤습니다.(이전 턴에 카드를 내서 1개가 되었습니다.)')
                    self.other_Uno = True
                else: # 그 외의 플레이어
                    print(self.playerList.idxPlayer(idx).playerName,'가', self.playerList.prevPlayer().playerName,' 의 UNO 우노를 저지했습니다.')
                    self.playerList.prevPlayer().draw(self, 1)
        else:
            print('state == UNO에서만 이 메서드가 동작합니다.')
    
    def searchUserIdx(self): # 하나의 user만 있을 때 동작합니다.
        result = -1
        for i in self.playerList.lst():
            if i.isUser == True:
                result = self.playerList.lst().index(i)
                break
        
        return result
        
    def userHand(self): # 유저의 패 리스트를 반환합니다.
        result = self.playerList.idxPlayer(self.searchUserIdx()).handCardList
        
        return result
    
    def playerTurnTable(self): # 플레이어의 턴 순서를 표시하기 위한 정보를 반환합니다.    
        result = []
        for i in range(0, self.playerList.size()):
            idx = (i+self.playerList.turnIdx)%self.playerList.size()
            result.append(self.playerList.idxPlayer(idx))
        return result
 
    def unoCompeteTable(self): # 우노 경쟁을 위한 테이블을 생성합니다.

        plst = self.playerList.lst()
        time = -1
        temp = []
        
        if self.playerList.turnPlayer().isUser == True:
            time = BOT_TIME
        else:
            time = BOT_TIME
            
        for i in plst:
            if i.isUser == False:
                temp.append(random.randrange(round(time//2),round(time*4//5)))
            else:
                temp.append(time+1)
        self.botCompeteList = temp.copy()
        self.state = UNO