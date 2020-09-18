from pico2d import *

open_canvas()

gra = load_image('grass.png')
ch = load_image('run_animation.png')

gra.draw_now(400, 30)
ch.draw_now(400, 85)

gra.draw_now(400, 30)

x = 0
frame_index = 0 #그림을 바꿔가며 그려야 한다는건 바꿔가며 잘라야한다는것
while x < 800:
	clear_canvas() #백버퍼를 지운다
	gra.draw(400,30) #백버퍼에 그린다
	#아래 문장에서 y좌표는 어떤 동작을 하고 있느냐. 
	ch.clip_draw(frame_index * 100, 100, 100, 100, x, 85) #백버퍼에 그린다, 앞의 좌표 4개는 자를 영역, 뒤에 두개는 그릴 위치
	update_canvas() #백버퍼에 그린 것을 프론트버퍼로 옮겨온다

	get_events() #마우스 움직이던 그거까지 이벤트로 처리되었었으니.


	x += 2 #위의 블럭은 그림을 그리는 부분, 아래 블럭은 작업을 해주는 부분 
	frame_index += 1
	#if frame_index >= 8: #루프돌게, 8프레임동안 도는거죠. 
		#frame_index = 0

	frame_index = (frame_index + 1) % 8 #이게 윗쪽보다 더 좋은 표현, if는 분기를 쓰는건데 cpu는 분기 별로 안 좋아함 


	delay(0.02)

delay(10)

close_canvas()


