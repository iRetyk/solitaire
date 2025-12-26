from classes import Card
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))




screen.blit(Card(1, 'S').get_picture(), (0, 0))
screen.blit(Card(1, 'D').get_picture(), (50, 0))
screen.blit(Card(1, 'H').get_picture(), (100, 0))
screen.blit(Card(1, 'C').get_picture(), (150, 0))
screen.blit(Card(9, 'S').get_picture(), (200, 0))
screen.blit(Card(7, 'D').get_picture(), (250, 0))
pygame.display.flip()

# Keep window alive for a moment
pygame.event.pump()
pygame.time.wait(3000)