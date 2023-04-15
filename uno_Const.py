## game.state ##
NORM = 0
UNO = 1

### Card Attribute ###
## Color Const ##
NO_COLOR = -1
RED = 0
GREEN = 1
YELLOW = 2
BLUE = 3

COLOR_TABLE = {NO_COLOR:'black', RED:'red', GREEN:'green', YELLOW:'yellow', BLUE:'blue'}

## Number Const ##
NO_NUMBER = -1

## Skill Card Effect Const ## 이진법으로 변경
IS_EFFECT = 0B00
NO_EFFECT = 0B01
EFFECT_DRAW = 0B10
EFFECT_SKIP = 0B100
EFFECT_REVERSE = 0B1000
EFFECT_COLOR = 0B10000
EFFECT_NUMBER = 0B100000

## Time ##
USER_TIME = 15
BOT_TIME = 10

EFFECT_TIME = 10


## Bot ##
MODE_NORMAL = 0B00
MODE_COMBO = 0B01
MODE_ALLCARD = 0B10
MODE_CHANGECOLOR = 0B100

## Test

# EFFECT_NUMBER = 32
#print(type(EFFECT_NUMBER), EFFECT_NUMBER)
# NO_EFFECT & EFFECT_NUMBER = 0
#print(type(NO_EFFECT & EFFECT_NUMBER), NO_EFFECT & EFFECT_NUMBER)