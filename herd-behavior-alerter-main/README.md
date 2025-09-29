# Real-time E-commerce Herd Behavior Alerter

## 🚀 Project Overview
Detects herd behavior in e-commerce when a product suddenly trends.

- **Backend:** FastAPI + WebSocket
- **Frontend:** React.js
- **Detection:** Z-score anomaly detection
- **Deployment:** Docker-ready

## 🛠️ How to Run
1. Start backend:
   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
   ```

2. Start frontend:
   ```bash
   cd frontend
   npm install
   npm start
   ```

3. Open `http://localhost:3000`
