import pygame
import random

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_row = 0
        mole_col = 0

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    click_row = x // 32
                    click_col = y // 32
                    if (click_row, click_col) == (mole_row, mole_col):
                        mole_row = random.randrange(0, 20)
                        mole_col = random.randrange(0, 15)
            screen.fill("light green")
            for i in range(17):
                for j in range(21):
                    pygame.draw.line(screen, "black", (0, i * 32), (640, i * 32))
                    pygame.draw.line(screen, "black", (j * 32, 0), (j * 32, 512))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_row * 32, mole_col * 32)))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
