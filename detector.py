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
