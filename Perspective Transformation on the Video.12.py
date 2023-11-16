import cv2
import numpy as np

def perspective_transform(frame):
    # Get frame dimensions
    height, width = frame.shape[:2]
    original_points = np.float32([[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]])
    transformed_points = np.float32([[50, 50], [width - 100, 100], [10, height - 150], [width - 50, height - 50]])

   
    perspective_matrix = cv2.getPerspectiveTransform(original_points, transformed_points)


    perspective_transformed_frame = cv2.warpPerspective(frame, perspective_matrix, (width, height))

    return perspective_transformed_frame

cap = cv2.VideoCapture(r"C:\Users\Sakam\Don.mp4") 


if not cap.isOpened():
    print("Error opening video file")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

while True:
    ret, frame = cap.read()

    if not ret:
        break  
    transformed_frame = perspective_transform(frame)


    cv2.imshow('Original Frame', frame)
    cv2.imshow('Perspective Transformed Frame', transformed_frame)


    out.write(transformed_frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()

cv2.destroyAllWindows()
