import { Controller, Get, Post, Body, Query } from '@nestjs/common';
import { ApiTags, ApiOperation } from '@nestjs/swagger';
import { FinanceService } from './finance.service';

@ApiTags('Financial Risk & Persona')
@Controller('finance')
export class FinanceController {
  constructor(private readonly financeService: FinanceService) {}

  @Get('transactions')
  @ApiOperation({ summary: 'Lấy danh sách lịch sử giao dịch' })
  async getTransactions(@Query('user_id') userId: string) {
    return this.financeService.getTransactions(userId);
  }

  @Post('transactions')
  @ApiOperation({ summary: 'Thêm mới giao dịch' })
  async addTransaction(@Body() body: any) {
    return this.financeService.addTransaction(body);
  }

  @Get('anomalies')
  @ApiOperation({ summary: 'Phát hiện biến động tài chính bất thường & Tốc độ tiêu ngân sách' })
  async getAnomalies(@Query('user_id') userId: string) {
    return this.financeService.getAnomalies(userId);
  }

  @Post('advisor/decision')
  @ApiOperation({ summary: 'Trợ lý gợi ý quyết định & chi tiêu dựa trên Persona' })
  async getAdvisorDecision(@Body() body: any) {
    return this.financeService.getAdvisorDecision(body);
  }
}
