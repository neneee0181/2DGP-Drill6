import random
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def moveImg():
    global x, y
    global img_position_x, img_position_y

    if x < img_position_x:
        img_position_x -= 1
    elif x > img_position_x:
        img_position_x += 1

    if y < img_position_y:
        img_position_y -= 1
    elif y > img_position_y:
        img_position_y += 1

def handle_events():
    global running
    global x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
img_position_x, img_position_y = TUK_WIDTH // 2, TUK_HEIGHT // 2

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(x,y)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, img_position_x, img_position_y)
    update_canvas()
    frame = (frame + 1) % 8
    if (x == img_position_x and y == img_position_y):
        x, y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
    else:
        moveImg()

    handle_events()

close_canvas()
