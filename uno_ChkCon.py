from uno_Const import * # const

def canUse(top, chk): # 카드를 낼 수 있는지 체크하는 메서드

        if (top.number == chk.number) and ((top.effectCode & NO_EFFECT) == NO_EFFECT): # 숫자 같으면 낼 수 있음
            return True
        
        if (top.color == chk.color) and (top.color != NO_COLOR): # 색깔 같아도 낼 수 있음
            return True
        
        if (top.color == NO_COLOR) and (top.applyColor == chk.color): # 바뀐 색이 같아도 낼 수 있음.
            return True
        
        if (top.number == NO_NUMBER) and (top.applyNumber == chk.number): # 바뀐 숫자가 같아도 낼 수 있음.
            return True
        
        if (chk.number == NO_NUMBER): # 색이 없는 카드는 언제든 낼 수 있음.
            return True
    
        return chk_eCode(top.effectCode, chk.effectCode)
    

def chk_eCode(top, chk):
    
    temp = top & chk
    if temp & 0B0 == 0B0:
        return False
    
    if temp & 0B01 == 0B01:
        return False
    
    return True