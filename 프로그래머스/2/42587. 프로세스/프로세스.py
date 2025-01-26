from collections import deque

def solution(priorities, location):
    cnt = 0
    proc = deque(enumerate(priorities))
    sorted_prior = sorted(priorities, reverse=True)
    
    while proc:
        idx, priority = proc.popleft()
        if priority == sorted_prior[0]:
            cnt += 1
            sorted_prior.pop(0)
            if idx == location:
                return cnt 
        else:
            proc.append((idx, priority))
                