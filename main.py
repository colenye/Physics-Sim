import pygame as p
from sys import exit

p.init()

RESOLUTION = (800, 600)
display = p.display.set_mode(RESOLUTION)

while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            exit()
    