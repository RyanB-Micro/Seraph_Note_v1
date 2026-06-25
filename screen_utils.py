import pygame
import project_style as proj_style

# PyGame Settings
#-----------------
FPS = 60
pygame_running = False
screen = None
clock = None
font_big = None
font_big_italic = None
font = None
font_bold = None
font_bold_italic = None
font_small = None
pygame_version = pygame.version.ver
working_sheet = None

window_prefix = "SeraphNote_"
current_caption = ""

def change_sheet(sheet):
    global working_sheet
    #pygame.display.set_caption(window_prefix + sheet.sheet_name)
    working_sheet = sheet

def init_screen(sheet):
    global clock, font_big, font, font_small, screen, pygame_running, pygame_version, font_bold_italic, font_big_italic, font_bold
    change_sheet(sheet)
    pygame.init()

    pygame_version = pygame.version.ver

    clock = pygame.time.Clock()
    font_big_italic = pygame.font.SysFont(None, 50, italic=True)
    font_big = pygame.font.SysFont(None, 50)
    font = pygame.font.SysFont(None, 20)
    font_bold = pygame.font.SysFont(None, 20, bold=True)
    font_bold_italic = pygame.font.SysFont(None, 20, italic=True, bold=True)
    font_small = pygame.font.SysFont(None, 16)
    screen = pygame.display.set_mode((working_sheet.screen_width, working_sheet.screen_height))

    #pygame.display.set_caption("SeraphNote_Concept")
    pygame_running = True



def screen_loop():
    global pygame_running, current_caption

    while pygame_running:
        # Clock timing
        delta_time = clock.tick(FPS) / 1000
        delta_time = max(0.001, min(0.1, delta_time))  # clamp for math error

        # check if caption is correct
        caption = window_prefix + working_sheet.sheet_name
        if current_caption != caption:
            pygame.display.set_caption(caption)
            current_caption = caption

        # blank screen
        screen.fill(proj_style.CALM_AZURE)

        for event in pygame.event.get():
            # Detect if window is being closed
            if event.type == pygame.QUIT:
                pygame_running = False

        # Update screen
        pygame.display.flip()

    # Quit pygame on main loop finish
    pygame.quit()
