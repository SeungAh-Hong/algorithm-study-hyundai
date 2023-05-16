from collections import deque
import sys

deq = deque()

n = int(sys.stdin.readline())
for i in range(0, n):
    command = sys.stdin.readline().split()
    if command[0] == "push_front":
        deq.appendleft(int(command[1]))
    elif command[0] == "push_back":
        deq.append(int(command[1]))
    elif command[0] == "pop_front":
        if len(deq)>0:
            print(deq.popleft())
        else:
            print("-1")
    elif command[0] == "pop_back":
        if len(deq)>0:
            print(deq.pop())
        else:
            print("-1")
    elif command[0] == "size":
        print(len(deq))
    elif command[0] == "empty":
        if len(deq)==0:
            print("1")
        else:
            print("0")
    elif command[0] == "front":
        if len(deq)>0:
            print(deq[0])
        else:
            print("-1")
    elif command[0] == "back":
        if len(deq)>0:
            print(deq[-1])
        else:
            print("-1")