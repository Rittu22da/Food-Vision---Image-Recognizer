
<img width="1919" height="912" alt="image" src="https://github.com/user-attachments/assets/8a5b463f-a73d-4596-8c90-737b699f1afa" />


🍔 Food Vision – Food Image Classification using EfficientNetB0

Food Vision is an end-to-end deep learning computer vision project that classifies food images into 101 different categories using EfficientNetB0 with transfer learning.
The project includes model training, evaluation, and a Flask-based web interface for real-time food image prediction.

📌 Project Highlights

🔍 101-class food image classification

🧠 EfficientNetB0 pretrained on ImageNet

⚡ Optimized tf.data input pipeline

📊 TensorBoard training visualization

💾 Model checkpointing for best weights

🌐 Flask web app for image upload & prediction

🎓 Designed as a college final-year ML project

🧠 Technologies & Tools Used

Python

TensorFlow / Keras

TensorFlow Datasets (Food-101)

EfficientNetB0

Flask

HTML / CSS

NumPy, Matplotlib

TensorBoard


📊 Dataset Information

Dataset: Food-101

Classes: 101 food categories

Source: TensorFlow Datasets (TFDS)

Images: Real-world food images with varied backgrounds

🏗️ Model Architecture

Input Layer: 224 × 224 × 3

Pretrained EfficientNetB0 (ImageNet weights, frozen initially)

Global Average Pooling

Dense Layer (101 units)

Softmax activation for multi-class classification

⚙️ Training Strategy
Phase 1 – Feature Extraction

Base EfficientNetB0 frozen

Trains only classification head

Faster and stable training

Phase 2 – Fine-Tuning (Optional)

Unfreeze top layers of EfficientNet

Improves food-specific feature learning

Optimization Details

Optimizer: Adam

Loss: Sparse Categorical Cross-Entropy

Metric: Accuracy

Callbacks: ModelCheckpoint, TensorBoard

📈 Model Performance

Feature Extraction Accuracy: ~30–50%

Fine-Tuned Accuracy: ~60–75%

Accurate predictions on real-world images

(Performance depends on hardware and training duration)

🔍 Inference Pipeline

Upload food image

Image resized & normalized using EfficientNet preprocessing

Model predicts class probabilities

Highest probability class selected

Result displayed with confidence score

🌐 Flask Web Application

The project includes a simple Flask-based web interface:

Upload food image

Get predicted food category

View prediction confidence

Responsive UI with CSS styling

Run Flask App
python app.py


Open browser at:

http://127.0.0.1:5000/

🚀 How to Run the Project
1️⃣ Clone Repository
git clone https://github.com/your-username/food-vision.git
cd food-vision

2️⃣ Install Dependencies
pip install tensorflow tensorflow-datasets flask numpy matplotlib

3️⃣ Train the Model

Open and run:

vision.ipynb

4️⃣ Run Web App
python app.py

🎓 Academic Significance

This project demonstrates:

Practical application of CNNs

Real-world transfer learning

Model optimization on limited hardware

End-to-end ML project workflow

Deployment using Flask

🧠 Key Learnings

Transfer learning with pretrained CNNs

Efficient data preprocessing using tf.data

Debugging model training & inference pipelines

Model checkpointing & evaluation

Integrating ML models with web applications

📜 License

This project is intended for educational and academic purposes only.

✨ Author

Ritesh Kumar Singh
Final-Year Machine Learning Project
Food Vision – Food Image Classification System
