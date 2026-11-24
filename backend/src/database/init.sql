-- ====================================================
-- FinGuard AI - Initial Database Schema (PostgreSQL 17)
-- ====================================================

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Bảng USERS
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    phone_masked VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Bảng USER_PERSONAS (Hồ sơ đặc trưng tài chính)
CREATE TABLE IF NOT EXISTS user_personas (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    monthly_income NUMERIC(15, 2) DEFAULT 0,
    safe_spending_limit NUMERIC(15, 2) DEFAULT 0,
    risk_appetite VARCHAR(50) DEFAULT 'MODERATE', -- LOW, MODERATE, HIGH
    spending_habits JSONB DEFAULT '[]'::jsonb,
    emergency_fund_months INT DEFAULT 3,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. Bảng TRANSACTIONS (Lịch sử giao dịch & cảnh báo Anomaly)
CREATE TABLE IF NOT EXISTS transactions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    amount NUMERIC(15, 2) NOT NULL,
    category VARCHAR(100) NOT NULL,
    description TEXT,
    recipient VARCHAR(255),
    is_anomaly BOOLEAN DEFAULT FALSE,
    anomaly_reason TEXT,
    transaction_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 4. Bảng SCAM_SCANS (Lịch sử quét lừa đảo & XAI)
CREATE TABLE IF NOT EXISTS scam_scans (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    input_type VARCHAR(50) NOT NULL, -- TEXT, IMAGE, URL
    original_content_masked TEXT NOT NULL,
    risk_score INT NOT NULL, -- 0 to 100
    risk_level VARCHAR(50) NOT NULL, -- SAFE, SUSPICIOUS, CRITICAL
    summary TEXT,
    manipulation_tactics JSONB DEFAULT '[]'::jsonb,
    xai_explanation JSONB DEFAULT '{}'::jsonb,
    actionable_checklist JSONB DEFAULT '[]'::jsonb,
    scanned_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 5. Bảng USER_DOCUMENTS (Tài liệu RAG & Bóc tách bẫy chữ nhỏ)
CREATE TABLE IF NOT EXISTS user_documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    doc_name VARCHAR(255) NOT NULL,
    file_path TEXT,
    doc_type VARCHAR(100), -- LOAN_CONTRACT, CREDIT_TERMS, INVESTMENT_PROPOSAL
    risk_rating VARCHAR(50), -- LOW_RISK, MEDIUM_RISK, HIGH_RISK
    summary TEXT,
    hidden_traps JSONB DEFAULT '[]'::jsonb,
    suggested_questions JSONB DEFAULT '[]'::jsonb,
    uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 6. Bảng INCIDENT_REPORTS (Hồ sơ sự cố lừa đảo)
CREATE TABLE IF NOT EXISTS incident_reports (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    incident_code VARCHAR(100) UNIQUE NOT NULL,
    status VARCHAR(50) DEFAULT 'DRAFT', -- DRAFT, EXPORTED, SUBMITTED
    total_financial_loss NUMERIC(15, 2) DEFAULT 0,
    executive_summary TEXT,
    timeline_events JSONB DEFAULT '[]'::jsonb,
    attached_scam_ids JSONB DEFAULT '[]'::jsonb,
    attached_transaction_ids JSONB DEFAULT '[]'::jsonb,
    pdf_file_path TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 7. Bảng AUDIT_LOGS (Giám sát bảo mật & PII Privacy)
CREATE TABLE IF NOT EXISTS audit_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    action VARCHAR(100) NOT NULL, -- LOGIN, DATA_DELETE, SCAN, EXPORT_REPORT
    ip_address_masked VARCHAR(100),
    user_agent TEXT,
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
