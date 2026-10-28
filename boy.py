from pico2d import (
    SDL_KEYDOWN, SDL_KEYUP, SDLK_LEFT, SDLK_RIGHT, SDLK_a,
    get_canvas_width, get_time, load_image,
)


PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KMPH = 20.0
RUN_SPEED_PPS = RUN_SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
FRAMES_PER_SECOND = 8.0 / 0.5


def left_down(event):
    return event[0] == 'INPUT' and event[1].type == SDL_KEYDOWN and event[1].key == SDLK_LEFT


def right_down(event):
    return event[0] == 'INPUT' and event[1].type == SDL_KEYDOWN and event[1].key == SDLK_RIGHT


def arrow_up(event):
    return event[0] == 'INPUT' and event[1].type == SDL_KEYUP and event[1].key in (SDLK_LEFT, SDLK_RIGHT)


def a_down(event):
    return event[0] == 'INPUT' and event[1].type == SDL_KEYDOWN and event[1].key == SDLK_a


class Idle:
    @staticmethod
    def enter(boy, event):
        boy.frame = 0.0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy, frame_time):
        boy.frame = (boy.frame + FRAMES_PER_SECOND * frame_time) % 8

    @staticmethod
    def draw(boy):
        row = 3 if boy.dir == 1 else 2
        boy.image.clip_draw(int(boy.frame) * 100, row * 100, 100, 100, boy.x, boy.y)


class Run:
    @staticmethod
    def enter(boy, event):
        boy.frame = 0.0
        if left_down(event):
            boy.dir = -1
        elif right_down(event):
            boy.dir = 1

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy, frame_time):
        boy.frame = (boy.frame + FRAMES_PER_SECOND * frame_time) % 8
        boy.x += boy.dir * RUN_SPEED_PPS * frame_time
        boy.x = max(50, min(get_canvas_width() - 50, boy.x))

    @staticmethod
    def draw(boy):
        row = 1 if boy.dir == 1 else 0
        boy.image.clip_draw(int(boy.frame) * 100, row * 100, 100, 100, boy.x, boy.y)


class AutoRun:
    @staticmethod
    def enter(boy, event):
        boy.frame = 0.0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy, frame_time):
        boy.frame = (boy.frame + FRAMES_PER_SECOND * frame_time) % 8
        boy.x += boy.dir * RUN_SPEED_PPS * frame_time

    @staticmethod
    def draw(boy):
        Run.draw(boy)


class StateMachine:
    def __init__(self, boy):
        self.boy = boy
        self.current_state = Idle
        self.transitions = {
            Idle: {left_down: Run, right_down: Run, a_down: AutoRun},
            Run: {left_down: Run, right_down: Run, arrow_up: Idle},
            AutoRun: {},
        }
        self.current_state.enter(boy, ('START', None))

    def handle_event(self, event):
        for condition, next_state in self.transitions[self.current_state].items():
            if condition(event):
                self.current_state.exit(self.boy, event)
                self.current_state = next_state
                self.current_state.enter(self.boy, event)
                return

    def update(self, frame_time):
        self.current_state.do(self.boy, frame_time)

    def draw(self):
        self.current_state.draw(self.boy)


class Boy:
    def __init__(self):
        self.x, self.y = get_canvas_width() / 2, 90
        self.dir = 1
        self.frame = 0.0
        self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine(self)

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def update(self, frame_time):
        self.state_machine.update(frame_time)

    def draw(self):
        self.state_machine.draw()
