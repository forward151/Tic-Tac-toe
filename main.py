import pygame
import sys
from random import choice

def check_win():
    global winList, list_bot, list_user, running, dr, user, bot
    for i in winList:
        if len(list(set(i) & set(list_user))) == 3:
            user = True
            pygame.time.delay(1000)
            running = False
    if not user:
        for i in winList:
            if len(list(set(i) & set(list_bot))) == 3:
                bot = True
                pygame.time.delay(1000)
                running = False
    if not user and not bot and (len(list_user) + len(list_bot)) == 9:
        dr = True
        pygame.time.delay(1000)
        running = False


userAttack = False


def check_move():
    global winList, list_bot, list_user, move_bot, userAttack, allList, fm
    bt1 = False
    movex = False
    superattack = False
    draw = True
    if len(list_bot) == 0:
        if 5 in list_user:
            move_bot = fm
            list_bot.append(move_bot)
        else:
            move_bot = 5
            list_bot.append(move_bot)

    for i in winList:
        if len(list(set(i) & set(list_user))) == 2:
            if list(set(i) - set(list_user))[0] not in list_bot:
                userAttack = True
                break

    for i in winList:
        if len(list(set(i) & set(list_bot))) == 2:
            if list(set(i) - set(list_bot))[0] not in list_user:
                move_bot = list(set(i) - set(list_bot))[0]
                list_bot.append(move_bot)
                superattack = True
                break

    if userAttack and not superattack:
        for i in winList:
            if len(list(set(i) & set(list_user))) == 2 and list(set(i) - set(list_user))[0] not in list_bot:
                move_bot = list(set(i) - set(list_user))[0]
                list_bot.append(move_bot)
                userAttack = False
                break
    elif not userAttack and not superattack:
        for i in winList:
            if len(list(set(i) & set(list_bot))) == 2 and list(set(i) - set(list_user))[0] not in list_user and list(set(i) - set(list_user))[0] not in list_bot:
                move_bot = list(set(i) - set(list_user))[0]
                list_bot.append(move_bot)
                bt1 = True
                draw = False
                break

        if not bt1:
            for i in winList:
                if len(list(set(i) & set(list_bot))) == 1 and len(list(set(list_bot).difference(set(i)))) == 0 and len(list(set(list_user).difference(set(i)))) == 2:

                    move_bot = list(set(i) - set(list_bot))[0]
                    list_bot.append(move_bot)
                    draw = False
                    movex = True
                    break
            if not movex:
                for i in winList:
                    if len(list(set(i) & set(list_bot))) == 1 and len(
                            list(set(list_bot).difference(set(i)))) == 1 and len(
                            list(set(list_user).difference(set(i)))) == 3:
                        move_bot = list(set(i) - set(list_bot))[0]
                        list_bot.append(move_bot)
                        draw = False
                        break

        if draw:
            for i in allList:
                if i not in list_user and i not in list_bot and(len(list_user) + len(list_bot)) > 5:

                    move_bot = i
                    list_bot.append(move_bot)
                    break









fm = choice([1, 2, 3, 4, 6, 7, 8, 9])
# здесь определяются константы,
# классы и функции
FPS = 60
running = True
dr = False
user = False
bot = False
winList = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           [1, 4, 7],
           [2, 5, 8],
           [3, 6, 9],
           [1, 5, 9],
           [3, 5, 7]]
allList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_user = []
list_bot = []
move_bot = 0
# здесь происходит инициация,
# создание объектов
pygame.init()
pygame.display.set_mode((170, 170))
clock = pygame.time.Clock()
sc = pygame.display.set_mode((170, 170))

myfont = pygame.font.SysFont("Comic Sans MS", 28)
# apply it to text on a label
label = myfont.render("Tic-Tac toe", True, (255, 255, 255))
# put the label object on the screen at point x=100, y=100
sc.blit(label, (10, 10))
pygame.display.update()
pygame.time.delay(1000)

sc.fill((0, 0, 0))
pygame.display.update()
move = True
mode1 = False
mode2 = False
myfont2 = pygame.font.SysFont("Comic Sans MS", 23)
label2 = myfont2.render("Select a player", True, (255, 255, 255))

while not mode1 and not mode2:
    sc.blit(label2, (10, 10))

    pygame.draw.line(sc, (255, 255, 255), [85, 60], [85, 170], 2)

    pygame.draw.aaline(sc, (255, 0, 0), [10, 78], [74, 142])
    pygame.draw.aaline(sc, (255, 0, 0), [74, 78], [10, 142])

    pygame.draw.circle(sc, (0, 0, 255), (128, 110), 32, 1)

    for i in pygame.event.get():
        if i.type == pygame.MOUSEMOTION:
            if i.pos[0] > 10 and i.pos[0] < 85 and i.pos[1] > 60 and i.pos[1] < 170:
                pygame.draw.polygon(sc, (50, 50, 50), [[0, 60], [85, 60], [85, 170], [0, 170]])
                pygame.draw.polygon(sc, (0, 0, 0), [[85, 60], [170, 60], [170, 170], [85, 170]])
            elif i.pos[0] > 85 and i.pos[0] < 160 and i.pos[1] > 60 and i.pos[1] < 170:
                pygame.draw.polygon(sc, (0, 0, 0), [[0, 60], [85, 60], [85, 170], [0, 170]])
                pygame.draw.polygon(sc, (50, 50, 50), [[85, 60], [170, 60], [170, 170], [85, 170]])
            else:
                pygame.draw.polygon(sc, (0, 0, 0), [[0, 60], [85, 60], [85, 170], [0, 170]])
                pygame.draw.polygon(sc, (0, 0, 0), [[85, 60], [170, 60], [170, 170], [85, 170]])
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if i.pos[0] > 10 and i.pos[0] < 85 and i.pos[1] > 78 and i.pos[1] < 142:
                    mode2 = True
                if i.pos[0] > 85 and i.pos[0] < 160 and i.pos[1] > 78 and i.pos[1] < 142:
                    mode1 = True
        pygame.display.update()

    pygame.display.update()

sc.fill((0, 0, 0))
pygame.display.update()


pygame.draw.line(sc, (255, 255, 255), [10, 60], [160, 60])
pygame.draw.line(sc, (255, 255, 255), [10, 110], [160, 110])
pygame.draw.line(sc, (255, 255, 255), [60, 10], [60, 160])
pygame.draw.line(sc, (255, 255, 255), [110, 10], [110, 160])
# если надо до цикла отобразить
# какие-то объекты, обновляем экран
pygame.display.update()


# главный цикл
while running:

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if move:
                if i.button == 1 and mode1:
                    if i.pos[0] > 10 and i.pos[0] < 60 and i.pos[1] > 10 and i.pos[1] < 60 and 1 not in list_user and 1 not in list_bot:
                        pygame.draw.circle(sc, (0, 0, 255), (35, 35), 20, 1)
                        list_user.append(1)
                        move = False
                    elif i.pos[0] > 60 and i.pos[0] < 110 and i.pos[1] > 10 and i.pos[1] < 60 and 2 not in list_user and 2 not in list_bot:
                        pygame.draw.circle(sc, (0, 0, 255), (85, 35), 20, 1)
                        list_user.append(2)
                        move = False
                    elif i.pos[0] > 110 and i.pos[0] < 160 and i.pos[1] > 10 and i.pos[1] < 60 and 3 not in list_user and 3 not in list_bot:
                        pygame.draw.circle(sc, (0, 0, 255), (135, 35), 20, 1)
                        list_user.append(3)
                        move = False
                    elif i.pos[0] > 10 and i.pos[0] < 60 and i.pos[1] > 60 and i.pos[1] < 110 and 4 not in list_user and 4 not in list_bot:
                        pygame.draw.circle(sc, (0, 0, 255), (35, 85), 20, 1)
                        list_user.append(4)
                        move = False
                    elif i.pos[0] > 10 and i.pos[0] < 60 and i.pos[1] > 110 and i.pos[1] < 170 and 7 not in list_user and 7 not in list_bot:
                        pygame.draw.circle(sc, (0, 0, 255), (35, 135), 20, 1)
                        list_user.append(7)
                        move = False
                    elif i.pos[0] > 60 and i.pos[0] < 110 and i.pos[1] > 60 and i.pos[1] < 110 and 5 not in list_user and 5 not in list_bot:
                        pygame.draw.circle(sc, (0, 0, 255), (85, 85), 20, 1)
                        list_user.append(5)
                        move = False
                    elif i.pos[0] > 110 and i.pos[0] < 160 and i.pos[1] > 110 and i.pos[1] < 160 and 9 not in list_user and 9 not in list_bot:
                        pygame.draw.circle(sc, (0, 0, 255), (135, 135), 20, 1)
                        list_user.append(9)
                        move = False
                    elif i.pos[0] > 110 and i.pos[0] < 160 and i.pos[1] > 60 and i.pos[1] < 110 and 6 not in list_user and 6 not in list_bot:
                        pygame.draw.circle(sc, (0, 0, 255), (135, 85), 20, 1)
                        list_user.append(6)
                        move = False
                    elif i.pos[0] > 60 and i.pos[0] < 110 and i.pos[1] > 110 and i.pos[1] < 160 and 8 not in list_user and 8 not in list_bot:
                        pygame.draw.circle(sc, (0, 0, 255), (85, 135), 20, 1)
                        list_user.append(8)
                        move = False
                elif i.button == 1 and mode2:
                    if i.pos[0] > 10 and i.pos[0] < 60 and i.pos[1] > 10 and i.pos[1] < 60 and 1 not in list_user and 1 not in list_bot:
                        pygame.draw.aaline(sc, (255, 0, 0), [15, 15], [55, 55])
                        pygame.draw.aaline(sc, (255, 0, 0), [55, 15], [15, 55])
                        list_user.append(1)
                        move = False
                    elif i.pos[0] > 60 and i.pos[0] < 110 and i.pos[1] > 10 and i.pos[1] < 60 and 2 not in list_user and 2 not in list_bot:
                        pygame.draw.aaline(sc, (255, 0, 0), [65, 15], [105, 55])
                        pygame.draw.aaline(sc, (255, 0, 0), [105, 15], [65, 55])
                        list_user.append(2)
                        move = False
                    elif i.pos[0] > 110 and i.pos[0] < 160 and i.pos[1] > 10 and i.pos[1] < 60 and 3 not in list_user and 3 not in list_bot:
                        pygame.draw.aaline(sc, (255, 0, 0), [115, 15], [155, 55])
                        pygame.draw.aaline(sc, (255, 0, 0), [155, 15], [115, 55])
                        list_user.append(3)
                        move = False
                    elif i.pos[0] > 10 and i.pos[0] < 60 and i.pos[1] > 60 and i.pos[1] < 110 and 4 not in list_user and 4 not in list_bot:
                        pygame.draw.aaline(sc, (255, 0, 0), [15, 65], [55, 105])
                        pygame.draw.aaline(sc, (255, 0, 0), [55, 65], [15, 105])
                        list_user.append(4)
                        move = False
                    elif i.pos[0] > 10 and i.pos[0] < 60 and i.pos[1] > 110 and i.pos[1] < 170 and 7 not in list_user and 7 not in list_bot:
                        pygame.draw.aaline(sc, (255, 0, 0), [15, 115], [55, 155])
                        pygame.draw.aaline(sc, (255, 0, 0), [55, 115], [15, 155])
                        list_user.append(7)
                        move = False
                    elif i.pos[0] > 60 and i.pos[0] < 110 and i.pos[1] > 60 and i.pos[1] < 110 and 5 not in list_user and 5 not in list_bot:
                        pygame.draw.aaline(sc, (255, 0, 0), [65, 65], [105, 105])
                        pygame.draw.aaline(sc, (255, 0, 0), [105, 65], [65, 105])
                        list_user.append(5)
                        move = False
                    elif i.pos[0] > 110 and i.pos[0] < 160 and i.pos[1] > 110 and i.pos[1] < 160 and 9 not in list_user and 9 not in list_bot:
                        pygame.draw.aaline(sc, (255, 0, 0), [115, 115], [155, 155])
                        pygame.draw.aaline(sc, (255, 0, 0), [155, 115], [115, 155])
                        list_user.append(9)
                        move = False
                    elif i.pos[0] > 110 and i.pos[0] < 160 and i.pos[1] > 60 and i.pos[1] < 110 and 6 not in list_user and 6 not in list_bot:
                        pygame.draw.aaline(sc, (255, 0, 0), [115, 65], [155, 105])
                        pygame.draw.aaline(sc, (255, 0, 0), [155, 65], [115, 105])
                        list_user.append(6)
                        move = False
                    elif i.pos[0] > 60 and i.pos[0] < 110 and i.pos[1] > 110 and i.pos[1] < 160 and 8 not in list_user and 8 not in list_bot:
                        pygame.draw.aaline(sc, (255, 0, 0), [65, 115], [105, 155])
                        pygame.draw.aaline(sc, (255, 0, 0), [65, 155], [105, 115])
                        list_user.append(8)
                        move = False
                pygame.display.update()
                check_win()
                check_move()
                if not running:
                    break
                pygame.display.update()

            if not move:
                if mode1:
                    if move_bot == 1:
                        pygame.time.delay(1000)
                        pygame.draw.aaline(sc, (255, 0, 0), [15, 15], [55, 55])
                        pygame.draw.aaline(sc, (255, 0, 0), [55, 15], [15, 55])
                        move = True
                    elif move_bot == 2:
                        pygame.time.delay(1000)
                        pygame.draw.aaline(sc, (255, 0, 0), [65, 15], [105, 55])
                        pygame.draw.aaline(sc, (255, 0, 0), [105, 15], [65, 55])
                        move = True
                    elif move_bot == 3:
                        pygame.time.delay(1000)
                        pygame.draw.aaline(sc, (255, 0, 0), [115, 15], [155, 55])
                        pygame.draw.aaline(sc, (255, 0, 0), [155, 15], [115, 55])
                        move = True
                    elif move_bot == 4:
                        pygame.time.delay(1000)
                        pygame.draw.aaline(sc, (255, 0, 0), [15, 65], [55, 105])
                        pygame.draw.aaline(sc, (255, 0, 0), [55, 65], [15, 105])
                        move = True
                    elif move_bot == 5:
                        pygame.time.delay(1000)
                        pygame.draw.aaline(sc, (255, 0, 0), [65, 65], [105, 105])
                        pygame.draw.aaline(sc, (255, 0, 0), [105, 65], [65, 105])
                        move = True
                    elif move_bot == 6:
                        pygame.time.delay(1000)
                        pygame.draw.aaline(sc, (255, 0, 0), [115, 65], [155, 105])
                        pygame.draw.aaline(sc, (255, 0, 0), [155, 65], [115, 105])
                        move = True
                    elif move_bot == 7:
                        pygame.time.delay(1000)
                        pygame.draw.aaline(sc, (255, 0, 0), [15, 115], [55, 155])
                        pygame.draw.aaline(sc, (255, 0, 0), [55, 115], [15, 155])
                        move = True
                    elif move_bot == 8:
                        pygame.time.delay(1000)
                        pygame.draw.aaline(sc, (255, 0, 0), [65, 115], [105, 155])
                        pygame.draw.aaline(sc, (255, 0, 0), [65, 155], [105, 115])
                        move = True
                    elif move_bot == 9:
                        pygame.time.delay(1000)
                        pygame.draw.aaline(sc, (255, 0, 0), [115, 115], [155, 155])
                        pygame.draw.aaline(sc, (255, 0, 0), [155, 115], [115, 155])
                        move = True
                if mode2:
                    if move_bot == 1:
                        pygame.time.delay(1000)
                        pygame.draw.circle(sc, (0, 0, 255), (35, 35), 20, 1)
                        move = True
                    elif move_bot == 2:
                        pygame.time.delay(1000)
                        pygame.draw.circle(sc, (0, 0, 255), (85, 35), 20, 1)
                        move = True
                    elif move_bot == 3:
                        pygame.time.delay(1000)
                        pygame.draw.circle(sc, (0, 0, 255), (135, 35), 20, 1)
                        move = True
                    elif move_bot == 4:
                        pygame.time.delay(1000)
                        pygame.draw.circle(sc, (0, 0, 255), (35, 85), 20, 1)
                        move = True
                    elif move_bot == 5:
                        pygame.time.delay(1000)
                        pygame.draw.circle(sc, (0, 0, 255), (85, 85), 20, 1)
                        move = True
                    elif move_bot == 6:
                        pygame.time.delay(1000)
                        pygame.draw.circle(sc, (0, 0, 255), (135, 85), 20, 1)
                        move = True
                    elif move_bot == 7:
                        pygame.time.delay(1000)
                        pygame.draw.circle(sc, (0, 0, 255), (35, 135), 20, 1)
                        move = True
                    elif move_bot == 8:
                        pygame.time.delay(1000)
                        pygame.draw.circle(sc, (0, 0, 255), (85, 135), 20, 1)
                        move = True
                    elif move_bot == 9:
                        pygame.time.delay(1000)
                        pygame.draw.circle(sc, (0, 0, 255), (135, 135), 20, 1)
                        move = True
                pygame.display.update()



        pygame.display.update()
        check_win()
    pygame.display.update()

sc.fill((0, 0, 0))
myfont = pygame.font.SysFont("Comic Sans MS", 28)
if user:
    label = myfont.render("User Win!", True, (255, 255, 255))
elif bot:
    label = myfont.render("Bot Win!", True, (255, 255, 255))
elif dr:
    label = myfont.render("Draw!", True, (255, 255, 255))

sc.blit(label, (10, 10))
pygame.display.update()
pygame.time.delay(1000)