import pygame
from particle import Particle

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill((0,0,0))
pygame.display.set_caption('Particles')

particles = []

mouse_down = False

def add_particles():
    mouse_pos = pygame.mouse.get_pos()

    for _ in range(10):
        particles.append(Particle(mouse_pos[0], mouse_pos[1]))

def draw_particles():
    for particle in particles:
        pygame.draw.circle(screen, particle.color, (particle.x, particle.y), particle.radius)
        particle.update()

def remove_small_particles():
    """
    remove particles when the radius is less than 0.2
    """
    for particle in particles:
        if particle.radius < 0.2:
            particles.remove(particle)

def main_loop():
    global mouse_down

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
            if event.type == pygame.QUIT:
                done = True

        screen.fill((0,0,0))

        if mouse_down:
            add_particles()

        draw_particles()
        remove_small_particles()

        pygame.display.update()

def main():
    main_loop()
    pygame.quit()
    quit()

if __name__ == '__main__': main()
