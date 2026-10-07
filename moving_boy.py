from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
FRAME_W, FRAME_H = 100, 100
FRAME_COUNT = 8
SPEED = 5
DELAY = 0.05

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running, dir_x

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1


running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
action = 3
dir_x = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * FRAME_W, action * FRAME_H, FRAME_W, FRAME_H, x, y)
    update_canvas()
    handle_events()
    if dir_x > 0:
        action = 1
    elif dir_x < 0:
        action = 0
    else:
        action = 3
    x += dir_x * SPEED
    frame = (frame + 1) % FRAME_COUNT
    delay(DELAY)

close_canvas()
