import Screen
import pygame
import Button
from predict import predict
from Colours import colours


def guess_number():
    pygame.image.save(draw_surface, "image.jpg")   # first, we save the image
    draw_surface.fill(colours['black'])    # reset the screen

    return predict()      # then predict using our save model and return the number


def display_number(number):
    txt_surf = pygame.font.Font(None, 100).render(number, True, colours['black'])
    window.gameDisplay.blit(txt_surf, (500, 175))


def handleEvents(events):
    global number

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        mouse_position = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if submit_button.rect.collidepoint(mouse_position):
                number = guess_number()
            if clear_button.rect.collidepoint(mouse_position):
                draw_surface.fill(colours['black'])


def draw_digit(events):
    for event in events:
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(
                draw_surface,
                colours['white'],
                pygame.mouse.get_pos(),
                1
            )


def loop():
    # Our main loop
    while True:
        events = pygame.event.get()
        handleEvents(events)

        window.gameDisplay.blit(draw_surface, (0,0))   # display the drawing surface

        # displaying the buttons
        submit_button.draw()
        clear_button.draw()

        draw_digit(events)   # capture the mouse positions and draw circles to represent the number

        if number:
            display_number(str(number))

        window.run()


# Creating the pygame window
display_width = 600
display_height = 400
window = Screen.Window(display_width, display_height, 'Draw a Number')

# Creating the surface where the user would draw
draw_surface_size = (450, 400)
draw_surface = pygame.Surface(draw_surface_size)
draw_surface.fill(colours['black'])

# Creating a button to submit our drawing
submit_button = Button.Button(
                    window.gameDisplay,
                    colours['black'],
                    (475, 25), (95, 40),
                )
submit_button.setText('Guess')

# Clear Button
clear_button = Button.Button(
                    window.gameDisplay,
                    colours['black'],
                    (475, 90), (95, 40)
                )
clear_button.setText('Clear')

# Finally, initialize the guessed number to None
number = None

loop()
