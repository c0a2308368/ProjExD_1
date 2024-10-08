import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kk_rct = kk_img.get_rect() #練習8‐1 
    kk_rct.center = 300,200 #練習8‐1 初期座標


    tmr = 0
    while True:
        dy = 0
        dz = 0
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed() #練習8-3
        if key_lst[pg.K_UP]:
            dz += -1
        if key_lst[pg.K_DOWN]: 
            dz += 1
        if key_lst[pg.K_RIGHT]:
            dy += 2
        if key_lst[pg.K_LEFT]:
            dy += -1
        dy -= 1
        kk_rct.move_ip((dy,dz))
           
        x = -(tmr%3200)
        screen.blit(bg_img, [x,0])
        screen.blit(bg_img2, [x+1600,0])
        screen.blit(bg_img, [x+3200,0])
        screen.blit(bg_img2, [x+4800,0])
        screen.blit(kk_img,kk_rct) #練習４
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習５


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()