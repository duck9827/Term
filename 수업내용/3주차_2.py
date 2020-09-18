from pico2d import*

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
	global running
	global x, y
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_MOUSEMOTION:
			x, y = event.x, KPU_HEIGHT - 1 - event.y
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			running = False

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('grass.png')
character = load_image('run_animation.png')

running = True
x = 800 // 2
frame = 0
dir = 0

while running:
	clear_canvas()
	kpu_ground.draw(400,30)
	character.clip_draw(frame * 100, 0, 100, 100, x, 90)
	update_canvas()
	handle_events()
	frame = (frame + 1) % 8
	x += dir * 5
	delay(0.01)

