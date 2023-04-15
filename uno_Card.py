from uno_Const import * # const
from Effect import effect # Effect
import uno_ChkCon # Check Condition

class Card: # 카드 클래스 생성
    ## 카드의 오리지널 데이터 ##    
    color = NO_COLOR # 0: red, 1: green, 2: yellow, 3: blue, -1: none_color_card
    number = NO_NUMBER # -1: special_card
    effectCode = NO_EFFECT # 카드가 가진 효과의 종류
    attackNumber = -1
    
    ## 카드가 게임에서 실제로 적용되는 데이터 ##
    applyColor = NO_COLOR
    applyNumber = NO_NUMBER
    
    def __init__(self, color = NO_COLOR, number = NO_NUMBER, effectCode = NO_EFFECT, attackNumber = -1): # card 클래스 생성자
        self.color = color
        self.number = number
        self.effectCode = effectCode
        self.attackNumber = attackNumber
        
        self.applyNumber = self.number # applyNumber 는 cardNumber 로 초기값 설정
        self.applyColor = self.color # applyColor 는 cardColor 로 초기값 설정

    def __del__(self): # card class 소멸자
        pass

    def cardEffect(self, game): # 특수 카드의 효과를 처리하기 위한 메서드.
       effect(self, game)
        
    def canUse(self, game):
        top = game.openCard.cardList[-1]
        result = uno_ChkCon.canUse(top, self)
        
        return result

    def reset(self):
        self.applyColor = self.color
        self.applyNumber = self.number

    def info(self): # 카드 정보 출력용 함수
        return self.imgName()
    
    def imgName(self): # 카드에 연결될 이미지의 스트링에 대한 데이터를 반환
        result = COLOR_TABLE[self.color]+'_'
        temp = ''
        if self.number != NO_NUMBER:
            temp = str(self.number)
        else:
            if self.effectCode & EFFECT_DRAW == EFFECT_DRAW:
                temp += '+' + str(self.attackNumber)
            if self.effectCode & EFFECT_SKIP == EFFECT_SKIP:
                temp += 'skip'
            if self.effectCode & EFFECT_REVERSE == EFFECT_REVERSE:
                temp += 'reverse'
            if self.effectCode & EFFECT_COLOR == EFFECT_COLOR:
                temp += 'wildColor'
            if self.effectCode & EFFECT_NUMBER == EFFECT_NUMBER:
                temp += 'wildNumber'
        result += temp
        
        return result
    
    def data(self): # Front에서 card instance의 정보를 dictionary로 확인하기 위한 메서드
        o_Col = self.color
        o_Num = self.number
        e_Code = self.effectCode
        atk_Num = self.attackNumber
        
        a_Col = self.applyColor
        a_Num = self.applyNumber
        
        result = {'orignColor': o_Col, 'orignNumber': o_Num, 'effctCode': e_Code, 'attackNumber': atk_Num, 'applyColor': a_Col,'applyNumber': a_Num}
        
        return result
    
#test code#

#c1 = Card(RED, 2)
#c2 = Card(RED, effectCode = EFFECT_DRAW+EFFECT_REVERSE, attackNumber = 2)
#c3 = Card(NO_COLOR, effectCode = EFFECT_DRAW, attackNumber = 4)

#print(c1.imgName(), c2.imgName(), c3.imgName())