from pico2d import (
    SDL_KEYDOWN, SDL_QUIT, SDLK_ESCAPE,
    clear_canvas, close_canvas, delay, get_events, get_time,
    open_canvas, update_canvas,
)

from boy import Boy
from grass import Grass


def main():
    open_canvas(800, 600)
    try:
        grass = Grass()
        boy = Boy()
        running = True
        previous_time = get_time()

        while running:
            current_time = get_time()
            frame_time = current_time - previous_time
            previous_time = current_time

            for event in get_events():
                if event.type == SDL_QUIT:
                    running = False
                elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                    running = False
                else:
                    boy.handle_event(event)
            if not running:
                break

            grass.update(frame_time)
            boy.update(frame_time)
            clear_canvas()
            grass.draw()
            boy.draw()
            update_canvas()
            delay(0.01)
    finally:
        close_canvas()


if __name__ == '__main__':
    main()
