def postorder(n, inorder, preorder):
    #후위순회는 왼쪽 노드->오른쪽 노드->루트노드 순으로 방문.

    if preorder[0] in inorder: #중위순회 list 안에 전위순회[0]이 있을 때     (전위순회[0]은 루트노드를 의미)
        root = inorder.index(preorder[0]) #중위순회에서 루트노드의 list위치를 root로 한다.

    if root != 0: #중위순회의 루트노드의 위치가 0이 아니라는 것은 왼쪽 서브트리가 있음을 의미
        postorder(len(inorder[:root]), inorder[:root], preorder[1:root + 1]) #왼쪽 서브트리를 재귀호출 한다.


    if root != n - 1: #중위순회의 루트노드의 위치가 마지막이 아니라는 것은 오른쪽 서브트리가 있음을 의미
        postorder(len(inorder[root + 1:]), inorder[root + 1:], preorder[root + 1:]) #오른쪽 서브트리를 재귀호출 한다.


    print(preorder[0],end=" ") #루트노드가 가장 뒤에 print되기 때문에 후위순회라고 할 수 있다.



count = int(input('테스트케이스 개수 : ')) #입력받을 트리 개수를 입력받는다.

while(count):
    preorder = [] #전위순회 list 선언
    inorder = [] #중위순회 list 선언

    n = int(input('노드의 개수 : ')) #트리 노드 개수를 입력받는다.
    preorder = list(map(int, input('input preorder traversal : ').split())) #전위순회 트리를 입력받고, 공백을 기준으로 split하고 int형태로 list에 집어넣는다.
    inorder = list(map(int, input('input inorder traversal : ').split())) #중위순회 트리를 입력받고, 공백을 기준으로 split하고 int형태로 list에 집어넣는다.

    print("Postorder traversal : ")
    postorder(n, inorder, preorder) #postorder 메소드 실행
    print("")
    count-=1 #count를 1씩 줄여 0이되면 while문 종료

print('테스트 종료')