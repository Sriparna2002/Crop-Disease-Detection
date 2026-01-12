import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import base64
# -------------------------------------------------------------------
# 🔹 FUNCTION TO ADD BACKGROUND IMAGE
# -------------------------------------------------------------------
def add_bg_image(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
# Add your background image file here
add_bg_image("img_1.avif")   
# -------------------------------------------------------------------
# Load Saved Model
# -------------------------------------------------------------------
MODEL_PATH = "best_mobilenet_model.keras"
model = tf.keras.models.load_model(MODEL_PATH)
# -------------------------------------------------------------------
# Class Names
# -------------------------------------------------------------------
class_names = [
    'Cashew_anthracnose', 'Cashew_gumosis', 'Cashew_healthy', 'Cashew_leaf miner',
    'Cashew_red rust', 'Cassava_bacterial blight', 'Cassava_brown spot',
    'Cassava_green mite', 'Cassava_healthy', 'Cassava_mosaic',
    'Maize_fall armyworm', 'Maize_grasshoper', 'Maize_healthy',
    'Maize_leaf beetle', 'Maize_leaf blight', 'Maize_leaf spot',
    'Maize_streak virus', 'Tomato_healthy', 'Tomato_leaf blight',
    'Tomato_leaf curl', 'Tomato_septoria leaf spot', 'Tomato_verticulium wilt'
]
# -------------------------------------------------------------------
# Streamlit UI
# -------------------------------------------------------------------
st.set_page_config(page_title="Crop Pest & Disease Detection", page_icon="🌱", layout="centered")
st.title("🌱 Crop Pest & Disease Detection")
st.write("Upload a leaf image to identify the crop disease using your fine-tuned MobileNetV2 model.")
st.markdown("---")
# Upload Section ---------------------------------------------------------
uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "jpeg", "png"])
# Prediction Helpers -----------------------------------------------------
def preprocess(image):
    img = image.resize((224, 224))
    img_arr = tf.keras.utils.img_to_array(img)
    img_arr = img_arr / 255.0
    img_arr = np.expand_dims(img_arr, axis=0)
    return img_arr
def predict(image):
    processed = preprocess(image)
    preds = model.predict(processed)
    pred_class = np.argmax(preds[0])
    confidence = preds[0][pred_class]
    return pred_class, confidence
# Display + Prediction ---------------------------------------------------
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(image, caption="Uploaded Image", width=250)
    with col2:
        if st.button("🔍 Predict Disease"):
            with st.spinner("Analyzing image..."):
                label_index, confidence = predict(image)
            st.success(f"### Prediction: **{class_names[label_index]}**")
            st.info(f"Confidence: **{confidence*100:.2f}%**")
else:
    st.info("👆 Upload a leaf image to begin.")
