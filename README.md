# 🌦️ Playwright & Pytest Automated Testing for OpenWeather 🌦️

This project automates the **testing of OpenWeather's web UI and API** using **Playwright & Pytest**.

## 📌 Features
- **✅ API Testing**: Verifies OpenWeather API responses and structure.
- **✅ UI Testing**: Automates city weather searches on OpenWeather's website.
- **✅ Playwright & Pytest**: End-to-end testing framework for both FE & BE.
- **✅ Fixtures for Test Setup**: Centralized test setup for API & UI testing.
- **✅ CI/CD Integration**: GitHub Actions for automated test execution.

---

## 🛠️ Installation & Setup

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/LumboIshinaja/openweather-tests.git
cd playwright_tests
```

### 2️⃣ **Create a Virtual Environment**
```sh
python -m venv venv
source venv/Scripts/activate  # macOS/Linux/Git Bash (Windows)
venv\Scripts\activate      # Windows CMD
venv\Scripts\Activate.ps1  # Windows PowerShell
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
playwright install
```

### 4️⃣ **Set API Key as Environment Variable**
```sh
export OPENWEATHER_API_KEY=your_api_key_here  # macOS/Linux/Git Bash (Windows)
set OPENWEATHER_API_KEY=your_api_key_here     # Windows CMD
$env:OPENWEATHER_API_KEY="your_api_key_here"  # Windows PowerShell
```

---

## 🏃 Running Tests

### **✅ Run All Tests**
```sh
pytest
```

### **✅ Run Only API Tests**
```sh
pytest -m api
```

### **✅ Run All UI Tests in Parallel**
```sh
pytest -m api -n auto
```

### **✅ Run Only UI Tests**
```sh
pytest -m ui
```

### **✅ Run All UI Tests in Parallel**
```sh
pytest -m ui -n auto
```

---

## 👤 CI/CD with GitHub Actions
The project includes **GitHub Actions** workflow to **automatically run tests** on every **push to `main`** and **pull request**:
- Located in `.github/workflows/ci.yml`
- Secrets configured via **GitHub → Repo → Settings → Secrets → Actions**:
  - `OPENWEATHER_API_KEY`

### **CI/CD Setup Summary:**
1. Automatically runs on **push to `main`** and **PRs targeting `main`**.
2. **API & UI tests** executed in a **Linux environment**.
3. API Key securely stored as **GitHub Secret**.


---

## 📂 Project Structure

```
playwright_tests/
│── .github/                   # CI/CD Workflows
│   └── workflows/
│       └── ci.yml             # GitHub Actions config
│ 
│── utils/                     # Utility functions & configurations
│   ├── config.py              # API key & base URLs
│   ├── api_client.py          # API request handler
│   ├── weather_models.py      # Pydantic models for API validation
│
│── pages/                     # Playwright Page Object Model (POM)
│   ├── main_page_search.py    # UI interactions for city search
│
│── tests/
│   │── tests_be/              # Backend API tests
│   │   ├── test_auth.py       # API auth validation
│   │   ├── test_status.py     # API status tests
│   │   ├── test_response.py   # API response validation
│   │
│   │── tests_fe/              # Frontend UI tests
│   │   ├── test_weather_ui.py # UI automation for city search
│
├── conftest.py                # Shared fixtures for API & UI tests
├── pytest.ini                 # Pytest configurations (markers, warnings)
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
```

---


## 📢 Creator
- **Milos Jovanovic** - Test Engineer

---
