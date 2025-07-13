

---

# Aeronous - Project README

This repository contains two main projects:

* **Frontend** (`aeronous-frontend/`): Angular application for the Target Tracking System UI
* **Backend** (`server/`): FastAPI server handling targets data and API endpoints

---

## Prerequisites

* Node.js (v16+ recommended for Angular frontend)
* npm (comes with Node.js)
* Python 3.10+
* pip (Python package manager)
* (Optional) Python virtual environment tool (e.g., `venv`)

---

## Installation & Running - Frontend (Angular)

1. Navigate to the frontend directory:

   ```bash
   cd aeronous-frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Run the development server:

   ```bash
   ng serve
   ```

   * The app will be available at: [http://localhost:4200](http://localhost:4200)

---

## Installation & Running - Backend (FastAPI)

1. Navigate to the backend directory:

   ```bash
   cd ../server
   ```

2. (Optional) Create and activate a Python virtual environment:

   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   *(If `requirements.txt` does not exist, install manually:)*

   ```bash
   pip install fastapi uvicorn
   ```

4. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```

   * The API will be available at: [http://localhost:8000](http://localhost:8000)

---

## Usage

* Make sure the backend server is running before starting the frontend
* The frontend calls the backend API at `http://127.0.0.1:8000` by default
* You can add, view, filter, and delete targets using the frontend UI

---

## Tips & Suggestions

* To change the API URL, edit the `apiUrl` variable in `aeronous-frontend/src/app/api.service.ts`
* You can extend the backend with more endpoints as needed
* Use `ng build` to create a production build of the frontend


