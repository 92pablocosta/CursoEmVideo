"""Faça um programa em Python que abra e reproduza o áudio
de um arquivo mp3. (eita)"""

import pygame

pygame.init()
pygame.mixer.music.load('something.mp3')
pygame.mixer.music.play()
