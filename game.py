import pygame as p
import random as r

# Initialize Pygame
p.init()
screen = p.display.set_mode((800, 600))
movement_speed = 5
font_size = 70
font = p.font.SysFont("timesnewroman", font_size)

# Sprite class
class sprite(p.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = p.Surface((width, height))
        self.image.fill(p.Color("cyan"))
        p.draw.rect(self.image, color, p.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, x, y):
        self.rect.x = max(min(self.rect.x + x, screen.get_width() - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y, screen.get_height() - self.rect.height), 0)

# Create sprites
p.display.set_caption("Sprite collision")
sprites = p.sprite.Group()

sp1 = sprite(p.Color("blue"), 50, 50)
sp1.rect.x, sp1.rect.y = r.randint(0, screen.get_width() - sp1.rect.width), r.randint(0, screen.get_height() - sp1.rect.height)
sprites.add(sp1)

sp2 = sprite(p.Color("red"), 50, 50)
sp2.rect.x, sp2.rect.y = r.randint(0, screen.get_width() - sp2.rect.width), r.randint(0, screen.get_height() - sp2.rect.height)
sprites.add(sp2)

# Main loop
running = True
won = False
clock = p.time.Clock()

while running:
    for event in p.event.get():
        if event.type == p.QUIT or (event.type == p.KEYDOWN and event.key == p.K_ESCAPE):
            running = False

    if not won:
        keys = p.key.get_pressed()
        x_change = (keys[p.K_RIGHT] - keys[p.K_LEFT]) * movement_speed
        y_change = (keys[p.K_DOWN] - keys[p.K_UP]) * movement_speed
        sp1.move(x_change, y_change)

        if sp1.rect.colliderect(sp2.rect):
            sprites.remove(sp2)
            won = True

    # Drawing
    screen.fill(p.Color("white"))  # Clear the screen
    sprites.draw(screen)

    # Display win message
    if won:
        win_text = font.render("You win!", True, p.Color('black'))
        screen.blit(
            win_text,
            ((screen.get_width() - win_text.get_width()) // 2,
             (screen.get_height() - win_text.get_height()) // 2)
        )

    p.display.flip()
    clock.tick(90)

p.quit()
