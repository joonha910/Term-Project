class Stack(list):
    push = list.append    # Insert
                          # Delete - 내장 pop 메소드 활용
    def is_empty(self):   # 데이터가 없는지 확인
        if not self:
            return True
        else:
            return False

    def peek(self):        # 최상단 데이터 확인
        return self[-1]
#최대 직사각형을 찾는 함수
def find():
    s= Stack() #스택생성 (판자의 index를 저장)
    answer = 0 # 최대 직사각형의 크기를 저장할 변수
    s.push(0) # 초기에 0을 넣음
    now=0 # 현재의 인덱스(밑변을 구하기 위함)
    for i in range(1,N+2): # 밑변을 쉽게 구하기위해 1부터 시작
        while(1):
            if(s.is_empty()):# 스텍이 비어있을때 break
                break
            index = s.peek()# 스텍의 top값을 보여줌
            if(H[index]<H[i]):# 현재의 판자 높이가 전의 높이보다 크면 break
                break
            s.pop()# 스텍의 top값을 제거함

            if(not s.is_empty()):
                area = H[index]*(now - s.peek())# 넓이를 구함
                if(area>answer):
                    answer = area# 전에 구했던 넓이보다 현재 넓이가 더 크면 answer에 저장함
        s.push(i) # 스택에 인덱스를 저장함
        now = now + 1 # 밑변을 구하기 위해 계속 +1을 해줌
    return answer
H=[] # 리스트 선언
C=input("테스트케이스 개수 : ")
C=int(C)
for count in range(0,C):
    N=input("판자의 수 : ")
    N=int(N)
    H = [] # 리스트 초기화
    H.append(0) # 초기에 0을 넣어줌 ( 밑변의 길이를 쉽게 구하기 위함 )
    for i in range(0,N):
        temp=input()
        temp=int(temp)
        H.append(temp) # 판자의 높이를 입력 받음
    H.append(0) # 마지막 값으로 0으로 넣어줌 ( 마지막 밑변을 쉽게 구하기 위함 )
    print("직사각형의 크기 : ", str(find()))