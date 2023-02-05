import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("My Game")

# Set the background color
bg_color = (0, 0, 0)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update the game state
    
    # Draw the screen
    screen.fill(bg_color)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
