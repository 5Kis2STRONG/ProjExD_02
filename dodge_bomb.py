import pygame as pg
import sys
import random as rd

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    bomb_img = pg.Surface((20, 20))
    pg.draw.circle(bomb_img, (255, 0, 0), (10, 10), 10)
    bomb_img.set_colorkey((0,0,0))
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    key_lst = pg.key.get_pressed()
    if key_lst[pg.K_UP]:
        kk_img.move_ip((0, -1))
    bomb_X = rd.randint(0, 1600)
    bomb_Y = rd.randint(0, 900)
    tmr = 0
    vx = 0
    vy = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        vx += 1
        vy += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(bomb_img, [bomb_X + vx, bomb_Y + vy])
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()