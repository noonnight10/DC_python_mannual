#파이썬 공부에 조금이라도 도움이 되길..
#Made by DC문재윤



#샵(#)으로 시작되는 것은 주석들입니다. (코드의 보충설명을 해주는 것)
#1. print() 사용하기

#print를 사용할 때에는, print("자신이 쓰고 싶은 문자열") 을 작성하면 됩니다. 예를 들면,
print("와 ㅇㅇ님 팬이에요오") #를 입력하게 되면 이 파이썬이라는 놈은 와 ㅇㅇ님 팬이에요오 를 출력하게 됩니다.

#2. 변수(변하는 수)
#변수를 사용할 때에는, 우선 변수를 정의해주어야 합니다. 만약 내가 gf라는 변수에다가 "DC" 라는 단어를 저장하고 싶으면
grd="DC" #으로 지정하면 됩니다. 이 변수는 print를 사용할 때에도 사용할 수 있는데 예를 들면

grd="DC" #변수 지정
print(gf) #를 입력하게 되면 파이썬은 DC 라고 출력해 줍니다.

#변수에는 여러가지 유형이 있습니다. [문자열, 정수형, 실수형, 참/거짓 형] 등이 있는데 아직 참/거짓 형은 몰라도 딱히 상관 없고 많이 쓰지도 않는 편이라..
#파이썬은 처음 변수를 지정하게 되면 모두 문자열로 처리해버리는데 이 때문에 우리가 일일이 변수의 유형을 정해주어야 합니다.
#정수는 int, 실수는 float, 문자열은 str로 지정할 수 있는데,

#만약 내가 정수형 변수 en에 1이라는 값을 저장하고 싶다면,
en=1 #en이라는 변수에 1을 저장한다
en=int(en) #en은 이제부터 문자열이 아니고 정수형 변수인 것을 알려주는 구문
#이러하게 작성하면 이제 en이라는 변수에는 1이라는 정수의 값이 저장됩니다.

#만약 문자열 사이에 변수를 출력하고 싶을 때에는
#[내 손안의 파이썬 13강 문제에서 발췌]
my_year=input() #입력받기 (후 입력 파트에서 다시 기술할 명령어 input입니다.)
my_year=int(my_year) #a라는 변수를 정수로 환산하기
hg_y=my_year+60 #b라는 새로운 변수에 60을 더함 (b는 환갑이 되는 연도를 의미함)
print("당신은 {}년에 환갑을 맞이합니다.".format(hg_y)) #여기서 format이 사용되었는데 이는 코드의 양을 줄이기 위해 사용되었습니다.

# format을 사용하지 않을 시,

my_year=input() #입력받기 (후 입력 파트에서 다시 기술할 명령어 input입니다.)
my_year=int(my_year) #a라는 변수를 정수로 환산하기
hg_y=my_year+60 #b라는 새로운 변수에 60을 더함 (b는 환갑이 되는 연도를 의미함)
hg_y=str(hg_y) #hg_y라는 값에 입력한 나이+60을 해주는데 다음 단계에서 문자와 정수는 더할 수 없으니 쩡수형이었던 변수를 다시 문자형으로 바꾸어주는 작업.
print("당신은 "+hg_y+"년에 환갑을 맞이합니다.") #출력

#위와 같은 코드로 작성될 수도 있습니다. 물론 뭘 쓰던 간에 개인 취향이긴 하지만..


#3. 입출력
#엔트리에서는 주로 묻고 답하기 형식을 입력으로 대체하는데, 파이썬에서는 input이라는 명령어를 사용합니다.
#다만 엔트리에서는 대답을 저장할 '대답' 이라는 변수를 내장하고 있지만, 파이썬은 그딴 거 없습니다. 애초에 파이썬에서는 '대답' 변수가 있는 게 더 불편하고요.
#input문의 작성법은 다음과 같습니다.
#만들자 하는 변수=input("입력받기 전 하고 싶은 말을 적으면 되지만 없으면 공백으로 비워도 됩니다.")
#이를 응용해보아 방금 입력받은 값을 그대로 출력하는 코드를 짜 보면
recieve=input()
print(recieve)
#가 됩니다.
#하지만 이 input문을 가용할 때는 주의할 점이 있는데, 어떤 값을 받아버리든 무조건 문자열로 처리해버려 코드가 길어지고 복잡해질 시 오류가 발생할 수 있습니다.
#이를 해결하려면, 다음과 같이 나중에 그 변수의 자료형을 정해주어야 하는데, 예제 코드는 다음돠 같습니다.
a1=input()
a1=int(a1)
print(a1)
#이 말고도 input문 자체에 자료형을 선언해버리는 방법이 있습니다.
#그 방법은 다음과 같습니다.
b1=int(input())
print(b1)
#input문에 더 붙일 수 있는 구문을 알아봅시다.
#한번에 많은 변수를 입력받을 수 있는 명령어가 있는데, 이를 split이라고 합니다.
#split문은 '어떤 문자' 를 중심으로 입력받은 글자를 나누어 각각의 변수에 저장하게 할 수 있습니다.
#예를 들어, 당신이 정수형 변수 a2, b2, b3에 입력받은 수를 ','자를 기준으로 나누어 저장하고 싶다면
a2,b2,c2=int(input("두 수를 ,를 기준으로 나누어 입력하세요.").split(","))
print(a2)
print(b2)
print(c2)
#으로 입력된 값이 변수별로 각각 잘 나누어지는 것을 볼 수 있습니다.

#4. 함수
#파이썬에서 함수는 특정한 상황에 코드를 꺼내서 쓰기 위해 만든 기능입니다.
#예를 들어 내가 a3에다가 5를 더해서 그 수를 b3에 저장하고 출력하는 함수를 만드려고 한다면 함수를 사용하기 전 우선 정의해야 하는데,
#함수를 정의할 때는 주로 def를 사용합니다. 사용법은 다음과 같습니다.
a3=0 #a3의 초기 값은 0으로 설정
a3=int(a3) #a3의 형태는 정수형이다
def ap1(): #함수 정의
    b3=int(a3+1) #b3은 a3+1이다 라는 식을 세움
    print(b3) #출력

ap1() #함수 호출하기

#5.인덱싱
#만약 a4라는 변수에 Hello World라는 문자열이 저장되어 있다고 해 봅시다.
#근데 만약 내가 a4에서 H만 출력하고 싶을 때 쓰는 것이 인덱싱이고. 그 중에서 필요한 부분(예: Hello)만 사용하는 것을 슬라이싱이라고 한다.
#인덱싱은 다음과 같이 사용할 수 있다.
a4="Hello World"
#   012345678910 <-인덱스 번호(쉽게 방이라 칭하겠습니다.)
print(a4[0]) #0번 방에 있는 문자 출력(인덱싱)
print(a4[0:5])#0번 방 부터 4번 방에 있는 곳까지 출력(슬라이싱)


#도움이 되셨길 바랍니다..
#아님말구