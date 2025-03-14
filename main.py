import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # delta time
    player_score = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)    

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("\nGame over!")
                print(f"Player score: {player_score}")
                sys.exit(0)
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()  
                    # update player score when asteroid is destroy          
                    player_score += 10

        screen.fill("black")

        # Render and display score
        font = pygame.font.SysFont("Times New Roman", 28)
        score_text = font.render(f'Score: {player_score}', True, ("white"))
        screen.blit(score_text, (20, 10))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        # limit the framerate to 60 FPS
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()





