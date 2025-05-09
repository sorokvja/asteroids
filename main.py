# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, sys
from constants import * 
from player import Player 
from asteroid import Asteroid 
from asteroidfield import AsteroidField 
from shot import Shot 

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable) 
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    print("Starting Asteroids!") 
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black") # clear the screen

        #player.update(dt) # updates player state 
        #player.draw(screen) # renders the player
        updatable.update(dt) # updates all objects' state 
        
        # add collision detection
        for asteroid in asteroids:
            if player.collision(asteroid) :
                print("Game over!")
                sys.exit()
            # add asteroid destruction
            for shot in shots:
                if shot.collision(asteroid):
                    #asteroid.kill()
                    asteroid.split()
                    shot.kill()
        
        # draw everything 
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip() # update the display 
        
        dt = clock.tick(60) / 1000 # manage the clock and calculate delta time 

if __name__ == "__main__":
    main() 
