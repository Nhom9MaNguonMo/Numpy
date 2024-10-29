import pygame, sys
from pygame.locals import *
import random
chieu_dai = 800 # Chiều dài cửa sổ
chieu_rong = 500 # Chiều cao cửa sổ
pygame.init()  # Khởi tạo game
w = pygame.display.set_mode((chieu_dai, chieu_rong))# Tạo 1 cửa sổ game tên là w
pygame.display.set_caption('Tiêu đề của game')
# khởi tạo giá trị ban đầu của các biến vào đây!
#------------- tạo nền của game là 1 ảnh -----------------
anh_nen = pygame.image.load('game/h2.jpg')
anh_nen = pygame.transform.scale(anh_nen, (chieu_dai, chieu_rong))
#------------ tạo ảnh các quả táo, cam, oài ------------
'''tao = pygame.image.load('tao.png')
tao = pygame.transform.scale(tao, (60, 70))
cam = pygame.image.load('cam.png')
cam = pygame.transform.scale(cam, (60, 70))
xoai = pygame.image.load('xoai.png')
xoai = pygame.transform.scale(xoai, (60, 70))
# ------------- Tạo vị trí ban đầu----------
x_tao = 100
y_tao = 0
x_cam = 200
y_cam = 0
x_xoai = 300
y_xoai =0'''
#----------- tạo ảnh con chim--------------
chim1 = pygame.image.load('game/chimbe.jpg')
chim1 = pygame.transform.scale(chim1, (80, 70))
chim2 = pygame.image.load('game/chimto.jpg')
chim2 = pygame.transform.scale(chim2, (80, 70))
nui = pygame.image.load('game/h2.jpg')
nui = pygame.transform.scale(nui, (250, 250))
#---------- tạo vị trí ban đầu--------------
x1 = 0
y1 = 200
x2 = chieu_dai
y2 = 50
#---------- Khoi tao khung thoi gian--------------
FPS = 60
fpsClock = pygame.time.Clock()
while True: # tạo vòng lặp game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                y1 = y1-5
            if event.key == K_DOWN:
                y1 = y1 + 5
        

    # -----vẽ ảnh nền ----------------
    w.blit(anh_nen,(0,0))
    w.blit(nui,(300,200))
    w.blit(chim1,(x1,y1))
    w.blit(chim2,(x2,y2))
    x1 = x1 + 1
    x2 = x2 - 5
    if x1 >= 350 and x1 < 400 and y1 >=160 :
        x1 = 350
        y1 = y1+5
    if x1 > chieu_dai:
        x1 = 0
    if x2 < 0:
        x2 = chieu_dai
    '''w.blit(tao,(x_tao,y_tao))
    w.blit(cam,(x_cam,y_cam))
    w.blit(xoai,(x_xoai,y_xoai))
    y_tao = y_tao + 1
    y_cam  = y_cam + 10
    y_xoai = y_xoai + 30
    if y_tao > chieu_rong:
        y_tao = 0
    if y_cam > chieu_rong:
        y_cam = 0
    if y_xoai > chieu_rong:
        y_xoai = 0'''
    # Điền các thao tác game vào đây!
    pygame.display.update()
    fpsClock.tick(FPS)
'''Bài tập :
    1) tìm hoặc vẽ 2 con chim. Viết chương trinh cho 1 con chim bay từ trái qua phải, 1 con bay từ phải qua trái màn hình
    2) Tìm hoặc vẽ 2 ô tô, cho 2 ô tô chuyển động với vận tốc khác nhau
    3) vẽ 10 hình tròn với 10 màu khác nhau chuyển động từ trên xuống dưới màn hình với 10 tốc độ khác nhau'''
