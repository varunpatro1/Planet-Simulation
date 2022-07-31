# INPSIRED BY TECH WITH TIM
import pygame
from Planet import *

pygame.init()

# Dimensions of pygame window
W, H = 800, 800
SOLAR_SYSTEM = pygame.display.set_mode((W,H))
pygame.display.set_caption('PLANETARY SIMULATION')

FONT = pygame.font.SysFont("calibri", 18)

MASS_OF_MOON = 7.43* 10 ** 22

# Colors for denoting planets
YELLOW = (255, 255, 0)
ORANGE = (255, 150, 125)
BLUE = (0, 255, 240)
RED = (255, 75, 75)
GREY = (180, 80, 80)

COLORS = [YELLOW, GREY, ORANGE, BLUE, RED]
X_DIST_INIT = [0, -0.387, 0.723, -1, -1.524]
Y_DIST_INIT = [0, 0, 0, 0, 0]
MASS_INIT = [1.98892 * 10**30, 3.30 * 10**23, 4.8685 * 10**24, 5.9742 * 10**24, 6.39 * 10**23]
RADIUS_INIT = [30, 8, 14, 16, 12]
NAMES = ['SUN', 'MERCURY', 'VENUS', 'EARTH', 'MARS']
# giving planets an initial velocity
TANG_VEL_INIT = [0, 47400, 35020, 29783, 24077]

def main():
    run = True
    clock = pygame.time.Clock()

    planet_list = []

    # Initializing all planets (including sun)
    # order will be sun, mercury, venus, earth, mars
    for i in range(5):
        planet = Planet(X_DIST_INIT[i] * Planet.AU, Y_DIST_INIT[i], MASS_INIT[i], RADIUS_INIT[i], COLORS[i], NAMES[i], TANG_VEL_INIT[i])
        planet_list.append(planet)

    sun = planet_list[0] #mercury = planet_list[1]; venus = planet_list[2]; earth = planet_list[3]; mars = planet_list[4]
    sun.is_sun = True

    while run:
        clock.tick(40)
        SOLAR_SYSTEM.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planet_list:
            planet.calculate_path(planet_list)
            planet.draw(SOLAR_SYSTEM)

        pygame.display.update()

    pygame.quit()
    

main()





