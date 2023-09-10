import pygame as pg
from pygame.math import Vector2
from time import time
import scripts as cl

from random import randint

pg.init()
screen = pg.display.set_mode((1024, 750), pg.DOUBLEBUF)
pg.display.set_caption("AstroStike")

font = pg.font.Font("Assets/Fonts/Comfortaa.ttf", 20)


def debug(string: str):
    text = font.render(string, True, "#FFFFFF", "#000000")
    screen.blit(text, (0, 0))


def game():
    clock = pg.time.Clock()
    FPS = 0

    camPos = Vector2(0, 0)
    player = cl.Player(camPos + Vector2(512, 375))

    stars = [pg.Rect(x * 50, y * 50, 2, 2) for x in range(0, 21) for y in range(0, 17)]

    prevTime = time()
    while True:
        clock.tick(FPS)

        deltaTime = time() - prevTime
        prevTime = time()

        # ---Event-Handling--------------------------------------
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        # -------------------------------------------------------

        camPos = player.pos - Vector2(512, 375)
        screen.fill("#000020")

        # ---Drawing---------------------------------------------

        for obj in stars:
            pg.draw.rect(
                screen,
                "#555555",
                (obj.x - camPos.x % 50, obj.y - camPos.y % 50, obj.height, obj.width),
            )

        player.update(deltaTime)
        player.draw(screen, camPos)

        cl.BulletGroup.update(deltaTime)
        cl.BulletGroup.draw(screen, camPos)
        for i in range(6):pg.draw.circle(screen, "#09cb8a", - camPos, 9950 + i *20, 10)


        # -------------------------------------------------------

        cl.draw_gizmos(screen, camPos, player)

        debug(
            f"FPS: {round(clock.get_fps())} | ({camPos.x:.0f},{camPos.y:.0f}) | Vel: {player.vel.length():.0f} | {player.dir.angle_to(Vector2(0,-1)):.0f} | {player.targetDir.angle_to(Vector2(0,-1)):.0f} | {len(cl.ObstacleGroup)}"
        )
        pg.display.update()


if __name__ == "__main__":
    func = game
    params = ()

    while True:
        func, params = func(*params)
