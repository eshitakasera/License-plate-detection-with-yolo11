# 🚗 License Plate Detection for Vehicles (YOLOv11)

An end-to-end **Automated License Plate Recognition (ALPR)** system featuring a fine-tuned **YOLOv11** model for high-precision object detection and **EasyOCR** for robust text extraction. This solution is optimized for real-world deployment in traffic monitoring and smart parking systems.

---

## 🔗 Live Demo
Experience the deployment here:  
👉 **[ALPR Live Application](https://license-plate-detection-with-yolo11-onocmqkvxqdyzu6zgxgztz.streamlit.app/)**

---

## 🛠️ Tech Stack
* **Core Logic:** Python, PyTorch
* **Object Detection:** YOLOv11 (Fine-tuned on custom datasets)
* **Computer Vision:** OpenCV (Real-time stream processing)
* **OCR Engine:** EasyOCR
* **Web Framework:** Flask / Streamlit (Current deployment on Streamlit for cloud ease)

---

## 🚀 Key Highlights & Optimizations
* **Fine-Tuned YOLOv11:** Custom-trained model achieving **~95% accuracy** in detecting and recognizing license plates across diverse environments.
* **40% Inference Speedup:** Optimized the detection pipeline, reducing inference time to **2.3ms** without compromising precision—making it ideal for high-speed traffic monitoring.
* **Robust Processing:** Implemented OpenCV-based preprocessing to handle real-time video streams and complex environmental conditions.
* **End-to-End Extraction:** Seamlessly integrates detection and character recognition to provide instant alphanumeric output.

---

## 📊 System Performance Metrics
| Metric | Value |
| :--- | :--- |
| **Model** | YOLOv11n (Custom Fine-tuned) |
| **Detection Accuracy** | ~95% |
| **mAP50** | 94.1% |
| **Precision** | 96.6% |
| **Inference Time** | 2.3ms (Optimized by 40%) |

---

## 🌍 Real-World Use Cases
This system is designed for scalability in:
* **Traffic Monitoring:** Tracking vehicle flow and identifying violations.
* **Automated Toll Systems:** Seamless toll collection via high-speed plate recognition.
* **Smart Parking:** Automated entry/exit management for residential and commercial spaces.
* **Security Systems:** Enhanced surveillance for restricted areas.
```

## 📂 Project Structure


├── Car-License-Plate-Detection-main/
│   ├── app.py                # Flask/Streamlit Web App
│   └── yolo11n.pt            # Fine-tuned Weights
├── requirements.txt          # PyTorch, OpenCV, EasyOCR, etc.
├── packages.txt              # libGL system dependencies
└── README.md                 # Project Documentation
```


 🖼️ Result Analysis & Pipeline Workflow

The system uses a sequential dual-stage pipeline to ensure maximum accuracy in character extraction.

🔍 Stage 1: Plate Localization (YOLOv11)
* **Detection**: The fine-tuned YOLOv11 model identifies the vehicle and draws a high-precision bounding box around the license plate.
* **Visualization**: The application displays the original image alongside the "Detection Result" highlighting the localized plate.

📝 Stage 2: Character Recognition (EasyOCR)
* **Image Cropping**: The detected plate area is automatically cropped and pre-processed for clarity.
* **OCR Extraction**: EasyOCR identifies alphanumeric characters and outputs the plate number (e.g., **GSTBS**).
* **Confidence Scoring**: Each extraction includes a confidence percentage (e.g., **65.10%**) to indicate result reliability.

| Process Step | Visual Output | Data Extracted |
| :--- | :--- | :--- |
| **Localization** | Bounding Box Overlay | Plate Coordinates |
| **Recognition** | Cropped Plate View | Alphanumeric String |
| **Validation** | Confidence Metric | Probability Score |


> [!TIP]
> System Intelligence: If a plate is too blurry or obscured, the system flags a "Could not read text" warning to prevent incorrect data capture, ensuring high data integrity for real-world use.

## 🛠️ Installation & Local Setup

Follow these steps to get a local copy of the project up and running on your machine.

### 📋 Prerequisites & Environment
* **Python 3.11+**: Ensure Python is installed on your system.
* **System Dependencies**: OpenCV requires certain libraries (like `libGL`) which are listed in `packages.txt`.
* **Git**: To clone the repository.

### ⚙️ Execution Commands

 1. Clone the repository
git clone [https://github.com/eshitakasera/License-plate-detection-with-yolo11.git](https://github.com/eshitakasera/License-plate-detection-with-yolo11.git)
cd Car-License-Plate-Detection-main

 2. Create and activate a virtual environment (Recommended)
python -m venv venv
# For Windows:
venv\Scripts\activate
# For Mac/Linux:
source venv/bin/activate

 3. Install all required Python libraries
This includes ultralytics, easyocr, streamlit, and opencv-python-headless
pip install -r requirements.txt

4. Launch the application
Run the streamlit app located in the main sub-folder
streamlit run Car-License-Plate-Detection-main/app.py
🚗 Car License Plate Detection & Recognition (YOLOv11 + EasyOCR)

An end-to-end computer vision pipeline designed to detect vehicle license plates and extract alphanumeric text with high precision. This project leverages the state-of-the-art **YOLOv11** for object detection and **EasyOCR** for robust character recognition.

