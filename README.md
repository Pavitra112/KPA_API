﻿# KPA_API
# 🚀 KPA Backend API Assignment

This project is a backend API service built with **Django REST Framework** to handle form submissions related to wheel specifications. It implements two key endpoints:

- ✅ `POST /api/forms/wheel-specifications` — Submit a wheel specification form
- ✅ `GET /api/forms/wheel-specifications` — Retrieve submitted forms with optional filters

---

## 📦 Tech Stack

| Tool/Tech        | Description                              |
|------------------|------------------------------------------|
| Django           | Backend framework (v4+)                  |
| Django REST      | API development                          |
| PostgreSQL / MySQL / SQLite | Supported DBs (you can switch easily) |
| JSONField        | Used to store nested `fields` data       |
| dotenv           | For environment-based configuration      |

---

## 📁 Project Setup

### 1. 📥 Clone or unzip this repo


git clone https://github.com/Pavitra112/KPA_API.git
cd kpa_project

### 2. 🐍 Create virtual environment and install dependencies
python -m venv venv
venv\Scripts\activate   
source venv/bin/activate 

pip install -r requirements.txt

### 3. 🛠️ Run migrations and start server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


# 🔌 API Endpoints
### 1. 🔻 POST /api/forms/wheel-specifications
Used to submit a new wheel specification form.

✅ Headers

Content-Type: application/json

✅ Request Body (Example)

{
  "form_number": "WHEEL-2025-001",
  "submitted_by": "user_id_123",
  "submitted_date": "2025-07-13",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "lastShopIssueSize": "837 (800-900)",
    "condemningDia": "825 (800-900)",
    "wheelGauge": "1600 (+2,-1)",
    "variationSameAxle": "0.5",
    "variationSameBogie": "5",
    "variationSameCoach": "13",
    "wheelProfile": "29.4 Flange Thickness",
    "intermediateWWP": "20 TO 28",
    "bearingSeatDiameter": "130.043 TO 130.068",
    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
    "rollerBearingWidth": "93 (+0/-0.250)",
    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
    "wheelDiscWidth": "127 (+4/-0)"
  }
}

✅ Successful Response

{
  "success": true,
  "message": "Wheel specification submitted successfully.",
  "data": {
    "formNumber": "WHEEL-2025-001",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-13",
    "status": "Saved"
  }
}


### 2. 🔍 GET /api/forms/wheel-specifications

✅ Response Example

{
  "success": true,
  "message": "Filtered wheel specification forms fetched successfully.",
  "data": [
    {
      "form_number": "WHEEL-2025-001",
      "submitted_by": "user_id_123",
      "submitted_date": "2025-07-13",
      "status": "Saved",
      "fields": {
        "treadDiameterNew": "915 (900-1000)",
        "lastShopIssueSize": "837 (800-900)",
        "condemningDia": "825 (800-900)",
        "wheelGauge": "1600 (+2,-1)"
      }
    }
  ]
}




