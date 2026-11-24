import { Controller, Post, Body, Get, Param } from '@nestjs/common';
import { ApiTags, ApiOperation, ApiResponse } from '@nestjs/swagger';
import { ScamService } from './scam.service';

@ApiTags('Scam Intelligence')
@Controller('scam')
export class ScamController {
  constructor(private readonly scamService: ScamService) {}

  @Post('scan')
  @ApiOperation({ summary: 'Quét nhận diện lừa đảo từ Tin nhắn, Ảnh OCR hoặc URL' })
  @ApiResponse({ status: 200, description: 'Kết quả phân tích rủi ro và giải thích XAI' })
  async scanContent(
    @Body() body: { type: string; content: string; context?: string; user_id?: string },
  ) {
    return this.scamService.scan(body);
  }

  @Get('history')
  @ApiOperation({ summary: 'Lấy lịch sử quét rủi ro' })
  async getHistory() {
    return this.scamService.findAll();
  }
}
