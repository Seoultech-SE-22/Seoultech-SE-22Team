import pygame.image
from Data.GAME_LOGIC.uno_Const import MODE_COMBO, MODE_CHANGECOLOR, MODE_OPENSHUFFLE, MODE_ALLCARD
from Data.GAME_VIEW.OBJECT.button import Button
from Data.GAME_VIEW.OBJECT.view import init_view
from Data.GAME_VIEW.util import *

init_pygame()
check_config(config)

if bool(config['system']['COLOR_WEAKNESS_MODE']):
    color_weakness_value = True
else:
    color_weakness_value = False


def story_mode(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT):
    init_bg(SCREEN, SCREEN_PATH + "story_mode_map.png", SCREEN_WIDTH, SCREEN_HEIGHT)
    x_pos = SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2
    y_pos = SCREEN_HEIGHT / 2 - BUTTON_HEIGHT / 2
    back_button = Button(image=pygame.image.load(BUTTON_PATH + "back_button.png"),
                         pos=(set_size(30, SCREEN_WIDTH), set_size(30, SCREEN_WIDTH)),
                         size=(set_size(50, SCREEN_WIDTH), set_size(50, SCREEN_WIDTH)))

    story_mode_1 = Button(image=pygame.image.load(BUTTON_PATH + "story_mode_1.png"),
                          pos=(SCREEN.get_rect().centerx - set_size(420, SCREEN_WIDTH),
                               SCREEN.get_rect().centery - set_size(200, SCREEN_WIDTH)),
                          size=(set_size(70, SCREEN_WIDTH), set_size(70, SCREEN_WIDTH)))

    story_mode_2 = Button(image=pygame.image.load(BUTTON_PATH + "story_mode_2.png"),
                          pos=(SCREEN.get_rect().centerx - set_size(400, SCREEN_WIDTH),
                               SCREEN.get_rect().centery + set_size(100, SCREEN_WIDTH)),
                          size=(set_size(70, SCREEN_WIDTH), set_size(70, SCREEN_WIDTH)))

    story_mode_3 = Button(image=pygame.image.load(BUTTON_PATH + "story_mode_3.png"),
                          pos=(SCREEN.get_rect().centerx + set_size(150, SCREEN_WIDTH),
                               SCREEN.get_rect().centery - set_size(180, SCREEN_WIDTH)),
                          size=(set_size(70, SCREEN_WIDTH), set_size(70, SCREEN_WIDTH)))

    story_mode_4 = Button(image=pygame.image.load(BUTTON_PATH + "story_mode_4.png"),
                          pos=(SCREEN.get_rect().centerx + set_size(390, SCREEN_WIDTH),
                               SCREEN.get_rect().centery + set_size(110, SCREEN_WIDTH)),
                          size=(set_size(70, SCREEN_WIDTH), set_size(70, SCREEN_WIDTH)))

    start_button = Button(image=pygame.image.load(BUTTON_PATH + "start_button.png"),
                          pos=(x_pos, y_pos + set_size(260, SCREEN_WIDTH)),
                          size=(BUTTON_WIDTH, BUTTON_HEIGHT))

    if config['system']['STORY_A_WIN'] == "False" and config['system']['STORY_B_WIN'] == "False" and config['system']['STORY_C_WIN'] == "False" and config['system']['STORY_D_WIN'] == "False":
        story_mode_2.image = pygame.image.load(BUTTON_PATH + "story_mode_4_completed.png")
        story_mode_3.image = pygame.image.load(BUTTON_PATH + "story_mode_4_completed.png")
        story_mode_4.image = pygame.image.load(BUTTON_PATH + "story_mode_4_completed.png")
    elif config['system']['STORY_B_WIN'] == "False" and config['system']['STORY_C_WIN'] == "False" and config['system']['STORY_D_WIN'] == "False":
        story_mode_3.image = pygame.image.load(BUTTON_PATH + "story_mode_4_completed.png")
        story_mode_4.image = pygame.image.load(BUTTON_PATH + "story_mode_4_completed.png")
    elif config['system']['STORY_C_WIN'] == "False" and config['system']['STORY_D_WIN'] == "False":
        story_mode_4.image = pygame.image.load(BUTTON_PATH + "story_mode_4_completed.png")

    init_view(SCREEN, [back_button, story_mode_1, story_mode_2, story_mode_3, story_mode_4, start_button])
    
    def show_popup(stage):
        global text, mode, text_rect
        font = pygame.font.Font(FONT_PATH, set_size(36, SCREEN_WIDTH))
        description = [
            "첫 분배시 컴퓨터 플레이어가 기술 카드를 50% 더 높은 확률로 받게 됨.",
            "3명의 컴퓨터 플레이어와 대전 / 첫 카드를 제외하고 모든 카드를 같은 수만큼 플레이어들에게 분배.",
            "2명의 컴퓨터 플레이어와 대전 / 매 5턴마다 낼 수 있는 카드의 색상이 무작위로 변경됨.",
            "5턴마다 무작위로 opencard가 셔플된다. 그 후 맨 위 카드의 효과가 적용됨.",
            "이전 단계를 완료해야 시작할 수 있습니다."]

        if stage == "A":
            text = font.render(description[0], True, (0, 0, 0))
        elif stage == "B":
            text = font.render(description[1], True, (0, 0, 0))
        elif stage == "C":
            text = font.render(description[2], True, (0, 0, 0))
        elif stage == "D":
            text = font.render(description[3], True, (0, 0, 0))
        elif stage == "none":
            text = font.render(description[4], True, (0, 0, 0))

        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        init_bg(SCREEN, SCREEN_PATH + "story_mode_map.png", SCREEN_WIDTH, SCREEN_HEIGHT)
        init_view(SCREEN, [back_button, story_mode_1, story_mode_2, story_mode_3, story_mode_4, start_button])

        pygame.draw.rect(SCREEN, (255, 255, 255),
                         (text_rect.left - set_size(10, SCREEN_WIDTH),
                          text_rect.top - set_size(10, SCREEN_WIDTH),
                          text_rect.width + set_size(20, SCREEN_WIDTH),
                          text_rect.height + set_size(20, SCREEN_WIDTH)))

        pygame.draw.rect(SCREEN, (0, 0, 0),
                         (text_rect.left - set_size(10, SCREEN_WIDTH),
                          text_rect.top - set_size(10, SCREEN_WIDTH),
                          text_rect.width + set_size(20, SCREEN_WIDTH),
                          text_rect.height + set_size(20, SCREEN_WIDTH)), 2)

        SCREEN.blit(text, text_rect)
        pygame.display.flip()
    
    popup = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    from Data.GAME_VIEW.SCREEN.game_mode import select_game_mode
                    select_game_mode(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
                elif story_mode_1.rect.collidepoint(event.pos):
                    mode = "A"
                    show_popup(mode)
                    popup = True
                elif story_mode_2.rect.collidepoint(event.pos):
                    mode = "B"
                    show_popup(mode)
                    popup = True
                elif story_mode_3.rect.collidepoint(event.pos):
                    mode = "C"
                    show_popup(mode)
                    popup = True
                elif story_mode_4.rect.collidepoint(event.pos):
                    mode = "D"
                    show_popup(mode)
                    popup = True
                elif popup and text_rect.collidepoint(event.pos):
                    init_bg(SCREEN, SCREEN_PATH + "story_mode_map.png", SCREEN_WIDTH, SCREEN_HEIGHT)
                    init_view(SCREEN,
                          [back_button, story_mode_1, story_mode_2, story_mode_3, story_mode_4, start_button])
                    pygame.display.flip()
                    popup = False
                elif start_button.rect.collidepoint(event.pos):
                    if mode == "A":
                        from Data.GAME_VIEW.SCREEN.start import start_game
                        start_game(int(config['system']['SCREEN_WIDTH']), int(config['system']['SCREEN_HEIGHT']), 1,
                                   ["USER", "COMPUTER1"], color_weakness_value, MODE_COMBO)
                    elif mode == "B":
                        if config['system']['STORY_A_WIN'] == "True":
                            from Data.GAME_VIEW.SCREEN.start import start_game
                            start_game(int(config['system']['SCREEN_WIDTH']), int(config['system']['SCREEN_HEIGHT']), 2,
                                       ["USER", "COMPUTER1", "COMPUTER2"], color_weakness_value, MODE_ALLCARD)
                        else:
                            show_popup("none")
                    elif mode == "C":
                        if config['system']['STORY_B_WIN'] == "True":
                            from Data.GAME_VIEW.SCREEN.start import start_game
                            start_game(int(config['system']['SCREEN_WIDTH']), int(config['system']['SCREEN_HEIGHT']), 2,
                                       ["USER", "COMPUTER1", "COMPUTER2"], color_weakness_value, MODE_CHANGECOLOR)
                        else:
                            show_popup("none")
                    elif mode == "D":
                        if config['system']['STORY_C_WIN'] == "True":
                            from Data.GAME_VIEW.SCREEN.loby import loby
                            loby(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, MODE_OPENSHUFFLE)
                        else:
                            show_popup("none")
        pygame.display.flip()
        