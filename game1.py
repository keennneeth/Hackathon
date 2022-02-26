# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#initialize object
import pygame
pygame.init()
#create game
screen = pygame.display.set_mode((800, 600))
# Title
pygame.display.set_caption("TEST GAMe")
icon = pygame.image.load(chess.png)

running = True
# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False

    screen.fill((255, 0, 0))
    pygame.display.update()
