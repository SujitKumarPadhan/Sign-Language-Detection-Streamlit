# 🤟 Real-Time Sign Language Detection System

An interactive **Real-Time Sign Language & Hand Gesture Detection** application built using **Streamlit**, **MediaPipe**, and **OpenCV**. The system captures live video from the webcam, extracts hand landmarks, and instantly classifies hand gestures in real time.

---

## 🚀 Features

- 🎥 Real-Time Video Processing using `streamlit-webrtc`
- ✋ 21-Point Hand Landmark Detection powered by MediaPipe
- ⚡ Instant Gesture Recognition
- 🎨 Live Skeleton & Text Overlay
- 🔊 Text-to-Speech Ready Architecture (`pyttsx3`)
- 🏗️ Modular Project Structure for easy expansion

---

## 🖐️ Supported Gestures

| Gesture | Description |
|----------|-------------|
| ✊ FIST | Closed Hand |
| ✋ FIVE | Open Palm |
| ☝️ ONE | Index Finger Up |
| ✌️ VICTORY | Peace Sign |
| 👍 THUMBS UP | Positive Gesture |
| 🤟 LOVE YOU | I Love You Sign |
| 📐 L | Letter "L" Gesture |

---

## 📂 Project Structure

```text
Sign-Language-Detection-Streamlit/
│
├── backend/
│   ├── camera_stream.py
│   ├── drawing_utils.py
│   ├── gesture_rules.py
│   ├── hand_landmarker.py
│   └── speaker.py
│
├── models/
│   └── hand_landmarker.task
│
├── app.py
├── req.txt
└── README.md
```

---

## 💻 Tech Stack

- **Frontend:** Streamlit
- **Computer Vision:** MediaPipe, OpenCV, PyAV
- **Language:** Python 3.9+

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Sign-Language-Detection-Streamlit.git
cd Sign-Language-Detection-Streamlit
```

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r req.txt
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

Open your browser and visit:

```text
http://localhost:8501
```

---

## 📷 How It Works

1. Open the application in your browser.
2. Allow webcam access.
3. Show a supported hand gesture.
4. MediaPipe detects hand landmarks.
5. Gesture rules classify the sign.
6. The detected gesture is displayed on the live video stream.

---
## 📸 Project Demo

## img-1
<img width="1457" height="1078" alt="Screenshot 2026-06-18 164614" src="https://github.com/user-attachments/assets/8a35445d-979f-4576-99ca-b450d695ef75" />

## img-2
<img width="1440" height="1078" alt="Screenshot 2026-06-18 165113" src="https://github.com/user-attachments/assets/a8586570-96eb-437f-a00f-4ff31bab324c" />

## img-3
<img width="1438" height="1078" alt="Screenshot 2026-06-18 164950" src="https://github.com/user-attachments/assets/8ed8440f-9037-48f7-a730-402bedea391a" />



## 🔮 Future Roadmap

- [ ] Machine Learning-based Gesture Classification
- [ ] Deep Learning Gesture Recognition
- [ ] Dynamic Text-to-Speech Feedback
- [ ] Continuous Sign-to-Sentence Conversion
- [ ] Multi-Hand Detection Support
- [ ] Custom Gesture Training Interface

---

## 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---
## 📜 License

This project is intended for educational and learning purposes.

---
## 👨‍💻 Author

**Sujit Kumar Padhan**

🔗 GitHub: https://github.com/your-github-username

💼 LinkedIn: https://www.linkedin.com/in/your-linkedin-username/

⭐ If you found this project useful, consider giving it a star on GitHub!
