from __future__ import annotations
import pygame as p
from sys import exit

p.init()

class Floor:
    def __init__(self) -> None:
        self.rect = p.Rect(0, RESOLUTION[1] * 0.8, RESOLUTION[0], RESOLUTION[1] * 0.2)
    def update(self):
        p.draw.rect(display, p.Color(0, 0, 0), self.rect)

class Ball:
    def __init__(self, radius=50, x=50, y=50) -> None:
        self.x = 5
        self.rect = p.Rect(x, y, 50, 50)
        self.radius = radius
        self.gravity = GRAVITY
    
    def update(self):
        self.rect.y += self.gravity
        self.gravity += 0.01
RESOLUTION = (800, 600)
GRAVITY = 0.1
balls = []
display = p.display.set_mode(RESOLUTION)

floor = Floor()

while True:
    for event in p.event.get():
        if event.type == p.MOUSEBUTTONDOWN:
            mouse_pos = p.mouse.get_pos()
            balls.append(Ball(50, mouse_pos[0], mouse_pos[1]))
        if event.type == p.QUIT:
            p.quit()
            exit()
    display.fill(p.Color(255, 255, 255))
    floor.update()
    for ball in balls:
        p.draw.circle(display, p.Color(255, 0, 0), (ball.rect.x, ball.rect.y), ball.radius)
        if p.Rect.colliderect(ball.rect, floor.rect):
            ball.gravity = -(ball.gravity * 0.5)
        ball.update()
    
    p.display.update()
    