'''

队列：先进先出表

表头|A,B,C,D,E,F,G,H,J,K,L,M.N,O,P|表尾

'''
import collections

#创建一个队列
queue = collections.deque()
print(queue)

#进队
queue.append("A")
print(queue)
queue.append("B")
print(queue)
queue.append("C")
print(queue)

#出队
res1 = queue.popleft()
print("res1 = ",res1)
res2 = queue.popleft()
print("res2 = ",res2)
res3 = queue.popleft()
print("res3 = ",res3)

