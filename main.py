import pygame
from models import Square

#初始化
pygame.init()

clock = pygame.time.Clock()#游戏主时钟

#定义窗口
width, height = 400,400
screen = pygame.display.set_mode((width,height))

square = Square(40)



while True: #主循环
    screen.fill((255,255,255))
    screen.blit(square.surface,square.rect)

    #检测按键事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#退出事件
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                square.direction('left')
            
            if event.key == pygame.K_RIGHT:
                square.direction('right')
            
            if event.key == pygame.KEYUP:
                square.direction('up')

            if event.key == pygame.KEYDOWN:
                square.direction('down')

    pygame.display.flip()#刷新屏幕
    clock.tick(60)#帧率