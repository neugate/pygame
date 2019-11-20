# ***********************************************************
# 雲が動き、鳥が十字キーで動かせるプログラム
# 
# ***********************************************************
import sys
import pygame
from pygame.locals import QUIT , Rect,  \
        KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

pygame.init()
pygame.key.set_repeat(5,5)

#画面サイズ
screenWidht = 1000
screenHeight = 600
SURFACE = pygame.display.set_mode((screenWidht,screenHeight))    

# タイトルの設定
pygame.display.set_caption("鳥が動くプログラム")

# 画像ロード
cloud = pygame.image.load("img/cloud.png")
bird = pygame.image.load("img/bird_0.png")

# 画像サイズの設定
cloudWidth = 235
cloudHeight = 150
birdWidth = 70
birdHeight = 60

def main():

    # データの初期
    # 雲の初期値
    cloud_x = 0

    # 鳥の初期値
    bird_x = 30
    bird_y = 200

    
    while True:

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # 押されているキーをチェック (単押しVer)
            elif event.type == KEYDOWN:
                if event.key == K_LEFT :
                    bird_x -= 5
                if event.key == K_RIGHT :
                    bird_x += 5
                if event.key == K_UP :
                    bird_y -= 5
                if event.key == K_DOWN :
                    bird_y += 5


        # メインプログラム
        # 画面背景カラー
        SURFACE.fill((40,128,215)) 

        # 地面の描写
        start_pos = (0,screenHeight-25)
        end_pos = (screenWidht,screenHeight-25)
        pygame.draw.line(SURFACE,(0,255,0),start_pos,end_pos,50)

        # 雲の描写
        # 画面端までいったら画像を右端からスタートする
        if cloud_x > 0 - cloudWidth:
            cloud_x -= 0.8
        else:                       
            cloud_x = screenWidht
        SURFACE.blit(cloud,(cloud_x,0))

        # 鳥の描写
        # 左右の画面端は反対側へ、上下の画面端は行き止まり
        if bird_x > screenWidht :
            bird_x = 0 - birdWidth
        if bird_x < 0 - birdWidth :
            bird_x = screenWidht
        if bird_y > screenHeight - birdHeight -25 :
            bird_y = screenHeight - birdHeight -25
        if bird_y < 0 :
            bird_y = 0
        SURFACE.blit(bird,(bird_x,bird_y))

        # 画面アップデート
        pygame.display.update()

# while end
if __name__ == '__main__':
    main()
