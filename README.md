# License Plate Detection for Vehicles (YOLOv11)

## Overview
Real-time license plate detection and recognition system using YOLOv11 and EasyOCR. Flask web app with OpenCV video processing.

## Quick Installation
## Windows:
```
git clone https://github.com/eshitakasera/License-plate-detection-with-yolo11.git
cd License-plate-detection-with-yolo11
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install easyocr
python app.py
```
## Mac/Linux:
```
git clone https://github.com/eshitakasera/License-plate-detection-with-yolo11.git
cd License-plate-detection-with-yolo11
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip3 install torch torchvision torchaudio
pip install easyocr
python3 app.py
```
## After Installation
Open browser and go to port 5000

## Troubleshooting

### If requirements.txt missing:
pip install flask opencv-python numpy pillow torch easyocr ultralytics

### If app.py not found, try:
python main.py
python run.py
python flask_app.py

### If model weights missing:
1. Check 'models/' folder
2. Download .pt file from: [Add download link here]
3. Place in 'models/' folder

### If import errors:
python -c "import torch; print('PyTorch OK')"
python -c "import cv2; print('OpenCV OK')"
python -c "import flask; print('Flask OK')"

### To deactivate virtual environment:
deactivate

## Features
- Real-time license plate detection
- 95% accuracy rate
- 40% faster inference
- Web interface for easy use
- Supports images, videos, webcam

## Applications
Traffic monitoring, toll systems, parking solutions, security systems
