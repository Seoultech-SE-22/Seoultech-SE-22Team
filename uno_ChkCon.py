from uno_Const import * # 
from uno_Card import * #

def canUse(top, chk): # 카드를 낼 수 있는지 체크하는 메서드

        if (top.number == chk.number) and ((top.effectCode & NO_EFFECT) == NO_EFFECT): # 숫자 같으면 낼 수 있음
            #print(1)
            return True
        
        if (top.color == chk.color) and (top.color != NO_COLOR): # 색깔 같아도 낼 수 있음
            #print(2)
            return True
        
        if (top.color == NO_COLOR) and (top.applyColor == chk.color): # 바뀐 색이 같아도 낼 수 있음.
            #print(3)
            return True
        
        #if (top.number == NO_NUMBER) and (top.applyNumber == chk.number): # 바뀐 숫자가 같아도 낼 수 있음.
         #   print(4)
          #  return True
        
        if (chk.color == NO_COLOR): # 색이 없는 카드는 언제든 낼 수 있음.
            #print(5)
            return True
    
        return chk_eCode(top, chk)
    

def chk_eCode(top, chk):
    #print(1)
    temp = top.effectCode & chk.effectCode
    if temp & EFFECT_DRAW == EFFECT_DRAW:
        if top.attackNumber <= chk.attackNumber:
            return True
    
    if temp & EFFECT_SKIP == EFFECT_SKIP:
        return True
    
    if temp & EFFECT_REVERSE == EFFECT_REVERSE:
        return True
    
    if temp & EFFECT_COLOR == EFFECT_REVERSE:
        return True
    
    if temp & EFFECT_NUMBER == EFFECT_NUMBER:
        return True
    
    return False
