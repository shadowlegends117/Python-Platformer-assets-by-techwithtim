import pygame
from os.path import join

def get_background(name, width, height):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, img_width, img_height = image.get_rect()
    tiles = []

    for i in range(width // img_width + 1):
        for j in range(height // img_height + 1):
            pos = (i * img_width, j * img_height)
            tiles.append(pos)

    return tiles, image

def get_block(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)
