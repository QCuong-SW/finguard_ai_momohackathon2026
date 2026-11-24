# 🛡️ FinGuard AI – Your Intelligent Financial Guardian
> **Dự án dự thi MoMo Hackathon 2026**  
> Trợ lý tài chính thông minh: Chủ động nhận diện lừa đảo, bảo vệ dòng tiền số và tối ưu quyết định tài chính cá nhân hóa.

---

## 🚀 Khung Công Nghệ (Tech Stack)
* **Frontend:** Next.js 14 (App Router) + React + Tailwind CSS + Lucide Icons
* **Backend:** NestJS (TypeScript) + TypeORM + JWT Auth + Swagger API Docs + PII Masking
* **Database:** PostgreSQL 17 (chạy cùng Docker) + pgAdmin
* **AI Engine:** Python (FastAPI) + RAG Pipeline + ChromaDB + Anomaly Detection + Explainable AI (XAI)

---

## 📂 Cấu Trúc Mã Nguồn (Directory Structure)

```text
finguard_ai_momohackathon2026/
├── docker-compose.yml              # Quản lý PostgreSQL 17, PgAdmin, Backend, Frontend, AI Engine
├── .env.example                    # File mẫu biến môi trường
├── docs/                           # Tài liệu thiết kế kiến trúc & Mock specs
│   └── FINGUARD_ARCHITECTURE_AND_MOCK.md
├── frontend/                       # [THÀNH VIÊN 1: FRONTEND]
│   ├── src/
│   │   ├── app/                    # Next.js App Router (Dashboard, Scan, Finance, RAG, Advisor)
│   │   ├── components/             # Reusable UI components
│   │   └── services/               # API Client & Mock Data JSON
│   ├── tailwind.config.js
│   └── package.json
├── backend/                        # [THÀNH VIÊN 2: BACKEND + DB]
│   ├── src/
│   │   ├── database/init.sql       # Script khởi tạo 7 bảng dữ liệu PostgreSQL 17
│   │   ├── common/middlewares/     # PII Masking Middleware (bảo vệ quyền riêng tư)
│   │   └── modules/                # Scam, Finance, RAG, Incidents, Auth, AiBridge
│   └── package.json
└── ai_engine/                      # [THÀNH VIÊN 3: AI ENGINEER]
    ├── pipelines/                  # OCR, Scam XAI, RAG Engine, Anomaly Detector, Persona Advisor
    ├── prompts/                    # Prompts chuyên biệt cho từng tác vụ AI
    ├── knowledge_base/             # Dữ liệu cẩm nang phòng chống lừa đảo (NCSC, BCA)
    └── server.py                   # FastAPI service phục vụ internal endpoints
```

---

## ⚡ Hướng Dẫn Khởi Chạy Nhanh (Quick Start)

### 1. Khởi động Cơ sở dữ liệu PostgreSQL 17 (Docker)
Chạy lệnh sau tại thư mục gốc:
```bash
docker compose up -d postgres pgadmin
```
* **PostgreSQL 17** lắng nghe tại cổng `5432`.
* **PgAdmin** truy cập tại: `http://localhost:5050` (Email: `admin@finguard.ai` / Pass: `admin_finguard_2026`).

---

### 2. Dành cho Thành viên 1: Frontend (Next.js + Tailwind CSS)
Thành viên Frontend có thể lập trình giao diện ngay lập tức với dữ liệu Mock mà không cần đợi Backend/AI:
```bash
cd frontend
npm install
npm run dev
```
* Ứng dụng chạy tại: **http://localhost:3000**
* *Ghi chú:* Biến `NEXT_PUBLIC_USE_MOCK=true` trong file `next.config.js` cho phép dùng toàn bộ mock data đã chuẩn bị sẵn trong `src/services/mockData/`.

---

### 3. Dành cho Thành viên 2: Backend (NestJS + TypeORM)
```bash
cd backend
npm install
npm run start:dev
```
* **API Endpoint:** `http://localhost:4000/api/v1`
* **Swagger API Docs:** `http://localhost:4000/api/docs`

---

### 4. Dành cho Thành viên 3: AI Engine (Python FastAPI)
```bash
cd ai_engine
python -m venv venv
# Windows:
venv\Scripts\activate
# Cài đặt thư viện:
pip install -r requirements.txt
python server.py
```
* **AI Service:** `http://localhost:8000`
* **Swagger AI Docs:** `http://localhost:8000/docs`

---

### 5. Chạy toàn bộ hệ thống bằng Docker Compose (Full Stack)
Khi cả 3 thành viên đã hoàn thiện tính năng và muốn chạy kiểm thử đồng bộ:
```bash
docker compose up --build
```
Mở trình duyệt tại: `http://localhost:3000` để trải nghiệm hệ thống!
