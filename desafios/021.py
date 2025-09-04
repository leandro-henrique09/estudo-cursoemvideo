# minha versao, não foi um mp3 mas aprendi como colocar sons do windows 
# import winsound

# winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)

# versão do video

import pygame
pygame.init()
pygame.mixer.music.load('introraul.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
