import pygame
import os
import sys

from InputBox import InputBox
from button import Button
from main import init_bg, init_pygame
from start import start
from uno_Const import MODE_NORMAL, MODE_ALLCARD, MODE_CHANGECOLOR, MODE_OPENSHUFFLE
from view import init_view
from text import Text
import configparser

os.chdir(os.getcwd() + "/img")

init_pygame()

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')


def save_config():
    with open('config.ini', 'w', encoding='utf-8') as config_file:
        config.write(config_file)


def change_str_to_var(str):
    return eval(f"{str}")


try:
    if config['system']['is_new'] == "False":
        print("config file o")
except:
    print("config file x")
    config['system'] = {}
    config['system']['is_new'] = "False"
    config['system']['COLOR_WEAKNESS_MODE'] = "FALSE"
    config['system']['SCREEN_WIDTH'] = "1280"
    config['system']['SCREEN_HEIGHT'] = "720"
    config['system']['UNO'] = 'pygame.K_u'
    config['system']['LEFT_MOVE'] = 'pygame.K_RIGHT'
    config['system']['RIGHT_MOVE'] = 'pygame.K_LEFT'
    config['system']['SELECT'] = 'pygame.K_RETURN'
    config['system']['DRAW'] = 'pygame.K_d'
    save_config()

screen_width = 1280
screen_height = 720

if config['system']['COLOR_WEAKNESS_MODE'] == "True":
    color_weakness_value = True
else:
    color_weakness_value = False

button_width = 220
button_height = 50

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont(None, 30)

x_pos = screen_width / 2 - button_width / 2
y_pos = screen_height / 2 - button_height / 2


def play():
    screen.fill("black")
    play_bg = init_bg("options_screen.png", screen_width, screen_height)
    screen.blit(play_bg, (0, 0))
    back_button = Button(image=pygame.image.load("back_button.png"),
                         pos=(30, 30),
                         size=(50, 50))

    default_mode_button = Button(image=pygame.image.load("default_mode_button.png"),
                                 pos=(x_pos, y_pos - 50),
                                 size=(button_width, button_height))

    story_mode_button = Button(image=pygame.image.load("story_mode_button.png"),
                               pos=(x_pos, y_pos + 50),
                               size=(button_width, button_height))

    title_text = Text(text_input="Select game mode",
                      font="notosanscjkkr",
                      color=(0, 0, 0),
                      pos=(screen.get_rect().centerx, screen.get_rect().top + 100),
                      size=50,
                      screen=screen)
    title_text.init_text()
    init_view(screen, [back_button, default_mode_button, story_mode_button])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if default_mode_button.rect.collidepoint(event.pos):
                    loby()
                elif story_mode_button.rect.collidepoint(event.pos):
                    story_mode()
                elif back_button.rect.collidepoint(event.pos):
                    main_screen()
        pygame.display.flip()


def loby(mode=MODE_NORMAL):
    screen.fill("black")
    play_bg = init_bg("options_screen.png", screen_width, screen_height)
    screen.blit(play_bg, (0, 0))
    back_button = Button(image=pygame.image.load("back_button.png"),
                         pos=(30, 30),
                         size=(50, 50))
    start_button = Button(image=pygame.image.load("start_button.png"),
                          pos=(x_pos, y_pos + 260),
                          size=(button_width, button_height))

    AI_1 = Button(image=pygame.image.load("1_checked.png"),
                  pos=(x_pos - 360, y_pos - 120),
                  size=(100, 100))
    AI_2 = Button(image=pygame.image.load("empty.png"),
                  pos=(x_pos - 160, y_pos - 120),
                  size=(100, 100))
    AI_3 = Button(image=pygame.image.load("empty.png"),
                  pos=(x_pos + 40, y_pos - 120),
                  size=(100, 100))
    AI_4 = Button(image=pygame.image.load("empty.png"),
                  pos=(x_pos + 240, y_pos - 120),
                  size=(100, 100))
    AI_5 = Button(image=pygame.image.load("empty.png"),
                  pos=(x_pos + 440, y_pos - 120),
                  size=(100, 100))

    title_text = Text(text_input="Set computer that will play with you",
                      font="notosanscjkkr",
                      color=(0, 0, 0),
                      pos=(screen.get_rect().centerx, screen.get_rect().top + 100),
                      size=50,
                      screen=screen)
    subtitle_text = Text(text_input="Set your name",
                         font="notosanscjkkr",
                         color=(0, 0, 0),
                         pos=(screen.get_rect().centerx, screen.get_rect().top + 450),
                         size=50,
                         screen=screen)
    title_text.init_text()
    subtitle_text.init_text()

    input_boxes = [InputBox(screen.get_rect().left + 520, 500, 80, 32),
                   InputBox(screen.get_rect().left + 120, 350, 80, 32),
                   InputBox(screen.get_rect().left + 320, 350, 80, 32),
                   InputBox(screen.get_rect().left + 520, 350, 80, 32),
                   InputBox(screen.get_rect().left + 720, 350, 80, 32),
                   InputBox(screen.get_rect().left + 920, 350, 80, 32)]

    init_view(screen, [back_button, start_button, AI_1, AI_2, AI_3, AI_4, AI_5])
    bool_list = [True, False, False, False, False]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(event.pos):
                    AI_num = 0
                    name_list = []
                    temp = 1
                    if input_boxes[0].text == '':
                        name_list.append("USER")
                    else:
                        name_list.append(input_boxes[0].text)
                    for i in bool_list:
                        if i:
                            AI_num += 1
                            if input_boxes[temp].text == '':
                                name_list.append("Computer" + str(temp))
                            else:
                                name_list.append(input_boxes[temp].text)
                        temp += 1
                    start(screen, int(config['system']['SCREEN_WIDTH']), int(config['system']['SCREEN_HEIGHT']), AI_num,
                          name_list, color_weakness_value, mode)
                elif back_button.rect.collidepoint(event.pos):
                    play()
                elif AI_2.rect.collidepoint(event.pos):
                    if bool_list[1]:
                        AI_2.image = pygame.image.load("empty.png")
                        bool_list[1] = False
                    else:
                        AI_2.image = pygame.image.load("2_checked.png")
                        bool_list[1] = True
                    init_view(screen, [back_button, start_button, AI_1, AI_2, AI_3, AI_4, AI_5])
                elif AI_3.rect.collidepoint(event.pos):
                    if bool_list[2]:
                        AI_3.image = pygame.image.load("empty.png")
                        bool_list[2] = False
                    else:
                        AI_3.image = pygame.image.load("3_checked.png")
                        bool_list[2] = True
                    init_view(screen, [back_button, start_button, AI_1, AI_2, AI_3, AI_4, AI_5])
                elif AI_4.rect.collidepoint(event.pos):
                    if bool_list[3]:
                        AI_4.image = pygame.image.load("empty.png")
                        bool_list[3] = False
                    else:
                        AI_4.image = pygame.image.load("4_checked.png")
                        bool_list[3] = True
                    init_view(screen, [back_button, start_button, AI_1, AI_2, AI_3, AI_4, AI_5])
                elif AI_5.rect.collidepoint(event.pos):
                    if bool_list[4]:
                        AI_5.image = pygame.image.load("empty.png")
                        bool_list[4] = False
                    else:
                        AI_5.image = pygame.image.load("5_checked.png")
                        bool_list[4] = True
                    init_view(screen, [back_button, start_button, AI_1, AI_2, AI_3, AI_4, AI_5])
            for box in input_boxes:
                box.handle_event(event)
        for box in input_boxes:
            box.update()
        screen.blit(play_bg, (0, 0))
        init_view(screen, [back_button, start_button, AI_1, AI_2, AI_3, AI_4, AI_5])
        title_text.init_text()
        subtitle_text.init_text()
        for box in input_boxes:
            box.draw(screen)
        pygame.display.flip()


def story_mode():
    screen.fill("white")
    bg = init_bg("story_mode_map.png", screen_width, screen_height)
    screen.blit(bg, (0, 0))
    back_button = Button(image=pygame.image.load("back_button.png"),
                         pos=(30, 30),
                         size=(50, 50))

    story_mode_1 = Button(image=pygame.image.load("story_mode_1.png"),
                          pos=(screen.get_rect().centerx - 420, screen.get_rect().centery - 200),
                          size=(70, 70))

    story_mode_2 = Button(image=pygame.image.load("story_mode_2.png"),
                          pos=(screen.get_rect().centerx - 400, screen.get_rect().centery + 100),
                          size=(70, 70))

    story_mode_3 = Button(image=pygame.image.load("story_mode_3.png"),
                          pos=(screen.get_rect().centerx + 150, screen.get_rect().centery - 180),
                          size=(70, 70))

    story_mode_4 = Button(image=pygame.image.load("story_mode_4.png"),
                          pos=(screen.get_rect().centerx + 390, screen.get_rect().centery + 110),
                          size=(70, 70))

    init_view(screen, [back_button, story_mode_1, story_mode_2, story_mode_3, story_mode_4])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    play()
                elif story_mode_1.rect.collidepoint(event.pos):
                    loby()
                elif story_mode_2.rect.collidepoint(event.pos):
                    start(screen, int(config['system']['SCREEN_WIDTH']), int(config['system']['SCREEN_HEIGHT']), 3,
                          ["USER", "COMPUTER1", "COMPUTER2", "COMPUTER3", "COMPUTER4"], color_weakness_value,
                          MODE_ALLCARD)
                elif story_mode_3.rect.collidepoint(event.pos):
                    start(screen, int(config['system']['SCREEN_WIDTH']), int(config['system']['SCREEN_HEIGHT']), 2,
                          ["USER", "COMPUTER1", "COMPUTER2"], color_weakness_value,
                          MODE_CHANGECOLOR)
                elif story_mode_4.rect.collidepoint(event.pos):
                    loby(MODE_OPENSHUFFLE)
        pygame.display.flip()


def options():
    global UNO, SELECT, LEFT, RIGHT, DRAW, width, height
    global color_weakness_value

    # option screen에서 필요한 버튼 설정
    back_button = Button(image=pygame.image.load("back_button.png"),
                         pos=(30, 30),
                         size=(50, 50))
    save_button = Button(image=pygame.image.load("save_button.png"),
                         pos=(x_pos, y_pos + 230),
                         size=(button_width, button_height))
    reset_button = Button(image=pygame.image.load("reset_button.png"),
                          pos=(x_pos, y_pos + 300),
                          size=(button_width, button_height))

    on_button = Button(image=pygame.image.load("on.png"),
                       pos=(screen.get_rect().centerx - 150, screen.get_rect().centery - 230),
                       size=(130, 60))
    off_button = Button(image=pygame.image.load("off.png"),
                        pos=(screen.get_rect().centerx + 50, screen.get_rect().centery - 230),
                        size=(130, 60))
    button_1920 = Button(image=pygame.image.load("1920_button.png"),
                         pos=(screen.get_rect().centerx - 300, screen.get_rect().centery - 80),
                         size=(160, 60))
    button_1280 = Button(image=pygame.image.load("1280_button.png"),
                         pos=(screen.get_rect().centerx - 80, screen.get_rect().centery - 80),
                         size=(160, 60))
    button_960 = Button(image=pygame.image.load("960_button.png"),
                        pos=(screen.get_rect().centerx + 140, screen.get_rect().centery - 80),
                        size=(160, 60))

    color_weakness_mode_text = Text(text_input="Color Weakness Mode",
                                    font="notosanscjkkr",
                                    color=(0, 0, 0),
                                    pos=(screen.get_rect().centerx, screen.get_rect().top + 100),
                                    size=50,
                                    screen=screen)

    resolution_text = Text(text_input="Resolution",
                           font="notosanscjkkr",
                           color=(0, 0, 0),
                           pos=(screen.get_rect().centerx, screen.get_rect().top + 240),
                           size=50,
                           screen=screen)

    key_setting_text = Text(text_input="Key Setting",
                            font="notosanscjkkr",
                            color=(0, 0, 0),
                            pos=(screen.get_rect().centerx, screen.get_rect().top + 380),
                            size=50,
                            screen=screen)

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
    draw_move_text = Text(text_input="DRAW",
                          font="notosanscjkkr",
                          color=(0, 0, 0),
                          pos=(screen.get_rect().centerx + 200, screen.get_rect().top + 420),
                          size=25,
                          screen=screen)

    if config['system']['COLOR_WEAKNESS_MODE'] == "True":
        on_button.image = pygame.image.load("on_checked.png")
        off_button.image = pygame.image.load("off.png")
    else:
        on_button.image = pygame.image.load("on.png")
        off_button.image = pygame.image.load("off_checked.png")

    if config['system']['SCREEN_WIDTH'] == "1920":
        width = "1920"
        height = "1080"
        button_1920.image = pygame.image.load("1920_checked.png")
        button_1280.image = pygame.image.load("1280_button.png")
        button_960.image = pygame.image.load("960_button.png")
    elif config['system']['SCREEN_WIDTH'] == "1280":
        width = "1280"
        height = "720"
        button_1920.image = pygame.image.load("1920_button.png")
        button_1280.image = pygame.image.load("1280_checked.png")
        button_960.image = pygame.image.load("960_button.png")
    elif config['system']['SCREEN_WIDTH'] == "960":
        width = "960"
        height = "540"
        button_1920.image = pygame.image.load("1920_button.png")
        button_1280.image = pygame.image.load("1280_button.png")
        button_960.image = pygame.image.load("960_checked.png")

    while True:
        screen.fill("black")
        options_bg = init_bg("options_screen.png", screen_width, screen_height)
        screen.blit(options_bg, (0, 0))

        # 텍스트 설정
        color_weakness_mode_text.init_text()
        resolution_text.init_text()
        key_setting_text.init_text()
        uno_text.init_text()
        return_text.init_text()
        left_move_text.init_text()
        right_move_text.init_text()
        draw_move_text.init_text()
        init_view(screen,
                  [back_button, save_button, on_button, off_button, button_1920, button_1280, button_960, reset_button])

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

        # 메인 루프
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    main_screen()
                elif save_button.rect.collidepoint(event.pos):
                    config['system']['SCREEN_WIDTH'] = str(width)
                    config['system']['SCREEN_HEIGHT'] = str(height)
                    save_config()
                    main_screen()
                elif reset_button.rect.collidepoint(event.pos):
                    on_button.image = pygame.image.load("on.png")
                    off_button.image = pygame.image.load("off_checked.png")
                    button_1920.image = pygame.image.load("1920_button.png")
                    button_1280.image = pygame.image.load("1280_checked.png")
                    button_960.image = pygame.image.load("960_button.png")
                    width = "1280"
                    height = "720"
                    config['system']['COLOR_WEAKNESS_MODE'] = "FALSE"
                    config['system']['SCREEN_WIDTH'] = "1280"
                    config['system']['SCREEN_HEIGHT'] = "720"
                    config['system']['UNO'] = 'pygame.K_u'
                    config['system']['LEFT_MOVE'] = 'pygame.K_RIGHT'
                    config['system']['RIGHT_MOVE'] = 'pygame.K_LEFT'
                    config['system']['SELECT'] = 'pygame.K_RETURN'
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
                    print("Press the key for Select")
                    SELECT = key_change()
                    pygame.key.name(SELECT)
                    if pygame.key.name(SELECT) == 'up' or pygame.key.name(SELECT) == 'right' or pygame.key.name(
                            SELECT) == 'left' or pygame.key.name(SELECT) == 'return':
                        config['system']['SELECT'] = 'pygame.K_' + (pygame.key.name(SELECT)).upper()
                    else:
                        config['system']['SELECT'] = 'pygame.K_' + pygame.key.name(SELECT)
                    save_config()
                elif L_button_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Press the key for LEFT")
                    LEFT = key_change()
                    pygame.key.name(LEFT)
                    if pygame.key.name(LEFT) == 'up' or pygame.key.name(LEFT) == 'right' or pygame.key.name(
                            LEFT) == 'left' or pygame.key.name(LEFT) == 'return':
                        config['system']['LEFT_MOVE'] = 'pygame.K_' + (pygame.key.name(LEFT)).upper()
                    else:
                        config['system']['LEFT_MOVE'] = 'pygame.K_' + pygame.key.name(LEFT)
                    save_config()
                elif R_button_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Press the key for RIGHT")
                    RIGHT = key_change()
                    if pygame.key.name(RIGHT) == 'up' or pygame.key.name(RIGHT) == 'right' or pygame.key.name(
                            RIGHT) == 'left' or pygame.key.name(RIGHT) == 'return':
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
                elif on_button.rect.collidepoint(event.pos):
                    print("on")
                    on_button.image = pygame.image.load("on_checked.png")
                    off_button.image = pygame.image.load("off.png")
                    config['system']['COLOR_WEAKNESS_MODE'] = "True"
                    color_weakness_value = True
                elif off_button.rect.collidepoint(event.pos):
                    on_button.image = pygame.image.load("on.png")
                    off_button.image = pygame.image.load("off_checked.png")
                    config['system']['COLOR_WEAKNESS_MODE'] = "False"
                    color_weakness_value = False
                elif button_1920.rect.collidepoint(event.pos):
                    button_1920.image = pygame.image.load("1920_checked.png")
                    button_1280.image = pygame.image.load("1280_button.png")
                    button_960.image = pygame.image.load("960_button.png")
                    width = "1920"
                    height = "1080"
                elif button_1280.rect.collidepoint(event.pos):
                    button_1920.image = pygame.image.load("1920_button.png")
                    button_1280.image = pygame.image.load("1280_checked.png")
                    button_960.image = pygame.image.load("960_button.png")
                    width = "1280"
                    height = "720"
                elif button_960.rect.collidepoint(event.pos):
                    button_1920.image = pygame.image.load("1920_button.png")
                    button_1280.image = pygame.image.load("1280_button.png")
                    button_960.image = pygame.image.load("960_checked.png")
                    width = "960"
                    height = "540"
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


def quit():
    pygame.quit()
    sys.exit()


# 메인 루프
def main_screen():
    print(config['system']['LEFT_MOVE'])
    main_bg = init_bg("start_screen.jpeg", 1280, 720)
    while True:
        screen.blit(main_bg, (0, 0))
        play_button = Button(image=pygame.image.load("play_button.png"),
                             pos=(x_pos, y_pos + 200),
                             size=(button_width, button_height))

        options_button = Button(image=pygame.image.load("options_button.png"),
                                pos=(x_pos, y_pos + 260),
                                size=(button_width, button_height))

        exit_button = Button(image=pygame.image.load("exit_button.png"),
                             pos=(x_pos, y_pos + 320),
                             size=(button_width, button_height))

        title_text = Text(text_input="UNO GAME",
                          font="notosanscjkkr",
                          color=(0, 0, 0),
                          pos=(screen.get_rect().centerx, screen.get_rect().top + 30),
                          size=70,
                          screen=screen)

        init_view(screen, [play_button, options_button, exit_button])
        title_text.init_text()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(event.pos):
                    play()
                elif options_button.rect.collidepoint(event.pos):
                    options()
                elif exit_button.rect.collidepoint(event.pos):
                    quit()
        pygame.display.update()


main_screen()
