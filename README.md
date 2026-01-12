🌱 Crop Disease Detection using MobileNetV2

📌 Overview

Crop Disease Detection using MobileNetV2 is a deep learning–based project that identifies and classifies crop diseases from leaf images. The system leverages MobileNetV2, a lightweight and efficient convolutional neural network, making it suitable for real-time and resource-constrained environments such as mobile and edge devices.

Early detection of crop diseases helps farmers take timely action, reduce crop loss, and improve agricultural productivity.

🎯 Objectives

i) Detect crop diseases from leaf images with high accuracy

ii) Utilize transfer learning for efficient model training

iii) Reduce computational cost using a lightweight CNN architecture

iv) Support precision and smart agriculture


🧠 Model Architecture

Base Model: MobileNetV2 (pretrained on ImageNet)

Approach: Transfer Learning + Fine-tuning

Input: RGB leaf images (resized & normalized)

Output: Multi-class disease classification using Softmax

MobileNetV2 is chosen for its balance between accuracy and efficiency, using depthwise separable convolutions.

🗂️ Dataset

Leaf images of healthy and diseased crops

Organized into class-wise folders

Includes multiple disease categories

Dataset split into:

Training set

Validation set

Test set

Dataset Link

https://data.mendeley.com/datasets/bwh3zbpkpv/1

⚙️ Technologies Used

Programming Language: Python

Deep Learning Framework: TensorFlow / Keras

Model: MobileNetV2

Libraries: NumPy, Pandas, Matplotlib, Scikit-learn


🔄 Project Workflow

Data collection and preprocessing

Image resizing and normalization

Data augmentation

Transfer learning using MobileNetV2

Model training and validation

Performance evaluation

Disease prediction


📊 Evaluation Metrics

Accuracy

Precision

Recall

F1-score

Confusion Matrix

The trained model achieves high accuracy while maintaining low computational complexity.

▶️ How to Run the Project

1️⃣ Clone the Repository

git clone https://github.com/Sriparna2002/Crop-Disease-Detection.git

cd Crop-Disease-Detection

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Train the Model

python train.py

4️⃣ Test / Predict

python predict.py

🚀 Applications

Smart agriculture systems

Mobile-based crop disease diagnosis

Agricultural decision support tools

Research and academic projects

🔮 Future Enhancements

Real-time disease detection using webcam or mobile camera

Web or mobile application deployment

Support for more crop varieties

Integration with IoT-based agricultural systems

🔮streamlit web app

<img width="876" height="426" alt="image" src="https://github.com/user-attachments/assets/02317584-38f0-453c-b887-108da9f3ffa1" />

Confusion Matrix

<img width="1094" height="864" alt="image" src="https://github.com/user-attachments/assets/eab7205d-dd72-4bc6-bc15-633f3b6780b4" />




🙋 Author

Sriparna Majumder

If you found this project helpful, please ⭐ the repository!
