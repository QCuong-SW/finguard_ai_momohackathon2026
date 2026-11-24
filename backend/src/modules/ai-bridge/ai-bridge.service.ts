import { Injectable, Logger } from '@nestjs/common';
import axios from 'axios';
import { ConfigService } from '@nestjs/config';

@Injectable()
export class AiBridgeService {
  private readonly logger = new Logger(AiBridgeService.name);
  private readonly aiUrl: string;

  constructor(private configService: ConfigService) {
    this.aiUrl = this.configService.get<string>('AI_ENGINE_URL', 'http://localhost:8000');
  }

  // 1. Gửi sang AI Scam Pipeline
  async analyzeScam(payload: { type: string; content: string; context?: string }) {
    try {
      const response = await axios.post(`${this.aiUrl}/api/v1/ai/scam/analyze`, payload, { timeout: 15000 });
      return response.data;
    } catch (error) {
      this.logger.warn(`AI Engine Scam Service offline, falling back to mock logic: ${error.message}`);
      return this.getMockScamResult(payload.content);
    }
  }

  // 2. Gửi sang AI RAG Pipeline bóc tách bẫy tài liệu
  async analyzeDocument(docName: string, textContent: string) {
    try {
      const response = await axios.post(`${this.aiUrl}/api/v1/ai/rag/analyze-doc`, { doc_name: docName, text: textContent }, { timeout: 30000 });
      return response.data;
    } catch (error) {
      this.logger.warn(`AI Engine RAG Service offline, falling back to mock: ${error.message}`);
      return this.getMockRagResult(docName);
    }
  }

  // 3. Gửi sang AI Persona & Decision Advisor
  async getAdvice(proposedAction: any, persona: any) {
    try {
      const response = await axios.post(`${this.aiUrl}/api/v1/ai/advisor/recommend`, { action: proposedAction, persona }, { timeout: 10000 });
      return response.data;
    } catch (error) {
      this.logger.warn(`AI Engine Advisor offline, falling back to mock: ${error.message}`);
      return this.getMockAdvisorResult(proposedAction);
    }
  }

  // Fallback mocks khi chưa chạy AI service
  private getMockScamResult(content: string) {
    const isHighRisk = content.toLowerCase().includes('công an') || content.toLowerCase().includes('otp') || content.toLowerCase().includes('khóa tài khoản');
    return {
      risk_score: isHighRisk ? 92 : 25,
      risk_level: isHighRisk ? 'CRITICAL' : 'SAFE',
      summary: isHighRisk 
        ? 'Phát hiện kịch bản giả mạo cơ quan nhà nước / ngân hàng để đe dọa hoặc chiếm đoạt OTP.' 
        : 'Nội dung thông thường, chưa phát hiện dấu hiệu thao túng tâm lý nguy hiểm.',
      psychological_manipulation: isHighRisk ? [
        { tactic: 'Authority Impersonation', evidence: content.slice(0, 50), explanation: 'Tự xưng cơ quan có thẩm quyền.' }
      ] : [],
      actionable_checklist: isHighRisk ? [
        'TUYỆT ĐỐI KHÔNG chia sẻ mã OTP hoặc chuyển tiền.',
        'Liên hệ trực tiếp cơ quan/ngân hàng qua hotline chính thức.'
      ] : ['Giao dịch bình thường, hãy luôn kiểm tra tài khoản nhận.']
    };
  }

  private getMockRagResult(docName: string) {
    return {
      doc_name: docName,
      risk_rating: 'HIGH_RISK',
      summary: 'Tài liệu chứa điều khoản lãi suất thả nổi và mức phạt tất toán cao.',
      hidden_traps: [
        { category: 'Lãi suất ngầm', trap_warning: 'Lãi suất thả nổi có thể tăng sau thời gian ưu đãi ban đầu.' },
        { category: 'Phí phạt tất toán', trap_warning: 'Mức phạt trả trước hạn lên đến 15% dư nợ còn lại.' }
      ],
      suggested_questions: [
        'Tổng số tiền lãi và gốc sau 12 tháng là bao nhiêu?',
        'Mức phí phạt trả chậm là bao nhiêu?'
      ]
    };
  }

  private getMockAdvisorResult(action: any) {
    return {
      recommendation: 'CAUTION_HOLD',
      headline: 'Cân nhắc hoãn khoản chi này để bảo đảm quỹ dự phòng khẩn cấp!',
      personalized_analysis: {
        current_budget_status: 'Khoản chi dự kiến chiếm tỷ lệ lớn trong ngân sách còn lại của tháng.',
        upcoming_obligations: 'Bạn còn các hóa đơn thiết yếu cuối tháng cần ưu tiên.',
        emergency_fund_impact: 'Quỹ dự phòng an toàn có thể bị giảm dưới ngưỡng 3 tháng sinh hoạt.'
      },
      action_options: [
        { option: 'Hoãn mua sang tháng sau', description: 'Tránh áp lực dòng tiền cuối tháng.' },
        { option: 'Tìm gói trả góp 0%', description: 'Chia nhỏ số tiền thanh toán theo từng tháng.' }
      ]
    };
  }
}
