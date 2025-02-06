# 🌦️ Playwright & Pytest Automated Testing for OpenWeather 🌦️

This project automates the **testing of OpenWeather's web UI and API** using **Playwright & Pytest**.

## 📌 Features
- **✅ API Testing**: Verifies OpenWeather API responses and structure.
- **✅ UI Testing**: Automates city weather searches on OpenWeather's website.
- **✅ Playwright & Pytest**: End-to-end testing framework for both FE & BE.

---

## 🛠️ Installation & Setup

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/your-repo-name.git
cd playwright_tests
```

### 2️⃣ **Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
playwright install
```

### 4️⃣ **Set API Key as Environment Variable**
```sh
set OPENWEATHER_API_KEY=your_api_key_here  # Windows
export OPENWEATHER_API_KEY=your_api_key_here  # macOS/Linux
```

---

## 🏃 Running Tests

### **✅ Run All Tests**
```sh
pytest
```

### **✅ Run Only API Tests**
```sh
pytest tests/tests_be/
```

### **✅ Run Only UI Tests (Headless)**
```sh
pytest tests/tests_fe/
```

### **✅ Run UI Tests in Visible Browser**
```sh
pytest tests/tests_fe/ --headed
```

---

## 📂 Project Structure

```
playwright_tests/
│── utils/                     # Utility functions & configurations
│   ├── config.py              # API key & base URLs
│   ├── api_client.py          # API request handler
│   ├── weather_models.py      # Pydantic models for API validation
│
│── pages/                     # Playwright Page Object Model (POM)
│   ├── weather_page.py        # UI interactions for weather search
│
│── tests/
│   │── tests_be/              # Backend API tests
│   │   ├── test_status.py     # API status tests
│   │   ├── test_response.py   # API response validation
│   │
│   │── tests_fe/              # Frontend UI tests
│   │   ├── test_weather_ui.py # UI automation for city search
│
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
```

---

## 📝 Future Improvements
- 🔹 **Expand test coverage** (e.g., multi-city search, forecast validation).
- 🔹 **Integrate with CI/CD pipelines** (GitHub Actions, Jenkins).
- 🔹 **Improve error handling & logging**.

---

## 📢 Contributors
- **[Your Name]** - Test Engineer

---

### 🚀 **Happy Testing!**
