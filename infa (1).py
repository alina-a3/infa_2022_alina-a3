#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[1]:


import pygame
import time
import random

pygame.init() #открыть окно

white = (255, 255, 255) #цвета в игре
darkred = (139, 0, 0)
black = (0, 0, 0)
deepsky = (75, 0, 130)
plum = (221, 160, 221)
xyi = (255, 255, 254)

dis_w = 600 #размер поля
dis_h = 400

dis = pygame.display.set_mode((dis_w, dis_h)) #вывод экрана
pygame.display.set_caption('ЗМЕЙКА') #заголовок

clock = pygame.time.Clock() #использование библиотеки времни

snake_size = 10
snake_speed = 8

snake1_size = 10
snake1_speed = 8

font_style = pygame.font.SysFont("times new roman", 23) #шрифты для слов
score_font = pygame.font.SysFont("calibri", 35)


def Your_score(score): #функция счета баллов
    value = score_font.render("Счет: " + str(score), True, darkred) #встроенный счетчик
    dis.blit(value, [150, 0]) #вывод счета
    
def Your_score1(score): #функция счета баллов
    value = score_font.render("Счет: " + str(score), True, darkred) #встроенный счетчик
    dis.blit(value, [300, 0]) #вывод счета



def our_snake(snake_size, snake_list): #функция роста змейка
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_size, snake_size]) #проход по каждому элементу массива-доп квадрат змеи

def our_snake1(snake_size, snake_list): #функция роста змейка
    for x in snake_list:
        pygame.draw.rect(dis, xyi, [x[0], x[1], snake_size, snake_size]) #проход по каждому элементу массива-доп квадрат змеи


def message(msg, color): #функция вывода надписи на экран и ее располнжение
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_w / 8, dis_h/ 3])


def game3aLoopa(): #функция начать сначала
    game_over = False
    game_close = False

    x1 = dis_w / 3 #начальное положение точки
    y1 = dis_h / 2

    x1_change = 0 #переменные для задачи изменения положения
    y1_change = 0

    snake_List = [] #начальная длина змеи, нулевой элемент массива
    Length_of_snake = 1
    
    x2 = 2 * dis_w / 3 #начальное положение точки
    y2 = dis_h / 2

    x2_change = 0 #переменные для задачи изменения положения
    y2_change = 0

    snake1_List = [] #начальная длина змеи, нулевой элемент массива
    Length_of_snake1 = 1

    foodx = round(random.randrange(0, dis_w - snake_size) / 10.0) * 10.0 #рандомно задается положение еды в начале
    foody = round(random.randrange(45, dis_h - snake_size) / 10.0) * 10.0

    while not game_over: #продолжаем игру

        while game_close == True: #когда проиграли
            dis.fill(plum)
            pygame.draw.rect(dis, white, [0, 0, 600, 45]) #рамка
            message("Проигрыш!Нажмите C-играть снова или Q-выйти", black)
            Your_score(Length_of_snake - 1) #присвоить значение счету
            Your_score1(Length_of_snake1 - 1) #присвоить значение счету
            pygame.display.update() #обновление экрана-выведен счет

            for event in pygame.event.get(): #тип события клавиатуры
                if event.type == pygame.KEYDOWN: #нажатие кнопки
                    if event.key == pygame.K_q: #закрытие экрана если нажали q
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c: #повторение игры если нажали с
                        game3aLoopa()

        for event in pygame.event.get(): #событие нажатие кнопки
            if event.type == pygame.QUIT: #можем выйти из игры в процессе
                game_over = True
            if event.type == pygame.KEYDOWN: #нажатие одной из стрелок задает изменение положения, 4 варианта перемещения
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0
                elif event.key == pygame.K_a:
                    x2_change = -snake1_size
                    y2_change = 0
                elif event.key == pygame.K_d:
                    x2_change = snake1_size
                    y2_change = 0
                elif event.key == pygame.K_w:
                    y2_change = -snake1_size
                    x2_change = 0
                elif event.key == pygame.K_s:
                    y2_change = snake1_size
                    x2_change = 0

        if x1 >= dis_w or x1 < 0 or y1 >= dis_h or y1 < 45: # условия выхода змеи с поля - проигрыш
            game_close = True
        if x2 >= dis_w or x2 < 0 or y2 >= dis_h or y2 < 45: # условия выхода змеи с поля - проигрыш
            game_close = True
        x1 += x1_change #координатам змеи присваивается новое положение
        y1 += y1_change
        x2 += x2_change #координатам змеи присваивается новое положение
        y2 += y2_change
        dis.fill(plum) #цвет экрана
        pygame.draw.rect(dis, white, [0, 0, 600, 45]) #рамка
        pygame.draw.rect(dis, deepsky, [foodx, foody, snake_size, snake_size]) #нарисовать еду по заданным координатам и размеру
        snake_Head = [] #координаты головы в массив
        snake_Head.append(x1) #внести в массив координаты
        snake_Head.append(y1)
        snake_List.append(snake_Head) #в массив длины змейки вводим эти координаты
       
        snake1_Head = [] #координаты головы в массив
        snake1_Head.append(x2) #внести в массив координаты
        snake1_Head.append(y2)
        snake1_List.append(snake1_Head) #в массив длины змейки вводим эти координаты
        
        if snake_Head == snake1_Head:
            game_close = True

        if len(snake_List) > Length_of_snake:
            del snake_List[0] #удаляем нулевой элемент, далее при его вызозве получаем следующий
            
        if len(snake1_List) > Length_of_snake1:
            del snake1_List[0] #удаляем нулевой элемент, далее при его вызозве получаем следующий

        for x in snake_List[:-1]: #пробегает массив кроме последнего элемента
            if x == snake_Head:
                game_close = True
            if x == snake1_Head:
                game_close = True
        for x in snake1_List[:-1]: #пробегает массив кроме последнего элемента
            if x == snake1_Head:
                game_close = True
            if x == snake_Head:
                game_close = True

        our_snake(snake_size, snake_List)
        our_snake1(snake1_size, snake1_List)
        Your_score(Length_of_snake - 1) #итоговый счет про формуле
        Your_score1(Length_of_snake1 - 1) #итоговый счет про формуле

        pygame.display.update() #обновление экрана

        if x1 == foodx and y1 == foody: #совпадение змеи и еды
            foodx = round(random.randrange(0, dis_w - snake_size) / 10.0) * 10.0 #новые координаты еды
            foody = round(random.randrange(45, dis_h - snake_size) / 10.0) * 10.0
            Length_of_snake += 1
        if x2 == foodx and y2 == foody: #совпадение змеи и еды
            foodx = round(random.randrange(0, dis_w - snake1_size) / 10.0) * 10.0 #новые координаты еды
            foody = round(random.randrange(45, dis_h - snake1_size) / 10.0) * 10.0
            Length_of_snake1 += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()


game3aLoopa()


# In[ ]:




