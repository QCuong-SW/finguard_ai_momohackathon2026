import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { IncidentReport } from './entities/incident-report.entity';

@Injectable()
export class IncidentsService {
  constructor(
    @InjectRepository(IncidentReport)
    private incidentRepo: Repository<IncidentReport>,
  ) {}

  async createReport(dto: any) {
    const code = `INC-${new Date().toISOString().slice(0, 10).replace(/-/g, '')}-${Math.floor(100 + Math.random() * 900)}`;
    const report = this.incidentRepo.create({
      user_id: dto.user_id || null,
      incident_code: code,
      status: 'READY_FOR_EXPORT',
      total_financial_loss: dto.total_loss || 8500000,
      executive_summary: dto.summary || 'Vụ việc lừa đảo mạo danh ngân hàng nâng hạn mức thẻ tín dụng. Nạn nhân truy cập link giả mạo và phát sinh giao dịch trái phép.',
      timeline_events: dto.timeline || [
        { time: '09:15', event: 'Nhận SMS Brandname giả mạo báo duyệt hạn mức thẻ' },
        { time: '09:22', event: 'Truy cập link phishing và nhập mã OTP' },
        { time: '09:25', event: 'Tài khoản bị trừ tiền trái phép' },
      ],
      attached_scam_ids: dto.scam_ids || [],
      attached_transaction_ids: dto.transaction_ids || [],
      pdf_file_path: `/exports/${code}.pdf`,
    });

    await this.incidentRepo.save(report);

    return {
      incident_code: report.incident_code,
      status: report.status,
      generated_at: new Date().toISOString(),
      victim_info: { name: 'Người dùng FinGuard', masked_phone: '098****123' },
      executive_summary: report.executive_summary,
      total_financial_loss: report.total_financial_loss,
      timeline: report.timeline_events,
      download_pdf_url: `/api/v1/incidents/${report.id}/download-pdf`,
    };
  }

  async findAll() {
    return this.incidentRepo.find({ order: { created_at: 'DESC' } });
  }

  async findOne(id: string) {
    const item = await this.incidentRepo.findOne({ where: { id } });
    if (!item) throw new NotFoundException('Incident not found');
    return item;
  }
}
