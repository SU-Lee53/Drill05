from pico2d import *
from random import randint

# 'hand_arrow.png' 이미지 사용 - 수업 실습 자료에 포함
# 랜덤 위치에 손이 표시됨.(1점)
# 소년은 손을 따라감.(3점)
# 손에 도착하면, 다시 손이 자동으로 랜덤위치로 이동합.(1점)
# 캐릭터의 바라보는 방향(좌우)을 이동방향과 일치시켜야함(1점)


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

frame = 0
def animation_right(x, y, arrx, arry):
	global frame
	clear_canvas()
	TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
	arrow.draw(arrx, arry)
	character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y, 100, 100)
	update_canvas()
	frame = (frame + 1) % 8

def animation_left(x, y, arrx, arry):
	global frame
	clear_canvas()
	TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
	arrow.draw(arrx, arry)
	character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)
	update_canvas()
	frame = (frame + 1) % 8

def Linear_Move(p1, p2):
	x1, y1 = p1[0], p1[1]
	x2, y2 = p2[0], p2[1]


	for i in range(0, 100):
		t = i / 100
		x = (1 - t)*x1 + t*x2
		y = (1 - t)*y1 + t*y2

		arrow.draw(x2, y2)

		if(x2 - x1 < 0):
			animation_left(x, y, x2, y2)
		else:
			animation_right(x, y, x2, y2)
		delay(0.01)


x = TUK_WIDTH / 2
y = TUK_HEIGHT / 2
before = [x, y]
while True:
	goto = [randint(0, TUK_WIDTH), randint(0, TUK_HEIGHT)]
	Linear_Move(before, goto)
	before = goto



close_canvas()
