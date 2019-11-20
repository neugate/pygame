# ***********************************************************
# 雲とビルが動き、鳥が十字キーで動かせるプログラム
# 鳥がパタパタ羽ばたき同時押しに対応したプログラム
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
pygame.display.set_caption("鳥が動くプログラムver2")

# 画像ロード
cloud = pygame.image.load("img/cloud.png")
chicken = [pygame.image.load("img/bird_0.png"), \
    pygame.image.load("img/bird_1.png"), \
    pygame.image.load("img/bird_2.png"), \
    pygame.image.load("img/bird_3.png")]

building = [pygame.image.load("img/building1.png"), \
    pygame.image.load("img/building2.png"), \
    pygame.image.load("img/building3.png")]

buildingwidht = [95,42,45]
buildingheight = [200,210,84]

# 画像サイズの設定
cloudWidth = 235
cloudHeight = 150
birdWidth = 70
birdHeight = 60

class buildings():

    # 引数1：使用するビルの画像0～2　
    # 引数2：ビルの移動速度 
    def __init__(self,num,speed):
        self.number = num
        self.moveSpeed = speed
        self.pic = building[num]
        self.builX = screenWidht - ((num + 1) * 500)
        self.builY = screenHeight - buildingheight[num] - 40

    def buildingMoves(self):
        self.builX -= self.moveSpeed
        if self.builX <= (0 - buildingwidht[self.number]):
            self.builX = screenWidht


def main():

    # データの初期値
    # 雲の初期値
    cloud_x = 0

    # ビルの初期化
    building_0 = buildings(0,0.5)
    building_1 = buildings(1,0.5)
    building_2 = buildings(2,0.5)

    # 鳥の初期値
    bird_x = 30
    bird_y = 200
    chickenimg = 0
    chickenimgCount = 0
    
    while True:

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 押されているキーをチェック (同時押しVer)
        pressed_keys = pygame.key.get_pressed()

        # 押されているキーに応じて画像を移動
        if pressed_keys[K_LEFT]:
            bird_x -= 5
        if pressed_keys[K_RIGHT]:
            bird_x += 5
        if pressed_keys[K_UP]:
            bird_y -= 5
        if pressed_keys[K_DOWN]:
            bird_y += 5

        # メインプログラム
        # 画面背景カラー
        SURFACE.fill((40,128,215)) 

        # 地面の描写
        start_pos = (0,screenHeight-25)
        end_pos = (screenWidht,screenHeight-25)
        pygame.draw.line(SURFACE,(0,255,0),start_pos,end_pos,50)

        # 雲の描写
        # 画面端までいったら画像を左端からスタートする
        if cloud_x > 0 - cloudWidth:
            cloud_x -= 0.8
        else:                       
            cloud_x = screenWidht
        SURFACE.blit(cloud,(cloud_x,0))

        # ビルの描写
        building_0.buildingMoves()
        SURFACE.blit(building_0.pic, \
            (building_0.builX,building_0.builY))

        building_1.buildingMoves()
        SURFACE.blit(building_1.pic, \
            (building_1.builX,building_1.builY))

        building_2.buildingMoves()
        SURFACE.blit(building_2.pic, \
            (building_2.builX,building_2.builY))


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
        
        if chickenimgCount == 20:
            chickenimg = (chickenimg + 1 )% 4
            chickenimgCount = 0
        else:
            chickenimgCount += 1

        SURFACE.blit(chicken[chickenimg],(bird_x,bird_y))


        # 画面アップデート
        pygame.display.update()

# while end
if __name__ == '__main__':
    main()