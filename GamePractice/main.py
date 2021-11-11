import pygame
import os
pygame.font.init()
pygame.mixer.init()


# Create our Main Surface
WIDTH, HEIGHT = 1200, 800  # Define Width and Height as a Tuple
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the surface
pygame.display.set_caption("Play Tag!")  # Label the window with game name

WHITE = (255, 255, 255)

# Color Pallette
GRASS_GREEN = (80, 200, 80)

# Sprite creation and dimensions
SPRITE_WIDTH = 30
SPRITE_HEIGHT = 40
DEER_SPRITE = pygame.image.load(os.path.join('deer.png'))
DEER = pygame.transform.scale(DEER_SPRITE, (SPRITE_WIDTH, SPRITE_HEIGHT))
WOLF_SPRITE = pygame.image.load(os.path.join('wolf.png'))
WOLF = pygame.transform.scale(WOLF_SPRITE, (SPRITE_WIDTH, SPRITE_HEIGHT))

# Define
FPS = 60

# User Events
CAUGHT = pygame.USEREVENT + 1

# Game Parameters
SPEED = 5

# Lives
LIVES_FONT = pygame.font.SysFont('ariel', 40)


# Define a main function that runs the game
def main():
    # Create hit boxes
    deer = pygame.Rect(300, 200, SPRITE_WIDTH, SPRITE_HEIGHT)
    wolf = pygame.Rect(900, 600, SPRITE_WIDTH, SPRITE_HEIGHT)

    clock = pygame.time.Clock()
    lives = 3
    run = True  # set run to True
    # While loop that runs the game
    while lives > 0:  # Game Loop
        clock.tick(FPS)

        for event in pygame.event.get():  # Checks for EVENTS
            if event.type == pygame.QUIT:  # if close clicked
                lives = 0  # change run to False to break loop

            if event.type == CAUGHT:
                # run = False
                print('GOTCHA')
                lives = lives - 1
                deer.x = 200
                deer.y = 400
                wolf.x = 800
                wolf.y = 600

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and deer.x - SPEED > 0:  # Deer Left
            deer.x -= SPEED # SPEED=5 which will move the sprite on x-axis
        if keys_pressed[pygame.K_d] and deer.x + SPEED + SPRITE_WIDTH < 1200:  # Deer Right
            deer.x += SPEED
        if keys_pressed[pygame.K_w] and deer.y - SPEED > 0:  # Deer Up
            deer.y -= SPEED
        if keys_pressed[pygame.K_s] and deer.y + SPEED + SPRITE_HEIGHT < 800:  # Deer Down
            deer.y += SPEED

        if keys_pressed[pygame.K_LEFT] and wolf.x - SPEED > 0:  # Wolf Left
            wolf.x -= SPEED
        if keys_pressed[pygame.K_RIGHT] and wolf.x + SPEED + SPRITE_WIDTH < 1200:  # Wolf Right
            wolf.x += SPEED
        if keys_pressed[pygame.K_UP] and wolf.y - SPEED > 0:  # Wolf Up
            wolf.y -= SPEED
        if keys_pressed[pygame.K_DOWN] and wolf.y + SPEED + SPRITE_HEIGHT < 800:  # Wolf Down
            wolf.y += SPEED

        draw_window(deer, wolf, lives)  # This function draws the screen
        deer_tagged(deer, wolf)  # Check if tagged


    pygame.quit()  # will close game

# Draw Window Function
def draw_window(deer, wolf, lives):
    WIN.fill(GRASS_GREEN)  # Draw the Grass
    WIN.blit(DEER, (deer.x, deer.y))  # Sprites at a location
    WIN.blit(WOLF, (wolf.x, wolf.y))  # Sprites at a location
    lives_text = LIVES_FONT.render(
        "Lives: " + str(lives), 1, WHITE)
    WIN.blit(lives_text, ((WIDTH/2 - lives_text.get_width()/2), 10))
    pygame.display.update()  # Update the screen


# Create a function to determine if tagged
def deer_tagged(deer, wolf, ):
    if deer.colliderect(wolf):
        pygame.event.post(pygame.event.Event(CAUGHT)) # posting a custom event to the event queue


if __name__ == "__main__":
    main()
