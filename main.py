from message_generator import generate_message
from detector import is_forged
import time

def main():
    print("CAN Message Simulator & Intrusion Detector\n")

    for i in range(10):  # 10개의 메시지를 생성하고 검사
        msg = generate_message()
        forged, reasons = is_forged(msg)

        print(f"[{i+1}] Received Message: {msg}")

        if forged:
            print(f"❌ Forged Message Detected! Reasons: {', '.join(reasons)}\n")
        else:
            print("✅ Valid Message\n")

        time.sleep(1)  # 1초 간격으로 메시지 출력

if __name__ == "__main__":
    main()

    if forged:
        print(f"❌ Forged Message Detected! Reasons: {', '.join(reasons)}")
    if detect_flooding():
            print("⚠️ Flooding Attack Suspected!")
    if detect_spoofing(msg["id"]):
            print("⚠️ Spoofing Attack Detected!")

    print()
    time.sleep(0.2)  # Flooding 감지를 위해 메시지 속도 조절
