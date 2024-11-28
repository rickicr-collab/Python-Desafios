#tocando uma musica no python 
from playsound import playsound
playsound('sample.mp3')

#importa da bliblioteca do playsound 
#só dá playsound com a musica dentro da pasta do projetopar aque seja reproduzida 
#---------------------------------------------------------------------------
#utilizando o pygame
import pygame
pygame.mixer.init
pygame.init
pygame.mixer.music.load('sample.mp3')
pygame.mixer.music.play(loops=0,start=0.0)
pygame.event.wait()

