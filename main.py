import pygame
from pygame.constants import QUIT

pygame.init()

HEIGHT = 800 
WIDTH = 1200
COLOT_WHITE = (255, 255, 255)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill(COLOT_WHITE)
player_rect = player.get_rect()
player_speed = [1, 1]


playing = True

while playing:
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
    
    main_display.blit(player, player_rect)

    pygame.display.flip()