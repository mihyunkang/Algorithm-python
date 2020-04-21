# Programming Report 1
filename = str(input()) #파일 이름을 받는다.

f = open("PR1_data/"+filename,'r') #입력한 파일을 연다.

n, m = map(int,f.readline().split()) #파일의 첫 줄을 읽어 정점 개수와 방향 에지 개수를 알아낸다.
# n = 정점 개수, m = 방향 에지 개수

A = [[9999 for i in range(n)] for j in range(n)] #인접행렬의 비용을 다 9999로 초기화 해놓는다.
#9999는 인접하지 않았음을 뜻한다.
for i in range(n): #자신에게 가는 비용은 0으로 바꾼다.
    A[i][i] = 0


for i in range(m): #인접행렬에 에지로 연결된 노드 비용을 업데이트한다.
    a, b, w = map(int,f.readline().split())
    A[a-1][b-1] = w
#인접행렬의 A[a-1][b-1]는 a에서 b로 연결된 방향에지 가중치와 같다.
f.close() #파일 닫기

print("Adjacency matrix") #인접행렬 출력

for i in range(n):    
    for j in range(n):
        print(("{:>5}").format(A[i][j]), end = "")
    print("")

#현재 노드와 가까운 가중치가 작은 노드를 찾고 그 노드와 연결된 노드들의 값 최소 경로로 업데이트
def minNode(i, A, node, n): 
    min1 = 9999
    min_node = None
    node[i] = True
    for j in range(n):#시작노드 인접 노드 체크
        if not node[j] and min1 > A[i][j]: #방문하지 않았고 지금까지 확인한 노드 중 i로 가는 비용이 가장 작은 노드 
            min_node = j #노드 저장
            min1 = A[i][j] #비용 값
    for k in range(n):
        if min_node is None: #방문하지 않았고 가중치가 매겨진 노드를 못 찾았을 때
            break 
        if A[min_node][k] + A[i][min_node] < A[i][k]: #찾았고 갱신할 최단 경로가 있을 때
            A[i][k] = A[min_node][k] + A[i][min_node] #갱신
    return min_node, node, A    


for i in range(n): #각 노드를 시작노드로 해서 최소경로 구하기
    node = [False for _ in range(n)] #방문 노드 체크 리스트
    now, node, A = minNode(i, A, node, n) #첫 노드의 인접 노드 중 가장 작은 경로 찾고 갱신
    while now is not None:
        node[now] = True
        now, node, A = minNode(i, A, node, n)


print("")
for i in range(n): #각 노드로 부터의 최단 거리 출력
    print("Shortest paths from v{} = (".format(i), end = "")
    print(", ".join(map(str,A[i])), end= "")
    print(")")
    



