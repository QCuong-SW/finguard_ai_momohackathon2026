import { Controller, Post, Body, Get } from '@nestjs/common';
import { ApiTags, ApiOperation } from '@nestjs/swagger';
import { RagService } from './rag.service';

@ApiTags('RAG Document & Knowledge')
@Controller('rag')
export class RagController {
  constructor(private readonly ragService: RagService) {}

  @Post('analyze-document')
  @ApiOperation({ summary: 'Phân tích tài liệu PDF/Hợp đồng vay và bóc tách Bẫy chữ nhỏ' })
  async analyzeDocument(@Body() body: { doc_name: string; text?: string; user_id?: string }) {
    return this.ragService.analyze(body);
  }

  @Get('documents')
  @ApiOperation({ summary: 'Lấy danh sách tài liệu đã phân tích' })
  async getDocuments() {
    return this.ragService.findAll();
  }
}
