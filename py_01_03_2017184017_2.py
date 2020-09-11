##과제2: 격자가 그려지는 프로그램. 0,0 부터 500,500까지 크기 100짜리 격자가 그려지도록
#for이나 while등의 반복문 사용
#크기가 100이라는건 선이 5등분 났다는 소리, 그렇다는 건 가로 세로 선을 여섯개 그어야?
#화면 크기문제로 사이즈를 0,0부터 300,300까지 크기 60 격자가 그려지는 것으로 바꾸었습니다,
#죄송합니다ㅠㅠㅠㅠㅠㅠㅠ

import turtle   #일단 터틀모듈 임포

turtle.speed(0)     #속도 빠르게
start_x = 0  #시작점 좌표
start_y = 0

def turtle_move(a,b):   #거북이 이동시킬 함수
    turtle.penup()
    turtle.goto(a,b)
    turtle.pendown()

for i in range(6):  #세로줄부터 먼저 긋기로, 즉슨 가로방향으로 이동(x축방향)
    turtle.goto(start_x,start_y-300)
    start_x = start_x + 60 
    turtle_move(start_x, start_y)

start_x = 0  #시작점 좌표값 클리어
start_y = 0
turtle_move(0,0)

for i in range(6):  #마지막으로 가로줄!
    turtle.goto(start_x+300,start_y)
    start_y = start_y - 60 
    turtle_move(start_x, start_y)



turtle.exitonclick()
    
