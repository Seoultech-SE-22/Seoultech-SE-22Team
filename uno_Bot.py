import random


def distribution(game, mode): # 카드를 분배
    pass

def strategy(game, mode): # 봇이 선택하는 전략
    strategy_random(game)

def endEvent(game, mode): # 엔드 페이즈에 일어나는 이벤트
    pass


def strategy_random(game): # 전략 - 무작위 선택
    chkList = game.playerList.turnPlayer().canUseIdx(game)
    print("무작위 전략")
    if chkList != []: # 낼 수 있는 카드가 있다면
        randIdx = random.choice(chkList) # 무작위의 카드를 내고
        useCard = game.playerList.turnPlayer().delCard(randIdx)
        game.placeOpenCardZone(useCard)
        print( useCard.info() + "를 냅니다.")
    else:             # 낼 수 있는 카드가 없다면
        game.playerList.turnPlayer().draw(game, 1) # 카드를 뽑고
        print("낼 카드가 없어서 1장 뽑습니다.")
    
    print(game.playerList.turnPlayer().playerName + ": ", game.playerList.turnPlayer().allHand())
    print()
    print()

def strategy_combo(): # 전략 - 콤보
    pass

def distribution_allCard(): # 분배 - 모든 카드
    pass

def distribution_skillCard(): # 분배 - 높은 확률로 기술 카드를 더 받음
    pass

def event_changeColor(): # 이벤트 - 카드의 색이 바뀜
    pass