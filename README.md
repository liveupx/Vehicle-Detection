
```markdown
# Vehicle Detection and Counting

![Vehicle Detection](https://img.shields.io/badge/Computer%20Vision-OpenCV-blue) ![Flask](https://img.shields.io/badge/Framework-Flask-orange)

## Introduction
The **Vehicle Detection and Counting** web application is a powerful tool designed to detect and count vehicles from a video stream using computer vision techniques and machine learning algorithms. Built with Python, OpenCV, and Flask, this application offers a user-friendly web interface to analyze vehicle traffic in real-time.

## Features
- Vehicle detection using OpenCV's built-in algorithms.
- Real-time counting of vehicles (cars, trucks, etc.).
- Simple web-based UI for easy video uploads and processing.
- Visualization of detected vehicles with bounding boxes overlaid on the video.

## Project Architecture
The project consists of two main components:
### 1. **Object Detection Algorithm**
   - Uses OpenCV to detect vehicles in a video stream.
   - Haar-like features and the Viola-Jones algorithm are employed for vehicle detection.
   - Bounding boxes are drawn around detected vehicles.

### 2. **Web Application**
   - Built with the Flask framework.
   - Provides an interface for uploading videos and viewing the processed output.
   - Displays the total vehicle count on the web page.

## Files Explanation
- **app.ipynb**: Initial implementation of the vehicle detection algorithm in Jupyter Notebook.
- **app.py**: Main Flask application file for running the web server and vehicle detection.
- **index.html**: Frontend web page structure, includes video uploading and results display.
- **video.mp4**: Input video file used for vehicle detection.
  
## Functionality
The "Vehicle Detection and Counting" application follows this flow:
1. User uploads a video file via the web interface.
2. The video is processed using OpenCV, with vehicles being detected frame by frame.
3. Bounding boxes are drawn around each detected vehicle.
4. The total number of vehicles passing through the video is counted.
5. The processed video with vehicle counts is displayed on the web interface.

## Block Diagram

```
User Uploads Video -> Video Processing with OpenCV -> Vehicle Detection -> Bounding Boxes Displayed -> Vehicle Count Displayed
```

## How to Use the Application
1. Open the web browser and access the application URL.
2. Upload the video file by clicking on the "Upload Video" button.
3. Once uploaded, click on "Process Video" to analyze the video.
4. Wait for processing to complete, and view the processed video with bounding boxes and vehicle count displayed on the webpage.

## Demo Video

Check out the demo video below to see the project in action:

[![Vehicle Detection Demo](https://img.youtube.com/vi/lVJgxExK2xg/0.jpg)](https://www.youtube.com/watch?v=lVJgxExK2xg)

## Setup Instructions

To run the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/liveupx/Vehicle-Detection.git
   cd Vehicle-Detection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open a browser and navigate to `http://127.0.0.1:5000/` to use the application.

## References
- [OpenCV Vehicle Detection & Speed Estimation](https://pyimagesearch.com/2019/12/02/opencv-vehicle-detection-tracking-and-speed-estimation/)
- [TechVidvan OpenCV Vehicle Detection](https://techvidvan.com/tutorials/opencv-vehicle-detection-classification-counting/)
- [AR Research Publication](http://www.arresearchpublication.com/images/shortpdf/286a.pdf)
- [Core.ac.uk PDF](https://core.ac.uk/download/pdf/83533829.pdf)
- [Jetir.org Paper](https://www.jetir.org/papers/JETIRFM06016.pdf)

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**GitHub Repository**: [Vehicle Detection](https://github.com/liveupx/Vehicle-Detection)
```

This `README.md` covers all the essential details about the project and provides easy navigation for users. 
