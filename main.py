import pygame, sys
from pygame.examples.sound import mixer
from pygame.locals import *
import random
import math

pygame.init()
# x and Y coordinates of the window
x = 900
y = 600
screen = pygame.display.set_mode((x, y), 0, 32)  # print out the screen
pygame.display.set_caption('Racing Gear 2D')  # title of the window
icon = pygame.image.load('Image/icon.png')
pygame.display.set_icon(icon)

mainClock = pygame.time.Clock()

# set common font
font = pygame.font.SysFont(None, 40)
fon = pygame.font.SysFont(None, 25)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    click = False
    while True:
        
        screen.fill((0, 0, 0))
        background = pygame.image.load('Image/background.png')
        draw_text('Main Menu', font, (40, 40, 40), screen, 30, 20)
        mx, my = pygame.mouse.get_pos()
        button_6 = pygame.Rect(30, 100, 200, 30)
        button_1 = pygame.Rect(30, 135, 200, 30)
        button_2 = pygame.Rect(30, 170, 200, 30)
        button_3 = pygame.Rect(30, 205, 200, 30)
        button_4 = pygame.Rect(30, 240, 200, 30)
        button_5 = pygame.Rect(30, 275, 200, 30)
        if button_1.collidepoint(mx, my):
            if click:
                game()
        if button_2.collidepoint(mx, my):
            if click:
                level()
        if button_3.collidepoint(mx, my):
            if click:
                score()
        if button_4.collidepoint(mx, my):
            if click:
                option()
        if button_5.collidepoint(mx, my):
            if click:
                pygame.quit()
                sys.exit()
        if button_6.collidepoint(mx, my):
            if click:
                pass
        pygame.draw.rect(screen, (47, 47, 47), button_1)
        pygame.draw.rect(screen, (47, 47, 47), button_2)
        pygame.draw.rect(screen, (47, 47, 47), button_3)
        pygame.draw.rect(screen, (47, 47, 47), button_4)
        pygame.draw.rect(screen, (47, 47, 47), button_5)
        pygame.draw.rect(screen, (27, 27, 27), button_6)
        draw_text('Resume', fon, (200, 200, 200), screen, 40, 105)
        draw_text('New Game', fon, (250, 250, 250), screen, 40, 140)
        draw_text('Select Level', fon, (250, 250, 250), screen, 40, 174)
        draw_text('High Score', fon, (250, 250, 250), screen, 40, 210)
        draw_text('About', fon, (250, 250, 250), screen, 40, 245)
        draw_text('Exit', fon, (250, 250, 250), screen, 40, 280)
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        screen.blit(background, (0, 0))
        pygame.display.update()
        mainClock.tick(60)


def pause_game():
    pauseImg = pygame.image.load('Image/pause.png')
    screen.blit(pauseImg, (0, 0))


def game():
    global count
    count = 0
    # Enemy 2
    enemImg = pygame.image.load('Image/second enemy.png')
    enemY = -1000
    enemX = random.randint(300, 500)
    enemX_change = 0
    enemY_change = 0
    # Enemy
    enemyImg = pygame.image.load('Image/enemy.png')
    enemyX = random.randint(300, 500)
    enemyY = -85
    enemyX_change = 0
    enemyY_change = 0
    # Player
    playerImg = pygame.image.load('Image/player.png')
    playerX = 380
    playerY = 400
    playerX_change = 0
    playerY_change = 0
    # background
    black = pygame.image.load('Image/road.png')
    blackX = 0
    blackY = -600
    blackX_change = 0
    blackY_change = 0
    black2 = pygame.image.load('Image/road.png')
    blackX2 = 0
    blackY2 = -1200
    blackX2_change = 0
    blackY2_change = 0
    running = True
    while running:
        screen.fill((0, 0, 0))
        background = pygame.image.load('Image/backg.png')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    main_menu()
                if event.key == K_ESCAPE:
                    running = False
                    start = True
                    while start:
                        pause_game()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                start = False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP:
                                    running = True
                                    start = False
                if event.key == K_LEFT:
                    playerX_change = -12
                if event.key == K_RIGHT:
                    playerX_change = 12
                if event.key == K_UP:
                    playerY_change = -12
                    enemyY_change = 12
                    blackY_change = 12
                    blackY2_change = 12
                    enemY_change = 15
            if event.type == KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
                if event.key == pygame.K_UP:
                    playerY_change = 5
                    blackY_change = 5
                    black2_change = 5

        def collison(enemyX, enemyY, playerX, playerY, enemX, enemY):
            dis = math.sqrt(math.pow(enemX - playerX, 2) + math.pow(enemY - playerY, 2))
            distance = math.sqrt(math.pow(enemyX - playerX, 2) + math.pow(enemyY - playerY, 2))
            if distance < 60:
                return True
            if dis < 60:
                return True

        playerX += playerX_change
        if playerX <= 300:
            game_over()
        if playerX >= 520:
            game_over()
        playerY += playerY_change
        if playerY <= 310:
            playerY = 310
        if playerY > 470:
            game_over()
        if enemyY > 590:
            count += 1
            enemyY = -230
            enemyX = random.randint(310, 500)
        if blackY > 500:
            blackY = -650
            blackY2 = -1700
        if enemY > 700:
            count += 1
            score_value1()
            value = str(count)
            outfile = open('file/store.txt', 'r')
            cou = outfile.readline()

            if count >= 116:
                level2()
            if count >= int(cou):
                file = open('file/store.txt', "w")
                file.write(value)
                file.close()
            enemY = -2000
            enemX = random.randint(310, 500)
        enemY += enemY_change
        enemyY += enemyY_change
        blackY += blackY_change
        blackY2 += blackY2_change
        colide = collison(enemyX, enemyY, playerX, playerY, enemX, enemY)
        if colide:
            game_over()

        screen.blit(background, (0, 0))
        screen.blit(black, (blackX, blackY))
        screen.blit(black2, (blackX2, blackY2))
        draw_text('Score: ' + str(count), font, (255, 255, 255), screen, 20, 20)
        screen.blit(enemImg, (enemX, enemY))
        screen.blit(enemyImg, (enemyX, enemyY))
        screen.blit(playerImg, (playerX, playerY))
        pygame.display.update()
        mainClock.tick(60)


def game_over():
    click = False
    again = True
    while again:
        screen.fill((0, 0, 0))
        background = pygame.image.load('Image/background.png')
        draw_text('Game Over', font, (255, 255, 255), screen, 20, 20)
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(30, 100, 200, 30)
        button_2 = pygame.Rect(30, 135, 200, 30)
        if button_1.collidepoint(mx, my):
            if click:
                game()
        if button_2.collidepoint(mx, my):
            if click:
                main_menu()

        pygame.draw.rect(screen, (47, 47, 47), button_1)
        pygame.draw.rect(screen, (47, 47, 47), button_2)
        score_value1()
        draw_text('Restart', fon, (200, 200, 200), screen, 40, 105)
        draw_text('Main Menu', fon, (250, 250, 250), screen, 40, 140)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        screen.blit(background, (0, 0))
        pygame.display.update()


def game_over2():
    click = False
    again = True
    while again:
        screen.fill((0, 0, 0))
        background = pygame.image.load('Image/background.png')
        draw_text('Game Over', font, (255, 255, 255), screen, 20, 20)
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(30, 100, 200, 30)
        button_2 = pygame.Rect(30, 135, 200, 30)
        if button_1.collidepoint(mx, my):
            if click:
                level2()
        if button_2.collidepoint(mx, my):
            if click:
                main_menu()
        pygame.draw.rect(screen, (47, 47, 47), button_1)
        pygame.draw.rect(screen, (47, 47, 47), button_2)

        draw_text('Restart', fon, (200, 200, 200), screen, 40, 105)
        draw_text('Main Menu', fon, (250, 250, 250), screen, 40, 140)
        score_value()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        screen.blit(background, (0, 0))
        pygame.display.update()


def level():
    click = False
    again = True
    level1 = pygame.image.load('Image/level1.png')
    lvl2 = pygame.image.load('Image/level2.png')
    while again:
        screen.fill((0, 0, 0))
        draw_text('Select Level', font, (255, 255, 255), screen, 20, 20)
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(90, 350, 300, 50)
        button_2 = pygame.Rect(470, 350, 300, 50)
        if button_1.collidepoint(mx, my):
            if click:
                game()
        if button_2.collidepoint(mx, my):
            if click:
                level2()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    again = False

        screen.blit(level1, (90, 150))
        screen.blit(lvl2, (470, 150))
        pygame.draw.rect(screen, (47, 47, 47), button_1)
        pygame.draw.rect(screen, (47, 47, 47), button_2)
        draw_text('Play', font, (250, 250, 250), screen, 210, 360)
        draw_text('Play', font, (250, 250, 250), screen, 600, 360)

        pygame.display.update()


def level2():
    global count
    count = 0
    # Enemy 2
    enemImg = pygame.image.load('Image/second enemy.png')
    enemY = -1000
    enemX = random.randint(300, 500)
    enemX_change = 0
    enemY_change = 0
    # Enemy
    enemyImg = pygame.image.load('Image/enemy.png')
    enemyX = random.randint(300, 500)
    enemyY = -85
    enemyX_change = 0
    enemyY_change = 0
    # Player
    playerImg = pygame.image.load('Image/player.png')
    playerX = 380
    playerY = 400
    playerX_change = 0
    playerY_change = 0
    # background
    black = pygame.image.load('Image/road.png')
    blackX = 0
    blackY = -600
    blackX_change = 0
    blackY_change = 0
    black2 = pygame.image.load('Image/road.png')
    blackX2 = 0
    blackY2 = -1200
    blackX2_change = 0
    blackY2_change = 0
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Game', font, (255, 255, 255), screen, 20, 20)
        background = pygame.image.load('Image/back2.png')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    main_menu()
                if event.key == K_ESCAPE:
                    running = False
                    start = True
                    while start:
                        screen.fill((47, 47, 47))
                        pause_game()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                start = False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP:
                                    running = True
                                    start = False
                if event.key == K_LEFT:
                    playerX_change = -10
                if event.key == K_RIGHT:
                    playerX_change = 10
                if event.key == K_UP:
                    playerY_change = -10
                    enemyY_change = 20
                    blackY_change = 20
                    blackY2_change = 20
                    enemY_change = 25
            if event.type == KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
                if event.key == pygame.K_UP:
                    playerY_change = 5
                    blackY_change = 5
                    black2_change = 5

        def collison(enemyX, enemyY, playerX, playerY, enemX, enemY):
            dis = math.sqrt(math.pow(enemX - playerX, 2) + math.pow(enemY - playerY, 2))
            distance = math.sqrt(math.pow(enemyX - playerX, 2) + math.pow(enemyY - playerY, 2))
            if distance < 60:
                return True
            if dis < 60:
                return True

        playerX += playerX_change
        if playerX <= 300:
            game_over2()
        if playerX >= 520:
            game_over2()
        playerY += playerY_change
        if playerY <= 310:
            playerY = 310
        if playerY > 470:
            game_over2()
        if enemyY > 590:
            count += 1
            enemyY = -230
            enemyX = random.randint(310, 500)
        if blackY > 500:
            blackY = -650
            blackY2 = -1700
        if enemY > 700:
            count += 1
            score_value()
            value = str(count)
            outfile = open('file/store.txt', 'r')
            cou = outfile.readline()

            if count >= int(cou):
                file = open('file/store.txt', "w")
                file.write(value)
                file.close()
            enemY = -2000
            enemX = random.randint(310, 500)
        enemY += enemY_change
        enemyY += enemyY_change
        blackY += blackY_change
        blackY2 += blackY2_change
        colide = collison(enemyX, enemyY, playerX, playerY, enemX, enemY)
        if colide:
            game_over2()

        screen.blit(background, (0, 0))
        screen.blit(black, (blackX, blackY))
        screen.blit(black2, (blackX2, blackY2))
        draw_text('Score: ' + str(count), font, (255, 255, 255), screen, 20, 20)
        screen.blit(enemImg, (enemX, enemY))
        screen.blit(enemyImg, (enemyX, enemyY))
        screen.blit(playerImg, (playerX, playerY))
        pygame.display.update()
        mainClock.tick(60)


def score_value():
    draw_text('Score: ' + str(count), font, (255, 255, 255), screen, 700, 20)


def score_value1():
    draw_text('Score: ' + str(count), font, (255, 255, 255), screen, 700, 20)


def score():
    opt = True
    while opt:
        screen.fill((0, 0, 0))
        background = pygame.image.load('Image/background.png')
        draw_text('High Score', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    opt = False
        file = open('file/store.txt', "r")
        value = file.readline()
        file.close()
        draw_text('High Score: ' + value, font, (0, 0, 255), screen, 100, 100)
        screen.blit(background, (0, 0))
        pygame.display.update()
        mainClock.tick(60)


def option():
    opt = True
    while opt:
        screen.fill((0, 0, 0))
        draw_text('About', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    opt = False
        draw_text('The role of the game is simple, just go forward dont loose spped if speed becomes zero', fon,
                  (255, 255, 255), screen, 60, 100)
        draw_text('you lose the game if you went off the road you lose the game, you can progress to the s-', fon,
                  (255, 255, 255), screen, 50, 130)
        draw_text('-econd part of the game if you get a total score of 116 watch out for the black cars they', fon,
                  (255, 255, 255), screen, 50, 160)
        draw_text('move a little faster than the others some times they overlap with other cars so carefull,',
                  fon, (255, 255, 255), screen, 50, 190)
        draw_text('and the game doesn\'t end it continues forever the role of the game is to gate the highest', fon,
                  (255, 255, 255), screen, 50, 220)
        draw_text('score possible just simple 2D boring game created in 2 days wish you Enjoy!!', fon, (255, 255, 255),
                  screen, 50, 250)
        pygame.display.update()
        mainClock.tick(60)


main_menu()
