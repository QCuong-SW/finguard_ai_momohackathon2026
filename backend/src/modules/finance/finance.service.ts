import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Transaction } from './entities/transaction.entity';
import { UserPersona } from '../users/entities/user-persona.entity';
import { AiBridgeService } from '../ai-bridge/ai-bridge.service';

@Injectable()
export class FinanceService {
  constructor(
    @InjectRepository(Transaction)
    private txRepo: Repository<Transaction>,
    @InjectRepository(UserPersona)
    private personaRepo: Repository<UserPersona>,
    private aiBridge: AiBridgeService,
  ) {}

  async getTransactions(userId?: string) {
    if (userId) {
      return this.txRepo.find({ where: { user_id: userId }, order: { transaction_time: 'DESC' } });
    }
    return this.txRepo.find({ order: { transaction_time: 'DESC' }, take: 50 });
  }

  async addTransaction(dto: any) {
    const isAnomaly = dto.amount > 2000000 && new Date().getHours() < 5;
    const tx = this.txRepo.create({
      ...dto,
      is_anomaly: isAnomaly,
      anomaly_reason: isAnomaly ? 'Giao dịch số tiền lớn vào khung giờ đêm muộn bất thường' : null,
    });
    return this.txRepo.save(tx);
  }

  async getAnomalies(userId?: string) {
    // Demo metrics
    return {
      period: 'LAST_30_DAYS',
      anomaly_count: 2,
      burn_rate: {
        days_passed_percent: 40,
        budget_spent_percent: 72,
        status: 'FAST_BURN_WARNING',
        message: 'Bạn đã tiêu hết 72% ngân sách tháng dù mới qua 12 ngày!',
      },
      anomalies: [
        {
          transaction_id: 'tx_8812',
          amount: 2500000,
          recipient: 'NGUYEN VAN X - MB BANK',
          timestamp: '2026-11-23T02:15:00Z',
          reason: 'Giao dịch số tiền lớn phát sinh vào khung giờ 2:15 sáng (lệch hoàn toàn so với lịch sử sinh hoạt của bạn).',
        },
        {
          transaction_id: 'tx_8815',
          amount: 99000,
          recipient: 'GLOBAL_DIGITAL_SERVICES_HK',
          timestamp: '2026-11-23T08:30:00Z',
          reason: 'Giao dịch lặp lại lần thứ 4 trong tuần với số tiền nhỏ cố định tới dịch vụ nước ngoài (dấu hiệu rò rỉ thông tin thẻ).',
        },
      ],
    };
  }

  async getAdvisorDecision(body: any) {
    const persona = {
      monthly_income: 15000000,
      safe_spending_limit: 5000000,
      risk_appetite: 'MODERATE',
    };
    return this.aiBridge.getAdvice(body, persona);
  }
}
