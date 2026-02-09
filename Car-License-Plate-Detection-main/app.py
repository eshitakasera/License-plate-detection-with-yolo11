import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import easyocr
import os

# Page Config
st.set_page_config(page_title="License Plate Detector", layout="wide")

# --- AUTO CLEANUP CACHE ---
# Deployment ke waqt purani cache files delete karne ke liye
if st.button("Clear System Cache"):
    for file in os.listdir('.'):
        if file.endswith(".cache"):
            os.remove(file)
            st.success(f"Deleted {file}")

# --- MODEL LOADING ---
@st.cache_resource
def load_model():
    # PDF ke mutabiq model path: runs/detect/train6/weights/best.pt [cite: 280]
    # Agar model main folder mein hai toh sirf 'best.pt' likho
    model_path = 'best.pt' 
    model = YOLO(model_path)
    
    # 🔥 FIX: Labels overwrite (Manya Singhal -> License Plate)
    model.names = {0: 'License Plate'} 
    return model

# --- OCR INITIALIZATION ---
# PDF mein EasyOCR implemented bataya gaya hai [cite: 16, 46]
reader = easyocr.Reader(['en'])

model = load_model()

st.title("🚗 License Plate Detection & OCR System")
st.write("YOLOv11 Optimized Pipeline [cite: 2] | 94.1% Accuracy [cite: 6]")

uploaded_file = st.file_uploader("Upload Car Image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Image preprocessing
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    
    # 1. Detection Stage [cite: 156]
    results = model.predict(image, conf=0.25) # [cite: 127]
    
    # 2. Results Annotation [cite: 159]
    res_plotted = results[0].plot()
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original")
        st.image(image, channels="BGR", use_container_width=True)
    with col2:
        st.subheader("Detection Result")
        st.image(res_plotted, channels="BGR", use_container_width=True)

    # 3. OCR Stage (Extraction) [cite: 157, 158]
    st.divider()
    st.subheader("📝 Extracted Plate Information")
    
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        # Crop the plate [cite: 152]
        plate_crop = image[y1:y2, x1:x2]
        
        # Display cropped plate
        st.image(plate_crop, caption="Cropped Plate", width=200)
        
        # EasyOCR Text Recognition [cite: 66]
        ocr_result = reader.readtext(plate_crop)
        if ocr_result:
            text = ocr_result[0][-2]
            conf = ocr_result[0][-1]
            st.success(f"**Plate Number:** {text.upper()} (Confidence: {conf:.2%})")
        else:
            st.warning("Could not read text from this plate.")

# --- SYSTEM SPECS (From Status Report) ---
with st.sidebar:
    st.info("System Performance [cite: 222]")
    st.write("- **Model:** YOLOv11n")
    st.write("- **mAP50:** 94.1% [cite: 6]")
    st.write("- **Precision:** 96.6% [cite: 222]")
    st.write("- **Inference:** 2.3ms [cite: 222]")
