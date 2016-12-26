# -----------------------------------------------------------------------------------
from pico2d import *
import framework

# -----------------------------------------------------------------------------------
from jumper import Jumper

# -----------------------------------------------------------------------------------
name = "gameMain"
# -----------------------------------------------------------------------------------
jumper = None
background = None
portal = None
# -----------------------------------------------------------------------------------

def create_world():
    global jumper, background, portal
    jumper = Jumper()
    background = load_image("stage1.png")
    portal = load_image('portal.png')



def enter():
    create_world()
    framework.reset_time()


def exit():
    pass


def pause():
    pass


def resume():
    pass


# -----------------------------------------------------------------------------------

jumping = 0
movement = 0
portalX = 750
portalY = 160

def handle_events(frame_time):
    global jumping, movement

    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
            framework.quit()

        # 조작

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                jumper.state = jumper.RUNRIGHT
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                jumper.state = jumper.RUNLEFT
        if (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
                jumper.state = jumper.STANDRIGHT
        if (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                jumper.state = jumper.STANDLEFT

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                jumping = 1

        if jumping == 1:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                movement = 1

            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                movement = 2

            if jumper.state == jumper.RUNRIGHT or jumper.state == jumper.STANDRIGHT:
                jumper.state = jumper.JUMPRIGHT

            if jumper.state == jumper.RUNLEFT or jumper.state == jumper.STANDLEFT:
                jumper.state = jumper.JUMPLEFT


def update(frame_time):
    global jumping

    jumper.update(frame_time)

    if movement == 1:
        jumper.x += 10

    if movement == 2:
        jumper.x -= 10

    if jumper.x > portalX:
        print("move to next stage")

    update_canvas()


def draw(frame_time):
    global portalX, portalY

    clear_canvas()

    background.draw(400, 300)
    jumper.draw()
    portal.draw(portalX, portalY)

    update_canvas()

# -----------------------------------------------------------------------------------



