import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play(1)
pygame.event.wait()
