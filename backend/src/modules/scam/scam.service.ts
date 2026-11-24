import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { ScamScan } from './entities/scam-scan.entity';
import { AiBridgeService } from '../ai-bridge/ai-bridge.service';

@Injectable()
export class ScamService {
  constructor(
    @InjectRepository(ScamScan)
    private scamRepo: Repository<ScamScan>,
    private aiBridge: AiBridgeService,
  ) {}

  async scan(payload: { type: string; content: string; context?: string; user_id?: string }) {
    // 1. Gửi sang AI Engine phân tích
    const aiResult = await this.aiBridge.analyzeScam(payload);

    // 2. Lưu vào Database
    const scanRecord = this.scamRepo.create({
      user_id: payload.user_id || null,
      input_type: payload.type,
      original_content_masked: payload.content,
      risk_score: aiResult.risk_score,
      risk_level: aiResult.risk_level,
      summary: aiResult.summary,
      manipulation_tactics: aiResult.psychological_manipulation,
      xai_explanation: aiResult,
      actionable_checklist: aiResult.actionable_checklist,
    });

    await this.scamRepo.save(scanRecord);

    return {
      scan_id: scanRecord.id,
      ...aiResult,
    };
  }

  async findAll() {
    return this.scamRepo.find({ order: { scanned_at: 'DESC' }, take: 20 });
  }
}
