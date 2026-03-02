import cv2

rtsp_url = "rtsp://admin:1234567a@192.168.0.67:554/cam/realmonitor?channel=1&subtype=0"

cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("❌ Failed to open RTSP stream")
    exit()

print("✅ Stream opened successfully")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to read frame")
        break

    cv2.imshow("RTSP Stream", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:  # 27 is ESC
        print("⏹ Exiting...")
        break

cap.release()
cv2.destroyAllWindows()