import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Enhanced Animation")

# Define colors
WHITE = (255, 255, 255)

# Load images
image = pygame.image.load('your_image.png')
image = pygame.transform.scale(image, (100, 100))  # Resize as needed
image_rect = image.get_rect()

background = pygame.image.load('background_image.png')
background = pygame.transform.scale(background, (screen_width, screen_height))

# Set initial position and movement variables
x, y = random.randint(0, screen_width - image_rect.width), random.randint(0, screen_height - image_rect.height)
dx, dy = random.choice([-5, 5]), random.choice([-5, 5])  # Random speed in x and y direction

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Reset position on 'r' key press
                x, y = random.randint(0, screen_width - image_rect.width), random.randint(0, screen_height - image_rect.height)
                dx, dy = random.choice([-5, 5]), random.choice([-5, 5])

    # Update position
    x += dx
    y += dy

    # Boundary checking
    if x < 0 or x + image_rect.width > screen_width:
        dx = -dx
    if y < 0 or y + image_rect.height > screen_height:
        dy = -dy

    # Draw everything
    screen.blit(background, (0, 0))
    screen.blit(image, (x, y))

    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Limit frame rate to 30 FPS

pygame.quit()
sys.exit()
