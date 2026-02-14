# 🚀 DevOps Final Project -- Student Grade Pipeline

## 📌 Project Overview

This project demonstrates a complete DevOps CI/CD pipeline using:

-   Jenkins Controller (Windows)
-   Linux Agent (WSL Ubuntu)
-   GitHub SCM
-   Python automation script
-   Parameterized Pipeline
-   HTML Artifact generation

The pipeline calculates a student's final grade, generates a modern
styled HTML report (with animated UI & confetti effect), and publishes
it as a Jenkins artifact.

------------------------------------------------------------------------

## 🏗 Architecture

**Controller:** Windows (Built-in node)\
**Agent:** Linux (WSL Ubuntu)\
**SCM:** GitHub\
**Language:** Python 3\
**CI/CD Tool:** Jenkins

------------------------------------------------------------------------

## ⚙ Pipeline Features

-   Pipeline from SCM (Jenkinsfile)
-   Parameterized build:
    -   NAME (String)
    -   GRADE (Number)
    -   BONUS (Boolean)
    -   EXAM_DATE (Date)
-   Runs on:
    -   Windows Controller
    -   Linux Agent
-   HTML Artifact generation
-   Log file generation
-   Modern UI design
-   Confetti celebration effect (if PASSED 🎉)

------------------------------------------------------------------------

## 📊 Script Functionality

The Python script:

1.  Validates all input parameters
2.  Applies bonus points (if selected)
3.  Determines Pass/Fail status
4.  Generates:
    -   `report.html`
    -   `log.txt`
5.  Archives artifacts in Jenkins

------------------------------------------------------------------------

## 🧪 How to Run

### Windows (Built-in Node)

Select:

RUN_ON = built-in

### Linux Agent

Select:

RUN_ON = linux

Then click:

Build with Parameters

------------------------------------------------------------------------

## 📁 Project Structure

devops-final-project/ │ ├── script/ │ └── app.py │ ├── output/ │ ├──
Jenkinsfile │ └── README.md

------------------------------------------------------------------------

## 🎨 UI Highlights

-   Gradient animated background
-   Glassmorphism card design
-   Large dynamic grade display
-   Status color indicators
-   Floating confetti animation (on pass)
-   Responsive modern layout

------------------------------------------------------------------------

## 👨‍💻 Author

Shlomi\
DevOps Student Project
