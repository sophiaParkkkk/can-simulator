from collections import deque
import time

def is_forged(message):
    forged = False
    reasons = []

    # 정상 ID 범위: 100 ~ 150
    if message["id"] < 100 or message["id"] > 150:
        forged = True
        reasons.append("Invalid ID")

    # 속도는 0~250 사이가 정상
    if message["speed"] < 0 or message["speed"] > 250:
        forged = True
        reasons.append("Unrealistic Speed")

    # RPM은 500~8000 정도가 정상
    if message["rpm"] < 500 or message["rpm"] > 8000:
        forged = True
        reasons.append("Abnormal RPM")

    return forged, reasons

msg_times = deque()

def detect_flooding():
    now = time.time()
    msg_times.append(now)

    # 1초 내 메시지만 남기기
    while msg_times and now - msg_times[0] > 1:
        msg_times.popleft()

    return len(msg_times) >= 5

spoof_counter = 0

def detect_spoofing(msg_id):
    global spoof_counter
    if msg_id not in range(100, 151):  # 정상 ID 범위
        spoof_counter += 1
    else:
        spoof_counter = 0

    return spoof_counter >= 3