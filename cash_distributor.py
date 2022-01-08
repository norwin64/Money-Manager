import pygame, os, Button
import startscreen

#init
pygame.init()

#fonts
header_font = pygame.font.SysFont("comicsans", 70, bold=True)
standard_font = pygame.font.SysFont("comicsans", 50)
standard_font_italic = pygame.font.SysFont("comicsans", 70, italic=True)

#colours
BLACK = (0, 0, 0)
BLUE_1 = (0, 0, 100)

#root
root = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Money_manager 2.0")
FPS = 60
WIDTH,HEIGHT = root.get_width(), root.get_height()

#images
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("material", "background.jpg")),(root.get_size()))
EXIT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("material", "exit.png")), (70, 70))
MTS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("material", "mts.png")), (150, 150))
MFC_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("material", "mfc.png")), (150, 150))
MS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("material", "ms.png")), (140, 160))
MFP_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("material", "mfp.png")), (150, 150))
ADD_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("material", "add.png")), (150, 150))
BACK_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("material", "back.png")), (150, 150))
CALCULATE_IMAGE = pygame.image.load(os.path.join("material", "calculate.png"))

#Widget
EXIT_BUTTON = Button.Button(WIDTH-120, 50, EXIT_IMAGE, 1)
INCOME_TEXT = header_font.render("Einkommen:", True, BLACK)
WIDGET_ENTRY = ""
BACK_ENTRY = pygame.Rect(WIDTH / 2 - 180, 190, 360, 80)
FREIZEIT_TEXT = standard_font_italic.render("Freizeit", True, BLUE_1)
ANLAGEN_TEXT = standard_font_italic.render("Anlagen", True, BLUE_1)
BACK_BUTTON = Button.Button(100, 50, BACK_IMAGE, 0.8)
CALCULATE_BUTTON = Button.Button(WIDTH/2, 260, CALCULATE_IMAGE, 0.7)

TEXT_MTS = standard_font.render("15% = ", True, BLACK)
TEXT_MFC = standard_font.render("5% = ", True, BLACK)
TEXT_MS = standard_font.render("60% = ", True, BLACK)
TEXT_MFP = standard_font.render("20% = ", True, BLACK)

ADD_BUTTON = Button.Button(WIDTH/2-75, HEIGHT-200, ADD_IMAGE, 1)

def show_window():
    global list_data
    root.blit(BACKGROUND, (0, 0))
    list_data = startscreen.import_data()
    if EXIT_BUTTON.draw(root):
        quit()
    root.blit(INCOME_TEXT, (WIDTH/2- 180, 80))
    pygame.draw.rect(root, (255, 255, 255), BACK_ENTRY)
    root.blit(header_font.render(WIDGET_ENTRY, True, BLACK), (WIDTH / 2 - 150, 180))
    root.blit(FREIZEIT_TEXT, (100, 210))
    root.blit(ANLAGEN_TEXT, (1000, 210))

    root.blit(MTS_IMAGE, (150, 320))
    root.blit(TEXT_MTS, (80, 460))

    root.blit(MFC_IMAGE, (150, 570))
    root.blit(TEXT_MFC, (80, 720))

    root.blit(MS_IMAGE, (1050, 320))
    root.blit(TEXT_MS, (980, 460))

    root.blit(MFP_IMAGE, (1050, 570))
    root.blit(TEXT_MFP, (980, 720))

    if ADD_BUTTON.draw(root):
        add_distribution()
        startscreen.main()
        quit()

    if BACK_BUTTON.draw(root):
        startscreen.main()
        quit()

    if CALCULATE_BUTTON.draw(root):
        try:
            calc_distribution()
        except:
            pass
    pygame.display.update()


def add_distribution():
    file = open("data.txt", "w")
    g = WIDGET_ENTRY.replace(",", ".")
    file.writelines([str(float(g)*0.15 + float(list_data[0])) + " ", str(float(g)*0.05 + float(list_data[1])) + " ", str(float(g)*0.6 + float(list_data[2])) + " ", str(float(g)*0.2 + float(list_data[3]))])



def calc_distribution():
    global TEXT_MTS
    global TEXT_MS
    global TEXT_MFC
    global TEXT_MFP
    try:
        g = WIDGET_ENTRY.replace(",", ".")
    except:
        pass
    TEXT_MTS = standard_font.render("15% = " + str("{:.2f}".format(float(g)*0.15)) , True, BLACK)
    TEXT_MFC = standard_font.render("5% = " + str("{:.2f}".format(float(g)*0.05)), True, BLACK)
    TEXT_MS = standard_font.render("60% = " + str("{:.2f}".format(float(g)*0.6)), True, BLACK)
    TEXT_MFP = standard_font.render("20% = " + str("{:.2f}".format(float(g) * 0.2)), True, BLACK)

def quit():
    pygame.display.quit()
    exit()

def main():
    global WIDGET_ENTRY
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    WIDGET_ENTRY = WIDGET_ENTRY[0:-1]
                elif event.key == pygame.K_COMMA and len(WIDGET_ENTRY) <= 4:
                    WIDGET_ENTRY += event.unicode
                elif event.key == pygame.K_RETURN:
                    calc_distribution()
                elif len(WIDGET_ENTRY) <= 6:
                    try:
                        int(event.unicode)
                        WIDGET_ENTRY += event.unicode
                    except:
                        pass
        show_window()
    quit()

if __name__ == "__main__":
    main()