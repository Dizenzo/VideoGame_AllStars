'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                       Load and Initialize Modules     
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#  Load and initialize Modules here
import random, pygame, sys, time
from pygame.locals import *
from collections import namedtuple
pygame.init()
pygame.mixer.init(channels=4)

#  Window Information
FPS = 60
windowwidth = 1280
windowheight = 800
CELLSIZE = 80
assert windowwidth % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert windowheight % CELLSIZE == 0, "Window height must be a multiple of cell size."
GAMEWINDOW = pygame.display.set_mode((windowwidth, windowheight))
CLOCK = pygame.time.Clock()


#  Colors
#             R    G    B
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARKRED = (139,0,0)
BLUE = (2, 54, 168)
GRAYBLUE = (211, 217, 230)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
LIGHTGRAY = (235, 230, 230)
GOLD = (255, 187, 15)
DARKGOLD = (255,140,0)
SILVER = (192,192,192)
DARKSILVER = (105,105,105)
BGCOLOR = BLACK

#  Keys
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

seconds_1 = 60
seconds_2 = 120
seconds_3 = 180
seconds_4 = 240
seconds_5 = 300



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
 Images     Images     Images     Images     Images     Images     Images     
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

title = pygame.image.load('images/videogame.png')
title2 = pygame.image.load('images/allstars.png')

titlebg_image = pygame.image.load('images/titlescreenbg.png')
CharSelect_bg = pygame.image.load('images/CharSelect_bg.jpg')
EnemySelect_bg = pygame.image.load('images/Enemyselect_bg.jpg')
ChocoboImage = pygame.image.load('images/Chocobo.png')

tutorial_heal_image = pygame.image.load('images/heal_image.png')
tutorial_special_image = pygame.image.load('images/special_image.png')
tutorial_box = pygame.image.load('images/mario_box.png')
life_image = pygame.image.load('images/tibia_life.png')
tutorialbg = pygame.image.load('images/tutorialbg.png')
Chocobo_tutorialImage = pygame.image.load('images/chocobo_tutorial.png')
Speech_bubble = pygame.image.load('images/speech_bubble.png')
tutorial_player = pygame.image.load('images/tutorial_player.png')
tutorial_enemy = pygame.image.load('images/tutorial_enemy.png')

GokuImage = pygame.image.load('images/Goku.png')
MarioImage = pygame.image.load('images/Mario.png')
KakashiImage = pygame.image.load('images/Kakashi.png')
KirbyImage = pygame.image.load('images/Kirby.png')
CloudImage = pygame.image.load('images/Cloud.png')
PikachuImage = pygame.image.load('images/Pikachu.png')
ChuckNorrisImage = pygame.image.load('images/ChuckNorris.png')
LinkImage = pygame.image.load('images/Link.png')

RobotnikImage = pygame.image.load('images/Robotnik.png')  # 290x200
FriezaImage = pygame.image.load('images/Frieza.png')  # 290x200
BowserImage = pygame.image.load('images/Bowser.png')  # 290x200
MagnetoImage = pygame.image.load('images/Magneto.png')  # 290x200
GanondorfImage = pygame.image.load('images/Ganondorf.png')  # 290x200
SephirothImage = pygame.image.load('images/Sephiroth.png')  # 290x200

ShieldImage = pygame.image.load('images/energyshield.png')
ShieldImage_small = pygame.image.load('images/energyshield_small.png')

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
 Audio     Audio     Audio     Audio     Audio     Audio     Audio     
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# hit_sound = pygame.mixer.Sound('audio/attack_sound.wav')
# normal_hit_sound = pygame.mixer.Sound('audio/normal_hit.wav')
shield_sound = pygame.mixer.Sound('audio/shield.wav')
shield_block_sound = pygame.mixer.Sound('audio/shield_block.wav')
enemy_attack_sound = pygame.mixer.Sound('audio/enemy_attack.wav')
chocobo_sound = pygame.mixer.Sound('audio/chocobo.wav')

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        Text/Fonts     Text/Fonts     Text/Fonts                
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

pygame.display.set_caption('VIDEO GAME ALL-STARS')

tutorial_text = pygame.font.Font('freesansbold.ttf', 20)
TEXT = pygame.font.Font('freesansbold.ttf', 48)
TEXT_special_dmg = pygame.font.Font('freesansbold.ttf', 60)
smallText = pygame.font.Font("freesansbold.ttf", 20)
mediumText = pygame.font.Font("freesansbold.ttf", 28)
tutorialhpText = pygame.font.Font("freesansbold.ttf", 32)
summaryFont = pygame.font.Font('freesansbold.ttf', 40)
titleFont = pygame.font.Font('freesansbold.ttf', 58)
large_titleFont = pygame.font.Font('freesansbold.ttf', 110)

def text_objects(text, font):  # text, font, color
    textsurface = font.render(text, True, BLACK)  # Change to color and add parameter to function?
    return textsurface, textsurface.get_rect()


def text_objects_white(text, font):
    textsurface = font.render(text, True, WHITE)
    return textsurface, textsurface.get_rect()

def drawbutton(msg, x, y, w, h, ic, ac, bc,
               action=None):  # ic=inact color, ac=active color(hover over,bc=button color)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(GAMEWINDOW, ac, (x, y, w, h))

        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(GAMEWINDOW, ic, (x, y, w, h))
        pygame.draw.rect(GAMEWINDOW, bc, (x - 3, y - 3, w - 2, h - 2))

    textsurf, textrect = text_objects(msg, smallText)
    textrect.center = ((x + (w / 2)), (y + (h / 2)))
    GAMEWINDOW.blit(textsurf, textrect)


def checkforkeypress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyupevents = pygame.event.get(KEYUP)
    if len(keyupevents) == 0:
        return None
    if keyupevents[0].key == K_ESCAPE:
        terminate()


def gameover():
    gameover_text = titleFont.render('Game Over!', True, WHITE)
    game_over = True
    while game_over is True:
        ev = pygame.event.get()
        x, y = pygame.mouse.get_pos()
        GAMEWINDOW.fill(BLACK)
        GAMEWINDOW.blit(gameover_text,
                        ((windowwidth/2) - 180, 350))
        drawbutton("Main Menu", 10, 10, 135, 50, BLACK, RED, LIGHTGRAY)
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if x in range(11, 144) and y in range(11, 59):
                    main()
        if checkforkeypress():
            pygame.event.get()  # clear event queue
            return
        pygame.display.update()
        CLOCK.tick(FPS)


def end_game_screen(name, player_max_health, player_max_energy, attack_power, defense, special_power,
                    total_green, total_yellow, total_red, total_misses, highest_combo):
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.load('audio/summary.wav')
    pygame.mixer.music.play(-1)
    player_image = pygame.image.load(f'images/{name}.png')

    while True:
        x, y = pygame.mouse.get_pos()
        ev = pygame.event.get()
        congratulations = large_titleFont.render('Congratulations!', True, WHITE)
        well_fought = summaryFont.render(f'Well fought, {name}!', True, RED)
        well_fought_shadow = summaryFont.render(f'Well fought, {name}!', True, BLACK)
        summary = summaryFont.render('Final Summary', True, WHITE)
        green_hit = mediumText.render(f'Excellent hits: {total_green}', True, GREEN)
        yellow_hit = mediumText.render(f'Moderate hits: {total_yellow}', True, GOLD)
        red_hit = mediumText.render(f'Poor hits: {total_red}', True, RED)
        missed_hits = mediumText.render(f'Missed hits: {total_misses}', True, DARKRED)
        max_combo = mediumText.render(f'Best combo streak: {highest_combo}', True, WHITE)
        max_health = smallText.render(f'Health: {player_max_health}', True, BLACK)
        max_energy = smallText.render(f'Energy: {player_max_energy}', True, BLACK)
        current_defense = smallText.render(f'Defense: {defense}', True, BLACK)
        current_special = smallText.render(f'Special: {special_power}', True, BLACK)
        current_attack = smallText.render(f'Attack: {attack_power}', True, BLACK)
        GAMEWINDOW.fill(BLACK)
        pygame.draw.rect(GAMEWINDOW, BLUE, (450, 240, 600, 400))
        pygame.draw.rect(GAMEWINDOW, GRAYBLUE, (460, 250, 580, 380))
        drawbutton("Continue", 1140, 745, 135, 50, BLACK, RED, LIGHTGRAY)
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if x in range(1140, 1274) and y in range(750, 794):
                    pygame.mixer.music.stop()
                    main()
        GAMEWINDOW.blit(congratulations,
                        ((windowwidth / 2) - 450, 50))
        GAMEWINDOW.blit(summary,
                        (30, 280))
        GAMEWINDOW.blit(green_hit,
                        (30, 350))
        GAMEWINDOW.blit(yellow_hit,
                        (30, 400))
        GAMEWINDOW.blit(red_hit,
                        (30, 450))
        GAMEWINDOW.blit(missed_hits,
                        (30, 500))
        GAMEWINDOW.blit(max_combo,
                        (30, 550))
        GAMEWINDOW.blit(well_fought_shadow,
                        (513, 283))
        GAMEWINDOW.blit(well_fought,
                        (510, 280))
        GAMEWINDOW.blit(max_health,
                        (800, 365))
        GAMEWINDOW.blit(max_energy,
                        (800, 415))
        GAMEWINDOW.blit(current_attack,
                        (800, 465))
        GAMEWINDOW.blit(current_defense,
                        (800, 515))
        GAMEWINDOW.blit(current_special,
                        (800, 565))
        GAMEWINDOW.blit(player_image,
                        (510, 340))
        if checkforkeypress():
            pygame.event.get()  # clear event queue
            return
        pygame.display.update()
        CLOCK.tick(FPS)


class StartScreen:
    def __init__(self):
        self.tutorial_text_timer = 0
        self.phrase = []
        self.phrase_words_printed = []
        self.line_one = []
        self.line_two = []
        self.line_three = []
        self.line_four = []
        self.line_five = []
        self.startmusic()
        self.drawbackground()

    def drawbackground(self):
        intro = True
        while intro:
            pygame.mixer.music.set_volume(0.5)
            ev = pygame.event.get()
            x, y = pygame.mouse.get_pos()
            GAMEWINDOW.blit(titlebg_image,
                            (0, 0))
            pygame.draw.rect(GAMEWINDOW, BLACK, (275, 95, 775, 250))
            pygame.draw.rect(GAMEWINDOW, RED, (280, 100, 765, 240))
            GAMEWINDOW.blit(title, (299, 130))
            GAMEWINDOW.blit(title2, (348, 230))
            GAMEWINDOW.blit(ChocoboImage, (1100, 550))
            drawbutton("Start", 575, 500, 135, 50, BLACK, GOLD, LIGHTGRAY)
            drawbutton("How to Play", 1105, 500, 135, 50, BLACK, GOLD, LIGHTGRAY)
            drawbutton("Quit", 575, 570, 135, 50, BLACK, GOLD, LIGHTGRAY, terminate)
            for event in ev:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if x in range(1105, 1237) and y in range(501, 549):
                        self.showtutorialscreen()
                    if x in range(576, 708) and y in range(501, 549):
                        self.stopmusic()
                        return
            if checkforkeypress():
                pygame.event.get()  # clear event queue
                return
            pygame.display.update()
            CLOCK.tick(FPS)

    def generate_text(self, line):
        text_speed = 5
        if self.tutorial_text_timer % text_speed == 0 and len(self.phrase) != 0:
            if line == 5:
                word = self.phrase.pop(0)
                self.line_five.append(word)
            if line == 4:
                word = self.phrase.pop(0)
                self.line_four.append(word)
            if line == 3:
                word = self.phrase.pop(0)
                self.line_three.append(word)
            elif line == 2:
                word = self.phrase.pop(0)
                self.line_two.append(word)
            elif line == 1:
                word = self.phrase.pop(0)
                self.line_one.append(word)

    def showtutorialscreen(self):
        pygame.mixer.music.set_volume(0.2)
        chocobo_sound_timer = 0
        cleanup = False
        current_step = 0
        total_steps = 9
        show_player = False
        show_enemy = False
        show_health = False
        show_energy = False
        show_lives = False
        show_timer = False
        show_ability_buttons = False

        welcome = True
        welcome_text = "Welcome to Video Game All-Stars!"

        overview = False
        overview_ln1 = "The objective of this game is to"
        overview_ln2 = "choose your favorite hero and battle"
        overview_ln3 = "your way through the evil villians."
        overview_ln4 = " Be careful though . . . . ."
        overview_ln5 = " If you lose all 3 lives, GAME OVER!"

        tutorial_pt1 = False
        tutorial_pt1_ln1 = "Each battle will increase in"
        tutorial_pt1_ln2 = "difficulty. But luckily for you,"
        tutorial_pt1_ln3 = "I will be teaching you how to fight!"
        tutorial_pt1_ln4 = "Each battle will have a time limit"
        tutorial_pt1_ln5 = "of 100 seconds. If you fail to defeat"

        tutorial_pt2 = False
        tutorial_pt2_ln1 = "your opponent in that time, you lose."
        tutorial_pt2_ln2 = "If either you or your opponent's"
        tutorial_pt2_ln3 = "health reaches 0, then the battle"
        tutorial_pt2_ln4 = "is over."
        tutorial_pt2_ln5 = "        Now, lets cover the basics!"

        tutorial_pt3 = False
        tutorial_pt3_ln1 = "First, we will look at ATTACKING."
        tutorial_pt3_ln2 = "During the battle, circles will pop up"
        tutorial_pt3_ln3 = "all over your opponent. If you click"
        tutorial_pt3_ln4 = "on the circle while it is green, you"
        tutorial_pt3_ln5 = "will do the most damage, red - least."

        tutorial_pt4 = False
        tutorial_pt4_ln1 = "Enemies will attack back!"
        tutorial_pt4_ln2 = "If you see circles on yourself,"
        tutorial_pt4_ln3 = "hold down the SPACE bar to shield"
        tutorial_pt4_ln4 = "while the circle disappears."
        tutorial_pt4_ln5 = " This costs energy, so timing is key!"

        tutorial_pt5 = False
        tutorial_pt5_ln1 = "Energy is a vital resource:"
        tutorial_pt5_ln2 = "25 energy is used to HEAL"
        tutorial_pt5_ln3 = "50 energy to cast your SPECIAL."
        tutorial_pt5_ln4 = "These can be cast by clicking"
        tutorial_pt5_ln5 = "these 2 buttons during a battle!"

        tutorial_pt6 = False
        tutorial_pt6_ln1 = "Energy is gained by performing"
        tutorial_pt6_ln2 = "combos. Each successful attack"
        tutorial_pt6_ln3 = "adds to your combo, the higher"
        tutorial_pt6_ln4 = "your combo, the more energy!"
        tutorial_pt6_ln5 = "You can also gain energy from stats."

        tutorial_pt7 = False
        tutorial_pt7_ln1 = "Which reminds me!"
        tutorial_pt7_ln2 = "After defeating an enemy, you will"
        tutorial_pt7_ln3 = "earn stat points! Spend them in"
        tutorial_pt7_ln4 = "SPECIAL, ATTACK, DEFENSE, ENERGY"
        tutorial_pt7_ln5 = "to customize your hero!"

        tutorial_pt8 = False
        tutorial_pt8_ln1 = "SPECIAL - stronger ability + heal"
        tutorial_pt8_ln2 = "ATTACK - stronger normal attacks"
        tutorial_pt8_ln3 = "DEFENSE - max health + less damage"
        tutorial_pt8_ln4 = "ENERGY - max energy + faster gain"
        tutorial_pt8_ln5 = "    Good luck out there HERO!"

        Point = namedtuple('Point', 'x y')
        speech_bubble = Point(200, 140)
        next_button_width = 55
        next_button_height = 30
        hide_next_button = False
        blocked_text = TEXT.render(f'BLOCKED!', True, WHITE)
        seconds = titleFont.render('100', True, WHITE)
        player_hp = tutorialhpText.render(' Health: 150', True, GREEN)
        player_energy = tutorialhpText.render('Energy: 200', True, GOLD)
        enemy_hp = tutorialhpText.render(' Health: 700', True, GREEN)
        enemy_energy = tutorialhpText.render('Energy: 500', True, GOLD)
        special_label = smallText.render('Special', True, BLACK)
        heal_label = smallText.render('Heal', True, BLACK)
        show_ln1 = 30
        show_ln2 = 90
        show_ln3 = 150
        show_ln4 = 210
        show_ln5 = 270
        chocobo_noise = 5

        self.phrase = welcome_text.split(" ")

        while True:
            ev = pygame.event.get()
            space = ' '
            x, y = pygame.mouse.get_pos()
            chocobo_sound_timer += 1
            GAMEWINDOW.blit(tutorialbg, (0, 0))
            GAMEWINDOW.blit(tutorial_box, (105, 510))
            GAMEWINDOW.blit(Chocobo_tutorialImage, (90, 360))
            GAMEWINDOW.blit(Speech_bubble, (speech_bubble.x, speech_bubble.y))
            drawbutton("Back", 10, 10, 135, 50, BLACK, RED, LIGHTGRAY)
            if not hide_next_button:
                drawbutton("Next ", (speech_bubble.x + 405), (speech_bubble.y + 195), next_button_width,
                           next_button_height, BLACK, GREEN, GOLD)
            step_info = tutorial_text.render(f'{current_step} / {total_steps}', True, BLACK)
            if not hide_next_button:
                GAMEWINDOW.blit(step_info, ((speech_bubble.x + 340), (speech_bubble.y + 200)))
            elif hide_next_button:
                GAMEWINDOW.blit(step_info, ((speech_bubble.x + 410), (speech_bubble.y + 200)))
            print(f'phrase: {self.phrase}')
            print(f'phrase words printed: {self.phrase_words_printed}')

            if show_player:
                GAMEWINDOW.blit(tutorial_player, (490, 535))

            if show_health:
                pygame.draw.rect(GAMEWINDOW, BLACK, (520, 710, 210, 45))    # player health
                pygame.draw.rect(GAMEWINDOW, BLACK, (900, 710, 210, 45))    # enemy health
                GAMEWINDOW.blit(player_hp,
                                (530, 720))
                GAMEWINDOW.blit(enemy_hp,
                                (910, 720))
            if show_energy:
                pygame.draw.rect(GAMEWINDOW, BLACK, (520, 750, 210, 45))    # player energy
                pygame.draw.rect(GAMEWINDOW, BLACK, (900, 750, 210, 45))    # enemy energy
                GAMEWINDOW.blit(player_energy,
                                (530, 760))
                GAMEWINDOW.blit(enemy_energy,
                                (910, 760))

            if show_enemy:
                GAMEWINDOW.blit(tutorial_enemy, (800, 265))

            if show_lives:
                life_count = smallText.render('x 3', True, BLACK)
                GAMEWINDOW.blit(life_count, (1235, 40))
                GAMEWINDOW.blit(life_image, (1190, 20))

            if show_timer:
                GAMEWINDOW.blit(seconds,
                                (((windowwidth / 2) - 35), 10))

            if show_ability_buttons:
                heal_x = 430
                heal_y = 460
                heal_image_x = heal_x - 110
                heal_image_y = heal_y - 110

                special_x = 570
                special_y = 460
                special_image_x = special_x - 110
                special_image_y = special_y - 110

                GAMEWINDOW.blit(tutorial_heal_image,
                                (heal_image_x, heal_image_y))
                pygame.draw.circle(GAMEWINDOW, GREEN, (heal_x, heal_y), 50)
                pygame.draw.circle(GAMEWINDOW, SILVER, (heal_x, heal_y), 45)
                GAMEWINDOW.blit(heal_label, (heal_x - 21, heal_y - 8))
                GAMEWINDOW.blit(tutorial_special_image,
                                (special_image_x, special_image_y))
                pygame.draw.circle(GAMEWINDOW, DARKGOLD, (special_x, special_y), 50)
                pygame.draw.circle(GAMEWINDOW, SILVER, (special_x, special_y), 45)
                GAMEWINDOW.blit(special_label, (special_x - 35, special_y - 8))

        # Brief description of game
            if overview:
                printed_line_one = tutorial_text.render(space.join(self.line_one), True, BLACK)
                printed_line_two = tutorial_text.render(space.join(self.line_two), True, BLACK)
                printed_line_three = tutorial_text.render(space.join(self.line_three), True, BLACK)
                printed_line_four = tutorial_text.render(space.join(self.line_four), True, BLACK)
                printed_line_five = tutorial_text.render(space.join(self.line_five), True, BLACK)

                if chocobo_sound_timer == chocobo_noise:
                    chocobo_sound.play()

                if self.tutorial_text_timer == show_ln5:
                    self.phrase = overview_ln5.split(" ")
                if self.tutorial_text_timer == show_ln4:
                    self.phrase = overview_ln4.split(" ")
                if self.tutorial_text_timer == show_ln3:
                    self.phrase = overview_ln3.split(" ")
                if self.tutorial_text_timer == show_ln2:
                    self.phrase = overview_ln2.split(" ")
                if self.tutorial_text_timer == show_ln1:
                    self.phrase = overview_ln1.split(" ")

                if self.tutorial_text_timer >= show_ln5:
                    self.generate_text(5)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))
                    GAMEWINDOW.blit(printed_line_five, ((speech_bubble.x + 105), (speech_bubble.y + 170)))
                    show_lives = True

                elif self.tutorial_text_timer >= show_ln4:
                    self.generate_text(4)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))
                    show_enemy = True

                elif self.tutorial_text_timer >= show_ln3:
                    self.generate_text(3)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    show_player = True

                elif self.tutorial_text_timer >= show_ln2:
                    self.generate_text(2)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))

                elif self.tutorial_text_timer >= show_ln1:
                    self.generate_text(1)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))

                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if x in range((speech_bubble.x + 405), ((speech_bubble.x + 405) + next_button_width)) and \
                                y in range((speech_bubble.y + 195), ((speech_bubble.y + 195) + next_button_height)):
                            overview = False
                            tutorial_pt1 = True
                            show_player = True
                            show_enemy = True
                            show_lives = True
                            cleanup = True

        # Showing tutorial 1
            elif tutorial_pt1:

                printed_line_one = tutorial_text.render(space.join(self.line_one), True, BLACK)
                printed_line_two = tutorial_text.render(space.join(self.line_two), True, BLACK)
                printed_line_three = tutorial_text.render(space.join(self.line_three), True, BLACK)
                printed_line_four = tutorial_text.render(space.join(self.line_four), True, BLACK)
                printed_line_five = tutorial_text.render(space.join(self.line_five), True, BLACK)

                if chocobo_sound_timer == chocobo_noise:
                    chocobo_sound.play()

                if self.tutorial_text_timer == show_ln5:
                    self.phrase = tutorial_pt1_ln5.split(" ")
                if self.tutorial_text_timer == show_ln4:
                    self.phrase = tutorial_pt1_ln4.split(" ")
                if self.tutorial_text_timer == show_ln3:
                    self.phrase = tutorial_pt1_ln3.split(" ")
                if self.tutorial_text_timer == show_ln2:
                    self.phrase = tutorial_pt1_ln2.split(" ")
                if self.tutorial_text_timer == show_ln1:
                    self.phrase = tutorial_pt1_ln1.split(" ")

                if self.tutorial_text_timer >= show_ln5:
                    self.generate_text(5)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))
                    GAMEWINDOW.blit(printed_line_five, ((speech_bubble.x + 105), (speech_bubble.y + 170)))
                    show_timer = True

                elif self.tutorial_text_timer >= show_ln4:
                    self.generate_text(4)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))

                elif self.tutorial_text_timer >= show_ln3:
                    self.generate_text(3)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))

                elif self.tutorial_text_timer >= show_ln2:
                    self.generate_text(2)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))

                elif self.tutorial_text_timer >= show_ln1:
                    self.generate_text(1)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))

                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if x in range((speech_bubble.x + 405), ((speech_bubble.x + 405) + next_button_width)) and \
                                y in range((speech_bubble.y + 195), ((speech_bubble.y + 195) + next_button_height)):
                            tutorial_pt1 = False
                            tutorial_pt2 = True
                            show_timer = True
                            cleanup = True

        # Showing tutorial 2
            elif tutorial_pt2:

                printed_line_one = tutorial_text.render(space.join(self.line_one), True, BLACK)
                printed_line_two = tutorial_text.render(space.join(self.line_two), True, BLACK)
                printed_line_three = tutorial_text.render(space.join(self.line_three), True, BLACK)
                printed_line_four = tutorial_text.render(space.join(self.line_four), True, BLACK)
                printed_line_five = tutorial_text.render(space.join(self.line_five), True, BLACK)

                if chocobo_sound_timer == chocobo_noise:
                    chocobo_sound.play()

                if self.tutorial_text_timer == show_ln5:
                    self.phrase = tutorial_pt2_ln5.split(" ")
                if self.tutorial_text_timer == show_ln4:
                    self.phrase = tutorial_pt2_ln4.split(" ")
                if self.tutorial_text_timer == show_ln3:
                    self.phrase = tutorial_pt2_ln3.split(" ")
                if self.tutorial_text_timer == show_ln2:
                    self.phrase = tutorial_pt2_ln2.split(" ")
                if self.tutorial_text_timer == show_ln1:
                    self.phrase = tutorial_pt2_ln1.split(" ")

                if self.tutorial_text_timer >= show_ln5:
                    self.generate_text(5)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))
                    GAMEWINDOW.blit(printed_line_five, ((speech_bubble.x + 105), (speech_bubble.y + 170)))

                elif self.tutorial_text_timer >= show_ln4:
                    self.generate_text(4)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))
                    show_health = True

                elif self.tutorial_text_timer >= show_ln3:
                    self.generate_text(3)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))

                elif self.tutorial_text_timer >= show_ln2:
                    self.generate_text(2)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))

                elif self.tutorial_text_timer >= show_ln1:
                    self.generate_text(1)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))

                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if x in range((speech_bubble.x + 405), ((speech_bubble.x + 405) + next_button_width)) and \
                                y in range((speech_bubble.y + 195), ((speech_bubble.y + 195) + next_button_height)):
                            tutorial_pt2 = False
                            tutorial_pt3 = True
                            show_health = True
                            cleanup = True

        # Showing tutorial 3
            elif tutorial_pt3:

                printed_line_one = tutorial_text.render(space.join(self.line_one), True, BLACK)
                printed_line_two = tutorial_text.render(space.join(self.line_two), True, BLACK)
                printed_line_three = tutorial_text.render(space.join(self.line_three), True, BLACK)
                printed_line_four = tutorial_text.render(space.join(self.line_four), True, BLACK)
                printed_line_five = tutorial_text.render(space.join(self.line_five), True, BLACK)
                good_hit = mediumText.render('GOOD', True, GREEN)
                moderate_hit = mediumText.render('MODERATE', True, GOLD)
                poor_hit = mediumText.render('POOR', True, RED)

                if chocobo_sound_timer == chocobo_noise:
                    chocobo_sound.play()

                if self.tutorial_text_timer == show_ln5:
                    self.phrase = tutorial_pt3_ln5.split(" ")
                if self.tutorial_text_timer == show_ln4:
                    self.phrase = tutorial_pt3_ln4.split(" ")
                if self.tutorial_text_timer == show_ln3:
                    self.phrase = tutorial_pt3_ln3.split(" ")
                if self.tutorial_text_timer == show_ln2:
                    self.phrase = tutorial_pt3_ln2.split(" ")
                if self.tutorial_text_timer == show_ln1:
                    self.phrase = tutorial_pt3_ln1.split(" ")

                if self.tutorial_text_timer >= show_ln5:
                    self.generate_text(5)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))
                    GAMEWINDOW.blit(printed_line_five, ((speech_bubble.x + 105), (speech_bubble.y + 170)))
                    pygame.draw.circle(GAMEWINDOW, RED, (990, 575), 10, 3)
                    GAMEWINDOW.blit(poor_hit, (1010, 565))
                    pygame.draw.circle(GAMEWINDOW, GOLD, (950, 495), 28, 3)
                    GAMEWINDOW.blit(moderate_hit, (980, 487))
                    pygame.draw.circle(GAMEWINDOW, GREEN, (1020, 380), 45, 3)
                    GAMEWINDOW.blit(good_hit, (1070, 375))

                elif self.tutorial_text_timer >= show_ln4:
                    self.generate_text(4)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))
                    pygame.draw.circle(GAMEWINDOW, RED, (990, 575), 15, 3)
                    pygame.draw.circle(GAMEWINDOW, GOLD, (950, 495), 38, 3)
                    pygame.draw.circle(GAMEWINDOW, GREEN, (1020, 380), 60, 3)

                elif self.tutorial_text_timer >= show_ln3:
                    self.generate_text(3)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    pygame.draw.circle(GAMEWINDOW, GOLD, (990, 575), 30, 3)
                    pygame.draw.circle(GAMEWINDOW, GREEN, (950, 495), 49, 3)

                elif self.tutorial_text_timer >= show_ln2:
                    self.generate_text(2)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    pygame.draw.circle(GAMEWINDOW, GREEN, (990, 575), 45, 3)
                    pygame.draw.circle(GAMEWINDOW, GREEN, (950, 495), 60, 3)

                elif self.tutorial_text_timer >= show_ln1:
                    self.generate_text(1)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    pygame.draw.circle(GAMEWINDOW, GREEN, (990, 575), 60, 3)

                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if x in range((speech_bubble.x + 405), ((speech_bubble.x + 405) + next_button_width)) and \
                                y in range((speech_bubble.y + 195), ((speech_bubble.y + 195) + next_button_height)):
                            tutorial_pt3 = False
                            tutorial_pt4 = True
                            cleanup = True

            # Showing tutorial 4
            elif tutorial_pt4:

                printed_line_one = tutorial_text.render(space.join(self.line_one), True, BLACK)
                printed_line_two = tutorial_text.render(space.join(self.line_two), True, BLACK)
                printed_line_three = tutorial_text.render(space.join(self.line_three), True, BLACK)
                printed_line_four = tutorial_text.render(space.join(self.line_four), True, BLACK)
                printed_line_five = tutorial_text.render(space.join(self.line_five), True, BLACK)

                if chocobo_sound_timer == chocobo_noise:
                    chocobo_sound.play()

                if self.tutorial_text_timer == show_ln5:
                    self.phrase = tutorial_pt4_ln5.split(" ")
                if self.tutorial_text_timer == show_ln4:
                    self.phrase = tutorial_pt4_ln4.split(" ")
                if self.tutorial_text_timer == show_ln3:
                    self.phrase = tutorial_pt4_ln3.split(" ")
                if self.tutorial_text_timer == show_ln2:
                    self.phrase = tutorial_pt4_ln2.split(" ")
                if self.tutorial_text_timer == show_ln1:
                    self.phrase = tutorial_pt4_ln1.split(" ")

                if self.tutorial_text_timer >= show_ln5:
                    self.generate_text(5)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))
                    GAMEWINDOW.blit(printed_line_five, ((speech_bubble.x + 105), (speech_bubble.y + 170)))
                    pygame.draw.circle(GAMEWINDOW, RED, (690, 675), 5, 3)
                    pygame.draw.circle(GAMEWINDOW, GOLD, (590, 605), 31, 3)
                    GAMEWINDOW.blit(ShieldImage_small, (440, 465))
                    GAMEWINDOW.blit(blocked_text,
                                    (640, 520))

                elif self.tutorial_text_timer >= show_ln4:
                    self.generate_text(4)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))
                    pygame.draw.circle(GAMEWINDOW, RED, (690, 675), 20, 3)
                    pygame.draw.circle(GAMEWINDOW, GREEN, (590, 605), 46, 3)
                    GAMEWINDOW.blit(ShieldImage_small, (440, 465))

                elif self.tutorial_text_timer >= show_ln3:
                    self.generate_text(3)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    pygame.draw.circle(GAMEWINDOW, GOLD, (690, 675), 34, 3)
                    pygame.draw.circle(GAMEWINDOW, GREEN, (590, 605), 60, 3)
                    GAMEWINDOW.blit(ShieldImage_small, (440, 465))

                elif self.tutorial_text_timer >= show_ln2:
                    self.generate_text(2)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    pygame.draw.circle(GAMEWINDOW, GREEN, (690, 675), 45, 3)

                elif self.tutorial_text_timer >= show_ln1:
                    self.generate_text(1)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    pygame.draw.circle(GAMEWINDOW, GREEN, (690, 675), 60, 3)

                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if x in range((speech_bubble.x + 405), ((speech_bubble.x + 405) + next_button_width)) and \
                                y in range((speech_bubble.y + 195), ((speech_bubble.y + 195) + next_button_height)):
                            tutorial_pt4 = False
                            tutorial_pt5 = True
                            cleanup = True

            # Showing tutorial 5
            elif tutorial_pt5:

                printed_line_one = tutorial_text.render(space.join(self.line_one), True, BLACK)
                printed_line_two = tutorial_text.render(space.join(self.line_two), True, BLACK)
                printed_line_three = tutorial_text.render(space.join(self.line_three), True, BLACK)
                printed_line_four = tutorial_text.render(space.join(self.line_four), True, BLACK)
                printed_line_five = tutorial_text.render(space.join(self.line_five), True, BLACK)

                if chocobo_sound_timer == chocobo_noise:
                    chocobo_sound.play()

                if self.tutorial_text_timer == show_ln5:
                    self.phrase = tutorial_pt5_ln5.split(" ")
                if self.tutorial_text_timer == show_ln4:
                    self.phrase = tutorial_pt5_ln4.split(" ")
                if self.tutorial_text_timer == show_ln3:
                    self.phrase = tutorial_pt5_ln3.split(" ")
                if self.tutorial_text_timer == show_ln2:
                    self.phrase = tutorial_pt5_ln2.split(" ")
                if self.tutorial_text_timer == show_ln1:
                    self.phrase = tutorial_pt5_ln1.split(" ")

                if self.tutorial_text_timer >= show_ln5:
                    self.generate_text(5)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))
                    GAMEWINDOW.blit(printed_line_five, ((speech_bubble.x + 105), (speech_bubble.y + 170)))
                    show_ability_buttons = True

                elif self.tutorial_text_timer >= show_ln4:
                    self.generate_text(4)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))

                elif self.tutorial_text_timer >= show_ln3:
                    self.generate_text(3)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))

                elif self.tutorial_text_timer >= show_ln2:
                    self.generate_text(2)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    show_energy = True

                elif self.tutorial_text_timer >= show_ln1:
                    self.generate_text(1)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))

                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if x in range((speech_bubble.x + 405), ((speech_bubble.x + 405) + next_button_width)) and \
                                y in range((speech_bubble.y + 195), ((speech_bubble.y + 195) + next_button_height)):
                            tutorial_pt5 = False
                            tutorial_pt6 = True
                            show_energy = True
                            show_ability_buttons = True
                            cleanup = True

            # Showing tutorial 6
            elif tutorial_pt6:

                printed_line_one = tutorial_text.render(space.join(self.line_one), True, BLACK)
                printed_line_two = tutorial_text.render(space.join(self.line_two), True, BLACK)
                printed_line_three = tutorial_text.render(space.join(self.line_three), True, BLACK)
                printed_line_four = tutorial_text.render(space.join(self.line_four), True, BLACK)
                printed_line_five = tutorial_text.render(space.join(self.line_five), True, BLACK)

                if chocobo_sound_timer == chocobo_noise:
                    chocobo_sound.play()

                if self.tutorial_text_timer == show_ln5:
                    self.phrase = tutorial_pt6_ln5.split(" ")
                if self.tutorial_text_timer == show_ln4:
                    self.phrase = tutorial_pt6_ln4.split(" ")
                if self.tutorial_text_timer == show_ln3:
                    self.phrase = tutorial_pt6_ln3.split(" ")
                if self.tutorial_text_timer == show_ln2:
                    self.phrase = tutorial_pt6_ln2.split(" ")
                if self.tutorial_text_timer == show_ln1:
                    self.phrase = tutorial_pt6_ln1.split(" ")

                if self.tutorial_text_timer >= show_ln5:
                    self.generate_text(5)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))
                    GAMEWINDOW.blit(printed_line_five, ((speech_bubble.x + 105), (speech_bubble.y + 170)))

                elif self.tutorial_text_timer >= show_ln4:
                    self.generate_text(4)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))

                elif self.tutorial_text_timer >= show_ln3:
                    self.generate_text(3)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))

                elif self.tutorial_text_timer >= show_ln2:
                    self.generate_text(2)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))

                elif self.tutorial_text_timer >= show_ln1:
                    self.generate_text(1)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))

                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if x in range((speech_bubble.x + 405), ((speech_bubble.x + 405) + next_button_width)) and \
                                y in range((speech_bubble.y + 195), ((speech_bubble.y + 195) + next_button_height)):
                            tutorial_pt6 = False
                            tutorial_pt7 = True
                            cleanup = True

            # Showing tutorial 7
            elif tutorial_pt7:

                printed_line_one = tutorial_text.render(space.join(self.line_one), True, BLACK)
                printed_line_two = tutorial_text.render(space.join(self.line_two), True, BLACK)
                printed_line_three = tutorial_text.render(space.join(self.line_three), True, BLACK)
                printed_line_four = tutorial_text.render(space.join(self.line_four), True, BLACK)
                printed_line_five = tutorial_text.render(space.join(self.line_five), True, BLACK)

                if chocobo_sound_timer == chocobo_noise:
                    chocobo_sound.play()

                if self.tutorial_text_timer == show_ln5:
                    self.phrase = tutorial_pt7_ln5.split(" ")
                if self.tutorial_text_timer == show_ln4:
                    self.phrase = tutorial_pt7_ln4.split(" ")
                if self.tutorial_text_timer == show_ln3:
                    self.phrase = tutorial_pt7_ln3.split(" ")
                if self.tutorial_text_timer == show_ln2:
                    self.phrase = tutorial_pt7_ln2.split(" ")
                if self.tutorial_text_timer == show_ln1:
                    self.phrase = tutorial_pt7_ln1.split(" ")

                if self.tutorial_text_timer >= show_ln5:
                    self.generate_text(5)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))
                    GAMEWINDOW.blit(printed_line_five, ((speech_bubble.x + 105), (speech_bubble.y + 170)))

                elif self.tutorial_text_timer >= show_ln4:
                    self.generate_text(4)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))

                elif self.tutorial_text_timer >= show_ln3:
                    self.generate_text(3)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))

                elif self.tutorial_text_timer >= show_ln2:
                    self.generate_text(2)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))

                elif self.tutorial_text_timer >= show_ln1:
                    self.generate_text(1)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))

                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if x in range((speech_bubble.x + 405), ((speech_bubble.x + 405) + next_button_width)) and \
                                y in range((speech_bubble.y + 195), ((speech_bubble.y + 195) + next_button_height)):
                            tutorial_pt7 = False
                            tutorial_pt8 = True
                            hide_next_button = True
                            cleanup = True

            # Showing tutorial 8
            elif tutorial_pt8:

                printed_line_one = tutorial_text.render(space.join(self.line_one), True, BLACK)
                printed_line_two = tutorial_text.render(space.join(self.line_two), True, BLACK)
                printed_line_three = tutorial_text.render(space.join(self.line_three), True, BLACK)
                printed_line_four = tutorial_text.render(space.join(self.line_four), True, BLACK)
                printed_line_five = tutorial_text.render(space.join(self.line_five), True, BLACK)

                if chocobo_sound_timer == chocobo_noise:
                    chocobo_sound.play()

                if self.tutorial_text_timer == show_ln5:
                    self.phrase = tutorial_pt8_ln5.split(" ")
                if self.tutorial_text_timer == show_ln4:
                    self.phrase = tutorial_pt8_ln4.split(" ")
                if self.tutorial_text_timer == show_ln3:
                    self.phrase = tutorial_pt8_ln3.split(" ")
                if self.tutorial_text_timer == show_ln2:
                    self.phrase = tutorial_pt8_ln2.split(" ")
                if self.tutorial_text_timer == show_ln1:
                    self.phrase = tutorial_pt8_ln1.split(" ")

                if self.tutorial_text_timer >= show_ln5:
                    self.generate_text(5)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))
                    GAMEWINDOW.blit(printed_line_five, ((speech_bubble.x + 105), (speech_bubble.y + 170)))

                elif self.tutorial_text_timer >= show_ln4:
                    self.generate_text(4)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))
                    GAMEWINDOW.blit(printed_line_four, ((speech_bubble.x + 105), (speech_bubble.y + 140)))

                elif self.tutorial_text_timer >= show_ln3:
                    self.generate_text(3)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))
                    GAMEWINDOW.blit(printed_line_three, ((speech_bubble.x + 105), (speech_bubble.y + 110)))

                elif self.tutorial_text_timer >= show_ln2:
                    self.generate_text(2)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))
                    GAMEWINDOW.blit(printed_line_two, ((speech_bubble.x + 105), (speech_bubble.y + 80)))

                elif self.tutorial_text_timer >= show_ln1:
                    self.generate_text(1)
                    GAMEWINDOW.blit(printed_line_one, ((speech_bubble.x + 105), (speech_bubble.y + 50)))

        # Showing welcome text
            elif welcome:
                if chocobo_sound_timer == 50:
                    chocobo_sound.play()
                if self.tutorial_text_timer >= 60:
                    self.generate_text(1)
                    printed_text = tutorial_text.render(space.join(self.line_one), True, BLACK)
                    GAMEWINDOW.blit(printed_text, ((speech_bubble.x + 115), (speech_bubble.y + 125)))
                    for event in ev:
                        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                            if x in range((speech_bubble.x + 405), ((speech_bubble.x + 405) + next_button_width)) and \
                                    y in range((speech_bubble.y + 195), ((speech_bubble.y + 195) + next_button_height)):
                                welcome = False
                                overview = True
                                cleanup = True

            if cleanup:
                chocobo_sound_timer = 0
                self.line_one = []
                self.line_two = []
                self.line_three = []
                self.line_four = []
                self.line_five = []
                self.tutorial_text_timer = 0
                current_step += 1
                cleanup = False

            for event in ev:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if x in range(11, 144) and y in range(11, 59):
                        chocobo_sound_timer = 0
                        self.line_one = []
                        self.line_two = []
                        self.line_three = []
                        self.line_four = []
                        self.line_five = []
                        self.tutorial_text_timer = 0
                        return
            if checkforkeypress():
                pygame.event.get()  # clear event queue
                return
            self.tutorial_text_timer += 1
            pygame.display.update()
            CLOCK.tick(FPS)

    def startmusic(self):
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.load('audio/introsong.wav')
        pygame.mixer.music.play(-1)

    def stopmusic(self):
        pygame.mixer.music.stop()


class CharacterSelect:
    def __init__(self):
        self.startmusic()
        self.playercharacter = ''
        self.continuebutton = 0
        self.enemycharacter = ''
        self.fightbutton = 0
        self.defeated = []
        self.coloredpictures = ['Dr. Robotnik']#, 'Bowser', 'Magneto', 'Ganondorf', 'Frieza', 'Sephiroth']
        self.grayedout = ['Bowser', 'Magneto', 'Ganondorf', 'Frieza', 'Sephiroth']
        self.playerselect()

    def playerselect(self):
        while True:
            title1 = titleFont.render('Choose your character!', True, RED)
            ev = pygame.event.get()
            x, y = pygame.mouse.get_pos()
            # print(self.x, self.y)
            charactertext = titleFont.render(str(self.playercharacter), True, WHITE)
            GAMEWINDOW.blit(CharSelect_bg,
                            (0, 0))
            GAMEWINDOW.blit(title1,
                            (315, 35)),
            self.drawcharselectbutton(CloudImage, 'Cloud', 340, 180, 200, 250, WHITE, GOLD, BLACK)
            self.drawcharselectbutton(KakashiImage, 'Kakashi', 140, 430, 200, 250, WHITE, GOLD, BLACK)
            self.drawcharselectbutton(PikachuImage, 'Pikachu', 540, 180, 200, 250, WHITE, GOLD, BLACK)
            self.drawcharselectbutton(KirbyImage, 'Kirby', 340, 430, 200, 250, WHITE, GOLD, BLACK)
            self.drawcharselectbutton(GokuImage, 'Goku', 740, 180, 200, 250, WHITE, GOLD, BLACK)
            self.drawcharselectbutton(ChuckNorrisImage, 'Chuck Norris', 540, 430, 200, 250, WHITE, GOLD, BLACK)
            self.drawcharselectbutton(MarioImage, 'Mario', 940, 430, 200, 250, WHITE, GOLD, BLACK)
            self.drawcharselectbutton(LinkImage, 'Link', 740, 430, 200, 250, WHITE, GOLD, BLACK)
            drawbutton("Main Menu", 10, 10, 135, 50, BLACK, RED, LIGHTGRAY)
            if self.continuebutton == 1:
                drawbutton("Continue", 1100, 720, 135, 50, BLACK, RED, LIGHTGRAY)

            GAMEWINDOW.blit(charactertext,
                            (520, 715))
            # drawGrid()
            for event in ev:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if x in range(11, 144) and y in range(11, 59):
                        StartScreen()
                    if x in range(1101, 1233) and y in range(722, 769) and self.continuebutton == 1:
                        return
            if checkforkeypress():
                pygame.event.get()  # clear event queue
                return
            pygame.display.update()
            CLOCK.tick(FPS)

    def drawcharselectbutton(self, image, name, x, y, w, h, ic, ac, bc):
        # ic=inactive color(White), ac=active color(Gold)(hover over,bc=button color)(Black)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if name == self.playercharacter:     # sets border color GOLD if selected
            pygame.draw.rect(GAMEWINDOW, ac, (x, y, w, h))
            pygame.draw.rect(GAMEWINDOW, bc, (x + 3, y + 3, w - 6, h - 6))
            GAMEWINDOW.blit(image,
                            (x, y))

        if x + w > mouse[0] > x and y + h > mouse[1] > y:   # sets border color GOLD while hovered over with mouse

            pygame.draw.rect(GAMEWINDOW, ac, (x, y, w, h))
            pygame.draw.rect(GAMEWINDOW, bc, (x + 3, y + 3, w - 6, h - 6))
            GAMEWINDOW.blit(image,
                            (x, y))

            if click[0] == 1:  # Sets playercharacter
                self.continuebutton = 1
                self.playercharacter = str(name)
                self.set_attributes()

        elif name != self.playercharacter:   # draws button without GOLD border for unselected characters
            pygame.draw.rect(GAMEWINDOW, ic, (x, y, w, h))
            pygame.draw.rect(GAMEWINDOW, bc, (x + 3, y + 3, w - 6, h - 6))
            GAMEWINDOW.blit(image,
                            (x, y))

    def set_attributes(self):
        # bruisers - hp, melee, defense
        if self.playercharacter == "Chuck Norris":
            self.player_attributes = {"health": 200, "energy": 100, "energy_gain": 5,
                                      "attack_power": 20, "defense": 18, "special_power": 12
                                      }
        if self.playercharacter == "Cloud":
            self.player_attributes = {"health": 180, "energy": 120, "energy_gain": 5,
                                      "attack_power": 18, "defense": 17, "special_power": 13
                                      }
        if self.playercharacter == "Link":
            self.player_attributes = {"health": 170, "energy": 130, "energy_gain": 5,
                                      "attack_power": 17, "defense": 16, "special_power": 14
                                      }
        if self.playercharacter == "Kakashi":
            self.player_attributes = {"health": 160, "energy": 140, "energy_gain": 5,
                                      "attack_power": 15, "defense": 15, "special_power": 16
                                      }
        # special fighters - energy, special power
        if self.playercharacter == "Goku":
            self.player_attributes = {"health": 150, "energy": 150, "energy_gain": 5,
                                      "attack_power": 15, "defense": 15, "special_power": 18
                                      }
        if self.playercharacter == "Mario":
            self.player_attributes = {"health": 130, "energy": 160, "energy_gain": 5,
                                      "attack_power": 13, "defense": 13, "special_power": 20
                                      }
        if self.playercharacter == "Kirby":
            self.player_attributes = {"health": 120, "energy": 180, "energy_gain": 5,
                                      "attack_power": 12, "defense": 12, "special_power": 22
                                      }
        if self.playercharacter == "Pikachu":
            self.player_attributes = {"health": 100, "energy": 200, "energy_gain": 5,
                                      "attack_power": 11, "defense": 11, "special_power": 23
                                      }
        print(f"Finished setting player_attributes for {self.playercharacter}: \n({self.player_attributes})")

    def set_enemy_attributes(self):
        if self.enemycharacter == "Dr. Robotnik":
            self.enemy_attributes = {"health": 400, "energy": 100, "energy_gain": 5,
                                     "attack_power": 25, "defense": 10, "special_power": 15
                                     }
        if self.enemycharacter == "Bowser":
            self.enemy_attributes = {"health": 550, "energy": 120, "energy_gain": 5,
                                     "attack_power": 32, "defense": 15, "special_power": 18
                                     }
        if self.enemycharacter == "Magneto":
            self.enemy_attributes = {"health": 700, "energy": 175, "energy_gain": 5,
                                     "attack_power": 38, "defense": 17, "special_power": 22
                                     }
        if self.enemycharacter == "Ganondorf":
            self.enemy_attributes = {"health": 850, "energy": 200, "energy_gain": 5,
                                     "attack_power": 43, "defense": 18, "special_power": 25
                                     }
        if self.enemycharacter == "Frieza":
            self.enemy_attributes = {"health": 1000, "energy": 325, "energy_gain": 5,
                                     "attack_power": 54, "defense": 20, "special_power": 30
                                     }
        if self.enemycharacter == "Sephiroth":
            self.enemy_attributes = {"health": 1200, "energy": 450, "energy_gain": 5,
                                     "attack_power": 60, "defense": 15, "special_power": 35
                                     }
        print(f"Finished setting enemy_attributes for {self.enemycharacter}: \n({self.enemy_attributes})")

    def enemyselect(self):
        self.startmusic()
        while True:
            title = titleFont.render('Choose your Opponent!', True, RED)
            ev = pygame.event.get()
            x, y = pygame.mouse.get_pos()
            enemytext = titleFont.render(str(self.enemycharacter), True, RED)
            GAMEWINDOW.blit(EnemySelect_bg,
                            (0, 0))
            GAMEWINDOW.blit(title,
                            (315, 25))
            self.drawenemyselectbutton(RobotnikImage, 'Dr. Robotnik', 200, 510, 296, 206, WHITE, RED, BLACK)
            self.drawenemyselectbutton(BowserImage, 'Bowser', 500, 510, 296, 206, WHITE, RED, BLACK)
            self.drawenemyselectbutton(MagnetoImage, 'Magneto', 800, 510, 296, 206, WHITE, RED, BLACK)
            self.drawenemyselectbutton(GanondorfImage, 'Ganondorf', 350, 300, 296, 206, WHITE, RED, BLACK)
            self.drawenemyselectbutton(FriezaImage, 'Frieza', 650, 300, 296, 206, WHITE, RED, BLACK)
            self.drawenemyselectbutton(SephirothImage, 'Sephiroth', 503, 90, 296, 206, WHITE, RED, BLACK)
            drawbutton("Main Menu", 10, 10, 135, 50, BLACK, RED, LIGHTGRAY)
            if self.fightbutton == 1:
                drawbutton("FIGHT!", 1140, 745, 135, 50, BLACK, RED, LIGHTGRAY)
            GAMEWINDOW.blit(enemytext,
                            (500, 735))
            for event in ev:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if x in range(11, 144) and y in range(11, 59):
                        StartScreen()
                    if x in range(1140, 1274) and y in range(750, 794) and self.fightbutton == 1:
                        self.stopmusic()
                        self.fightbutton = 0
                        return

            if checkforkeypress():
                pygame.event.get()  # clear event queue
                return
            pygame.display.update()
            CLOCK.tick(FPS)

    def drawenemyselectbutton(self, image, name, x, y, w, h, ic, ac, bc):
        # ic= inactive color, ac= active color(hover over, bc= button color)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if name == self.enemycharacter:     # sets border color RED if selected
            pygame.draw.rect(GAMEWINDOW, ac, (x, y, w, h))
            pygame.draw.rect(GAMEWINDOW, bc, (x + 3, y + 3, w - 6, h - 6))
            GAMEWINDOW.blit(image,
                            (x + 3, y + 3))

        if x + w > mouse[0] > x and y + h > mouse[1] > y:     # sets border color RED while hovered over with mouse
            if name in self.coloredpictures:
                pygame.draw.rect(GAMEWINDOW, ac, (x, y, w, h))
                pygame.draw.rect(GAMEWINDOW, bc, (x + 3, y + 3, w - 6, h - 6))
                GAMEWINDOW.blit(image,
                                (x + 3, y + 3))
            elif name in self.grayedout:
                image = pygame.image.load(f'images/{name}_blur.png')
                pygame.draw.rect(GAMEWINDOW, ac, (x, y, w, h))
                pygame.draw.rect(GAMEWINDOW, bc, (x + 3, y + 3, w - 6, h - 6))
                GAMEWINDOW.blit(image,
                                (x + 3, y + 3))

            if click[0] == 1 and name not in self.coloredpictures:   # Set enemycharacter to ??? if not available
                self.fightbutton = 0
                self.enemycharacter = '???'

            elif click[0] == 1 and name in self.coloredpictures:   # Set enemycharacter if available to fight
                print(f'colored: {self.coloredpictures}')
                print(f'defeated: {self.defeated}')
                if name in self.defeated:
                    self.enemycharacter = str(name)
                    self.fightbutton = 0
                else:
                    self.fightbutton = 1
                    self.enemycharacter = str(name)
                    self.set_enemy_attributes()

        elif name != self.enemycharacter:  # draws button without GOLD border for unselected enemies
            if name in self.coloredpictures:
                pygame.draw.rect(GAMEWINDOW, ic, (x, y, w + 1, h))
                pygame.draw.rect(GAMEWINDOW, bc, (x + 3, y + 3, w - 6, h - 6))
                GAMEWINDOW.blit(image,
                                (x + 3, y + 3))
            elif name in self.grayedout:
                image = pygame.image.load(f'images/{name}_blur.png')
                pygame.draw.rect(GAMEWINDOW, ic, (x, y, w + 1, h))
                pygame.draw.rect(GAMEWINDOW, bc, (x + 3, y + 3, w - 6, h - 6))
                GAMEWINDOW.blit(image,
                                (x + 3, y + 3))

    def setenemychar(self, name):
        self.fightbutton = 1
        self.enemycharacter = str(name)

    def startmusic(self):
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.load('audio/CharacterSelect.wav')
        pygame.mixer.music.play(-1)

    def stopmusic(self):
        pygame.mixer.music.stop()
        return


class BattleScreen:
    def __init__(self, player, enemy, x_min, x_max, y_min, y_max,
                player_x_min, player_x_max, player_y_min, player_y_max):
        self.player = player
        self.enemy = enemy
        self.sword_users = ['Cloud', 'Kakashi', 'Link']
        self.enemy_x_min = x_min
        self.enemy_x_max = x_max
        self.enemy_y_min = y_min
        self.enemy_y_max = y_max
        self.player_x_min = player_x_min
        self.player_x_max = player_x_max
        self.player_y_min = player_y_min
        self.player_y_max = player_y_max
        self.countdown_complete = False
        self.circle_radius = 60             # 40 = small  60 = medium    80 = large
        self.circle_thickness = 3           # 1 = thin    3 = medium     5 = thick
        self.circle_speed = 4               # 1 = slow    3 = medium     5 = fast
        self.game_over = False
        self.start_countdown_timer = False
        self.timer_seconds = 100
        self.timecounter = 0
        self.hit_circle_chance = 70         # Integer number representing % chance to spawn a circle every second
        self.hit_circle_spawn_timer = 45    # How often to try spawning a hit circle (60 = 1 second)

        self.player_atk_circle_1 = {'spawn_state': 2,
                                    'radius': 0,
                                    'x': 0,
                                    'y': 0}
        self.player_atk_circle_2 = {'spawn_state': 2,
                                    'radius': 0,
                                    'x': 0,
                                    'y': 0}
        self.player_atk_circle_3 = {'spawn_state': 2,
                                    'radius': 0,
                                    'x': 0,
                                    'y': 0}
        self.enemy_atk_circle_1 = {'spawn_state': 2,
                                   'radius': 0,
                                   'x': 0,
                                   'y': 0}
        self.enemy_atk_circle_2 = {'spawn_state': 2,
                                   'radius': 0,
                                   'x': 0,
                                   'y': 0}
        self.enemy_atk_circle_3 = {'spawn_state': 2,
                                   'radius': 0,
                                   'x': 0,
                                   'y': 0}
        self.enemy_attack_circle_radius = 80
        self.enemy_attack_circle_chance = 30  # Integer number representing % chance to spawn a circle every second
        self.enemy_attack_circle_spawn_timer = 45  # How often to try spawning a hit circle (60 = 1 second)
        self.enemy_attack_chance = 25
        self.enemy_attack_speed = 2               # 1 = slow    3 = medium     5 = fast
        self.green_hit = 0
        self.yellow_hit = 0
        self.red_hit = 0
        self.current_combo = 0
        self.max_combo = 0
        self.misses = 0
        self.battlescreen_bg = pygame.image.load(f'images/{enemy}_bg.png')
        self.startmusic()

    def showbattlescreen(self):
        GAMEWINDOW.fill(BLACK)
        GAMEWINDOW.blit(self.battlescreen_bg,
                        (0, 0))

    def startmusic(self):
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.load(f'audio/{self.enemy}.wav')
        pygame.mixer.music.play(-1)

    def stopmusic(self):
        pygame.mixer.music.stop()
        return

    def update_timecounter(self):
        self.timecounter = self.timecounter + 1

    def generate_hit_circles(self, ev):
        self.create_circles()
        self.draw_circles()
        dmg_taken, dmg_x, dmg_y = self.check_attack(ev)
        self.update_circles()
        return str(dmg_taken), int(dmg_x), int(dmg_y), self.current_combo

    def generate_enemy_attack_circles(self, shield_state):
        self.create_enemy_attack_circles()
        self.draw_enemy_attack_circles()
        hit_type, dmg_x, dmg_y = self.check_enemy_hit(shield_state)
        self.update_enemy_attack_circles()
        return str(hit_type), int(dmg_x), int(dmg_y)

    def check_spawn_timer(self):
        if self.timecounter % 40 == 0:
            return True
        pass

    def check_spawn_chance(self):
        spawn_chance = self.hit_circle_chance
        number = random.randint(1, 100)
        if number >= (100 - spawn_chance):
            return True
        pass

    def check_enemy_attack_chance(self):
        attack_chance = self.enemy_attack_chance
        number = random.randint(1, 100)
        if number >= (100 - attack_chance):
            return True
        pass

    def create_enemy_attack_circles(self):
        if self.check_spawn_timer():
            # generates new circle if one is not active
            if self.enemy_atk_circle_1['spawn_state'] == 0 and self.check_enemy_attack_chance():
                x, y = self.generate_and_check_circle_overlap('enemy_attack')
                self.enemy_atk_circle_1['spawn_state'] = 1
                self.enemy_atk_circle_1['radius'] = self.enemy_attack_circle_radius
                self.enemy_atk_circle_1['x'] = x
                self.enemy_atk_circle_1['y'] = y
                return
            # generates new circle if one is not active
            if self.enemy_atk_circle_2['spawn_state'] == 0 and self.check_enemy_attack_chance():
                x, y = self.generate_and_check_circle_overlap('enemy_attack')
                self.enemy_atk_circle_2['spawn_state'] = 1
                self.enemy_atk_circle_2['radius'] = self.enemy_attack_circle_radius
                self.enemy_atk_circle_2['x'] = x
                self.enemy_atk_circle_2['y'] = y
                return
            # generates new circle if one is not active
            if self.enemy_atk_circle_3['spawn_state'] == 0 and self.check_enemy_attack_chance():
                x, y = self.generate_and_check_circle_overlap('enemy_attack')
                self.enemy_atk_circle_3['spawn_state'] = 1
                self.enemy_atk_circle_3['radius'] = self.enemy_attack_circle_radius
                self.enemy_atk_circle_3['x'] = x
                self.enemy_atk_circle_3['y'] = y
                return
            pass
        pass

    def create_circles(self):
        if self.check_spawn_timer():
            if self.player_atk_circle_1['spawn_state'] == 0 and self.check_spawn_chance():  # generates new circle if one is not active
                x, y = self.generate_and_check_circle_overlap('hit_circle')
                self.player_atk_circle_1['spawn_state'] = 1
                self.player_atk_circle_1['radius'] = self.circle_radius
                self.player_atk_circle_1['x'] = x
                self.player_atk_circle_1['y'] = y
                return
            if self.player_atk_circle_2['spawn_state'] == 0 and self.check_spawn_chance():  # generates new circle if one is not active
                x, y = self.generate_and_check_circle_overlap('hit_circle')
                self.player_atk_circle_2['spawn_state'] = 1
                self.player_atk_circle_2['radius'] = self.circle_radius
                self.player_atk_circle_2['x'] = x
                self.player_atk_circle_2['y'] = y
                return
            if self.player_atk_circle_3['spawn_state'] == 0 and self.check_spawn_chance():  # generates new circle if one is not active
                x, y = self.generate_and_check_circle_overlap('hit_circle')
                self.player_atk_circle_3['spawn_state'] = 1
                self.player_atk_circle_3['radius'] = self.circle_radius
                self.player_atk_circle_3['x'] = x
                self.player_atk_circle_3['y'] = y
                return
            pass
        pass

    def generate_and_check_circle_overlap(self, circle_type):
        # Checks if new circle is too close to an existing circle and retries
        if circle_type == 'hit_circle':
            rand_x = random.randint(self.enemy_x_min, self.enemy_x_max)
            rand_y = random.randint(self.enemy_y_min, self.enemy_y_max)
        if circle_type == 'enemy_attack':
            rand_x = random.randint(self.player_x_min, self.player_x_max)
            rand_y = random.randint(self.player_y_min, self.player_y_max)
        buffer = 80
        circles = {1: {'x': self.player_atk_circle_1['x'], 'y': self.player_atk_circle_1['y']},
                   2: {'x': self.player_atk_circle_2['x'], 'y': self.player_atk_circle_2['y']},
                   3: {'x': self.player_atk_circle_3['x'], 'y': self.player_atk_circle_3['y']},
                   4: {'x': self.enemy_atk_circle_1['x'], 'y': self.enemy_atk_circle_1['y']},
                   5: {'x': self.enemy_atk_circle_2['x'], 'y': self.enemy_atk_circle_2['y']},
                   6: {'x': self.enemy_atk_circle_3['x'], 'y': self.enemy_atk_circle_3['y']}}
        x_1 = circles[1]['x']
        y_1 = circles[1]['y']
        x_2 = circles[2]['x']
        y_2 = circles[2]['y']
        x_3 = circles[3]['x']
        y_3 = circles[3]['y']
        x_4 = circles[4]['x']
        y_4 = circles[4]['y']
        x_5 = circles[5]['x']
        y_5 = circles[5]['y']
        x_6 = circles[6]['x']
        y_6 = circles[6]['y']
        if ((rand_x in range((x_1 - buffer), (x_1 + buffer)) and rand_y in range((y_1 - buffer), (y_1 + buffer))) or
            (rand_x in range((x_2 - buffer), (x_2 + buffer)) and rand_y in range((y_2 - buffer), (y_2 + buffer))) or
            (rand_x in range((x_3 - buffer), (x_3 + buffer)) and rand_y in range((y_3 - buffer), (y_3 + buffer))) or
            (rand_x in range((x_4 - buffer), (x_4 + buffer)) and rand_y in range((y_4 - buffer), (y_4 + buffer))) or
            (rand_x in range((x_5 - buffer), (x_5 + buffer)) and rand_y in range((y_5 - buffer), (y_5 + buffer))) or
            (rand_x in range((x_6 - buffer), (x_6 + buffer)) and rand_y in range((y_6 - buffer), (y_6 + buffer)))):
            self.generate_and_check_circle_overlap(circle_type)
        return rand_x, rand_y

    def draw_circles(self):     # Determines what color to draw each circle then draws them
        circle_radius = self.circle_radius
        circle_num_radius = {1: {'radius': self.player_atk_circle_1['radius']},
                             2: {'radius': self.player_atk_circle_2['radius']},
                             3: {'radius': self.player_atk_circle_3['radius']}}
        circle_coords = {1: {'x': self.player_atk_circle_1['x'], 'y': self.player_atk_circle_1['y']},
                         2: {'x': self.player_atk_circle_2['x'], 'y': self.player_atk_circle_2['y']},
                         3: {'x': self.player_atk_circle_3['x'], 'y': self.player_atk_circle_3['y']}}

        if self.player_atk_circle_1['spawn_state'] or self.player_atk_circle_2['spawn_state'] or self.player_atk_circle_3['spawn_state'] == 1:
            for num in [1, 2, 3]:
                radius = circle_num_radius[num]['radius']
                circle_x = circle_coords[num]['x']
                circle_y = circle_coords[num]['y']
                thickness = self.circle_thickness

                # Draws Circle (Green)
                if (circle_radius - (circle_radius / 3)) <= radius <= circle_radius:
                    pygame.draw.circle(GAMEWINDOW, GREEN, (circle_x, circle_y), radius, thickness)
                    # Draws Circle (Yellow)
                elif (circle_radius - ((circle_radius / 3) * 2)) \
                        <= radius \
                        <= circle_radius - (circle_radius / 3):
                    pygame.draw.circle(GAMEWINDOW, GOLD, (circle_x, circle_y), radius, thickness)
                # Draws Circle (Red)
                elif (circle_radius - (circle_radius - 1)) <= radius <= (circle_radius - ((circle_radius / 3) * 2)):
                    pygame.draw.circle(GAMEWINDOW, RED, (circle_x, circle_y), radius, thickness)
            else:
                pass

    def draw_enemy_attack_circles(self):     # Determines what color to draw each circle then draws them
        circle_radius = self.enemy_attack_circle_radius
        circle_num_radius = {1: {'radius': self.enemy_atk_circle_1['radius']},
                             2: {'radius': self.enemy_atk_circle_2['radius']},
                             3: {'radius': self.enemy_atk_circle_3['radius']}}
        circle_coords = {1: {'x': self.enemy_atk_circle_1['x'], 'y': self.enemy_atk_circle_1['y']},
                         2: {'x': self.enemy_atk_circle_2['x'], 'y': self.enemy_atk_circle_2['y']},
                         3: {'x': self.enemy_atk_circle_3['x'], 'y': self.enemy_atk_circle_3['y']}}

        if self.enemy_atk_circle_1['spawn_state'] or self.enemy_atk_circle_2['spawn_state'] or self.enemy_atk_circle_3['spawn_state'] == 1:
            for num in [1, 2, 3]:
                radius = circle_num_radius[num]['radius']
                circle_x = circle_coords[num]['x']
                circle_y = circle_coords[num]['y']
                thickness = self.circle_thickness

                # Draws Circle (Green)
                if (circle_radius - (circle_radius / 3)) <= radius <= circle_radius:
                    pygame.draw.circle(GAMEWINDOW, GREEN, (circle_x, circle_y), radius, thickness)
                    # Draws Circle (Yellow)
                elif (circle_radius - ((circle_radius / 3) * 2)) \
                        <= radius \
                        <= circle_radius - (circle_radius / 3):
                    pygame.draw.circle(GAMEWINDOW, GOLD, (circle_x, circle_y), radius, thickness)
                # Draws Circle (Red)
                elif (circle_radius - (circle_radius - 1)) <= radius <= (circle_radius - ((circle_radius / 3) * 2)):
                    pygame.draw.circle(GAMEWINDOW, RED, (circle_x, circle_y), radius, (thickness - 1))
            else:
                pass

    def get_circle_color(self, circle_radius, circle_num_radius):
        # This means its red
        if (circle_radius - circle_radius) <= circle_num_radius <= (circle_radius - ((circle_radius / 3) * 2)):
            return 'red'
        # This means its yellow
        elif (circle_radius - ((circle_radius / 3) * 2)) <= circle_num_radius <= (circle_radius - (circle_radius / 3)):
            return 'yellow'
        # This means its green
        elif (circle_radius - (circle_radius / 3)) <= circle_num_radius <= circle_radius:
            return 'green'

    def do_color_stuff(self, color):
        if str(color) == 'green':
            self.green_hit += 1
            self.current_combo += 1
        elif str(color) == 'yellow':
            self.yellow_hit += 1
            self.current_combo += 1
        elif str(color) == 'red':
            self.red_hit += 1
            self.current_combo += 1

    def reset_circle(self, num):
        if num == 1:
            self.player_atk_circle_1['radius'] = 0
            self.player_atk_circle_1['x'] = 0
            self.player_atk_circle_1['y'] = 0
        elif num == 2:
            self.player_atk_circle_2['radius'] = 0
            self.player_atk_circle_2['x'] = 0
            self.player_atk_circle_2['y'] = 0
        elif num == 3:
            self.player_atk_circle_3['radius'] = 0
            self.player_atk_circle_3['x'] = 0
            self.player_atk_circle_3['y'] = 0

    def check_attack(self, ev):
        # print(f'EVENT BEING PASSED IN: {ev}')
        if self.player in self.sword_users:
            hit_sound = pygame.mixer.Sound('audio/attack_sound_sword.wav')
        else:
            hit_sound = pygame.mixer.Sound('audio/attack_sound.wav')
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # if event.type == pygame.MOUSEBUTTONDOWN:
                print(f'EVENT IN EV: {event}')
                x, y = pygame.mouse.get_pos()
                circle_color, circle_x, circle_y = self.attack_handler(x, y, hit_sound)
                return circle_color, circle_x, circle_y
        return 'none', 0, 0

    def check_enemy_hit(self, shield_state):
        if self.countdown_complete:
            attack_circle_num_radius = {1: {'radius': self.enemy_atk_circle_1['radius']},
                                        2: {'radius': self.enemy_atk_circle_2['radius']},
                                        3: {'radius': self.enemy_atk_circle_3['radius']}}
            attack_circle_coords = {1: {'x': self.enemy_atk_circle_1['x'], 'y': self.enemy_atk_circle_1['y']},
                                    2: {'x': self.enemy_atk_circle_2['x'], 'y': self.enemy_atk_circle_2['y']},
                                    3: {'x': self.enemy_atk_circle_3['x'], 'y': self.enemy_atk_circle_3['y']}}
            for num in [1, 2, 3]:
                if num == 1:
                    spawn_state = self.enemy_atk_circle_1['spawn_state']
                if num == 2:
                    spawn_state = self.enemy_atk_circle_2['spawn_state']
                if num == 3:
                    spawn_state = self.enemy_atk_circle_3['spawn_state']
                radius = attack_circle_num_radius[num]['radius']
                x = attack_circle_coords[num]['x']
                y = attack_circle_coords[num]['y']
                if radius <= 1 and spawn_state == 1 and shield_state == 1:
                    print('BLOCKED!')
                    pygame.mixer.Channel(1).play(shield_block_sound)
                    # shield_block_sound.play()
                    if num == 1:
                        self.enemy_atk_circle_1['spawn_state'] = 0
                    if num == 2:
                        self.enemy_atk_circle_2['spawn_state'] = 0
                    if num == 3:
                        self.enemy_atk_circle_3['spawn_state'] = 0
                    return 'blocked', x, y
                if radius <= 1 and spawn_state == 1 and shield_state != 1:
                    print(f'NOT BLOCKED!{num}')
                    pygame.mixer.Channel(0).play(enemy_attack_sound)
                    if num == 1:
                        self.enemy_atk_circle_1['spawn_state'] = 0
                    if num == 2:
                        self.enemy_atk_circle_2['spawn_state'] = 0
                    if num == 3:
                        self.enemy_atk_circle_3['spawn_state'] = 0
                    return 'not blocked', x, y
        return 'none', 0, 0

    def attack_handler(self, x, y, hit_sound):
        print("CLICKED MOUSE")
        # Manages everything during an attack: gets circle number, color, location,
        # plays hit sound, resets circles, and returns hit information
        circle_radius = self.circle_radius

        circle_num_radius = {1: {'radius': self.player_atk_circle_1['radius']},
                             2: {'radius': self.player_atk_circle_2['radius']},
                             3: {'radius': self.player_atk_circle_3['radius']}}
        circle_coords = {1: {'x': self.player_atk_circle_1['x'], 'y': self.player_atk_circle_1['y']},
                         2: {'x': self.player_atk_circle_2['x'], 'y': self.player_atk_circle_2['y']},
                         3: {'x': self.player_atk_circle_3['x'], 'y': self.player_atk_circle_3['y']}}
        circle_max = {1: {'x_max': (self.player_atk_circle_1['x'] + self.player_atk_circle_1['radius']),
                          'y_max': (self.player_atk_circle_1['y'] + self.player_atk_circle_1['radius'])},
                      2: {'x_max': (self.player_atk_circle_2['x'] + self.player_atk_circle_2['radius']),
                          'y_max': (self.player_atk_circle_2['y'] + self.player_atk_circle_2['radius'])},
                      3: {'x_max': (self.player_atk_circle_3['x'] + self.player_atk_circle_3['radius']),
                          'y_max': (self.player_atk_circle_3['y'] + self.player_atk_circle_3['radius'])}}
        circle_min = {1: {'x_min': (self.player_atk_circle_1['x'] - self.player_atk_circle_1['radius']),
                          'y_min': (self.player_atk_circle_1['y'] - self.player_atk_circle_1['radius'])},
                      2: {'x_min': (self.player_atk_circle_2['x'] - self.player_atk_circle_2['radius']),
                          'y_min': (self.player_atk_circle_2['y'] - self.player_atk_circle_2['radius'])},
                      3: {'x_min': (self.player_atk_circle_3['x'] - self.player_atk_circle_3['radius']),
                          'y_min': (self.player_atk_circle_3['y'] - self.player_atk_circle_3['radius'])}}

        count = 0
        for num in [1, 2, 3]:
            count = count + 1
            x_min = circle_min[num]['x_min']
            y_min = circle_min[num]['y_min']
            x_max = circle_max[num]['x_max']
            y_max = circle_max[num]['y_max']
            circle_x = circle_coords[num]['x']
            circle_y = circle_coords[num]['y']
            radius = circle_num_radius[num]['radius']

            if x in range(x_min, x_max) and y in range(y_min, y_max):
                color = self.get_circle_color(circle_radius, radius)    # Get color of circle
                self.do_color_stuff(color)
                pygame.mixer.Channel(2).play(hit_sound)
                if num == 1:
                    self.player_atk_circle_1['spawn_state'] = 0
                    self.reset_circle(1)
                    return str(color), int(circle_x), int(circle_y)
                elif num == 2:
                    self.player_atk_circle_2['spawn_state'] = 0
                    self.reset_circle(2)
                    return str(color), int(circle_x), int(circle_y)
                elif num == 3:
                    self.player_atk_circle_3['spawn_state'] = 0
                    self.reset_circle(3)
                    return str(color), int(circle_x), int(circle_y)
        return 'none', 0, 0

    def update_enemy_attack_circles(self):
        if self.enemy_atk_circle_1['spawn_state'] == 1:
            if self.enemy_atk_circle_1['radius'] < 1:
                self.enemy_atk_circle_1['spawn_state'] = 0
            if self.timecounter % 5 == 0:
                self.enemy_atk_circle_1['radius'] -= self.enemy_attack_speed
        if self.enemy_atk_circle_2['spawn_state'] == 1:
            if self.enemy_atk_circle_2['radius'] < 1:
                self.enemy_atk_circle_2['spawn_state'] = 0
            if self.timecounter % 5 == 0:
                self.enemy_atk_circle_2['radius'] -= self.enemy_attack_speed
        if self.enemy_atk_circle_3['spawn_state'] == 1:
            if self.enemy_atk_circle_3['radius'] < 1:
                self.enemy_atk_circle_3['spawn_state'] = 0
            if self.timecounter % 5 == 0:
                self.enemy_atk_circle_3['radius'] -= self.enemy_attack_speed

    def update_circles(self):
        if self.player_atk_circle_1['spawn_state'] == 1:
            if self.timecounter % 5 == 0:
                self.player_atk_circle_1['radius'] -= self.circle_speed
            if self.player_atk_circle_1['radius'] < 1:
                self.player_atk_circle_1['spawn_state'] = 0
                self.current_combo = 0
                self.misses += 1
        if self.player_atk_circle_2['spawn_state'] == 1:
            if self.timecounter % 5 == 0:
                self.player_atk_circle_2['radius'] -= self.circle_speed
            if self.player_atk_circle_2['radius'] < 1:
                self.player_atk_circle_2['spawn_state'] = 0
                self.current_combo = 0
                self.misses += 1
        if self.player_atk_circle_3['spawn_state'] == 1:
            if self.timecounter % 5 == 0:
                self.player_atk_circle_3['radius'] -= self.circle_speed
            if self.player_atk_circle_3['radius'] < 1:
                self.player_atk_circle_3['spawn_state'] = 0
                self.current_combo = 0
                self.misses += 1

    def timer(self):
        if self.start_countdown_timer:
            if self.timecounter % 60 == 0:
                self.timer_seconds -= 1
        if self.timer_seconds <= 0:
            self.stopmusic()
            self.game_over = True
        elif self.timer_seconds <= 10:
            seconds = large_titleFont.render(f'{self.timer_seconds}', True, RED)
            GAMEWINDOW.blit(seconds,
                            (((windowwidth / 2) - 20), 25))
        elif self.timer_seconds > 10:
            seconds = titleFont.render(f'{self.timer_seconds}', True, WHITE)
            GAMEWINDOW.blit(seconds,
                            (((windowwidth / 2) - 35), 10))

    def combo_counter(self):
        if self.current_combo >= self.max_combo:
            self.max_combo = self.current_combo

    def match_summary(self):
        stat_points = 10
        return self.green_hit, self.yellow_hit, self.red_hit, self.max_combo, stat_points, self.misses

    def update(self):
        self.showbattlescreen()
        self.update_timecounter()
        self.draw_countdown()
        self.timer()
        self.combo_counter()

    def draw_countdown(self):
        if not self.countdown_complete:
            player_name = titleFont.render(f'{self.player}', True, RED)
            enemy_name = titleFont.render(f'{self.enemy}', True, RED)
            versus = titleFont.render('Versus', True, RED)
            ready = titleFont.render('Ready?', True, WHITE)
            countdown_3 = large_titleFont.render('3', True, WHITE)
            countdown_2 = large_titleFont.render('2', True, WHITE)
            countdown_1 = large_titleFont.render('1', True, WHITE)
            countdown_fight = large_titleFont.render('FIGHT!', True, RED)
            if 0 < self.timecounter < 120:
                GAMEWINDOW.blit(player_name,
                                (((windowwidth/2) - len(self.player * 18)), 275))
                GAMEWINDOW.blit(versus,
                                (((windowwidth/2) - (len('versus') * 20)), 350))
                GAMEWINDOW.blit(enemy_name,
                                (((windowwidth/2) - len(self.enemy * 16)), 425))
            elif 120 < self.timecounter < 240:
                GAMEWINDOW.blit(ready,
                                (((windowwidth/2) - (len('ready') * 20)), 350))
            elif 240 < self.timecounter < 300:
                GAMEWINDOW.blit(countdown_3,
                                ((windowwidth/2 - 30), 350))
            elif 300 < self.timecounter < 360:
                GAMEWINDOW.blit(countdown_2,
                                ((windowwidth/2 - 30), 350))
            elif 360 < self.timecounter < 420:
                GAMEWINDOW.blit(countdown_1,
                                ((windowwidth/2 - 30), 350))
            elif 420 < self.timecounter < 480:
                GAMEWINDOW.blit(countdown_fight,
                                (((windowwidth/2) - (len('versus') * 30)), 350))
            elif self.timecounter > 481:
                self.set_battle_parameters()

    def set_battle_parameters(self):
        self.player_atk_circle_1['spawn_state'] = 0
        self.player_atk_circle_2['spawn_state'] = 0
        self.player_atk_circle_3['spawn_state'] = 0
        self.enemy_atk_circle_1['spawn_state'] = 0
        self.enemy_atk_circle_2['spawn_state'] = 0
        self.enemy_atk_circle_3['spawn_state'] = 2
        self.countdown_complete = True
        self.start_countdown_timer = True

class Player(object):
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''
      Spawn a player     Spawn a player     Spawn a player     
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def __init__(self, name, **kwargs):
        self.debug = 0
        self.name = name
        self.health = kwargs.get("health")
        self.max_health = kwargs.get("health")
        self.defense = kwargs.get("defense")
        self.energy = kwargs.get("energy")
        self.max_energy = kwargs.get("energy")
        self.attack_power = kwargs.get("attack_power")
        self.special_power = kwargs.get("special_power")
        self.energy_gain = kwargs.get("energy_gain")
        self.special_attack_cost = 50
        self.heal_ability_cost = 25
        self.shieldactive = 0
        self.shieldtimer = 0
        self.stat_points = 0
        self.shorties = ['Pikachu', 'Kirby', 'Mario']
        self.player_scaler = 1
        self.frame = 0  # count frames
        self.timecounter = 0
        self.dmg_text_flag = 0
        self.dmg_text_counter = 0
        self.dmg_text_y = 0
        self.dmg_text_x = 0
        self.last_hit = 0
        self.last_fight_green = 0
        self.last_fight_yellow = 0
        self.last_fight_red = 0
        self.last_fight_combo = 0
        self.last_fight_misses = 0
        self.total_green = 0
        self.total_yellow = 0
        self.total_red = 0
        self.total_misses = 0
        self.highest_combo = 0
        self.current_combo = 0
        self.x_min = 150
        self.y_min = 250
        self.xpos = 150     # Player spawn X coordinate
        self.ypos = 250     # Player spawn Y coordinate
        self.player_width = 300
        self.shortie_width = 180
        self.platform_width = 300
        self.platform_height = 0
        self.platform_img_load = pygame.image.load('images/player_platform.png')
        self.player_img_load = pygame.image.load(f'images/{name}_battle.png')
        self.special_attack_image = pygame.image.load(f'images/{name}_special.png')
        self.special_attack_active = 0
        self.special_hit = 0
        self.special_attack_x = 0
        self.special_attack_y = 0
        self.special_attack_timer = 0
        self.heal_ability_active = 0
        self.heal_ability_x = 0
        self.heal_ability_y = 0
        self.heal_ability_timer = 0
        self.last_heal = 0
        self.heal_image_alpha = 0
        self.player_x1 = 0
        self.player_x2 = 0
        self.player_y1 = 0
        self.player_y2 = 0
        self.resize_image()
        self.player_platform = pygame.transform.scale(self.platform_img_load,
                                                      (self.platform_width, self.platform_height))
        self.bounds = self.player_img_load.get_size()
        self.heal_image = pygame.image.load('images/heal_image.png')
        self.special_image = pygame.image.load('images/special_image.png')
        self.x_max = (self.x_min + self.player_x2)
        self.y_max = (self.y_min + self.player_y2)

    def reset_heal_ability(self):
        # width = self.xpos + self.player_width
        # height = self.ypos + 10
        self.heal_ability_x = 425
        self.heal_ability_y = 650
        self.heal_ability_active = 0
        self.heal_ability_timer = 0

    def calculate_heal(self):
        base_heal = 5
        heal_range_low = int((base_heal + self.special_power) * 0.6)
        heal_range_high = int((base_heal + self.special_power) * 1.2)
        heal = random.randint(heal_range_low, heal_range_high)
        return heal

    def check_heal_ability(self, ev):
        mouse = pygame.mouse.get_pos()
        msg = 'Heal'
        x = 580
        y = 730
        back_circle_color = GREEN
        back_circle_radius = 50
        button_color = SILVER
        active_button_color = DARKSILVER
        button_radius = 45
        button_x_min = x - button_radius
        button_x_max = x + button_radius
        button_y_min = y - button_radius
        button_y_max = y + button_radius
        heal_image_x = x - 105
        heal_image_y = y - 110

        if self.heal_ability_active == 0:
            self.reset_heal_ability()

        elif self.heal_ability_active == 1:
            self.heal_ability_timer += 1
            last_heal = TEXT.render(f'+{self.last_heal}', True, GREEN)
            if self.heal_ability_timer < 80:
                GAMEWINDOW.blit(last_heal,
                                (self.heal_ability_x, self.heal_ability_y))
                GAMEWINDOW.blit(self.heal_image,
                                (heal_image_x, heal_image_y))
                if self.heal_ability_timer % 5 == 0:
                    self.heal_ability_y = self.heal_ability_y - 5
            if self.heal_ability_timer > 80:
                self.reset_heal_ability()

        # Has enough energy - no healing active
        if self.energy >= self.heal_ability_cost and self.heal_ability_active != 1:
            # Mouse over ability button
            if mouse[0] in range(button_x_min, button_x_max) and mouse[1] in range(button_y_min, button_y_max):
                pygame.draw.circle(GAMEWINDOW, back_circle_color, (x, y), back_circle_radius)
                pygame.draw.circle(GAMEWINDOW, active_button_color, (x, y), button_radius)
                # ON-CLICK
                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        self.heal_ability_active = 1
                        self.energy -= 25
                        heal_amount = self.calculate_heal()
                        self.last_heal = heal_amount
                        if self.health + self.last_heal > self.max_health:
                            self.health = self.max_health
                        else:
                            self.health = self.health + heal_amount
                        GAMEWINDOW.blit(self.heal_image,
                                        (heal_image_x, heal_image_y))
            # Not over button
            else:
                pygame.draw.circle(GAMEWINDOW, back_circle_color, (x, y), back_circle_radius)
                pygame.draw.circle(GAMEWINDOW, button_color, (x, y), button_radius)

            textsurf, textrect = text_objects(msg, smallText)
            textrect.center = (x, y)
            GAMEWINDOW.blit(textsurf, textrect)

        # Not enough energy or there is already an active heal ability
        if self.energy < self.heal_ability_cost or self.heal_ability_active == 1:
            back_circle_color = DARKRED
            # Mouse over ability button
            if mouse[0] in range(button_x_min, button_x_max) and mouse[1] in range(button_y_min, button_y_max):
                pygame.draw.circle(GAMEWINDOW, back_circle_color, (x, y), back_circle_radius)
                pygame.draw.circle(GAMEWINDOW, RED, (x, y), button_radius)
            # Not over button
            else:
                pygame.draw.circle(GAMEWINDOW, back_circle_color, (x, y), back_circle_radius)
                pygame.draw.circle(GAMEWINDOW, button_color, (x, y), button_radius)
            textsurf, textrect = text_objects(msg, smallText)
            textrect.center = (x, y)
            GAMEWINDOW.blit(textsurf, textrect)

    def reset_special_attack(self):
        if self.name in self.shorties:
            width = self.xpos + self.shortie_width
            height = self.ypos + 50
        else:
            width = self.xpos + self.player_width/2
            height = self.ypos + 75
        self.special_attack_x = width
        self.special_attack_y = height
        self.special_attack_active = 0
        self.special_attack_timer = 0
        self.special_hit = 0

    def special_attack(self, ev):
        mouse = pygame.mouse.get_pos()
        msg = 'Special'
        x = 710
        y = 730
        back_circle_color = DARKGOLD
        back_circle_radius = 50
        button_color = SILVER
        active_button_color = DARKSILVER
        button_radius = 45
        button_x_min = x - button_radius
        button_x_max = x + button_radius
        button_y_min = y - button_radius
        button_y_max = y + button_radius
        enemy_x = 850
        special_image_x = x - 110
        special_image_y = y - 110

        if self.special_attack_active == 0:
            self.reset_special_attack()

        if self.special_attack_active == 1:
            GAMEWINDOW.blit(self.special_attack_image,
                            (self.special_attack_x, self.special_attack_y))
            GAMEWINDOW.blit(self.special_image,
                            (special_image_x, special_image_y))
            self.special_attack_timer += 1
            if self.special_attack_x >= enemy_x:
                print('HIT!')
                self.special_hit = 1
                self.special_attack_active = 0
            if self.special_attack_timer % 1 == 0:
                self.special_attack_x = self.special_attack_x + 15

        # Has enough energy - no special attacks active
        if self.energy >= self.special_attack_cost and self.special_attack_active != 1:
            # Mouse over ability button
            if mouse[0] in range(button_x_min, button_x_max) and mouse[1] in range(button_y_min, button_y_max):
                pygame.draw.circle(GAMEWINDOW, back_circle_color, (x, y), back_circle_radius)
                pygame.draw.circle(GAMEWINDOW, active_button_color, (x, y), button_radius)
                # ON-CLICK
                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        self.special_attack_active = 1
                        self.energy -= 50
                        GAMEWINDOW.blit(self.heal_image,
                                        (special_image_x, special_image_y))
            # Not over button
            else:
                pygame.draw.circle(GAMEWINDOW, back_circle_color, (x, y), back_circle_radius)
                pygame.draw.circle(GAMEWINDOW, button_color, (x, y), button_radius)

            textsurf, textrect = text_objects(msg, smallText)
            textrect.center = (x, y)
            GAMEWINDOW.blit(textsurf, textrect)

        # Not enough energy or there is already an active special attack
        if self.energy < self.special_attack_cost or self.special_attack_active == 1:
            back_circle_color = DARKRED
            # Mouse over ability button
            if mouse[0] in range(button_x_min, button_x_max) and mouse[1] in range(button_y_min, button_y_max):
                pygame.draw.circle(GAMEWINDOW, back_circle_color, (x, y), back_circle_radius)
                pygame.draw.circle(GAMEWINDOW, RED, (x, y), button_radius)
            # Not over button
            else:
                pygame.draw.circle(GAMEWINDOW, back_circle_color, (x, y), back_circle_radius)
                pygame.draw.circle(GAMEWINDOW, button_color, (x, y), button_radius)
            textsurf, textrect = text_objects(msg, smallText)
            textrect.center = (x, y)
            GAMEWINDOW.blit(textsurf, textrect)

    def calc_dmg(self, atk_power):
        attack_range_low = int((atk_power - self.defense)*0.6)
        attack_range_high = int((atk_power - self.defense)*1.2)
        damage = random.randint(attack_range_low, attack_range_high)
        return damage

    def lose_hp(self, hit_type, dmg_x_coord, dmg_y_coord, atk_power):
        if hit_type == 'not blocked':
            self.reset_display_dmg_taken()
            damagetaken = self.calc_dmg(atk_power)
            self.health = (self.health - damagetaken)
            self.last_hit = damagetaken
            self.dmg_text_flag = 1
            self.dmg_text_x = dmg_x_coord
            self.dmg_text_y = dmg_y_coord
        if hit_type == 'blocked':
            self.reset_display_dmg_taken()
            self.last_hit = 'blocked'
            self.dmg_text_flag = 1
            self.dmg_text_x = dmg_x_coord
            self.dmg_text_y = dmg_y_coord
        else:
            pass

    def display_dmg_taken(self):
        if self.dmg_text_flag == 0:
            pass
        elif self.dmg_text_flag == 1:
            self.dmg_text_counter += 1
            if self.last_hit == 'blocked':
                dmg_text = TEXT.render(f'BLOCKED!', True, WHITE)
            else:
                dmg_text = TEXT.render(f'-{self.last_hit}', True, RED)
            if self.dmg_text_counter < 80:
                GAMEWINDOW.blit(dmg_text,
                                (self.dmg_text_x, (self.dmg_text_y - 60)))
                if self.dmg_text_counter % 5 == 0:
                    self.dmg_text_y = self.dmg_text_y - 5
            if self.dmg_text_counter > 80:
                self.reset_display_dmg_taken()

    def reset_display_dmg_taken(self):
        self.dmg_text_flag = 0
        self.dmg_text_counter = 0
        self.dmg_text_x = 0
        self.dmg_text_y = 0

    def resize_image(self):
        x2 = self.shortie_width
        if self.name not in self.shorties:
            x2 = self.player_width
        x1, y1 = self.player_img_load.get_size()
        y2 = int((x2 * y1) / x1)
        platx, platy = self.platform_img_load.get_size()
        platx2 = self.platform_width
        platy2 = int((platx2 * platy) / platx)
        self.platform_height = platy2
        self.player_x1 = x1
        self.player_x2 = x2
        self.player_y1 = y1
        self.player_y2 = y2

    def update_stats(self):
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.load('audio/summary.wav')
        pygame.mixer.music.play(-1)
        upgrading = True
        player_image = pygame.image.load(f'images/{self.name}.png')

        while upgrading:
            x, y = pygame.mouse.get_pos()
            ev = pygame.event.get()
            victory = large_titleFont.render('Victory!', True, WHITE)
            summary = summaryFont.render('Match Summary', True, WHITE)
            green_hit = mediumText.render(f'Excellent hits: {self.last_fight_green}', True, GREEN)
            yellow_hit = mediumText.render(f'Moderate hits: {self.last_fight_yellow}', True, GOLD)
            red_hit = mediumText.render(f'Poor hits: {self.last_fight_red}', True, RED)
            missed_hits = mediumText.render(f'Missed hits: {self.last_fight_misses}', True, DARKRED)
            max_combo = mediumText.render(f'Best combo streak: {self.last_fight_combo}', True, WHITE)
            available_points = mediumText.render(f'Stat Points available: {self.stat_points}', True, BLACK)
            max_health = smallText.render(f'Health: {self.max_health}', True, BLACK)
            max_energy = smallText.render(f'Energy: {self.max_energy}', True, BLACK)
            current_attack = smallText.render(f'Attack: {self.attack_power}', True, BLACK)
            current_defense = smallText.render(f'Defense: {self.defense}', True, BLACK)
            current_special = smallText.render(f'Special: {self.special_power}', True, BLACK)
            GAMEWINDOW.fill(BLACK)
            pygame.draw.rect(GAMEWINDOW, BLUE, (450, 200, 600, 400))
            pygame.draw.rect(GAMEWINDOW, GRAYBLUE, (460, 210, 580, 380))
            drawbutton("Continue", 1140, 745, 135, 50, BLACK, RED, LIGHTGRAY)
            if self.stat_points > 0:
                drawbutton("^", 800, 325, 30, 30, BLACK, GREEN, LIGHTGRAY)
                drawbutton("^", 800, 375, 30, 30, BLACK, GREEN, LIGHTGRAY)
                drawbutton("^", 800, 425, 30, 30, BLACK, GREEN, LIGHTGRAY)
                drawbutton("^", 800, 475, 30, 30, BLACK, GREEN, LIGHTGRAY)
                drawbutton("^", 800, 525, 30, 30, BLACK, GREEN, LIGHTGRAY)
            for event in ev:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if x in range(800, 830) and y in range(325, 355) and self.stat_points > 0:    # Health button (^)
                        self.stat_points -= 1
                        self.max_health += 10
                        pass
                    if x in range(800, 830) and y in range(375, 405) and self.stat_points > 0:    # Energy button (^)
                        self.stat_points -= 1
                        self.max_energy += 10
                        pass
                    if x in range(800, 830) and y in range(425, 455) and self.stat_points > 0:    # Attack button (^)
                        self.stat_points -= 1
                        self.attack_power += 1
                        pass
                    if x in range(800, 830) and y in range(475, 505) and self.stat_points > 0:    # Defense button (^)
                        self.stat_points -= 1
                        self.defense += 1
                        pass
                    if x in range(800, 830) and y in range(525, 555) and self.stat_points > 0:    # Special button (^)
                        self.stat_points -= 1
                        self.special_power += 1
                        pass
                    if x in range(1140, 1274) and y in range(750, 794):
                        pygame.mixer.music.stop()
                        self.setup_health()
                        return
            GAMEWINDOW.blit(victory,
                            ((windowwidth / 2) - 200, 50))
            GAMEWINDOW.blit(summary,
                            (30, 230))
            GAMEWINDOW.blit(green_hit,
                            (30, 300))
            GAMEWINDOW.blit(yellow_hit,
                            (30, 350))
            GAMEWINDOW.blit(red_hit,
                            (30, 400))
            GAMEWINDOW.blit(missed_hits,
                            (30, 450))
            GAMEWINDOW.blit(max_combo,
                            (30, 550))
            GAMEWINDOW.blit(available_points,
                            (575, 240))
            GAMEWINDOW.blit(max_health,
                            (835, 330))
            GAMEWINDOW.blit(max_energy,
                            (835, 380))
            GAMEWINDOW.blit(current_attack,
                            (835, 430))
            GAMEWINDOW.blit(current_defense,
                            (835, 480))
            GAMEWINDOW.blit(current_special,
                            (835, 530))
            GAMEWINDOW.blit(player_image,
                            (510, 310))
            if checkforkeypress():
                pygame.event.get()  # clear event queue
                return
            pygame.display.update()
            CLOCK.tick(FPS)

    def setup_health(self):
        self.health = self.max_health
        self.energy = self.max_energy

    def update_stat_info(self, green, yellow, red, combo, points, misses):
        self.last_fight_green = green
        self.last_fight_yellow = yellow
        self.last_fight_red = red
        self.last_fight_combo = combo
        self.last_fight_misses = misses
        self.total_green += green
        self.total_yellow += yellow
        self.total_red += red
        self.total_misses += misses
        if combo >= self.highest_combo:
            self.highest_combo = combo
        self.stat_points += points
        self.update_stats()

    def final_stat_update(self, green, yellow, red, combo, points, misses):
        self.last_fight_green = green
        self.last_fight_yellow = yellow
        self.last_fight_red = red
        self.last_fight_combo = combo
        self.last_fight_misses = misses
        self.total_green += green
        self.total_yellow += yellow
        self.total_red += red
        self.total_misses += misses
        if combo >= self.highest_combo:
            self.highest_combo = combo
        self.stat_points += points
        return str(self.name), int(self.max_health), int(self.max_energy), int(self.attack_power), int(self.defense), \
               int(self.special_power), int(self.total_green), int(self.total_yellow), int(self.total_red), \
               int(self.total_misses), int(self.highest_combo)

    def display_resources(self):
        hp = mediumText.render(f'Health: {self.health}', True, GREEN)
        x = self.player_x2
        y = self.player_y2
        hp_xpos = (self.xpos + (x / 3))
        hp_ypos = (windowheight - 70)
        GAMEWINDOW.blit(hp,
                        (hp_xpos, hp_ypos))
        energy = mediumText.render(f'Energy: {self.energy}', True, GOLD)
        GAMEWINDOW.blit(energy,
                        (hp_xpos, (hp_ypos + 30)))

    def update_timecounter(self):
        self.timecounter = self.timecounter + 1
        base_gain = 5 + int(self.special_power/10)
        bonus = 0
        if self.current_combo >= 5:
            bonus = int((self.current_combo/5)*2)
        total_gain = base_gain + bonus
        if self.timecounter % 120 == 0 and self.energy < self.max_energy:
            if self.energy + total_gain >= self.max_energy:
                self.energy = self.max_energy
            else:
                self.energy = self.energy + total_gain
                print(f'gained: {total_gain} energy')

    def drawplayer(self):
        x = int(self.player_x2 * self.player_scaler)
        y = int(self.player_y2 * self.player_scaler)
        player_img = pygame.transform.scale(self.player_img_load, (x, y))

        if self.debug == 1:
            width = smallText.render(f'Width: {x}', True, WHITE)
            height = smallText.render(f'Height: {y}', True, WHITE)
            scaler = smallText.render(f'Scaler: {self.player_scaler}', True, WHITE)
            GAMEWINDOW.blit(width,
                            (70, 730))
            GAMEWINDOW.blit(scaler,
                            (70, 750))
            GAMEWINDOW.blit(height,
                            (70, 775))
        if (self.player_y2 + self.ypos) > 600:
            self.ypos = (self.ypos - 50)
            GAMEWINDOW.blit(self.player_platform,
                            (self.xpos, ((self.ypos + self.player_y2) - 85)))
            GAMEWINDOW.blit(player_img,
                            (self.xpos, self.ypos))
        elif self.name in self.shorties:
            GAMEWINDOW.blit(self.player_platform,
                            (self.xpos, (((self.ypos + self.player_y2) - 85) + 50)))
            GAMEWINDOW.blit(player_img,
                            (self.xpos + 60, (self.ypos + 50)))
        else:
            GAMEWINDOW.blit(self.player_platform,
                            (self.xpos, ((self.ypos + self.player_y2) - 85)))
            GAMEWINDOW.blit(player_img,
                            (self.xpos, self.ypos))
        if self.shieldactive == 1:
            if self.name in self.shorties:
                GAMEWINDOW.blit(ShieldImage_small,
                                (self.xpos, self.ypos))
            else:
                GAMEWINDOW.blit(ShieldImage,
                            ((self.xpos - 100), (self.ypos - 40)))
        self.debug_change_image_size_buttons()

    def debug_change_image_size_buttons(self):
        if self.debug == 1:
            x, y = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            drawbutton("^", 50, 740, 20, 20, BLACK, RED, LIGHTGRAY)
            drawbutton("V", 50, 770, 20, 20, BLACK, RED, LIGHTGRAY)
            if click[0] == 1 and x in range(50, 70) and y in range(740, 760):
                ev = pygame.event.get()
                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.player_scaler = (self.player_scaler + 0.1)
            if click[0] == 1 and x in range(50, 70) and y in range(770, 790):
                ev = pygame.event.get()
                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.player_scaler = (self.player_scaler - 0.1)

    def checkforshieldkeypress(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            if self.shieldactive == 0 and self.energy > 5:
                self.energy -= 2
            if self.energy > 5:
                self.shieldactive = 1
                self.shieldtimer += 1
                shield_sound.play()
                if self.shieldtimer % 15 == 0:
                    self.energy -= 5
            elif self.energy < 5:
                self.shieldactive = 0
                shield_sound.stop()
                self.shieldtimer = 0
        else:
            self.shieldactive = 0
            shield_sound.stop()
            self.shieldtimer = 0

    def update(self, ev):
        self.update_timecounter()
        self.display_resources()
        self.checkforshieldkeypress()
        self.drawplayer()
        self.special_attack(ev)
        self.check_heal_ability(ev)
        self.display_dmg_taken()


class Enemy:
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''
      Spawn an enemy     Spawn an enemy     Spawn an enemy     
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def __init__(self, name, **kwargs):
        self.dead = False
        self.name = name
        self.health = kwargs.get("health")
        self.attack_speed = kwargs.get("attack_speed")
        self.defense = kwargs.get("defense")
        self.energy = kwargs.get("energy")
        self.max_energy = kwargs.get("energy")
        self.attack_power = kwargs.get("attack_power")
        self.special_power = kwargs.get("special_power")
        self.energy_gain = kwargs.get("energy_gain")
        self.ability = []
        self.timecounter = 0
        self.frame = 0  # count frames
        self.xpos = 800
        self.ypos = 200
        self.x_min = 800
        self.y_min = 200
        self.dmg_text_flag = 0
        self.current_combo = 0
        self.dmg_text_counter = 0
        self.special_dmg_text_flag = 0
        self.special_dmg_text_counter = 0
        self.dmg_text_y = 0
        self.dmg_text_x = 0
        self.special_dmg_text_y = 0
        self.special_dmg_text_x = 0
        self.last_hit = 0
        self.last_special_hit = 0
        self.enemy_width = 380
        self.platform_width = 390
        self.platform_height = 0
        self.platform_img_load = pygame.image.load('images/enemy_platform.png')
        self.enemy_img_load = pygame.image.load(f'images/{name}_battle.png')
        self.enemy_x1 = 0
        self.enemy_x2 = 0
        self.enemy_y1 = 0
        self.enemy_y2 = 0
        self.resize_image()
        self.enemy_img = pygame.transform.scale(self.enemy_img_load, (self.enemy_x2, self.enemy_y2))
        self.enemy_platform = pygame.transform.scale(self.platform_img_load,
                                                      (self.platform_width, self.platform_height))
        self.bounds = self.enemy_img_load.get_size()
        self.x_max = (self.x_min + self.enemy_x2)
        self.y_max = (self.y_min + self.enemy_y2)

    def resize_image(self):
        x1, y1 = self.enemy_img_load.get_size()
        x2 = self.enemy_width
        y2 = int((x2*y1)/x1)
        platx, platy = self.platform_img_load.get_size()
        platx2 = self.platform_width
        platy2 = int((platx2 * platy) / platx)
        self.platform_height = platy2
        self.enemy_x1 = x1
        self.enemy_x2 = x2
        self.enemy_y1 = y1
        self.enemy_y2 = y2

    def display_resources(self):
        hp = mediumText.render(f'Health: {self.health}', True, GREEN)
        x, y = self.enemy_img.get_size()
        hp_xpos = (self.xpos + (x/3))
        hp_ypos = (windowheight - 70)
        GAMEWINDOW.blit(hp,
                        (hp_xpos, hp_ypos))
        energy = mediumText.render(f'Energy: {self.energy}', True, GOLD)
        GAMEWINDOW.blit(energy,
                        (hp_xpos, (hp_ypos + 30)))

    def updatehp(self):
        damagetaken = random.randint(5, 10)
        self.health = (self.health - damagetaken)

    def calc_special_dmg(self, special_power):
        attack_range_low = int(((special_power - (self.defense/2)) * 1.6))
        attack_range_high = int(((special_power - (self.defense/2)) * 2.2))
        damage = random.randint(attack_range_low, attack_range_high)
        return damage

    def calc_dmg(self, atk_power):
        attack_range_low = int(((atk_power - (self.defense/2)) * 0.6))
        attack_range_high = int(((atk_power - (self.defense/2)) * 1.2))
        damage = random.randint(attack_range_low, attack_range_high)
        return damage

    def lose_hp(self, circle_color, dmg_x, dmg_y, atk_power):
        if circle_color == 'green':
            multiplier = 1.2
            damagetaken = self.calc_dmg(atk_power)
            damagetaken = int(damagetaken * multiplier)
            self.health = (self.health - damagetaken)
            self.last_hit = damagetaken
            self.dmg_text_flag = 1
            self.dmg_text_x = dmg_x
            self.dmg_text_y = dmg_y
        elif circle_color == 'yellow':
            multiplier = 0.9
            damagetaken = self.calc_dmg(atk_power)
            damagetaken = int(damagetaken * multiplier)
            self.health = (self.health - damagetaken)
            self.last_hit = damagetaken
            self.dmg_text_flag = 1
            self.dmg_text_x = dmg_x
            self.dmg_text_y = dmg_y
        elif circle_color == 'red':
            multiplier = 0.5
            damagetaken = self.calc_dmg(atk_power)
            damagetaken = int(damagetaken * multiplier)
            self.health = (self.health - damagetaken)
            self.last_hit = damagetaken
            self.dmg_text_flag = 1
            self.dmg_text_x = dmg_x
            self.dmg_text_y = dmg_y
        elif circle_color == 'none':
            pass

    def lose_hp_from_special(self, special_power):
        self.last_special_hit = self.calc_special_dmg(special_power)
        self.special_dmg_text_flag = 1
        self.special_dmg_text_x = 950
        self.special_dmg_text_y = 270
        self.health = self.health - self.last_special_hit

    def display_special_dmg_taken(self):
        if self.special_dmg_text_flag == 0:
            pass
        elif self.special_dmg_text_flag == 1:
            self.special_dmg_text_counter += 1
            dmg_text = TEXT_special_dmg.render(f'-{self.last_special_hit}', True, RED)
            if self.special_dmg_text_counter < 80:
                GAMEWINDOW.blit(dmg_text,
                                (self.special_dmg_text_x, (self.special_dmg_text_y - 60)))
                if self.special_dmg_text_counter % 5 == 0:
                    self.special_dmg_text_y = self.special_dmg_text_y - 5
            if self.special_dmg_text_counter > 80:
                self.reset_display_special_dmg_taken()

    def display_dmg_taken(self):
        if self.dmg_text_flag == 0:
            pass
        elif self.dmg_text_flag == 1:
            self.dmg_text_counter += 1
            dmg_text = TEXT.render(f'-{self.last_hit}', True, RED)
            if self.dmg_text_counter < 80:
                GAMEWINDOW.blit(dmg_text,
                                (self.dmg_text_x, (self.dmg_text_y - 60)))
                if self.current_combo % 5 == 0:
                    combo_text = tutorialhpText.render(f'(Combo x{self.current_combo}!)', True, GOLD)
                    GAMEWINDOW.blit(combo_text,
                                    ((self.dmg_text_x - 150), (self.dmg_text_y + 100)))
                if self.dmg_text_counter % 5 == 0:
                    self.dmg_text_y = self.dmg_text_y - 5
            if self.dmg_text_counter > 80:
                self.reset_display_dmg_taken()

    def reset_display_dmg_taken(self):
        self.dmg_text_flag = 0
        self.dmg_text_counter = 0
        self.dmg_text_x = 0
        self.dmg_text_y = 0

    def reset_display_special_dmg_taken(self):
        self.special_dmg_text_flag = 0
        self.special_dmg_text_counter = 0
        self.last_special_hit = 0

    def update_timecounter(self):
        self.timecounter = self.timecounter + 1
        if self.timecounter % 180 == 0 and self.energy < self.max_energy:
            self.energy = self.energy + 5

    def drawenemy(self):
        if (self.enemy_y2 + self.ypos) > 600:
            self.ypos = (self.ypos - 100)
            GAMEWINDOW.blit(self.enemy_platform,
                            (self.xpos, ((self.ypos + self.enemy_y2) - 85)))
            GAMEWINDOW.blit(self.enemy_img,
                            (self.xpos, self.ypos))
        else:
            GAMEWINDOW.blit(self.enemy_platform,
                            (self.xpos, ((self.ypos + self.enemy_y2) - 85)))
            GAMEWINDOW.blit(self.enemy_img,
                            (self.xpos, self.ypos))

    def check_boss_dead(self):
        if self.health <= 0:
            self.dead = True

    def update(self):
        self.update_timecounter()
        self.display_resources()
        self.drawenemy()
        self.display_dmg_taken()
        self.display_special_dmg_taken()
        self.check_boss_dead()


def terminate():
    pygame.quit()
    sys.exit()


# Main Game Loop
def main():
    # Put all variables up here
    stopped = False
    StartScreen()
    game = CharacterSelect()
    player_object = Player(game.playercharacter, **game.player_attributes)
    while not stopped:
        battle = True
        game.enemyselect()
        player_object.reset_display_dmg_taken()
        enemy_object = Enemy(game.enemycharacter, **game.enemy_attributes)
        fight = BattleScreen(str(game.playercharacter), str(game.enemycharacter), enemy_object.x_min,
                             enemy_object.x_max, enemy_object.y_min, enemy_object.y_max, player_object.x_min,
                             player_object.x_max, player_object.y_min, player_object.y_max)
        while battle:
            x, y = pygame.mouse.get_pos()
            ev = pygame.event.get()
            fight.update()
            enemy_object.update()
            player_object.update(ev)
            enemy_dmg_taken, enemy_dmg_x, enemy_dmg_y, current_combo = fight.generate_hit_circles(ev)
            hit_type, player_dmg_x, player_dmg_y = fight.generate_enemy_attack_circles(player_object.shieldactive)
            player_object.current_combo = current_combo
            enemy_object.current_combo = current_combo
            enemy_object.lose_hp(enemy_dmg_taken, enemy_dmg_x, enemy_dmg_y, player_object.attack_power)
            if player_object.special_hit == 1:
                enemy_object.lose_hp_from_special(player_object.special_power)
            player_object.lose_hp(hit_type, player_dmg_x, player_dmg_y, enemy_object.attack_power)
            drawbutton("Main Menu", 10, 10, 135, 50, BLACK, RED, LIGHTGRAY)
            if fight.game_over or player_object.health <= 0:
                battle = False
                fight.stopmusic()
                gameover()
            if enemy_object.dead:
                fight.stopmusic()
                if enemy_object.name == 'Sephiroth':
                    green, yellow, red, combo, stat_points, misses = fight.match_summary()
                    player_object.final_stat_update(green, yellow, red, combo, stat_points, misses)
                    end_game_screen(player_object.name,
                                    player_object.max_health,
                                    player_object.max_energy,
                                    player_object.attack_power,
                                    player_object.defense,
                                    player_object.special_power,
                                    player_object.total_green,
                                    player_object.total_yellow,
                                    player_object.total_red,
                                    player_object.total_misses,
                                    player_object.highest_combo
                                    )
                green, yellow, red, combo, stat_points, misses = fight.match_summary()
                player_object.update_stat_info(green, yellow, red, combo, stat_points, misses)
                enemy_killed = enemy_object.name
                name = game.grayedout.pop(0)
                game.defeated.append(enemy_killed)
                game.coloredpictures.append(name)
                game.enemycharacter = ''
                break
            for event in ev:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if x in range(11, 144) and y in range(11, 59):
                        main()
            if checkforkeypress():
                pygame.event.get()  # clear event queue
                return
            pygame.display.update()
            CLOCK.tick(FPS)


    # Event Tasking        Add all your event tasking things here
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             quit()
    #         elif event.type == pygame.KEYDOWN:
    #             stopped = True

        # pygame.display.update()
        # CLOCK.tick(FPS)

if __name__ == '__main__':
    main()