import configparser

import pygame
import os
from uno_Player import *
from unoCore import Game
from uno_Card import *
from uno_Pile import *
from uno_Const import *
from main import init_bg
from view import init_view
from text import Text
from button import Button
from screenSupporter import sliceRect
import configparser
from start_Object import *

bgm_volume = 1
click_volume = 1

check_os = True

start_color_weakness_value = False

config = configparser.ConfigParser()
config.read(os.getcwd() + "/img/" + 'config.ini', encoding='utf-8')

font = pygame.font.SysFont(None, 30)

def save_config():
    with open('config.ini', 'w', encoding='utf-8') as config_file:
        config.write(config_file)


def start(screen, screen_width, screen_height, num, name, color_weakness_value, mode):
    global start_color_weakness_value
    start_color_weakness_value = color_weakness_value
    screen_size = (screen_width, screen_height)
    screen = pygame.display.set_mode(screen_size)
    x_pos = screen_width / 2
    y_pos = screen_height / 2

    screen.fill((0, 0, 0))
    screen = pygame.display.set_mode(screen_size)

    user1 = Player(name[0], True)
    gamePlayerList = [user1]
    for i in range(1, num + 1):
        gamePlayerList.append(Player(name[i], False))
    g = Game(gamePlayerList, mode=mode)

    g.ready(screen_size)

    playerCardPage = 0
    nowCardIdx = 0
    ch = CardHolder(8)

    clock = pygame.time.Clock()
    global bgm
    global bet_card
    global cannot_bet
    global card_draw
    bgm = pygame.mixer.Sound("bgm.mp3")
    bgm.play(-1)
    bet_card = pygame.mixer.Sound("bet_card.wav")
    cannot_bet = pygame.mixer.Sound("cannot_bet.wav")
    card_draw = pygame.mixer.Sound("card_draw.mp3")

    while True:
        ##### 화면 초기화 #####
        screen.fill((0, 0, 0))
        screen_rect = (0, 0, screen_width, screen_height)
        
        slice_screen = sliceRect(screen_rect, [3, 2], 'vertical')
        bot_rect = slice_screen[1]
        pygame.draw.rect(screen, (120, 120, 0), bot_rect)
        
        
        slice_leftover = sliceRect(slice_screen[0], [3, 2], 'horizontal')
        user_rect = slice_leftover[1]
        pygame.draw.rect(screen, (120, 120, 120), user_rect)
        
        slice_userSpace = sliceRect(user_rect, [1, 1], 'horizontal')
        user_rect_u = slice_userSpace[0]
        pygame.draw.rect(screen, (120, 200, 100), user_rect_u)
        
        slice_cardSlot = sliceRect(slice_userSpace[1], [1, 8, 1], 'vertical')
        user_lBtn_rect = slice_cardSlot[0]
        user_cardZone_rect = slice_cardSlot[1]
        user_rBtn_rect = slice_cardSlot[2]

        pygame.draw.rect(screen, (0, 0, 255), user_lBtn_rect)
        pygame.draw.rect(screen, (0, 170, 255), user_cardZone_rect)
        pygame.draw.rect(screen, (0, 0, 255), user_rBtn_rect)

       

        board_rect = slice_leftover[0]
        pygame.draw.rect(screen, (25, 150, 75), board_rect)

        ##### slot_Area #####

        pSlotList = []

        for i in range(g.playerList.size()):  # player Slot
            ps = playerSlot(screen, i, g.playerList.idxPlayer(i), bot_rect)
            pSlotList.append(ps)

        turnIdx = g.playerList.turnIdx
        turnArrow(screen, pSlotList[turnIdx], g.playerList.direction)  # 턴 방향 표시

        ##### slot_Area #####

        ##### user_Area #####
        ch.update(g.userHand())
        cardHolderDict = {'lbtn': user_lBtn_rect, 'rbtn': user_rBtn_rect, 'cardZone': user_cardZone_rect} 
        cardHolder = veiwCardHolder(screen, ch, g ,cardHolderDict, start_color_weakness_value) 

        ##### user_Area #####

        ##### board_Area #####

        openCardIndicator(screen, g, board_rect, start_color_weakness_value)  # openCard
        createIndicator(screen, g.openCard.cardList[-1], board_rect, start_color_weakness_value)  # indicator
        createDeck(screen, g, board_rect)  # deck

        actlist = g.actList()
        # drawbtn

        dbtn = createDrawBtn(screen, g, board_rect)  # draw 버튼
        ubtn = createUnoBtn(screen, g, board_rect)  # uno 버튼
        
        if g.is_effctTime == False:    
            timerInd(screen, board_rect, g.timer.time)
        else:
            eTimerInd(screen, board_rect, g.effectTimer.time)
        turnInd(screen, board_rect, g.turn)

        g.update()

        # botHand(screen, screen_size, pc1)
        pause_button = Button(image=pygame.image.load("pause_button.png"),
                              pos=(30, 30),
                              size=(50, 50))
        init_view(screen, [pause_button])

        cbtn = createColorBtn(board_rect, start_color_weakness_value)

        # colorChangebtn
        if actlist['colorBtn']:
            init_view(screen, cbtn)
        # numberChangebtn
        if actlist['numberBtn']:
            pass

        ##### board_Area #####

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            eventCardHolder(ch, cardHolder, g, event ,config) # cardHolder
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(0, len(cbtn)):  # 색깔 바꾸는 버튼
                    if cbtn[i].rect.collidepoint(event.pos):
                        g.eventColorBtn(i)

                if dbtn.rect.collidepoint(event.pos):  # 드로우 버튼
                    if actlist['drawBtn']:  # actList가 true인 경우에만 함수 실행
                        g.eventDrawBtn()
                elif ubtn.rect.collidepoint(event.pos):  # 우노 버튼
                    if actlist['unoBtn']:  # actList가 true인 경우에만 함수 실행
                        g.eventUnoBtn()
                elif pause_button.rect.collidepoint(event.pos):
                    resolution = pause(screen, 1280, 720, screen_width)
                    screen_width = resolution[0]
                    screen_height = resolution[1]
                    pygame.display.set_mode((screen_width, screen_height))
                    cardHolder = veiwCardHolder(screen, ch, g ,cardHolderDict, start_color_weakness_value) # cardHolder
                    openCardIndicator(screen, g, board_rect, start_color_weakness_value)  # openCard
                    createIndicator(screen, g.openCard.cardList[-1], board_rect, start_color_weakness_value)  # indicator
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    resolution = pause(screen, 1280, 720, screen_width)
                    # print(resolution[0])
                    # print(resolution[1])
                    # userH = createCards(screen, g.userHand(), g, user_cardZone_rect, playerCardPage, nowCardIdx,
                    #                     start_color_weakness_value)
                    # openCardIndicator(screen, g, board_rect, start_color_weakness_value)  # openCard
                    # createIndicator(screen, g.openCard.cardList[-1], board_rect,
                    #                 start_color_weakness_value)  # indicator
                
                elif ("pygame.K_"+pygame.key.name(event.key)).upper() == (config['system']['DRAW']).upper():
                    if actlist['drawBtn']:  # actList가 true인 경우에만 함수 실행
                        g.eventDrawBtn()

        pygame.display.flip()

        if g.winner != None:
            winner_screen(screen, screen_width, screen_height, g.winner.playerName)

        clock.tick(60)


def pause(screen, screen_width, screen_height, width):
    global bgm_volume, check_os
    global click_volume
    global start_color_weakness_value
    global UNO, SELECT, LEFT, RIGHT, DRAW, height
    button_width = 220
    button_height = 50
    pygame.display.set_mode((screen_width, screen_height))
    resolution = width

    x_pos = screen_width / 2 - button_width / 2
    y_pos = screen_height / 2 - button_height / 2
    back_button = Button(image=pygame.image.load("back_button.png"),
                         pos=(30, 30),
                         size=(50, 50))

    master_volume_up_button = Button(image=pygame.image.load("volume_up_button.png"),
                                     pos=(screen.get_rect().centerx - 120, screen.get_rect().centery - 280),
                                     size=(100, 46))
    master_volume_down_button = Button(image=pygame.image.load("volume_down_button.png"),
                                       pos=(screen.get_rect().centerx + 30, screen.get_rect().centery - 280),
                                       size=(100, 46))

    bgm_volume_up_button = Button(image=pygame.image.load("volume_up_button.png"),
                                  pos=(screen.get_rect().centerx - 480, screen.get_rect().centery - 280),
                                  size=(100, 46))
    bgm_volume_down_button = Button(image=pygame.image.load("volume_down_button.png"),
                                    pos=(screen.get_rect().centerx - 330, screen.get_rect().centery - 280),
                                    size=(100, 46))

    click_volume_up_button = Button(image=pygame.image.load("volume_up_button.png"),
                                    pos=(screen.get_rect().centerx + 250, screen.get_rect().centery - 280),
                                    size=(100, 46))
    click_volume_down_button = Button(image=pygame.image.load("volume_down_button.png"),
                                      pos=(screen.get_rect().centerx + 400, screen.get_rect().centery - 280),
                                      size=(100, 46))

    on_button = Button(image=pygame.image.load("on.png"),
                       pos=(screen.get_rect().centerx - 150, screen.get_rect().centery - 170),
                       size=(100, 46))
    off_button = Button(image=pygame.image.load("off.png"),
                        pos=(screen.get_rect().centerx + 50, screen.get_rect().centery - 170),
                        size=(100, 46))

    exit_button = Button(image=pygame.image.load("exit_button.png"),
                         pos=(x_pos, y_pos + 320),
                         size=(button_width, button_height))

    button_1920 = Button(image=pygame.image.load("1920_button.png"),
                         pos=(screen.get_rect().centerx - 250, screen.get_rect().centery - 60),
                         size=(100, 46))
    button_1280 = Button(image=pygame.image.load("1280_button.png"),
                         pos=(screen.get_rect().centerx - 50, screen.get_rect().centery - 60),
                         size=(100, 46))
    button_960 = Button(image=pygame.image.load("960_button.png"),
                        pos=(screen.get_rect().centerx + 110, screen.get_rect().centery - 60),
                        size=(100, 46))

    master_volume_set_text = Text(text_input="Set master volume",
                                  font="notosanscjkkr",
                                  color=(0, 0, 0),
                                  pos=(screen.get_rect().centerx, screen.get_rect().top + 50),
                                  size=30,
                                  screen=screen)
    bgm_volume_set_text = Text(text_input="Set BGM volume",
                               font="notosanscjkkr",
                               color=(0, 0, 0),
                               pos=(screen.get_rect().centerx - 350, screen.get_rect().top + 50),
                               size=30,
                               screen=screen)

    click_volume_set_text = Text(text_input="Set click volume",
                                 font="notosanscjkkr",
                                 color=(0, 0, 0),
                                 pos=(screen.get_rect().centerx + 370, screen.get_rect().top + 50),
                                 size=30,
                                 screen=screen)

    color_weakness_mode_text = Text(text_input="Color Weakness Mode",
                                    font="notosanscjkkr",
                                    color=(0, 0, 0),
                                    pos=(screen.get_rect().centerx, screen.get_rect().top + 170),
                                    size=30,
                                    screen=screen)

    resolution_text = Text(text_input="Resolution",
                           font="notosanscjkkr",
                           color=(0, 0, 0),
                           pos=(screen.get_rect().centerx, screen.get_rect().top + 270),
                           size=30,
                           screen=screen)
    key_setting_text = Text(text_input="Key Setting",
                            font="notosanscjkkr",
                            color=(0, 0, 0),
                            pos=(screen.get_rect().centerx, screen.get_rect().top + 390),
                            size=30,
                            screen=screen)

    if start_color_weakness_value == True: 
        on_button.image = pygame.image.load("on_checked.png")
        off_button.image = pygame.image.load("off.png")
    else:
        on_button.image = pygame.image.load("on.png")
        off_button.image = pygame.image.load("off_checked.png")
    if width == 1920:
        button_1920.image = pygame.image.load("1920_checked.png")
        button_1280.image = pygame.image.load("1280_button.png")
        button_960.image = pygame.image.load("960_button.png")
    elif width == 1280:
        button_1920.image = pygame.image.load("1920_button.png")
        button_1280.image = pygame.image.load("1280_checked.png")
        button_960.image = pygame.image.load("960_button.png")
    elif width == 960:
        button_1920.image = pygame.image.load("1920_button.png")
        button_1280.image = pygame.image.load("1280_button.png")
        button_960.image = pygame.image.load("960_checked.png")

    bool = True
    screen.fill("black")
    options_bg = init_bg("options_screen.png", 1280, 720)
    while bool:
        screen.blit(options_bg, (0, 0))
        init_view(screen, [back_button, exit_button,
                           master_volume_up_button, master_volume_down_button,
                           bgm_volume_up_button, bgm_volume_down_button,
                           click_volume_up_button, click_volume_down_button,
                           on_button, off_button,
                           button_1920, button_1280, button_960])
        master_volume_set_text.init_text()
        bgm_volume_set_text.init_text()
        click_volume_set_text.init_text()
        color_weakness_mode_text.init_text()
        resolution_text.init_text()
        key_setting_text.init_text()

        UNO = eval(f"{config['system']['UNO']}")
        SELECT = eval(f"{config['system']['SELECT']}")
        LEFT = eval(f"{config['system']['LEFT_MOVE']}")
        RIGHT = eval(f"{config['system']['RIGHT_MOVE']}")
        DRAW = eval(f"{config['system']['DRAW']}")

        # 키 설정
        key_setting_bg = pygame.image.load("key_button.png")
        key_setting_bg = pygame.transform.scale(key_setting_bg, (80, 80))
        # 우노 버튼 설정
        Uno_button_rect = key_setting_bg.get_rect()
        Uno_button_rect.centerx = screen.get_rect().centerx - 200
        Uno_button_rect.centery = screen.get_rect().top + 480
        Uno_text = font.render(pygame.key.name(UNO), True, (0, 0, 0))
        Uno_rect = Uno_text.get_rect()
        Uno_rect.centerx = Uno_button_rect.centerx
        Uno_rect.centery = Uno_button_rect.centery
        # 선택 버튼 설정
        Select_button_rect = key_setting_bg.get_rect()
        Select_button_rect.centerx = screen.get_rect().centerx - 100
        Select_button_rect.centery = screen.get_rect().top + 480
        Select_text = font.render(pygame.key.name(SELECT), True, (0, 0, 0))
        Select_rect = Select_text.get_rect()
        Select_rect.centerx = Select_button_rect.centerx
        Select_rect.centery = Select_button_rect.centery
        # 왼쪽 이동 버튼 설정
        L_button_rect = key_setting_bg.get_rect()
        L_button_rect.centerx = screen.get_rect().centerx
        L_button_rect.centery = screen.get_rect().top + 480
        L_text = font.render(pygame.key.name(LEFT), True, (0, 0, 0))
        L_rect = L_text.get_rect()
        L_rect.centerx = L_button_rect.centerx
        L_rect.centery = L_button_rect.centery
        # 오른쪽 이동 버튼 설정
        R_button_rect = key_setting_bg.get_rect()
        R_button_rect.centerx = screen.get_rect().centerx + 100
        R_button_rect.centery = screen.get_rect().top + 480
        R_text = font.render(pygame.key.name(RIGHT), True, (0, 0, 0))
        R_rect = R_text.get_rect()
        R_rect.centerx = R_button_rect.centerx
        R_rect.centery = R_button_rect.centery
        # 드로우 버튼 설정
        Draw_button_rect = key_setting_bg.get_rect()
        Draw_button_rect.centerx = screen.get_rect().centerx + 200
        Draw_button_rect.centery = screen.get_rect().top + 480
        Draw_text = font.render(pygame.key.name(DRAW), True, (0, 0, 0))
        Draw_rect = Draw_text.get_rect()
        Draw_rect.centerx = Draw_button_rect.centerx
        Draw_rect.centery = Draw_button_rect.centery

        screen.blit(key_setting_bg, Uno_button_rect)
        screen.blit(Uno_text, Uno_rect)
        screen.blit(key_setting_bg, Select_button_rect)
        screen.blit(Select_text, Select_rect)
        screen.blit(key_setting_bg, L_button_rect)
        screen.blit(L_text, L_rect)
        screen.blit(key_setting_bg, R_button_rect)
        screen.blit(R_text, R_rect)
        screen.blit(key_setting_bg, Draw_button_rect)
        screen.blit(Draw_text, Draw_rect)

        uno_text = Text(text_input="UNO",
                        font="notosanscjkkr",
                        color=(0, 0, 0),
                        pos=(screen.get_rect().centerx - 200, screen.get_rect().top + 420),
                        size=25,
                        screen=screen)
        return_text = Text(text_input="RETURN",
                           font="notosanscjkkr",
                           color=(0, 0, 0),
                           pos=(screen.get_rect().centerx - 100, screen.get_rect().top + 420),
                           size=25,
                           screen=screen)

        left_move_text = Text(text_input="LEFT",
                              font="notosanscjkkr",
                              color=(0, 0, 0),
                              pos=(screen.get_rect().centerx, screen.get_rect().top + 420),
                              size=25,
                              screen=screen)
        right_move_text = Text(text_input="RIGHT",
                               font="notosanscjkkr",
                               color=(0, 0, 0),
                               pos=(screen.get_rect().centerx + 100, screen.get_rect().top + 420),
                               size=25,
                               screen=screen)
        draw_text = Text(text_input="DRAW",
                               font="notosanscjkkr",
                               color=(0, 0, 0),
                               pos=(screen.get_rect().centerx + 200, screen.get_rect().top + 420),
                               size=25,
                               screen=screen)

        uno_text.init_text()
        return_text.init_text()
        left_move_text.init_text()
        right_move_text.init_text()
        draw_text.init_text()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    if resolution==1920:
                        return [1920, 1080]
                    elif resolution == 1280:
                        return [1280, 720]
                    elif resolution == 960:
                        return [960, 540]
                elif master_volume_up_button.rect.collidepoint(event.pos):
                    bgm_volume += 0.1
                    click_volume += 0.1
                    bgm.set_volume(bgm_volume)
                    bet_card.set_volume(click_volume)
                    card_draw.set_volume(click_volume)
                    cannot_bet.set_volume(click_volume)
                elif master_volume_down_button.rect.collidepoint(event.pos):
                    bgm_volume -= 0.1
                    click_volume -= 0.1
                    bgm.set_volume(bgm_volume)
                    bet_card.set_volume(click_volume)
                    card_draw.set_volume(click_volume)
                    cannot_bet.set_volume(click_volume)
                elif bgm_volume_up_button.rect.collidepoint(event.pos):
                    bgm_volume += 0.1
                    bgm.set_volume(bgm_volume)
                elif bgm_volume_down_button.rect.collidepoint(event.pos):
                    bgm_volume -= 0.1
                    bgm.set_volume(bgm_volume)
                elif click_volume_up_button.rect.collidepoint(event.pos):
                    click_volume += 0.1
                    bet_card.set_volume(click_volume)
                    card_draw.set_volume(click_volume)
                    cannot_bet.set_volume(click_volume)
                elif click_volume_down_button.rect.collidepoint(event.pos):
                    click_volume -= 0.1
                    bet_card.set_volume(click_volume)
                    card_draw.set_volume(click_volume)
                    cannot_bet.set_volume(click_volume)
                elif exit_button.rect.collidepoint(event.pos):
                    bgm.stop()
                    if check_os == True:
                        file_path = os.getcwd()
                        dir_path = os.path.dirname(file_path)
                        os.chdir(dir_path)
                        check_os = False
                    from main_screen import main_screen
                    main_screen()
                elif button_1920.rect.collidepoint(event.pos):
                    resolution = 1920
                    button_1920.image = pygame.image.load("1920_checked.png")
                    button_1280.image = pygame.image.load("1280_button.png")
                    button_960.image = pygame.image.load("960_button.png")
                elif button_1280.rect.collidepoint(event.pos):
                    resolution = 1280
                    button_1920.image = pygame.image.load("1920_button.png")
                    button_1280.image = pygame.image.load("1280_checked.png")
                    button_960.image = pygame.image.load("960_button.png")
                elif button_960.rect.collidepoint(event.pos):
                    resolution = 960
                    button_1920.image = pygame.image.load("1920_button.png")
                    button_1280.image = pygame.image.load("1280_button.png")
                    button_960.image = pygame.image.load("960_checked.png")
                elif on_button.rect.collidepoint(event.pos):
                    print("on")
                    on_button.image = pygame.image.load("on_checked.png")
                    off_button.image = pygame.image.load("off.png")
                    config['system']['COLOR_WEAKNESS_MODE'] = "True"
                    save_config()
                    start_color_weakness_value = True
                elif off_button.rect.collidepoint(event.pos):
                    on_button.image = pygame.image.load("on.png")
                    off_button.image = pygame.image.load("off_checked.png")
                    config['system']['COLOR_WEAKNESS_MODE'] = "False"
                    save_config()
                    start_color_weakness_value = False
                elif Uno_button_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Press the key for Uno direction")
                    UNO = key_change()
                    if pygame.key.name(UNO) == 'up' or pygame.key.name(UNO) == 'right' or pygame.key.name(
                            UNO) == 'left' or pygame.key.name(UNO) == 'return':
                        config['system']['UNO'] = 'pygame.K_' + (pygame.key.name(UNO)).upper()
                    else:
                        config['system']['UNO'] = 'pygame.K_' + pygame.key.name(UNO)
                    save_config()
                elif Select_button_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Press the key for Select direction")
                    SELECT = key_change()
                    pygame.key.name(SELECT)
                    if pygame.key.name(SELECT) == 'up' or pygame.key.name(SELECT) == 'right' or pygame.key.name(SELECT) == 'left' or pygame.key.name(SELECT) == 'return':
                        config['system']['SELECT'] = 'pygame.K_' + (pygame.key.name(SELECT)).upper()
                    else:
                        config['system']['SELECT'] = 'pygame.K_' + pygame.key.name(SELECT)
                    save_config()
                elif L_button_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Press the key for LEFT direction")
                    LEFT = key_change()
                    pygame.key.name(LEFT)
                    if pygame.key.name(LEFT) == 'up' or pygame.key.name(LEFT) == 'right' or pygame.key.name(LEFT) == 'left' or pygame.key.name(LEFT) == 'return':
                        config['system']['LEFT_MOVE'] = 'pygame.K_' + (pygame.key.name(LEFT)).upper()
                    else:
                        config['system']['LEFT_MOVE'] = 'pygame.K_' + pygame.key.name(LEFT)
                    save_config()
                elif R_button_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Press the key for RIGHT direction")
                    RIGHT = key_change()
                    if pygame.key.name(RIGHT)=='up' or pygame.key.name(RIGHT)=='right' or pygame.key.name(RIGHT)=='left' or pygame.key.name(RIGHT) == 'return':
                        config['system']['RIGHT_MOVE'] = 'pygame.K_' + (pygame.key.name(RIGHT)).upper()
                    else:
                        config['system']['RIGHT_MOVE'] = 'pygame.K_' + pygame.key.name(RIGHT)
                    save_config()
                elif Draw_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Press the key for DRAW")
                    DRAW = key_change()
                    if pygame.key.name(DRAW) == 'up' or pygame.key.name(DRAW) == 'right' or pygame.key.name(
                            DRAW) == 'left' or pygame.key.name(DRAW) == 'return':
                        config['system']['DRAW'] = 'pygame.K_' + (pygame.key.name(DRAW)).upper()
                    else:
                        config['system']['DRAW'] = 'pygame.K_' + pygame.key.name(DRAW)
                    save_config()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bool = False
        pygame.display.flip()

def key_change():
    tmp = 0
    # 바꿀 조작키 입력 루프
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            tmp = event.key
            if tmp == UNO or tmp == SELECT or tmp == LEFT or tmp == RIGHT or tmp == DRAW:
                print("used key")
            else:
                break
    return tmp


##### winner_sreen #####
def winner_screen(screen, screen_width, screen_height, winner):
    global check_os
    screen_size = (screen_width, screen_height)
    screen = pygame.display.set_mode(screen_size)
    screen.fill("black")

    winner_bg = init_bg("options_screen.png", screen_width, screen_height)
    screen.blit(winner_bg, (0, 0))

    button_width = 220
    button_height = 50

    x_pos = screen_width / 2 - button_width / 2
    y_pos = screen_height / 2 - button_height / 2

    play_button = Button(image=pygame.image.load("play_button.png"),
                         pos=(x_pos, y_pos + 200),
                         size=(button_width, button_height))
    winnername_text = Text(text_input=winner + ' is winner!',
                           font=None,
                           color=(0, 0, 0),
                           pos=(screen.get_rect().centerx, screen.get_rect().top + 100),
                           size=screen_height // 5,
                           screen=screen)
    winnername_text.init_text()
    init_view(screen, [play_button])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(event.pos):
                    print("game start")
                    if check_os == True:
                        file_path = os.getcwd()
                        dir_path = os.path.dirname(file_path)
                        os.chdir(dir_path)
                        check_os = False
                    from main_screen import main_screen
                    main_screen()
        pygame.display.flip()


##### winner_sreen #####

def createOneCard(card_o, pos_o, size_o, start_color_weakness_value):
    c = card_o
    if start_color_weakness_value == False:
        c_img = f"images/" + c.imgName() + ".png"
    elif start_color_weakness_value == True:
        c_img = f"blind_images/" + c.imgName() + ".png"
    btn = Button(image=pygame.image.load(c_img), pos=pos_o, size=size_o)
    return btn


def createBackCard(pos_o, size_o, ):
    c_img = f"images/back.png"
    btn = Button(image=pygame.image.load(c_img), pos=pos_o, size=size_o)
    return btn


##### card generator #####
def createBackCards(card_lst, rect):
    temp = []
    for i in range(0, len(card_lst)):
        x = rect[2] / 8 * 0.8
        y = x * 1.2
        c_pos = (rect[0] + (x * 1.1) * i, rect[1])
        temp.append(createBackCard(c_pos, (x, y)))
    return temp


##### card generator #####

##### CardHolder #####

def veiwCardHolder(screen, cardHolder, game ,rectDict, start_color_weakness_value):
    
    ## rect ##
    lbtn = rectDict['lbtn']
    rbtn = rectDict['rbtn']
    cardZone = rectDict['cardZone']
    
    ## bg ##
    pygame.draw.rect(screen, (0, 0, 255), lbtn)
    pygame.draw.rect(screen, (0, 170, 255), cardZone)
    pygame.draw.rect(screen, (0, 0, 255), rbtn)
    
    temp = []
    result = {}
    btn = None
    size_x = cardZone[2]/8
    size_y = size_x * 1.2

    pos_x = cardZone[0]
    pos_y = cardZone[1] + size_y/4

    
    cardList = cardHolder.show()

    for i in range(len(cardList)):
        pos_o = (pos_x + size_x * i, pos_y)
        size_o = (size_x, size_y)
        if cardList[i].canUse(game):
            pos_o = (pos_o[0], cardZone[1])
        temp.append(createOneCard(cardList[i], pos_o, size_o, start_color_weakness_value))
        if cardHolder.realIdx(i) == cardHolder.nowIdx:
            btn = Button(image=pygame.image.load(f"select.png"), pos=pos_o, size=size_o)
    
    init_view(screen, temp)
    if btn != None:
        init_view(screen, [btn])
            
    centerL = rectCenter(lbtn)
    centerR = rectCenter(rbtn)

    size_lx, size_ly = lbtn[2], lbtn[2]  
    pos_lx, pos_ly = lbtn[0], centerL[1] - lbtn[2] / 2
    rectL = (pos_lx, pos_ly, size_lx, size_ly)
    pygame.draw.rect(screen, (255, 255, 255), rectL)
    lbtn = Button(image=pygame.image.load(f"leftArrow.png"), pos=(rectL[0], rectL[1]), size=(rectL[2], rectL[3]))
    
    size_rx, size_ry = rbtn[2], rbtn[2]
    pos_rx, pos_ry = rbtn[0], centerR[1] - rbtn[2] / 2
    rectR = (pos_rx, pos_ry, size_rx, size_ry)
    pygame.draw.rect(screen, (255, 255, 255), rectR)
    rbtn = Button(image=pygame.image.load(f"rightArrow.png"), pos=(rectR[0], rectR[1]), size=(rectR[2], rectR[3]))
    
    init_view(screen, [lbtn, rbtn])
    result['cards'] = temp
    result['lbtn'] = lbtn
    result['rbtn'] = rbtn
    

    return result

def eventCardHolder(cardHolder, rectDict, game, event ,config):
    
    ## rect ##
    cards = rectDict['cards'] 
    lbtn = rectDict['lbtn']
    rbtn = rectDict['rbtn']
    
    ## sound ##
    bet_card = pygame.mixer.Sound("bet_card.wav")
    cannot_bet = pygame.mixer.Sound("cannot_bet.wav")
    

    ## mouse ##
    if event.type == pygame.MOUSEBUTTONDOWN:
        for i in range(0, len(cards)):
            if cards[i].rect.collidepoint(event.pos):  # 카드 버튼
                played = game.eventCardBtn(cardHolder.realIdx(i))
                if played:
                    print("낼 수 있는 카드")
                    bet_card.play(0)
                    if len(cardHolder.userHand) == cardHolder.nowIdx:    
                        cardHolder.decIdx()
                else:
                    print("낼 수 없는 카드")
                    cannot_bet.play(0)
    
        if lbtn.rect.collidepoint(event.pos):  # 페이지 -1
            cardHolder.pageDown()
    
        if rbtn.rect.collidepoint(event.pos):  # 페이지 +1
            cardHolder.pageUp()
            
    mouse_pos = pygame.mouse.get_pos()
    for i in range(0, len(cards)):  # 마우스 감지
        if cards[i].rect.collidepoint(mouse_pos):
            cardHolder.nowIdx = cardHolder.realIdx(i)
    
    ## keyborad ##
    
    if event.type == pygame.KEYDOWN:
        if ("pygame.K_"+pygame.key.name(event.key)).upper() == (config['system']['LEFT_MOVE']).upper():
            print(config['system']['left_move']) # -1칸
            cardHolder.decIdx()
        
        elif ("pygame.K_"+pygame.key.name(event.key)).upper() == (config['system']['RIGHT_MOVE']).upper():
            print(config['system']['RIGHT_MOVE']) # +1칸
            cardHolder.incIdx()
        
        elif ("pygame.K_"+pygame.key.name(event.key)).upper() == (config['system']['SELECT']).upper():
            played = game.eventCardBtn(cardHolder.nowIdx)
            if played:
                print("낼 수 있는 카드")
                bet_card.play(0)
                if len(cardHolder.userHand) == cardHolder.nowIdx:    
                    cardHolder.decIdx()
            else:
                print("낼 수 없는 카드")
                cannot_bet.play(0)
    
##### CardHolder #####


##### board space #####

def openCardIndicator(screen, game, rect, start_color_weakness_value):
    topCard = game.openCard.cardList[-1]  # openCard

    center = rectCenter(rect)
    pos_o = (center[0], center[1])
    size_o = (rect[2] * 0.1, rect[2] * 0.1 * 1.2)
    topC = createOneCard(topCard, pos_o, size_o, start_color_weakness_value)
    init_view(screen, [topC])


def createIndicator(screen, card_o, rect, start_color_weakness_value):
    c = card_o
    txt = COLOR_TABLE2[c.applyColor]
    if start_color_weakness_value == False:
        c_img = f"images/" + txt + ".png"
    elif start_color_weakness_value == True:
        c_img = f"blind_images/" + txt + ".png"

    center = rectCenter(rect)
    pos_o = (center[0] + rect[2] * 0.1, center[1])
    size_o = (rect[2] * 0.1, rect[2] * 0.1 * 1.2)

    btn = Button(image=pygame.image.load(c_img), pos=pos_o, size=size_o)
    init_view(screen, [btn])


def createDeck(screen, game, rect):
    if len(game.deckList.cardList) == 0:
        pass
    else:
        center = rectCenter(rect)
        pos_o = (center[0] - rect[2] * 0.1, center[1])
        size_o = (rect[2] * 0.1, rect[2] * 0.1 * 1.2)
        btn = createBackCard(pos_o, size_o)
        init_view(screen, [btn])


def createDrawBtn(screen, game, rect):
    center = rectCenter(rect)
    pos_o = (center[0] - rect[2] * 0.1, center[1] + rect[2] * 0.1 * 1.2 * 0.25)
    size_o = (rect[2] * 0.1, rect[2] * 0.1 * 1.2)
    btn = createBackCard(pos_o, size_o)
    if game.actList()['drawBtn']:
        init_view(screen, [btn])

    return btn


def createUnoBtn(screen, game, rect):
    center = rectCenter(rect)
    pos_o = (center[0] - rect[2] * 0.1, center[1] - rect[2] * 0.1)
    size_o = (rect[2] * 0.1, rect[2] * 0.1)
    btn = Button(image=pygame.image.load(f"UNO.png"), pos=pos_o, size=size_o)
    if game.actList()['unoBtn']:
        init_view(screen, [btn])

    return btn


def timerInd(screen, rect, time):
    size_x = round(rect[2] / 20)
    size_y = size_x

    center = rectCenter(rect)
    pos_x = center[0] - size_x * 1.2
    pos_y = (rect[1] + center[1]) / 2

    Area = (pos_x, pos_y, size_x, size_y)
    pygame.draw.rect(screen, (255, 255, 255), Area)

    font_size = size_y
    font = pygame.font.Font(None, font_size)

    center = rectCenter(Area)
    text = font.render(str(time // 60), True, (0, 0, 0))
    screen.blit(text, (center[0] - text.get_width() / 2, center[1] - text.get_height() / 2))
    
def turnInd(screen, rect, turn):
    size_x = round(rect[2] / 20)
    size_y = size_x

    center = rectCenter(rect)
    pos_x = center[0] - size_x * 1.2
    pos_y = (rect[1] + center[1]) / 2 - size_x * 1.2

    Area = (pos_x, pos_y, size_x, size_y)
    pygame.draw.rect(screen, (255, 255, 255), Area)

    font_size = size_y
    font = pygame.font.Font(None, font_size)

    center = rectCenter(Area)
    text = font.render(str(turn+1), True, (0, 0, 0))
    screen.blit(text, (center[0] - text.get_width() / 2, center[1] - text.get_height() / 2))

    return Area


def eTimerInd(screen, rect, time):
    size_x = round(rect[2] / 20)
    size_y = size_x

    center = rectCenter(rect)
    pos_x = center[0]
    pos_y = (rect[1] + center[1]) / 2

    Area = (pos_x, pos_y, size_x, size_y)
    pygame.draw.rect(screen, (255, 255, 255), Area)

    font_size = size_y
    font = pygame.font.Font(None, font_size)

    center = rectCenter(Area)
    text = font.render(str(time // 60), True, (0, 0, 0))
    screen.blit(text, (center[0] - text.get_width() / 2, center[1] - text.get_height() / 2))

    return Area


##### board space #####


##### bot space #####

def playerSlotBG(screen, offset, player, rect):
    pos_x = rect[0] + rect[2] * 0.01
    pos_y = rect[1] + (offset * rect[3] / 6) + rect[3] * 0.01

    size_x = rect[2] * 0.98
    size_y = round(0.92 * rect[3] / 6)

    bgArea = (pos_x, pos_y, size_x, size_y)

    if player.isUser:
        pygame.draw.rect(screen, (0, 0, 0), bgArea)
    else:
        pygame.draw.rect(screen, (75, 75, 75), bgArea)

    return bgArea


def nameSlot(screen, rect, player):
    size_x = round(rect[2] / 5)
    size_y = round(rect[3] * 1 / 5)

    pos_x = rect[0]
    pos_y = rect[1] + rect[3] - size_y

    nameArea = (pos_x, pos_y, size_x, size_y)
    pygame.draw.rect(screen, (255, 255, 255), nameArea)

    font_size = size_y
    font = pygame.font.Font(None, font_size)

    center = rectCenter(nameArea)
    text = font.render(player.playerName, True, (0, 0, 0))
    screen.blit(text, (center[0] - text.get_width() / 2, center[1] - text.get_height() / 2))

    return nameArea


def effectSlot(screen, rect, player):
    pos_x = rect[0]
    pos_y = rect[1]

    size_x = round(rect[2] / 5)
    size_y = round(rect[3] * 4 / 5)

    effectArea = (pos_x, pos_y, size_x, size_y)
    pygame.draw.rect(screen, (200, 200, 200), effectArea)

    return effectArea


def playerSlot(screen, idx, player, rect):
    slotBg = playerSlotBG(screen, idx, player, rect)
    slotName = nameSlot(screen, slotBg, player)

    slotEffect = effectSlot(screen, slotBg, player)

    card_anchor = (slotEffect[0] + slotEffect[2], slotEffect[1] + slotEffect[3] // 3, slotBg[2], slotBg[3])

    numOfCard = len(player.handCardList)
    capacity = int((slotBg[2] - slotEffect[2]) / (slotBg[2] / 8 * 0.8)) - 1
    if numOfCard > capacity:
        temp = []
        for i in range(capacity):
            temp.append(Card(0, 0, NO_EFFECT))
        card_s = createBackCards(temp, card_anchor)
        init_view(screen, card_s)

        card_c = card_s[capacity - 1].rect
        font_size = card_c[3] * 2 // 3
        font = pygame.font.Font(None, font_size)

        center = rectCenter(card_c)
        text = font.render('+' + str(numOfCard - capacity + 1), True, (255, 255, 255))
        screen.blit(text, (center[0] - text.get_width() / 2, center[1] - text.get_height() / 2))
    else:
        card_s = createBackCards(player.handCardList, card_anchor)
        init_view(screen, card_s)
    return slotBg


##### bot space #####

##### near bot space #####


def turnArrow(screen, rect, direction):
    size_x = round(rect[3] / 2)
    size_y = size_x

    pos_x = rect[0] - size_x
    pos_y = rect[1]
    img_o = ''

    if direction == 1:
        img_o = f"downArrow.png"
        pos_y = rect[1] + size_y
    else:
        img_o = f"upArrow.png"

    size_o = (size_x, size_y)
    pos_o = (pos_x, pos_y)

    btn = Button(image=pygame.image.load(img_o), pos=pos_o, size=size_o)
    init_view(screen, [btn])


##### near bot space #####

def createColorBtn(rect, start_color_weakness_value):
    lst = []
    x = rect[2] * 0.05
    y = x * 1.2
    for i in range(0, 4):
        pos_o = (rect[0] + i * x, rect[1] + y + 50)
        size_o = (x, y)
        if start_color_weakness_value == False:
            img_o = f"images/" + COLOR_TABLE[i] + ".png"
        elif start_color_weakness_value == True:
            img_o = f"blind_images/" + COLOR_TABLE[i] + ".png"
        btn = Button(image=pygame.image.load(img_o), pos=pos_o, size=size_o)
        lst.append(btn)
    return lst


def createNumberBtn(rect):
    lst = []
    x = rect[2] * 0.05
    y = x * 1.2
    for i in range(0, 10):
        pos_o = (rect[0] + i * x, rect[1] + 2 * y)
        size_o = (x, y)
        img_o = f"images/red_" + str(i) + ".png"
        btn = Button(image=pygame.image.load(img_o), pos=pos_o, size=size_o)
        lst.append(btn)
    return lst


def rectCenter(rect):
    x1 = rect[0]
    x2 = rect[0] + rect[2]

    y1 = rect[1]
    y2 = rect[1] + rect[3]
    return ((x1 + x2) / 2, (y1 + y2) / 2)
