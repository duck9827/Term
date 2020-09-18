##과제 1번) 이름 쓰는 프로그램
#함수로 어떤 부분을?
#이름에 겹치는 부분이 없는데....
#펜업 펜다운 부분을 함수로 만들자
#방향 신경 안 쓰려면 goto만 써야?

import turtle   #터틀 모듈 임포트

def turtle_move(a, b):
    turtle.penup()
    turtle.goto(a,b)
    turtle.pendown()

def tri_draw(a,b):  #a,b는 현재 위치로?
    turtle.goto(a+50, b+50)
    turtle.goto(a+100, b-10)

def garo_l(a,b):  #긴 가로획을 긋는 함수
    turtle.goto(a+200, b)

def sero_l(a,b):    #세로로 긴 획을 긋는 함수
    turtle.goto(a, b-100)

def garo_s(a,b):    #가로로 짧은 획을 긋는 함수
    turtle.goto(a+50, b)

def sero_s(a,b):    #세로로 짧은  획을 긋는 함수
    turtle.goto(a, b-50)

turtle_move(-200, 200)   #우선 왼쪽으로 이동 
turtle.circle(-50)  # ㅇ자

turtle_move(-200,80)
sero_s(-200,80)
turtle_move(-300,30)
garo_l(-300,30) #ㅗ자

turtle_move(-50,120)    #ㅅ자
tri_draw(-50,120)

turtle_move(50,150)
garo_s(50,150)
turtle_move(100,190)
sero_l(100,190)     #ㅓ자

turtle_move(-30,80)
sero_s(-30,80)
turtle_move(-30,30)
garo_l(-30,30)  #받침 니은

turtle_move(200,180)
garo_s(200,180)
garo_s(250,180)
turtle_move(200,130)
tri_draw(200,130)   #지읒

turtle_move(320,180)
sero_l(320,180)
turtle_move(320,140)
garo_s(320,140)
turtle_move(370,180)
sero_l(370,180)

turtle.exitonclick()






