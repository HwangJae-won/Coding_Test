def solution(video_len, pos, op_start, op_end, commands):
    #계산 위해 분으로 변환 
    total_minute = int(video_len[0:2])*60+int(video_len[3:5])
    pose_minute = int(pos[0:2])*60+int(pos[3:5])
    op_start = int(op_start[0:2])*60+int(op_start[3:5])
    op_end = int(op_end[0:2])*60+int(op_end[3:5])
    
    
    if (pose_minute>= op_start and pose_minute<=op_end):
            pose_minute =op_end
    # 명령 전 후로 오프닝 구간에 속하는 지 확인해야함. 
    for status in commands:
        
        if status =="next":
            if total_minute-pose_minute < 10:
                pose_minute = total_minute
            else: 
                pose_minute += 10
        elif status =="prev":
            if pose_minute < 10:
                pose_minute =0
            else:
                pose_minute -=10
        if (pose_minute>= op_start and pose_minute<=op_end):
            pose_minute =op_end
    #두자리 수 유지하려면 f 포맷핑으로    
    answer= f"{pose_minute // 60:02}:{pose_minute % 60:02}"
    return answer