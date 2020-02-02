import random, pygame, sys, time
from pygame.locals import *
pygame.init()
pygame.mixer.init()

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
 Images     Images     Images     Images     Images     Images     Images     
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

title = pygame.image.load('videogame.png')
title2 = pygame.image.load('allstars.png')

titlebg_image = pygame.image.load('titlescreenbg.png')
CharSelect_bg = pygame.image.load('CharSelect_bg.jpg')
EnemySelect_bg = pygame.image.load('Enemyselect_bg.jpg')
BattleScreen_bg = pygame.image.load('pikachu_bg.png')
ChocoboImage = pygame.image.load('ChocoboResize.png')


GokuImage = pygame.image.load('Goku.png')
MarioImage = pygame.image.load('Mario.png')
KakashiImage = pygame.image.load('Kakashi.png')
KirbyImage = pygame.image.load('Kirby.png')
CloudImage = pygame.image.load('Cloud.png')
PikachuImage = pygame.image.load('Pikachu.png')

ChuckNorrisImage = pygame.image.load('ChuckNorris.png')
LinkImage = pygame.image.load('Link.png')
RobotnikImage = pygame.image.load('Robotnik.png')  # 290x200
FriezaImage = pygame.image.load('FriezaBlur.png')  # 290x200
BowserImage = pygame.image.load('BowserBlur.png')  # 290x200
MagnetoImage = pygame.image.load('MagnetoBlur.png')  # 290x200
GanondorfImage = pygame.image.load('GanondorfBlur.png')  # 290x200
SephirothImage = pygame.image.load('SephirothBlur.png')  # 290x200


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        Text/Fonts     Text/Fonts     Text/Fonts                
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

pygame.display.set_caption('VIDEO GAME ALL-STARS')

TEXT = pygame.font.Font('freesansbold.ttf', 48)
smallText = pygame.font.Font("freesansbold.ttf", 20)
mediumText = pygame.font.Font("freesansbold.ttf", 28)
titleFont = pygame.font.Font('freesansbold.ttf', 58)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
 Objects     Objects     Objects     Objects     Objects     Objects     Objects     
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# put Python classes and functions here


def showstartscreen():
    global startscreen, instructions
    pygame.mixer.music.load('introsong.wav')
    pygame.mixer.music.play(-1)

    while True:
        x, y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        GAMEWINDOW.blit(titlebg_image,
                        (0, 0))
        pygame.draw.rect(GAMEWINDOW, BLACK, (295, 95, 775, 250))
        pygame.draw.rect(GAMEWINDOW, RED, (300, 100, 765, 240))
        GAMEWINDOW.blit(title, (319, 130))
        GAMEWINDOW.blit(title2, (368, 230))
        GAMEWINDOW.blit(ChocoboImage, (1100, 550))
        drawbutton("Start", 575, 500, 135, 50, BLACK, GOLD, LIGHTGRAY)
        if click[0] == 1 and x in range(576, 708) and y in range(501, 549):
            return
        drawbutton("How to Play", 1105, 500, 135, 50, BLACK, GOLD, LIGHTGRAY, showTutorialScreen)
        drawbutton("Quit", 575, 570, 135, 50, BLACK, GOLD, LIGHTGRAY, terminate)
        # print("X: %d, Y: %d" % (x, y))
        if checkforkeypress():
            pygame.event.get()  # clear event queue
            return
        pygame.display.update()
        CLOCK.tick(FPS)


def mainMenu():
    global startscreen
    startscreen = True
    showstartscreen()


def showTutorialScreen():
    while True:
        GAMEWINDOW.blit(titlebg_image, (0,0))
        drawbutton("Back", 10, 10, 135, 50, BLACK, RED, LIGHTGRAY, showstartscreen)
        if checkforkeypress():
            pygame.event.get()  # clear event queue
            return
        pygame.display.update()
        CLOCK.tick(FPS)


def showcharacterselectscreen():
    title1 = titleFont.render('Choose your character!', True, RED)
    pygame.mixer.music.load('characterselect.wav')
    pygame.mixer.music.play(-1)

    while True:
        x, y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        charactertext = titleFont.render(str(playercharacter), True, WHITE)
        GAMEWINDOW.blit(CharSelect_bg,
                        (0, 0))
        GAMEWINDOW.blit(title1,
                        (315, 35)),
        drawcharselectbutton(CloudImage, 'Cloud', 340, 180, 200, 250, WHITE, GOLD, BLACK, setchar)
        drawcharselectbutton(KakashiImage, 'Kakashi', 140, 430, 200, 250, WHITE, GOLD, BLACK, setchar)
        drawcharselectbutton(PikachuImage, 'Pikachu', 540, 180, 200, 250, WHITE, GOLD, BLACK, setchar)
        drawcharselectbutton(KirbyImage, 'Kirby', 340, 430, 200, 250, WHITE, GOLD, BLACK, setchar)
        drawcharselectbutton(GokuImage, 'Goku', 740, 180, 200, 250, WHITE, GOLD, BLACK, setchar)
        drawcharselectbutton(ChuckNorrisImage, 'Chuck Norris', 540, 430, 200, 250, WHITE, GOLD, BLACK, setchar)
        drawcharselectbutton(MarioImage, 'Mario', 940, 430, 200, 250, WHITE, GOLD, BLACK, setchar)
        drawcharselectbutton(LinkImage, 'Link', 740, 430, 200, 250, WHITE, GOLD, BLACK, setchar)

        drawbutton("Main Menu", 10, 10, 135, 50, BLACK, RED, LIGHTGRAY, mainMenu)

        if continuebutton == 1:
            drawbutton("Continue", 1100, 720, 135, 50, BLACK, RED, LIGHTGRAY)
            if click[0] == 1 and x in range(1101, 1233) and y in range(722, 769):
                return
            pass

        GAMEWINDOW.blit(charactertext,
                        (520, 715)),
        # drawGrid()
        x, y = pygame.mouse.get_pos()
        print("X: %d, Y: %d" % (x, y))
        if checkforkeypress():
            pygame.event.get()  # clear event queue
            return
        pygame.display.update()
        CLOCK.tick(FPS)


def showEnemySelectScreen():
    title = titleFont.render('Choose your Opponent!', True, RED)

    while True:
        enemytext = titleFont.render(str(enemycharacter), True, RED)
        GAMEWINDOW.blit(EnemySelect_bg,
                        (0, 0))
        GAMEWINDOW.blit(title,
                        (315, 25))
        drawbutton("Main Menu", 10, 10, 135, 50, BLACK, RED, LIGHTGRAY, mainMenu)
        drawenemyselectbutton(RobotnikImage, 'Dr. Robotnik',       170, 545, 296, 206, WHITE, RED, BLACK, setenemy)
        drawenemyselectbutton(BowserImage, '',             500, 545, 296, 206, WHITE, RED, BLACK)
        drawenemyselectbutton(MagnetoImage, '',            830, 545, 296, 206, WHITE, RED, BLACK)
        drawenemyselectbutton(GanondorfImage, '',           335, 315, 296, 206, WHITE, RED, BLACK)
        drawenemyselectbutton(FriezaImage, '',             665, 315, 296, 206, WHITE, RED, BLACK)
        drawenemyselectbutton(SephirothImage, '',          503, 90, 296, 206, WHITE, RED, BLACK)
        x, y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if fightbutton == 1:
            drawbutton("FIGHT!", 1140, 745, 135, 50, BLACK, RED, LIGHTGRAY)
            if click[0] == 1 and x in range(1140, 1274) and y in range(750, 794):
                return
            pass

        GAMEWINDOW.blit(enemytext,
                        (500, 750)),

        # x, y = pygame.mouse.get_pos()
        # print("X: %d, Y: %d" % (x, y))
        # click = pygame.mouse.get_pressed()
        # if click[0] == 1 and x in range(1140, 1274) and y in range(750, 794):
        #     print('hi')
            #return
        if checkforkeypress():
            pygame.event.get()  # clear event queue
            return
        pygame.display.update()
        CLOCK.tick(FPS)


def showBattleScreen():
    countdowntitle = titleFont.render('3! 2! 1! FIGHT!', True, RED)
    pygame.mixer.music.load('robotnik.wav')
    pygame.mixer.music.play(-1)


    while True:
        GAMEWINDOW.blit(BattleScreen_bg,
                        (0, 0))
        GAMEWINDOW.blit(countdowntitle,
                        (315, 25))

        player = Player()  # spawn player
        player.rect.x = 50  # go to x
        player.rect.y = 500  # go to y
        player_list = pygame.sprite.Group()
        player_list.add(player)

        enemy = Enemy()
        enemy.rect.x = 900
        enemy.rect.y = 500
        enemy_list = pygame.sprite.Group()
        enemy_list.add(enemy)


        if checkforkeypress():
            pygame.event.get()  # clear event queue
            return

        player_list.draw(GAMEWINDOW)  # draw player
        enemy_list.draw(GAMEWINDOW)

        pygame.display.update()
        CLOCK.tick(FPS)


class Player(pygame.sprite.Sprite):
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''
      Spawn a player     Spawn a player     Spawn a player     
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = []
        self.movex = 0  # move along X
        self.movey = 0  # move along Y
        self.frame = 0  # count frames
        self.health = 10
        self.images = []
        self.weight = []
        self.speed = []
        self.ability = []
        self.healability = []
        img = pygame.image.load(f'{playercharacter}.png')
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()


    def control(self,x,y):
        '''''''''''''''''''''''''''''''''''''''''''''''''''''''''
           control player movement     control player movement     
        '''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        self.movex += x
        self.movey += y


class Enemy(pygame.sprite.Sprite):
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''
      Spawn an enemy     Spawn an enemy     Spawn an enemy     
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = []
        self.movex = 0  # move along X
        self.movey = 0  # move along Y
        self.frame = 0  # count frames
        self.health = 10
        self.images = []
        self.weight = []
        self.speed = []
        self.ability = []
        self.healability = []
        img = pygame.image.load(f'{enemycharacter}.png')
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()


    def control(self,x,y):
        '''''''''''''''''''''''''''''''''''''''''''''''''''''''''
           control player movement     control player movement     
        '''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        self.movex += x
        self.movey += y


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
   draw a menu button     draw a menu button     
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# class CharacterSelection(pygame.sprite.Sprite):

def drawcharselectbutton(image, name, x, y, w, h, ic, ac, bc, action1=None):
    mouse = pygame.mouse.get_pos()  # ic=inactive color(White), ac=active color(Gold)(hover over,bc=button color)(Black)
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:

        pygame.draw.rect(GAMEWINDOW, ac, (x, y, w, h))
        pygame.draw.rect(GAMEWINDOW, bc, (x + 3, y + 3, w - 6, h - 6))
        GAMEWINDOW.blit(image,
                        (x, y))

        if click[0] == 1 and action1 is not None:
            pygame.draw.rect(GAMEWINDOW, ac, (x, y, w, h))
            pygame.draw.rect(GAMEWINDOW, bc, (x + 3, y + 3, w - 6, h - 6))
            GAMEWINDOW.blit(image,
                            (x, y))
            action1(name)

    else:
        pygame.draw.rect(GAMEWINDOW, ic, (x, y, w, h))
        pygame.draw.rect(GAMEWINDOW, bc, (x + 3, y + 3, w - 6, h - 6))
        GAMEWINDOW.blit(image,
                        (x, y))

    textsurf, textrect = text_objects_white(name, mediumText)
    textrect.center = ((x + (w / 2)), (y + (h - 20)))
    GAMEWINDOW.blit(textsurf, textrect)


def setchar(name):
    global playercharacter, continuebutton
    continuebutton = 1
    playercharacter = str(name)
    CLOCK.tick(FPS)


def setenemy(name):
    global enemycharacter, fightbutton
    fightbutton = 1
    enemycharacter = str(name)
    CLOCK.tick(FPS)


def drawbutton(msg, x, y, w, h, ic, ac, bc, action=None):  # ic=inact color, ac=active color(hover over,bc=button color)
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


def drawenemyselectbutton(image, name, x, y, w, h, ic, ac, bc, action=None):  # ic= inactive color, ac= active color(hover over, bc= button color)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(GAMEWINDOW, ac, (x, y, w, h))
        pygame.draw.rect(GAMEWINDOW, bc, (x + 3, y + 3, w - 6, h - 6))
        GAMEWINDOW.blit(image,
                        (x+3, y+3))

        if click[0] == 1 and action != None:
            action(name)
    else:
        pygame.draw.rect(GAMEWINDOW, ic, (x, y, w+1, h))
        pygame.draw.rect(GAMEWINDOW, bc, (x + 3, y + 3, w - 6, h - 6))
        GAMEWINDOW.blit(image,
                        (x+3, y+3))

    textSurf, textRect = text_objects_white(name, mediumText)
    textRect.center = ((x + (w / 2)), (y + (h-20)))
    GAMEWINDOW.blit(textSurf, textRect)


def text_objects(text, font):  # text, font, color?
    textsurface = font.render(text, True, BLACK)  # Change to color and add parameter to function?
    return textsurface, textsurface.get_rect()


def text_objects_white(text, font):
    textsurface = font.render(text, True, WHITE)
    return textsurface, textsurface.get_rect()


def checkforkeypress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyupevents = pygame.event.get(KEYUP)
    if len(keyupevents) == 0:
        return None
    if keyupevents[0].key == K_ESCAPE:
        terminate()
    return keyupevents[0].key


def terminate():
    pygame.quit()
    sys.exit()


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
   Setup     Setup     Setup     Setup     Setup     Setup     Setup     Setup     
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# put run-once code here

FPS = 60
WINDOWWIDTH = 1280
WINDOWHEIGHT = 800
CELLSIZE = 80
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#             R    G    B
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
LIGHTGRAY = (235, 230, 230)
GOLD = (255, 187, 15)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
 Main Loop     Main Loop     Main Loop     Main Loop     Main Loop     Main Loop     
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# put game loop here

def main():
    global CLOCK, GAMEWINDOW, playercharacter, \
        continuebutton, enemycharacter, fightbutton, enemieskilled

    pygame.init()
    pygame.mixer.init()
    CLOCK = pygame.time.Clock()
    GAMEWINDOW = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    enemieskilled = []
    playercharacter = ''
    enemycharacter = ''
    continuebutton = 0
    fightbutton = 0


    showstartscreen()
    showcharacterselectscreen()
    print(f'Player has chose: {playercharacter}')
    showEnemySelectScreen()
    print(f'Enemy chosen: {enemycharacter}')
    showBattleScreen()


if __name__ == '__main__':
    main()