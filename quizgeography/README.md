# 🌍 Geography Quiz — CLI Game

An interactive, educational, and modern Command Line Interface (CLI) quiz game built with Python. This project tests users on fascinating and curious facts about world geography while delivering an engaging terminal user experience.

---

## 🚀 Features

* **Object-Oriented Architecture (OOP):** Built using robust and modular code structure with distinct classes for separation of concerns (`Question` and `QuizManager`).
* **Dynamic UI Elements:** Displays a custom text-based progress bar (`████░░░░`) that tracks your current score in real-time.
* **Safe File Handling:** Implements `os.path` utilities to automatically detect and resolve paths for the questions data file, ensuring standard-of-industry crash protection.
* **Robust Input Sanitization:** Gracefully handles unexpected user inputs, spacing, and casing seamlessly.

---

## 🛠️ Tech Stack & Concepts Applied

* **Language:** Python 3.x
* **Data Format:** JSON (for scalable question management)
* **Core Concepts:**
    * Object-Oriented Programming (OOP) — Classes, Attributes, and Methods
    * Dynamic State Management
    * File I/O (`json`, `utf-8` encoding)
    * Environment/Path Management (`os`)

---

## 📂 Project Structure

```text
quizgeography/
├── geographyquiz.py   # Main executable script containing game logic and classes
└── questions.json     # Encrypted data file containing questions, options, and keys

🎮 How to Run
1. Clone this repository to your local machine:
    git clone [https://github.com/priscilamouracodestudio-creator/quizgeography.git](https://github.com/priscilamouracodestudio-creator/quizgeography.git)

2. Navigate to the project directory:    
    cd primeirosprogramas/quizgeography

3. Run the script:
    python geographyquiz.py 

💡 Code Highlights
This project marks a significant evolution from traditional procedural scripting to Object-Oriented Programming (OOP).

Separation of Concerns
Question Class: Manages individual question schemas and handles encapsulating its own verification logic via is_correct().

QuizManager Class: Handles game loop orchestrations, score rendering, and cross-platform file parsing safely.

Developed with 💻 by Priscila Moura.    