import sys
import time
import pygame
from pygame.locals import *

def play_ball():
    
    pygame.init()
    
    #���ڴ�С
    window_size = (width, height) =(800, 600)
    
    #С������ƫ����[ˮƽ����ֱ]��ֵԽ���ƶ�Խ��
    a=1
    b=i=1
    
    speed = [a, b]
    
    
    #���ڱ���ɫRGBֵ
    color_black = (0, 255, 0)
    
    #���ô���ģʽ
    screen = pygame.display.set_mode(window_size)
    
    #���ô��ڱ���
    pygame.display.set_caption('�˶���С��')
    
    #����С��ͼƬ
    
    ball_image = pygame.image.load('ball.jpg')
    ball_image1 = pygame.image.load('fly0.png')
    
    #��ȡС��ͼƬ������״
    ball_rect = ball_image.get_rect()
    ball_rect = ball_image1.get_rect()
    screen.blit(ball_image1, ball_rect)

    
    
    while True:
        
        #�˳��¼�����
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        #ʹС���ƶ����ٶ���speed��������
        ball_rect = ball_rect.move(speed)
        
        #��С���˶�������ʱ����������ƫ����
        if (ball_rect.left < 0) or (ball_rect.right > width or ball_rect.top < 0) or (ball_rect.bottom > height):
            speed[0] =0
            speed[1] =0
        
            
        
        #��䴰�ڱ���
        screen.fill(color_black)
        
        #�ڱ���Surface�ϻ��� С��
        screen.blit(ball_image, ball_rect)
        
        
        #���´�������
        pygame.display.update()
        
if __name__ == '__main__':
    
    play_ball()
   
    
