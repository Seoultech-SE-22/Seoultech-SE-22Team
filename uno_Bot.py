import random
from uno_Const import * # const

def distribution(game, mode): # 카드를 분배
    if mode == MODE_ALLCARD:
        distribution_allCard(game)
    else:
        distribution_normal(game)

def strategy(game, mode): # 봇이 선택하는 전략 
    
    if mode == MODE_COMBO:
        pass
    else:
        strategy_random(game)
    game.playerList.turnPlayer().UnoAndWinnerChecker(game)

def endEvent(game, mode): # 엔드 페이즈에 일어나는 이벤트
    if mode == MODE_CHANGECOLOR:
        event_changeColor(game)
    elif mode == MODE_OPENSHUFFLE:
        event_shuffleOpen(game)
    else:
        pass
        #print('엔드 페이즈 이벤트가 존재하지 않습니다.')


def strategy_random(game): # 전략 - 무작위 선택
    chkList = game.playerList.turnPlayer().canUseIdx(game)
    #print("무작위 전략")
    if chkList != []: # 낼 수 있는 카드가 있다면
        randIdx = random.choice(chkList) # 무작위의 카드를 내고
        useCard = game.playerList.turnPlayer().delCard(randIdx)
        game.placeOpenCardZone(useCard)
        #print( useCard.info() + "를 냅니다.")
    else:             # 낼 수 있는 카드가 없다면
        game.playerList.turnPlayer().draw(game, 1) # 카드를 뽑고
        #print("낼 카드가 없어서 1장 뽑습니다.")
    
    #print(game.playerList.turnPlayer().playerName + ": ", game.playerList.turnPlayer().allHand())
    #print()
    #print()

def strategy_combo(): # 전략 - 콤보
    pass

def distribution_normal(game): # 분배 - 평범한 케이스
    for i in game.playerList.lst(): # 각 플레이어들에게 카드를 나눠줍니다.
            i.draw(game, 5) # 나눠줄 카드의 개수 : 임의로 5로 설정했음
            print(i.playerName + ": ", i.allHand(),"\n")

def distribution_allCard(game): # 분배 - 모든 카드
    n = len(game.deckList.cardList) # 덱의 총 카드 수
    k = game.playerList.size() # 플레이어 수
    
    for i in game.playerList.lst(): # n//k개 나눠줌
        i.draw(game, n//k)
            
    for i in game.playerList.lst(): # 남은 카드 나눠줌
        i.draw(game, 1)
        if len(game.deckList.cardList) == 0: # 뽑을 카드 없으면 종료
            break

    for i in game.playerList.lst(): # 플레이어가 들고 있는 카드 보여줌
        print(i.playerName + ": ", i.allHand(),"\n")

def distribution_skillCard(): # 분배 - 높은 확률로 기술 카드를 더 받음
    pass

def event_changeColor(game): # 엔드 이벤트 - 오픈 카드의 색이 바뀜
    if game.turn%5 == 0:
        game.openCard.cardList[-1].applyColor = random.randrange(0,4)

def event_shuffleOpen(game):
    if game.turn%5 == 0:
        game.openCard.shuffle()
        topCard = game.openCard.takeTopCard()
        game.placeOpenCardZone(topCard)
        print("뒤섞")
