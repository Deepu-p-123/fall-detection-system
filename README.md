# 🛡️ Fall Detection System Using Deep Learning

An IoT-based real-time fall detection system that uses **YOLOv11** and **ESP32-CAM** to monitor individuals and send instant alerts via **Telegram** when a fall is detected.

> 📌 **MSc Computer Science (AI) — Department of Computer Science**
> 
> **Team Members:**
> - Deepu P 
> - Revathy R.K 
> - Sreelakshmi L 

---

## 📋 Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Proposed Solution](#proposed-solution)
- [System Architecture](#system-architecture)
- [Hardware Components](#hardware-components)
- [Software Components](#software-components)
- [Dataset](#dataset)
- [YOLO11 Detection Pipeline](#yolo11-detection-pipeline)
- [Results](#results)
- [Advantages](#advantages)
- [Limitations](#limitations)
- [Applications](#applications)
- [Future Enhancements](#future-enhancements)
- [References](#references)

---

## 📖 Overview

Falls are one of the leading causes of injury among elderly people. With the aging population rapidly increasing worldwide, many older adults live alone without continuous supervision. Delayed medical assistance after a fall can lead to serious complications or even death.

This system provides an **automated, AI-powered fall detection solution** that enables immediate alerts and faster response times — without requiring any user interaction.

---

## ❗ Problem Statement

Current home security systems are **passive** — they record video but don't *understand* what is happening. If an elderly person falls, the camera just watches; it doesn't call for help. If a fall goes undetected for hours, it can lead to serious injury or death.

---

## 💡 Proposed Solution

This project uses **YOLO11** and a **Low-Cost ESP32-CAM** to create a system that:

- ✅ **Sees** the fall using computer vision
- ✅ **Analyzes** the situation instantly without human help
- ✅ **Triggers** a buzzer on fall confirmation
- ✅ **Sends alerts** to caregivers via **Telegram** — only when a fall is actually detected

---

## 🔧 System Architecture

### Workflow

```
Video Acquisition → Preprocessing → Frame Processing
        ↓
Fall Detection using AI (YOLO11)
        ↓
Fall Confirmation Logic (5-second check)
        ↓
Alert Generation (Buzzer + Image Capture)
        ↓
Notification System (Telegram Alert)
        ↓
Continuous Monitoring (with cooldown)
```

### Step-by-Step Breakdown

| Step | Description |
|------|-------------|
| **1. Video Capture** | ESP32-CAM / system camera captures real-time video |
| **2. Preprocessing** | OV2640 sensor compresses to JPEG; frames scaled to 320×240px; image normalization |
| **3. Frame Processing** | Video stream divided into individual frames |
| **4. Fall Detection** | Each frame processed using YOLO11 to detect human posture |
| **5. Fall Confirmation** | Fall confirmed only if condition persists for **5 seconds** (reduces false positives) |
| **6. Alert Generation** | Buzzer triggered + image of the frame captured |
| **7. Notification** | Alert sent via Telegram with warning message + captured image |
| **8. Continuous Monitoring** | System resumes monitoring with a cooldown mechanism |

---

## 🔩 Hardware Components

| Component | Purpose |
|-----------|---------|
| **ESP32-CAM** | Captures real-time video for monitoring |
| **ESP32** | Handles IoT communication and alert triggering |
| **Buzzer Module** | Generates an audible alert during fall detection |
| **Power Supply** | Powers the entire system |
| **Wi-Fi Module** (built-in ESP32) | Enables internet connectivity for Telegram alerts |
| **FTDI Programmer** | Used for programming the ESP32-CAM |

---

## 💻 Software Components

| Software | Role |
|----------|------|
| **Python** | Core system development |
| **OpenCV** | Image and video processing |
| **Ultralytics YOLO** | Detects human posture and fall events |
| **VS Code** | Development environment |
| **Roboflow / Open Images Dataset** | Training data source |

---

## 📊 Dataset

**Dataset:** UR Fall Detection Dataset

| Property | Value |
|----------|-------|
| Total Images | **11,936** |
| Fall Images | 2,995 |
| Non-Fall Images | 8,941 |
| Train Split | 80% |
| Test Split | 10% |
| Validation Split | 10% |

### Class Index Mapping

| Class Index | Label |
|-------------|-------|
| 0 | Violence |
| 1 | Fall |
| 2 | Sit |
| 5 | Standing |

---

## 🧠 YOLO11 Detection Pipeline

### 1. Input & Data Preprocessing
- **Letterboxing:** Resizes image to a fixed square while preserving aspect ratio using padding
- **Normalization:** Converts pixel values from RGB (0–255) to float range (0.0–1.0)

### 2. Feature Extraction (Backbone)
- **C3k2 Blocks:** Cross-Stage Partial bottlenecks with smaller kernels for efficient deep feature extraction
- **C2PSA (Position-Sensitive Attention):** Helps distinguish the human subject from complex backgrounds

### 3. Feature Fusion (Neck)
- **PANet (Path Aggregation Network):** Combines low-level spatial features with high-level semantic features for accurate detection even with occlusion

### 4. Prediction & Regression (Head)
Decoupled Task-Aligned Head performs three simultaneous tasks:
- **Classification:** Determines probability that the object is a "Person"
- **Bounding Box Regression:** Predicts precise coordinates (x, y, w, h)
- **Keypoint Estimation:** Tracks 17 skeletal joints to analyze body posture

### 5. Post-Processing
- **Confidence Thresholding:** Filters out weak detections
- **NMS (Non-Maximum Suppression):** Eliminates overlapping redundant boxes

---

## 📈 Results

| Metric | Value |
|--------|-------|
| **Recall (Sensitivity)** | 86.3% |
| **Precision** | 78.2% |
| **mAP@50** | 81.9% |
| **Fitness Score** | 0.687 |

---

## ✅ Advantages

- ⚡ **Real-Time Detection** — Detects falls instantly and reduces response time
- 🎯 **High Accuracy** — Uses Ultralytics YOLO for reliable detection
- 🤖 **Fully Automated** — No user interaction required
- 🕐 **24/7 Monitoring** — Continuous camera-based surveillance
- 📲 **Immediate Alerts** — Fast Telegram notifications to caregivers
- 💰 **Cost-Effective** — Uses affordable hardware components
- 🛡️ **Improves Safety** — Ensures timely assistance for elderly and patients

---

## ⚠️ Limitations

- 🌑 **Lighting Dependency** — May not work well in low-light or night conditions
- ❌ **False Positives/Negatives** — May occasionally misclassify activities (e.g., sitting vs. falling)
- 📷 **Camera Coverage** — Falls outside camera's field of view cannot be detected
- 📶 **Internet Dependency** — Requires stable Wi-Fi connection for IoT alerts
- 🔒 **Privacy Concerns** — Continuous video monitoring may raise privacy issues
- ⚙️ **Hardware Constraints** — Limited processing power of IoT devices may affect performance

---

## 🌐 Applications

| Domain | Use Case |
|--------|----------|
| **Elderly Care Homes** | Monitor senior citizens and provide immediate assistance |
| **Hospitals** | Continuous patient monitoring and emergency response |
| **Smart Homes** | Integration with home automation systems |
| **Rehabilitation Centers** | Track patient movements during recovery |
| **Assisted Living** | Support individuals with disabilities or mobility issues |
| **Home Care** | For patients living alone who need constant monitoring |

---

## 🚀 Future Enhancements

- 📱 **Mobile App Integration** — Real-time alerts and monitoring dashboard
- 🌙 **Night Vision** — Infrared camera support for low-light environments
- 🔊 **Voice Alert System** — Audio alerts or emergency voice assistance
- 📍 **GPS Tracking** — Location tracking during emergencies
- ☁️ **Cloud Integration** — Store data and alerts on cloud platforms
- 🤖 **Improved AI Models** — Advanced detection beyond current YOLO
- ⌚ **Wearable + Vision Hybrid** — Combine sensors with camera detection for better reliability

---

## 📚 References

- [Ultralytics YOLO Documentation](https://docs.ultralytics.com)
- [OpenCV Documentation](https://opencv.org)
- [Roboflow](https://roboflow.com)
- [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html)

---

## 📄 Presentation

The full project presentation is available in this repository: [`Fall_Detection_System_Presentation.pptx`](./Fall_Detection_System_Presentation.pptx)

---

*© 2024 — MSc CS AI Department of Computer Science*
