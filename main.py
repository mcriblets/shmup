import pygame
from constants import *
from player import *
from enemy import *

def main():
    print("Let's get started!")
    pygame.init()
    pygame.mixer.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("The Wheel of Fate is turning...")
    clock = pygame.time.Clock()
    
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    bullets = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    for i in range(8):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    
    alive = True
    
    while alive:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Your fate ends here...")
                return
            
        all_sprites.update()
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        
        hits = pygame.sprite.spritecollide(player, mobs, False)
        if hits:
            print("Your fate ends here...")
            alive = False
        
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()
    
if __name__ == "__main__":
    main()