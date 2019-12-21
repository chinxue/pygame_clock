import pygame
import os
from pygame import *
import math
import datetime
from datetime import datetime
pygame.init()
screen=display.set_mode((600,300))
font1=font.Font(None,20)
pos_x=300
pos_y=150
while True:
    screen.fill((0,0,0))
    if event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==pygame.K_a:
                print(1)       
    draw.circle(screen,(255,255,255),(pos_x,pos_y),70,2)
    for n in range(1,13):
        ang=math.radians(n*30-90)
        x=math.cos(ang)*60+pos_x-4
        y=math.sin(ang)*60+pos_y-5
        font_img=font1.render(str(n),True,(255,255,255))
        screen.blit(font_img,(x,y))
    h=datetime.today().hour%12
    m=datetime.today().minute
    s=datetime.today().second
    
    h_x=math.cos(math.radians(h*30-90))*40+pos_x-20
    h_y=math.sin(math.radians(h*30-90))*40+pos_y-20
    
    m_x=math.cos(math.radians(m*6-90))*50+pos_x-10
    m_y=math.sin(math.radians(m*6-90))*50+pos_y-10
    
    s_x=math.cos(math.radians(s*6-90))*60+pos_x
    s_y=math.sin(math.radians(s*6-90))*60+pos_y
    
    draw.aaline(screen,(255,255,255),(pos_x,pos_y),(h_x,h_y),20)
    draw.aaline(screen,(255,255,255),(pos_x,pos_y),(m_x,m_y),15)
    draw.aaline(screen,(255,255,0),(pos_x,pos_y),(s_x,s_y),5)
    display.update()

