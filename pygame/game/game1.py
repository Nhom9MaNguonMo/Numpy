# ăn táo bằng cách bấm chuột vào quả táo. khi ăn 1 quả táo được 5 điểm
import pygame, sys
from pygame.locals import *
import random
import time   # gọi thư viện thời gian
from score import score
WINDOWWIDTH = 800 # Chiều dài cửa sổ
WINDOWHEIGHT = 500 # Chiều cao cửa sổ
pygame.init()
w = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
ytao = 0
ycam = 0
yxoai = 0
y_b = 0
xtao=450
xcam=250
xxoai=350

#pygame.display.set_caption('Hinh  chuyen dong')
#oto = pygame.image.load('car.png') # đọc 1 file ảnh vào chương trình

BG = pygame.image.load('game/h1.jpg')
BG = pygame.transform.scale(BG, (WINDOWWIDTH, WINDOWHEIGHT))
#w.blit(BG,(0,0))
tao = pygame.image.load('game/h5.jpg')
tao = pygame.transform.scale(tao, (40, 50))
cam = pygame.image.load('game/h3.jpg')
xoai = pygame.image.load('game/h4.jpg')
cam = pygame.transform.scale(cam, (40, 50))
xoai = pygame.transform.scale(xoai, (40, 50))
width_img = BG.get_width()
FPS = 20
fpsClock = pygame.time.Clock()
clock = pygame.time.Clock()
diem = 0
round_around=False
time0 = time.time()
timestart=6000
toc_do = 1
scoretotal=score(1,0)



while True:
    if diem-scoretotal.diemmoc>=200:
        scoretotal.diemmoc=diem
        scoretotal.lv+=1
    for event in pygame.event.get():
        if event.type == QUIT :
            
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and round_around==False:  # sự kiện bấm chuột
            if event.pos[0]>410 and event.pos[0]<490 and event.pos[1]>ytao-50 and event.pos[1]<ytao+50:
            # event.pos[0] =x  và event.pos[1] =y   
                diem = diem +5
                ytao = 0
            if event.pos[0]>250 and event.pos[0]<300 and event.pos[1]>ycam-50 and event.pos[1]<ycam+50:
            # event.pos[0] =x  và event.pos[1] =y   
                diem = diem +10
                ycam = 0
            if event.pos[0]>350 and event.pos[0]<400 and event.pos[1]>yxoai-50 and event.pos[1]<yxoai+50:
            # event.pos[0] =x  và event.pos[1] =y   
                diem = diem +20
                yxoai = 0
        if event.type ==pygame.KEYDOWN and round_around==False:
            if event.key == K_UP:
                toc_do = toc_do +5

               
    w.blit(BG,(0,y_b))
    w.blit(tao, (xtao,ytao)) 
    w.blit(cam, (xcam,ycam))
    w.blit(xoai, (xxoai,yxoai))
    ytao = ytao+ toc_do*scoretotal.lv
    ycam = ycam+2*scoretotal.lv
    yxoai = yxoai+4*scoretotal.lv
    #if y_b < - WINDOWHEIGHT:
    #   y_b += WINDOWHEIGHT
    if ytao  > WINDOWHEIGHT:
        ytao =0
        toc_do  =1
        
    if ycam  > WINDOWHEIGHT:
        ycam =0
    if yxoai  > WINDOWHEIGHT:
        yxoai =-0
    
    time1 = time.time()
    if round_around==False:
        timestart=timestart-int(time1-time0)
    else:
        timestart=0
    #print(time)
    font = pygame.font.SysFont('Arial', 30)
    text = font.render('Tong diem: {} '.format(diem), True, (255, 0, 0)) # in ra màn hình tổng điểm
    text1 = font.render('Thoi gian: {} '.format(timestart/100), True, (255, 0, 0)) # in ra màn hình thời gian chơi
    text = font.render('Tong diem: {} '.format(diem), True, (255, 0, 0))
    text2 = font.render('Level: {} '.format(scoretotal.lv), True, (255, 0, 0))
    text3 = font.render('Het gio! Tong diem: {} '.format(diem), True, (255, 0, 0))
    w.blit(text, (50, 50))
    w.blit(text1, (50, 80))
    w.blit(text2, (50, 120))
    if(timestart<=0):
        timestart=0
        round_around=True

        w.blit(text3,(360,150))
    pygame.display.update() # vẽ lại hình trong vòng lặp
    fpsClock.tick(FPS)