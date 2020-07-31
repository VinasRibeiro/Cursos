#Faça um programa em Python que abra e repuduza um áudio de um arquivo em mp3
import pygame
'''Esta biblioteca é usado em jogos e possui varias funções
mas para usar o pygame vc deve inicia-lo primeiro usando a função pygame.init() como descrito abaixo'''
pygame.mixer.init()
#Esta função carrega o arquivo de mp3 para a memória
pygame.mixer.music.load('ex021.mp3')
#Esta função aciona ou da um play na musica
pygame.mixer.music.play()


