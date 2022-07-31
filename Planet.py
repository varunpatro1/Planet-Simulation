import math
import pygame

pygame.init()

W, H = 800, 800
FONT = pygame.font.SysFont("calibri", 18)

class Planet:
    G = 6.67428e-11
    AU = 149.6e6 * 1000
    SCALE = 250 / AU
    T_REF = 3600*24 # seeing one day at a time

    def __init__(self,x,y,mass,radius,color, name, tang_vel):
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = radius
        self.color = color
        self.name = name

        self.xvel = 0
        self.yvel = tang_vel

        self.is_Sun = False
        self.distance_to_sun = 0
        self.orbit_path = []

    def __str__(self):
        return 'Name: ' + self.name + ',(x,y): (' + self.x + ',' + self.y + '), ' \
            'radius: ' + self.radius + ', mass: ' + self.mass

    def draw(self, window):
        # draw a circle at prescribed coordinates
        x = self.x * self.SCALE + (W/2)
        y = self.y * self.SCALE + (H/2)

        
        if len(self.orbit_path) > 2:
            scaled_points_for_draw = []
            for point in self.orbit_path:
                x,y = point
                x = x * self.SCALE + (W/2)
                y = y * self.SCALE + (H/2)
                scaled_points_for_draw.append((x,y))

            pygame.draw.lines(window, self.color, False, scaled_points_for_draw, 4)
        
        pygame.draw.circle(window, self.color, (x,y), self.radius)

        if not self.is_Sun:
                name_text = FONT.render(f"{self.name}", 1, (255, 255, 255))
                window.blit(name_text, (x-name_text.get_width(), y + (1.25*name_text.get_height())))
                #distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, (255, 255, 255))
                #window.blit(distance_text, (x - distance_text.get_width(), y - distance_text.get_height()))

    def g_force_decomposition(self, other):

        distance_x = other.x - self.x; distance_y = other.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.is_Sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y
        

    def sum_g_force(self, planets):

    
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            pair_fx, pair_fy = self.g_force_decomposition(planet)
            total_fx += pair_fx
            total_fy += pair_fy
        
        return [total_fx, total_fy]

    def calculate_path(self, planets):

        acceleration_x = self.sum_g_force(planets)[0] / self.mass
        acceleration_y = self.sum_g_force(planets)[1] / self.mass

        self.xvel += acceleration_x * self.T_REF
        self.yvel += acceleration_y * self.T_REF

        self.x += self.xvel * self.T_REF
        self.y += self.yvel * self.T_REF

        self.orbit_path.append((self.x, self.y))