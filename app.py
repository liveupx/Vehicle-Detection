from flask import Flask, render_template, request, redirect, url_for, Response
import cv2
import time
import numpy as np
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

car_classifier = cv2.CascadeClassifier('haarcascade_car.xml')

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = 'video.mp4'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('detect_vehicles'))

@app.route('/detect_vehicles')
def detect_vehicles():
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], 'video.mp4')
    video_cap = cv2.VideoCapture(video_path)

    total_cars = 0
    total_trucks = 0
    unique_vehicles = set()

    car_min_box_height = 80  # Set the minimum height threshold for bounding boxes for cars
    truck_min_box_height = 120 # Set the minimum height threshold for bounding boxes for trucks

    while video_cap.isOpened():
        time.sleep(.05)
        # Read first frame
        ret, frame = video_cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Pass frame to our car classifier
        cars = car_classifier.detectMultiScale(gray, 1.4, 2)

        # Extract bounding boxes for any cars or trucks identified
        for (x,y,w,h) in cars:
            if h >= car_min_box_height or h >= truck_min_box_height:  # Filter out detections below height threshold
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

        # Count the number of unique cars and trucks detected in this frame and add it to the total count
        for (x,y,w,h) in cars:
            if h >= car_min_box_height or h >= truck_min_box_height:  # Filter out detections below height threshold
                vehicle_id = str(x) + str(y) + str(w) + str(h)
                if vehicle_id not in unique_vehicles:
                    unique_vehicles.add(vehicle_id)
                    if h >= car_min_box_height:
                        total_cars += 1
                    else:
                        total_trucks += 1

        # Write the count onto the frame
        cv2.putText(frame, "Cars Detected: " + str(total_cars) + ", Trucks Detected: " + str(total_trucks), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Display the frame with count
        cv2.imshow('Cars and Trucks', frame)

        if cv2.waitKey(1) ==13: #13 is the Enter Key
            break

    print("Total number of unique cars detected: ", total_cars)
    print("Total number of unique trucks detected: ", total_trucks)

    video_cap.release()
    cv2.destroyAllWindows()

    return render_template('output.html', total_cars=total_cars, total_trucks=total_trucks)

from flask import Response

@app.route('/video_feed')
def video_feed():
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], 'video.mp4')
    video_cap = cv2.VideoCapture(video_path)

    def generate_frames():
        while video_cap.isOpened():
            ret, frame = video_cap.read()
            if not ret:
                break

            # Process the frame here if needed

            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
