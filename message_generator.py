import random

def generate_message():
    # CAN 메시지는 보통 ID, 속도, RPM 등을 포함
    message = {
        "id": random.choice([100, 123, 150, 999, 666]),  # 정상 ID or 위조 ID
        "speed": random.randint(-10, 320),               # 정상: 0~200, 위조: 음수 또는 250이상
        "rpm": random.randint(500, 9000)                 # 예시 RPM
    }
    return message
