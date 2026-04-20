# 🚀 AI Adaptive Cyber Range Simulator

## 📌 Overview

This project is a **Cyber Range simulation system** that demonstrates real-time interaction between an **Attack module** and a **Defense module**. It provides a safe environment to understand how cyberattacks occur and how defensive systems detect and respond to them.

The system is built using Python and Streamlit, with communication between modules handled via a shared JSON file.

---

## 🎯 Features

* ⚔️ Separate Attack Interface
* 🛡️ Separate Defense Interface
* 📜 Centralized Logging System (Defense Side)
* 🔄 Real-time data sharing using JSON
* 🎛 Multiple attack types:

  * Brute Force
  * DoS (Denial of Service)
  * Port Scanning
* 🧠 Adaptive defense mechanism (blocks after repeated attacks)

---

## 🏗️ Project Structure

```
cyber-range/
│
├── attack_app.py       # Attack GUI (Streamlit)
├── defense_app.py      # Defense GUI (Streamlit)
├── shared_state.json   # Shared data file
├── README.md
```

---

## ⚙️ Technologies Used

* Python
* Streamlit
* JSON (for inter-process communication)
* Datetime & Time modules

---

## 🔁 How It Works

1. **Attack Module**

   * User selects attack type
   * Sends attack data to `shared_state.json`

2. **Defense Module**

   * Continuously monitors JSON file
   * Detects attack patterns
   * Logs events
   * Blocks attacker after threshold

3. **Logging**

   * Maintained only in Defense module
   * Displays attack type, timestamp, attempts, and block status

---

## ▶️ How to Run

### Step 1: Install dependencies

```
pip install streamlit
```

### Step 2: Start Attack App

```
streamlit run attack_app.py
```

### Step 3: Start Defense App (in new terminal)

```
streamlit run defense_app.py
```


## ⚠️ Notes

* Both apps must run simultaneously
* Uses file-based communication (not real-time network)
* Intended for educational purposes only

---

## 🚧 Limitations

* Basic rule-based detection
* No real network traffic analysis
* JSON-based communication may have minor delays

---

## 🔮 Future Improvements

* Replace JSON with sockets or APIs
* Add machine learning for detection
* Real-time dashboard visualization
* Deploy online for remote access

---

## 🧠 Concept

This project is based on **Cyber Range as a Service (CRaaS)**, where simulated cyber environments are used for training and testing without impacting real systems.

---
