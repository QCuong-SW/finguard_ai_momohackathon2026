import axios from 'axios';
import mockScam from './mockData/mockScam.json';
import mockFinance from './mockData/mockFinance.json';
import mockRag from './mockData/mockRag.json';
import mockAdvisor from './mockData/mockAdvisor.json';
import mockIncident from './mockData/mockIncident.json';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:4000/api/v1';
const USE_MOCK = process.env.NEXT_PUBLIC_USE_MOCK === 'true';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const apiService = {
  // 1. Phân hệ Scam
  async scanContent(type: 'TEXT' | 'IMAGE' | 'URL', content: string) {
    if (USE_MOCK) {
      await new Promise((res) => setTimeout(res, 800)); // Giả lập độ trễ AI
      return mockScam;
    }
    const response = await apiClient.post('/scam/scan', { type, content });
    return response.data;
  },

  // 2. Phân hệ Tài chính & Anomaly
  async getFinancialHealth() {
    if (USE_MOCK) {
      await new Promise((res) => setTimeout(res, 500));
      return mockFinance;
    }
    const response = await apiClient.get('/finance/anomalies');
    return response.data;
  },

  // 3. Phân hệ RAG Bóc tách tài liệu
  async analyzeDocument(docName: string, text?: string) {
    if (USE_MOCK) {
      await new Promise((res) => setTimeout(res, 1200));
      return mockRag;
    }
    const response = await apiClient.post('/rag/analyze-document', { doc_name: docName, text });
    return response.data;
  },

  // 4. Phân hệ Cố vấn Quyết định & Chi tiêu
  async getAdvisorDecision(action: { amount: number; category: string; notes?: string }) {
    if (USE_MOCK) {
      await new Promise((res) => setTimeout(res, 700));
      return mockAdvisor;
    }
    const response = await apiClient.post('/finance/advisor/decision', action);
    return response.data;
  },

  // 5. Phân hệ Tạo Hồ sơ Sự cố
  async createIncidentReport(payload: any) {
    if (USE_MOCK) {
      await new Promise((res) => setTimeout(res, 1000));
      return mockIncident;
    }
    const response = await apiClient.post('/incidents/create-report', payload);
    return response.data;
  },
};
