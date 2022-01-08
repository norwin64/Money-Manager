import pygame, os, Button, cash_distributor

#init
pygame.init()
pygame.font.init()

#fonts
header_font = pygame.font.SysFont("comicsans", 70, bold=True)
standard_font = pygame.font.SysFont("comicsans", 50)
standard_font_italic = pygame.font.SysFont("comicsans", 70, italic=True)

#colours
BLACK = (0, 0, 0)

#root
root = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Money_manager 2.0")
FPS = 60
WIDTH,HEIGHT = root.get_width(), root.get_height()

#images
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("material", "background.jpg")), (root.get_size()))
EXIT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("material", "exit.png")), (70, 70))
ADD_INCOME = pygame.image.load(os.path.join("material", "add_income.png"))

#Widgets
HEADER_TEXT = header_font.render("Kontenübersicht: ", True, BLACK)
EXIT_BUTTON = Button.Button(WIDTH-120, 50, EXIT_IMAGE, 1)
SWITCH_BUTTON = Button.Button(100, HEIGHT-230, ADD_INCOME, 0.7)


def show_window():
    import_data()
    root.blit(BACKGROUND, (0, 0))
    if EXIT_BUTTON.draw(root):
        quit()

    MTS = standard_font.render("Money to spend: " + str(round(float(lines[0]), 2)) + "$", True, BLACK)
    MFC = standard_font.render("Money for clothing: " + str(round(float(lines[1]), 2)) + "$", True, BLACK)
    MS = standard_font.render("Money saved: " + str(round(float(lines[2]), 2)) + "$", True, BLACK)
    MFP = standard_font.render("Money for paragliding: " + str(round(float(lines[3]), 2)) + "$", True, BLACK)

    root.blit(HEADER_TEXT, (100, 100))
    root.blit(MTS, (100, 250))
    root.blit(MFC, (100, 350))
    root.blit(MS, (100, 450))
    root.blit(MFP, (100, 550))

    if SWITCH_BUTTON.draw(root):
        switch_to_cash_distributor()
    pygame.display.update()

def import_data():
    global lines
    my_file = open("data.txt", "r")
    lines = my_file.read().split(" ")
    return lines

def switch_to_cash_distributor():
    cash_distributor.main()
    quit()

def quit():
    pygame.display.quit()
    exit()

def main():
    global ENTRY_WIDGET
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        show_window()
    quit()

if __name__ == "__main__":
    main()