import pygame

pygame.mixer.init() # inicia o mixer pygame
pygame.init() # inicia o pygame
pygame.mixer.music.load('darude.mp3') # guarda a musica a ser tocada
pygame.mixer.music.play() # inicia a música
pygame.event.wait() # espera a música acabar para encerrar o programa
