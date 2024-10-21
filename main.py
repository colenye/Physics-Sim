from __future__ import annotations
import pygame as p
from sys import exit

p.init()
class Ball:
    def __init__(self, radius=50, x=50, y=50) -> None:
        self.x = 5
        self.rect = p.Rect(x, y, 50, 50)
        self.radius = radius
        self.gravity = GRAVITY
    
    def update(self):
        self.rect.y += self.gravity
RESOLUTION = (800, 600)
GRAVITY = 1
balls = []
display = p.display.set_mode(RESOLUTION)



while True:
    for event in p.event.get():
        if event.type == p.MOUSEBUTTONDOWN:
            mouse_pos = p.mouse.get_pos()
            balls.append(Ball(50, mouse_pos[0], mouse_pos[1]))
        if event.type == p.QUIT:
            p.quit()
            exit()
    print(balls)
    display.fill(p.Color(255, 255, 255))
    for ball in balls:
        p.draw.circle(display, p.Color(255, 0, 0), (ball.rect.x, ball.rect.y), ball.radius)
        ball.update()
    
    p.display.update()
    