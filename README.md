# License Plate Detection for Vehicles (YOLOv11)
## Overview
This project implements an ML-based License Plate Detection and Recognition system for vehicles.  
The core detection model is YOLOv11, fine-tuned on a custom dataset for accurate license plate localization.  
For end-to-end recognition, EasyOCR is used to extract text from detected license plates.

The system is deployed as a Flask-based web application and supports real-time video stream processing using OpenCV.

## Key Features
- Fine-tuned YOLOv11 model for license plate detection
- End-to-end pipeline: detection + text recognition
- Real-time video stream processing
- Flask-based web application interface
- Optimized inference pipeline with reduced latency
- Suitable for real-world deployment scenarios

## Performance
- ~95% accuracy in license plate detection and recognition
- ~40% reduction in inference time after pipeline optimization
- Maintains high precision while improving speed

## Applications
- Traffic monitoring systems
- Automated toll collection
- Smart parking solutions
- Vehicle surveillance and security systems

## Tech Stack
- Python
- YOLOv11
- PyTorch
- OpenCV
- Flask
- EasyOCR
  
## Project Workflow
1. Input image/video stream is captured using OpenCV
2. YOLOv11 detects license plates in each frame
3. Detected plate regions are cropped
4. EasyOCR extracts text from cropped license plates
5. Results are displayed through a Flask web application

## Installation
git clone https://github.com/eshitakasera/License-plate-detection-with-yolo11.git
cd License-plate-detection-with-yolo11
pip install -r requirements.txt
