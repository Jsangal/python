print("Hola")
import sys
sys.path.append('./')

def factorial(num):
    if (num <= 2):
        return num * 1
    else:
        return num * factorial(num-1)

b = int(input())
print(factorial(b))

def tabla(a):
    for i in range(1,11):
        print(a, " por ", i, "=", a*i)

a = int(input())

print(tabla(a))

##ae

import pygame

pygame.init()
size = (800,500)
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(30, 10, 200)
    pygame.display.flip()    
