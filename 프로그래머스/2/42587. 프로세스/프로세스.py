from collections import deque

def solution(priorities, location):
    cnt = 0
    proc = deque(enumerate(priorities))  # (index, priority) 형태로 저장
    sorted_priorities = sorted(priorities, reverse=True)  # 우선순위를 정렬하여 사용
    
    while proc:
        idx, priority = proc.popleft()  # 가장 앞의 문서 가져오기
        if priority == sorted_priorities[0]:  # 현재 문서의 우선순위가 가장 높은 경우
            cnt += 1  # 실행된 문서 수 증가
            sorted_priorities.pop(0)  # 실행된 문서 제거
            if idx == location:  # 원하는 위치의 문서인지 확인
                return cnt
        else:
            proc.append((idx, priority))  # 다시 큐에 추가
