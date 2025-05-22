import cv2
from pyzbar.pyzbar import decode
import numpy as np

# Replace with your ESP32-CAM's IP address
ESP32_CAM_URL = ''

cap = cv2.VideoCapture(ESP32_CAM_URL)

if not cap.isOpened():
    print("Cannot open ESP32-CAM stream")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    decoded_objects = decode(frame)

    for obj in decoded_objects:
        # Draw bounding box
        points = obj.polygon
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points

        n = len(hull)
        for j in range(0, n):
            cv2.line(frame, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

        # Decode and print data
        qr_data = obj.data.decode('utf-8')
        print(f"Decoded QR Code Data: {qr_data}")

        # Display decoded data on the frame
        x = obj.rect.left
        y = obj.rect.top
        cv2.putText(frame, qr_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('ESP32-CAM QR Code Scanner', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
