import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { UserDocument } from './entities/user-document.entity';
import { AiBridgeService } from '../ai-bridge/ai-bridge.service';

@Injectable()
export class RagService {
  constructor(
    @InjectRepository(UserDocument)
    private docRepo: Repository<UserDocument>,
    private aiBridge: AiBridgeService,
  ) {}

  async analyze(body: { doc_name: string; text?: string; user_id?: string }) {
    const aiResult = await this.aiBridge.analyzeDocument(body.doc_name, body.text || '');

    const doc = this.docRepo.create({
      user_id: body.user_id || null,
      doc_name: body.doc_name,
      doc_type: 'LOAN_CONTRACT',
      risk_rating: aiResult.risk_rating,
      summary: aiResult.summary,
      hidden_traps: aiResult.hidden_traps,
      suggested_questions: aiResult.suggested_questions,
    });

    await this.docRepo.save(doc);

    return {
      document_id: doc.id,
      ...aiResult,
    };
  }

  async findAll() {
    return this.docRepo.find({ order: { uploaded_at: 'DESC' } });
  }
}
