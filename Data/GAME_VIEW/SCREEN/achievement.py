from Data.GAME_VIEW.OBJECT.view import init_view
from Data.GAME_VIEW.OBJECT.button import Button
from Data.GAME_VIEW.OBJECT.text import Text
from Data.GAME_VIEW.util import *
import pygame


# 메인 루프
def achievement_screen(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, OPTION):
    back_button = Button(image=pygame.image.load(BUTTON_PATH + "back_button.png"),
                         pos=(set_size(30, SCREEN_WIDTH), set_size(30, SCREEN_WIDTH)),
                         size=(set_size(50, SCREEN_WIDTH), set_size(50, SCREEN_WIDTH)))
    single_win_icon = Button(image=pygame.image.load(BUTTON_PATH + "single_win.png"),
                             pos=(set_size(100, SCREEN_WIDTH), set_size(30, SCREEN_WIDTH)),
                             size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    single_win_title = Text(text_input="SINGLE WIN",
                            font=FONT_PATH,
                            color=(0, 0, 0),
                            pos=(set_size(350, SCREEN_WIDTH), set_size(50, SCREEN_WIDTH)),
                            size=set_size(30, SCREEN_WIDTH),
                            screen=SCREEN)
    single_win_explain = Text(text_input="Winning a single-player game",
                              font=FONT_PATH,
                              color=(0, 0, 0),
                              pos=(set_size(350, SCREEN_WIDTH), set_size(75, SCREEN_WIDTH)),
                              size=set_size(20, SCREEN_WIDTH),
                              screen=SCREEN)
    single_win_date = Text(text_input="",
                           font=FONT_PATH,
                           color=(0, 0, 0),
                           pos=(set_size(350, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)),
                           size=set_size(20, SCREEN_WIDTH),
                           screen=SCREEN)
    single_win_achieve = Button(image=pygame.image.load(BUTTON_PATH + "achievement_button.png"),
                                pos=(set_size(500, SCREEN_WIDTH), set_size(30, SCREEN_WIDTH)),
                                size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    ten_turn_win_icon = Button(image=pygame.image.load(BUTTON_PATH + "ten_turn_win.png"),
                               pos=(set_size(700, SCREEN_WIDTH), set_size(30, SCREEN_WIDTH)),
                               size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    ten_turn_win_title = Text(text_input="10 WIN",
                              font=FONT_PATH,
                              color=(0, 0, 0),
                              pos=(set_size(950, SCREEN_WIDTH), set_size(50, SCREEN_WIDTH)),
                              size=set_size(30, SCREEN_WIDTH),
                              screen=SCREEN)
    ten_turn_win_explain = Text(text_input="Win in 10 turns in a single player game",
                                font=FONT_PATH,
                                color=(0, 0, 0),
                                pos=(set_size(950, SCREEN_WIDTH), set_size(75, SCREEN_WIDTH)),
                                size=set_size(20, SCREEN_WIDTH),
                                screen=SCREEN)
    ten_turn_win_date = Text(text_input="",
                             font=FONT_PATH,
                             color=(0, 0, 0),
                             pos=(set_size(950, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)),
                             size=set_size(20, SCREEN_WIDTH),
                             screen=SCREEN)
    ten_turn_win_achieve = Button(image=pygame.image.load(BUTTON_PATH + "achievement_button.png"),
                                  pos=(set_size(1100, SCREEN_WIDTH), set_size(30, SCREEN_WIDTH)),
                                  size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    story_a_win_icon = Button(image=pygame.image.load(BUTTON_PATH + "story_a_win.png"),
                              pos=(set_size(100, SCREEN_WIDTH), set_size(130, SCREEN_WIDTH)),
                              size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    story_a_win_title = Text(text_input="A WIN",
                             font=FONT_PATH,
                             color=(0, 0, 0),
                             pos=(set_size(350, SCREEN_WIDTH), set_size(150, SCREEN_WIDTH)),
                             size=set_size(30, SCREEN_WIDTH),
                             screen=SCREEN)
    story_a_win_explain = Text(text_input="Win in Area A in Story Mode",
                               font=FONT_PATH,
                               color=(0, 0, 0),
                               pos=(set_size(350, SCREEN_WIDTH), set_size(175, SCREEN_WIDTH)),
                               size=set_size(20, SCREEN_WIDTH),
                               screen=SCREEN)
    story_a_win_date = Text(text_input="",
                            font=FONT_PATH,
                            color=(0, 0, 0),
                            pos=(set_size(350, SCREEN_WIDTH), set_size(200, SCREEN_WIDTH)),
                            size=set_size(20, SCREEN_WIDTH),
                            screen=SCREEN)
    story_a_win_achieve = Button(image=pygame.image.load(BUTTON_PATH + "achievement_button.png"),
                                 pos=(set_size(500, SCREEN_WIDTH), set_size(130, SCREEN_WIDTH)),
                                 size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    story_b_win_icon = Button(image=pygame.image.load(BUTTON_PATH + "story_b_win.png"),
                              pos=(set_size(700, SCREEN_WIDTH), set_size(130, SCREEN_WIDTH)),
                              size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    story_b_win_title = Text(text_input="B WIN",
                             font=FONT_PATH,
                             color=(0, 0, 0),
                             pos=(set_size(950, SCREEN_WIDTH), set_size(150, SCREEN_WIDTH)),
                             size=set_size(30, SCREEN_WIDTH),
                             screen=SCREEN)
    story_b_win_explain = Text(text_input="Win in Area B in Story Mode",
                               font=FONT_PATH,
                               color=(0, 0, 0),
                               pos=(set_size(950, SCREEN_WIDTH), set_size(175, SCREEN_WIDTH)),
                               size=set_size(20, SCREEN_WIDTH),
                               screen=SCREEN)
    story_b_win_date = Text(text_input="",
                            font=FONT_PATH,
                            color=(0, 0, 0),
                            pos=(set_size(950, SCREEN_WIDTH), set_size(200, SCREEN_WIDTH)),
                            size=set_size(20, SCREEN_WIDTH),
                            screen=SCREEN)
    story_b_win_achieve = Button(image=pygame.image.load(BUTTON_PATH + "achievement_button.png"),
                                 pos=(set_size(1100, SCREEN_WIDTH), set_size(130, SCREEN_WIDTH)),
                                 size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    story_c_win_icon = Button(image=pygame.image.load(BUTTON_PATH + "story_c_win.png"),
                              pos=(set_size(100, SCREEN_WIDTH), set_size(230, SCREEN_WIDTH)),
                              size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    story_c_win_title = Text(text_input="C WIN",
                             font=FONT_PATH,
                             color=(0, 0, 0),
                             pos=(set_size(350, SCREEN_WIDTH), set_size(250, SCREEN_WIDTH)),
                             size=set_size(30, SCREEN_WIDTH),
                             screen=SCREEN)
    story_c_win_explain = Text(text_input="Win in Area C in Story Mode",
                               font=FONT_PATH,
                               color=(0, 0, 0),
                               pos=(set_size(350, SCREEN_WIDTH), set_size(275, SCREEN_WIDTH)),
                               size=set_size(20, SCREEN_WIDTH),
                               screen=SCREEN)
    story_c_win_date = Text(text_input="",
                            font=FONT_PATH,
                            color=(0, 0, 0),
                            pos=(set_size(350, SCREEN_WIDTH), set_size(300, SCREEN_WIDTH)),
                            size=set_size(20, SCREEN_WIDTH),
                            screen=SCREEN)
    story_c_win_achieve = Button(image=pygame.image.load(BUTTON_PATH + "achievement_button.png"),
                                 pos=(set_size(500, SCREEN_WIDTH), set_size(230, SCREEN_WIDTH)),
                                 size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    story_d_win_icon = Button(image=pygame.image.load(BUTTON_PATH + "story_d_win.png"),
                              pos=(set_size(700, SCREEN_WIDTH), set_size(230, SCREEN_WIDTH)),
                              size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    story_d_win_title = Text(text_input="D WIN",
                             font=FONT_PATH,
                             color=(0, 0, 0),
                             pos=(set_size(950, SCREEN_WIDTH), set_size(250, SCREEN_WIDTH)),
                             size=set_size(30, SCREEN_WIDTH),
                             screen=SCREEN)
    story_d_win_explain = Text(text_input="Win in Area D in Story Mode",
                               font=FONT_PATH,
                               color=(0, 0, 0),
                               pos=(set_size(950, SCREEN_WIDTH), set_size(275, SCREEN_WIDTH)),
                               size=set_size(20, SCREEN_WIDTH),
                               screen=SCREEN)
    story_d_win_date = Text(text_input="",
                            font=FONT_PATH,
                            color=(0, 0, 0),
                            pos=(set_size(950, SCREEN_WIDTH), set_size(300, SCREEN_WIDTH)),
                            size=set_size(20, SCREEN_WIDTH),
                            screen=SCREEN)
    story_d_win_achieve = Button(image=pygame.image.load(BUTTON_PATH + "achievement_button.png"),
                                 pos=(set_size(1100, SCREEN_WIDTH), set_size(230, SCREEN_WIDTH)),
                                 size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    story_all_win_icon = Button(image=pygame.image.load(BUTTON_PATH + "story_all_win.png"),
                                pos=(set_size(100, SCREEN_WIDTH), set_size(330, SCREEN_WIDTH)),
                                size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    story_all_win_title = Text(text_input="ALL WIN",
                               font=FONT_PATH,
                               color=(0, 0, 0),
                               pos=(set_size(350, SCREEN_WIDTH), set_size(350, SCREEN_WIDTH)),
                               size=set_size(30, SCREEN_WIDTH),
                               screen=SCREEN)
    story_all_win_explain = Text(text_input="Win all Area in Story Mode",
                                 font=FONT_PATH,
                                 color=(0, 0, 0),
                                 pos=(set_size(350, SCREEN_WIDTH), set_size(375, SCREEN_WIDTH)),
                                 size=set_size(20, SCREEN_WIDTH),
                                 screen=SCREEN)
    story_all_win_date = Text(text_input="",
                              font=FONT_PATH,
                              color=(0, 0, 0),
                              pos=(set_size(350, SCREEN_WIDTH), set_size(400, SCREEN_WIDTH)),
                              size=set_size(20, SCREEN_WIDTH),
                              screen=SCREEN)
    story_all_win_achieve = Button(image=pygame.image.load(BUTTON_PATH + "achievement_button.png"),
                                   pos=(set_size(500, SCREEN_WIDTH), set_size(330, SCREEN_WIDTH)),
                                   size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    after_uno_win_icon = Button(image=pygame.image.load(BUTTON_PATH + "after_uno_win.png"),
                                pos=(set_size(700, SCREEN_WIDTH), set_size(330, SCREEN_WIDTH)),
                                size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    after_uno_win_title = Text(text_input="SECOND UNO",
                               font=FONT_PATH,
                               color=(0, 0, 0),
                               pos=(set_size(950, SCREEN_WIDTH), set_size(350, SCREEN_WIDTH)),
                               size=set_size(30, SCREEN_WIDTH),
                               screen=SCREEN)
    after_uno_win_explain = Text(text_input="Win after another player declares UNO",
                                 font=FONT_PATH,
                                 color=(0, 0, 0),
                                 pos=(set_size(950, SCREEN_WIDTH), set_size(375, SCREEN_WIDTH)),
                                 size=set_size(20, SCREEN_WIDTH),
                                 screen=SCREEN)
    after_uno_win_date = Text(text_input="",
                              font=FONT_PATH,
                              color=(0, 0, 0),
                              pos=(set_size(950, SCREEN_WIDTH), set_size(400, SCREEN_WIDTH)),
                              size=set_size(20, SCREEN_WIDTH),
                              screen=SCREEN)
    after_uno_win_achieve = Button(image=pygame.image.load(BUTTON_PATH + "achievement_button.png"),
                                   pos=(set_size(1100, SCREEN_WIDTH), set_size(330, SCREEN_WIDTH)),
                                   size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    no_effect_win_icon = Button(image=pygame.image.load(BUTTON_PATH + "no_effect_win.png"),
                                pos=(set_size(100, SCREEN_WIDTH), set_size(430, SCREEN_WIDTH)),
                                size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    no_effect_win_title = Text(text_input="ONLY NUMBER",
                               font=FONT_PATH,
                               color=(0, 0, 0),
                               pos=(set_size(350, SCREEN_WIDTH), set_size(450, SCREEN_WIDTH)),
                               size=set_size(30, SCREEN_WIDTH),
                               screen=SCREEN)
    no_effect_win_explain = Text(text_input="Win without a single technical card",
                                 font=FONT_PATH,
                                 color=(0, 0, 0),
                                 pos=(set_size(350, SCREEN_WIDTH), set_size(475, SCREEN_WIDTH)),
                                 size=set_size(20, SCREEN_WIDTH),
                                 screen=SCREEN)
    no_effect_win_date = Text(text_input="",
                              font=FONT_PATH,
                              color=(0, 0, 0),
                              pos=(set_size(350, SCREEN_WIDTH), set_size(500, SCREEN_WIDTH)),
                              size=set_size(20, SCREEN_WIDTH),
                              screen=SCREEN)
    no_effect_win_achieve = Button(image=pygame.image.load(BUTTON_PATH + "achievement_button.png"),
                                   pos=(set_size(500, SCREEN_WIDTH), set_size(430, SCREEN_WIDTH)),
                                   size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    no_draw_win_icon = Button(image=pygame.image.load(BUTTON_PATH + "no_draw_win.png"),
                              pos=(set_size(700, SCREEN_WIDTH), set_size(430, SCREEN_WIDTH)),
                              size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    no_draw_win_title = Text(text_input="DO NOT DRAW",
                             font=FONT_PATH,
                             color=(0, 0, 0),
                             pos=(set_size(950, SCREEN_WIDTH), set_size(450, SCREEN_WIDTH)),
                             size=set_size(30, SCREEN_WIDTH),
                             screen=SCREEN)
    no_draw_win_explain = Text(text_input="Win without drawing a card",
                               font=FONT_PATH,
                               color=(0, 0, 0),
                               pos=(set_size(950, SCREEN_WIDTH), set_size(475, SCREEN_WIDTH)),
                               size=set_size(20, SCREEN_WIDTH),
                               screen=SCREEN)
    no_draw_win_date = Text(text_input="",
                            font=FONT_PATH,
                            color=(0, 0, 0),
                            pos=(set_size(950, SCREEN_WIDTH), set_size(500, SCREEN_WIDTH)),
                            size=set_size(20, SCREEN_WIDTH),
                            screen=SCREEN)
    no_draw_win_achieve = Button(image=pygame.image.load(BUTTON_PATH + "achievement_button.png"),
                                 pos=(set_size(1100, SCREEN_WIDTH), set_size(430, SCREEN_WIDTH)),
                                 size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    twenty_turn_win_icon = Button(image=pygame.image.load(BUTTON_PATH + "twenty_turn_win.png"),
                                  pos=(set_size(100, SCREEN_WIDTH), set_size(530, SCREEN_WIDTH)),
                                  size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    twenty_turn_win_title = Text(text_input="20 WIN",
                                 font=FONT_PATH,
                                 color=(0, 0, 0),
                                 pos=(set_size(350, SCREEN_WIDTH), set_size(550, SCREEN_WIDTH)),
                                 size=set_size(30, SCREEN_WIDTH),
                                 screen=SCREEN)
    twenty_turn_win_explain = Text(text_input="Win in 20 turns in a single player game",
                                   font=FONT_PATH,
                                   color=(0, 0, 0),
                                   pos=(set_size(350, SCREEN_WIDTH), set_size(575, SCREEN_WIDTH)),
                                   size=set_size(20, SCREEN_WIDTH),
                                   screen=SCREEN)
    twenty_turn_win_date = Text(text_input="",
                                font=FONT_PATH,
                                color=(0, 0, 0),
                                pos=(set_size(350, SCREEN_WIDTH), set_size(600, SCREEN_WIDTH)),
                                size=set_size(20, SCREEN_WIDTH),
                                screen=SCREEN)
    twenty_turn_win_achieve = Button(image=pygame.image.load(BUTTON_PATH + "achievement_button.png"),
                                     pos=(set_size(500, SCREEN_WIDTH), set_size(530, SCREEN_WIDTH)),
                                     size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))

    if config['system']['SINGLE_WIN'] == "True":
        single_win_achieve.image = pygame.image.load(BUTTON_PATH + "achievement_checked.png")
        single_win_date = Text(text_input=config['system']['SINGLE_WIN_DATE'],
                               font=FONT_PATH,
                               color=(0, 0, 0),
                               pos=(set_size(350, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)),
                               size=set_size(20, SCREEN_WIDTH),
                               screen=SCREEN)
    if config['system']['TEN_TURN_WIN'] == "True":
        ten_turn_win_achieve.image = pygame.image.load(BUTTON_PATH + "achievement_checked.png")
        ten_turn_win_date = Text(text_input=config['system']['TEN_TURN_WIN_DATE'],
                                 font=FONT_PATH,
                                 color=(0, 0, 0),
                                 pos=(set_size(950, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)),
                                 size=set_size(20, SCREEN_WIDTH),
                                 screen=SCREEN)
    if config['system']['STORY_A_WIN'] == "True":
        story_a_win_achieve.image = pygame.image.load(BUTTON_PATH + "achievement_checked.png")
        story_a_win_date = Text(text_input=config['system']['STORY_A_WIN_DATE'],
                                font=FONT_PATH,
                                color=(0, 0, 0),
                                pos=(set_size(350, SCREEN_WIDTH), set_size(200, SCREEN_WIDTH)),
                                size=set_size(20, SCREEN_WIDTH),
                                screen=SCREEN)
    if config['system']['STORY_B_WIN'] == "True":
        story_b_win_achieve.image = pygame.image.load(BUTTON_PATH + "achievement_checked.png")
        story_b_win_date = Text(text_input=config['system']['STORY_B_WIN_DATE'],
                                font=FONT_PATH,
                                color=(0, 0, 0),
                                pos=(set_size(950, SCREEN_WIDTH), set_size(200, SCREEN_WIDTH)),
                                size=set_size(20, SCREEN_WIDTH),
                                screen=SCREEN)
    if config['system']['STORY_C_WIN'] == "True":
        story_c_win_achieve.image = pygame.image.load(BUTTON_PATH + "achievement_checked.png")
        story_c_win_date = Text(text_input=config['system']['STORY_C_WIN_DATE'],
                                font=FONT_PATH,
                                color=(0, 0, 0),
                                pos=(set_size(350, SCREEN_WIDTH), set_size(300, SCREEN_WIDTH)),
                                size=set_size(20, SCREEN_WIDTH),
                                screen=SCREEN)
    if config['system']['STORY_D_WIN'] == "True":
        story_d_win_achieve.image = pygame.image.load(BUTTON_PATH + "achievement_checked.png")
        story_d_win_date = Text(text_input=config['system']['STORY_D_WIN_DATE'],
                                font=FONT_PATH,
                                color=(0, 0, 0),
                                pos=(set_size(950, SCREEN_WIDTH), set_size(300, SCREEN_WIDTH)),
                                size=set_size(20, SCREEN_WIDTH),
                                screen=SCREEN)
    if config['system']['STORY_ALL_WIN'] == "True":
        story_all_win_achieve.image = pygame.image.load(BUTTON_PATH + "achievement_checked.png")
        story_all_win_date = Text(text_input=config['system']['STORY_ALL_WIN_DATE'],
                                  font=FONT_PATH,
                                  color=(0, 0, 0),
                                  pos=(set_size(350, SCREEN_WIDTH), set_size(400, SCREEN_WIDTH)),
                                  size=set_size(20, SCREEN_WIDTH),
                                  screen=SCREEN)
    if config['system']['AFTER_UNO_WIN'] == "True":
        after_uno_win_achieve.image = pygame.image.load(BUTTON_PATH + "achievement_checked.png")
        after_uno_win_date = Text(text_input=config['system']['AFTER_UNO_WIN_DATE'],
                                  font=FONT_PATH,
                                  color=(0, 0, 0),
                                  pos=(set_size(950, SCREEN_WIDTH), set_size(400, SCREEN_WIDTH)),
                                  size=set_size(20, SCREEN_WIDTH),
                                  screen=SCREEN)
    if config['system']['NO_EFFECT_WIN'] == "True":
        no_effect_win_achieve.image = pygame.image.load(BUTTON_PATH + "achievement_checked.png")
        no_effect_win_date = Text(text_input=config['system']['NO_EFFECT_WIN_DATE'],
                                  font=FONT_PATH,
                                  color=(0, 0, 0),
                                  pos=(set_size(350, SCREEN_WIDTH), set_size(500, SCREEN_WIDTH)),
                                  size=set_size(20, SCREEN_WIDTH),
                                  screen=SCREEN)
    if config['system']['NO_DRAW_WIN'] == "True":
        no_draw_win_achieve.image = pygame.image.load(BUTTON_PATH + "achievement_checked.png")
        no_draw_win_date = Text(text_input=config['system']['NO_DRAW_WIN_DATE'],
                                font=FONT_PATH,
                                color=(0, 0, 0),
                                pos=(set_size(950, SCREEN_WIDTH), set_size(500, SCREEN_WIDTH)),
                                size=set_size(20, SCREEN_WIDTH),
                                screen=SCREEN)
    if config['system']['TWENTY_TURN_WIN'] == "True":
        twenty_turn_win_achieve.image = pygame.image.load(BUTTON_PATH + "achievement_checked.png")
        twenty_turn_win_date = Text(text_input=config['system']['TWENTY_TURN_WIN_DATE'],
                                    font=FONT_PATH,
                                    color=(0, 0, 0),
                                    pos=(set_size(350, SCREEN_WIDTH), set_size(600, SCREEN_WIDTH)),
                                    size=set_size(20, SCREEN_WIDTH),
                                    screen=SCREEN)
    init_bg(SCREEN, SCREEN_PATH + "options_screen.png", SCREEN_WIDTH, SCREEN_HEIGHT)
    init_view(SCREEN, [back_button, single_win_achieve, single_win_icon, ten_turn_win_icon, ten_turn_win_achieve,
                       story_a_win_icon, story_a_win_achieve, story_b_win_icon, story_b_win_achieve,
                       story_c_win_icon, story_c_win_achieve, story_d_win_icon, story_d_win_achieve,
                       story_all_win_icon, story_all_win_achieve, after_uno_win_icon, after_uno_win_achieve,
                       no_effect_win_icon, no_effect_win_achieve, no_draw_win_icon, no_draw_win_achieve,
                       twenty_turn_win_icon, twenty_turn_win_achieve])
    flag = True
    while flag:
        single_win_date.init_text()
        single_win_title.init_text()
        single_win_explain.init_text()
        ten_turn_win_title.init_text()
        ten_turn_win_explain.init_text()
        ten_turn_win_date.init_text()
        story_a_win_title.init_text()
        story_a_win_explain.init_text()
        story_a_win_date.init_text()
        story_b_win_title.init_text()
        story_b_win_explain.init_text()
        story_b_win_date.init_text()
        story_c_win_title.init_text()
        story_c_win_explain.init_text()
        story_c_win_date.init_text()
        story_d_win_title.init_text()
        story_d_win_explain.init_text()
        story_d_win_date.init_text()
        story_all_win_title.init_text()
        story_all_win_explain.init_text()
        story_all_win_date.init_text()
        after_uno_win_title.init_text()
        after_uno_win_explain.init_text()
        after_uno_win_date.init_text()
        no_effect_win_title.init_text()
        no_effect_win_explain.init_text()
        no_effect_win_date.init_text()
        no_draw_win_title.init_text()
        no_draw_win_explain.init_text()
        no_draw_win_date.init_text()
        twenty_turn_win_title.init_text()
        twenty_turn_win_explain.init_text()
        twenty_turn_win_date.init_text()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    flag = False
                    if OPTION == "main":
                        from UNO_RUN import main_screen
                        main_screen()
                    elif OPTION == "pause":
                        SCREEN.fill((0, 0, 0))
                        init_bg(SCREEN, SCREEN_PATH + "options_screen.png", SCREEN_WIDTH, SCREEN_HEIGHT)
        pygame.display.update()
