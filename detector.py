import cv2 as cv

def detect_video(input_path, output_path="output.avi"):

    net = cv.dnn.readNet("project_files/yolov4_tiny.weights",
                         "project_files/yolov4_tiny.cfg")

    net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

    model = cv.dnn_DetectionModel(net)
    model.setInputParams(size=(640, 480), scale=1/255, swapRB=True)

    cap = cv.VideoCapture(input_path)

    width  = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv.VideoWriter_fourcc(*'XVID')
    result = cv.VideoWriter(output_path, fourcc, 10, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        classes, scores, boxes = model.detect(frame, 0.5, 0.4)

        for (classid, score, box) in zip(classes, scores, boxes):
            if score >= 0.7:
                x, y, w, h = box
                cv.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
                cv.putText(frame,
                           f"{round(score*100,2)}% pothole",
                           (x, y-10),
                           cv.FONT_HERSHEY_SIMPLEX,
                           0.6,
                           (255,0,0),
                           2)

        result.write(frame)

    cap.release()
    result.release()

    return output_path
