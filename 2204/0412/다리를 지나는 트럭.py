bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge_weights = 0
    answer = 0
    bridge = deque([0] * bridge_length)
    while bridge:
        answer += 1
        a = bridge.popleft()
        bridge_weights -= a
        if truck_weights and bridge_weights + truck_weights[0] <= weight:
            bridge_weights += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        elif truck_weights and bridge_weights + truck_weights[0] > weight:
            bridge.append(0)


    return answer

solution(bridge_length, weight, truck_weights)