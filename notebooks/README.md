# ☀️ Solar Challenge: Week 0 - Git & Environment Setup

This repository establishes the foundational version control and **reproducible development environment** for the project.

---

## 🚀 Environment Setup Guide

To run this project locally, you must first create and activate a Python virtual environment.

### 1. Create & Activate Environment

The virtual environment directory is named `.venv`.

| OS | Command to Create | Command to Activate |
| :--- | :--- | :--- |
| **Linux/macOS** | `python3 -m venv .venv` | `source .venv/bin/activate` |
| **Windows (CMD)** | `python -m venv .venv` | `.venv\Scripts\activate.bat` |
| **Windows (PS)** | `python -m venv .venv` | `.venv\Scripts\Activate.ps1` |

### 2. Install Dependencies

Once the environment is active (you see `(.venv)` in your prompt), install all required libraries:

```bash
pip install -r requirements.txt