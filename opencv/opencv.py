from database import insert_serial  # Import the function to insert serial numbers into the database

import cv2  
#Import OpenCV for image processing
from pyzbar.pyzbar import decode  
# Import decode function for reading QR/barcodes
import numpy as np  
# Import NumPy for array operations

ESP32_CAM_URL = ''  # Set your ESP32-CAM stream URL here 

cap = cv2.VideoCapture(ESP32_CAM_URL)  # Open the video stream from ESP32-CAM

if not cap.isOpened(): 
    print("Cannot open ESP32-CAM stream")  
    exit() 

while True:  # Start an infinite loop to process video frames
    ret, frame = cap.read()  # Read a frame from the video stream
    if not ret:  # If frame not read successfully
        print("Failed to grab frame")  
        break  
    decoded_objects = decode(frame)  # Decode QR/barcodes in the frame

    for obj in decoded_objects:  # Loop through all detected QR/barcodes
        points = obj.polygon  # Get the corner points of the detected object
        if len(points) > 4:  # If more than 4 points, create a convex hull
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points  # Otherwise, use the points as is

        n = len(hull)  # Number of points in the hull
        for j in range(0, n):  
            # Draw lines between the points to form a box
            cv2.line(frame, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

        qr_data = obj.data.decode('utf-8')  # Decode the QR/barcode data as a string
        print(f"Decoded QR Code Data: {qr_data}")  
        # Print the decoded data
        insert_serial(qr_data)  # Insert the decoded data into the database

        x = obj.rect.left  # Get the x coordinate for text display
        y = obj.rect.top  # Get the y coordinate for text display
        cv2.putText(frame, qr_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)  
        # Display the decoded data on the frame

    cv2.imshow('ESP32-CAM QR Code Scanner', frame) 
     # Show the processed frame in a window

    if cv2.waitKey(1) & 0xFF == ord('q'): 
         # Exit the loop if 'q' is pressed
        break

cap.release()  # Release the video capture object
cv2.destroyAllWindows()  # Close all OpenCV windows