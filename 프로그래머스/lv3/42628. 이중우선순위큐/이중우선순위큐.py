#우선 순위 큐 ; heap 사용하여 구현 가능 
import heapq

def solution(operations):
    min_heap = []  # 최솟값을 저장하는 우선순위 큐
    max_heap = []  # 최댓값을 저장하는 우선순위 큐

    for op in operations:
        command, num = op.split()
        num = int(num)

        if command == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif command == 'D' and min_heap:
            if num == 1:
                max_value = heapq.heappop(max_heap)
                min_heap.remove(-max_value)
            else:
                min_value = heapq.heappop(min_heap)
                max_heap.remove(-min_value)

    if min_heap:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        return [0, 0]
