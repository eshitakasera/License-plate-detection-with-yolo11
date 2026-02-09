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

---

## 📂 Project Structure
```plaintext
.
├── Car-License-Plate-Detection-main/
│   ├── app.py                # Flask/Streamlit Web App
│   └── yolo11n.pt            # Fine-tuned Weights
├── requirements.txt          # PyTorch, OpenCV, EasyOCR, etc.
├── packages.txt              # libGL system dependencies
└── README.md                 # Project Documentation
