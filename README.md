# HNG Backend Stage 0 Task: Dynamic Profile Endpoint

## Overview
This is a simple RESTful API built with Flask that returns my profile information and a random cat fact fetched from the Cat Facts API at https://catfact.ninja/fact.

## Endpoint
**GET /me**

## Setup Instructions
1. Clone this repo:
```
git clone https://github.com/IniPrec/Dynamic-Profile-Endpoint.git
```
2. Navigate to the project:
```
cd HNG-Backend
```
3. Create and activate virtual environment:
```
python -m venv venv
venv\Scripts\activate
```
4. Install dependencies:
```
pip install -r requirements.txt
```
5. Run the app:
```
python app.py
```
6. Visit:
```
http://127.0.0.1:5000/me
```