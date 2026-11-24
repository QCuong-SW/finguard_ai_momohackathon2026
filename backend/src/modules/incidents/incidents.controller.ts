import { Controller, Post, Body, Get, Param } from '@nestjs/common';
import { ApiTags, ApiOperation } from '@nestjs/swagger';
import { IncidentsService } from './incidents.service';

@ApiTags('Incident Reporting')
@Controller('incidents')
export class IncidentsController {
  constructor(private readonly incidentsService: IncidentsService) {}

  @Post('create-report')
  @ApiOperation({ summary: 'Tự động đóng gói Hồ sơ Sự cố Lừa đảo để trình báo' })
  async createReport(@Body() body: any) {
    return this.incidentsService.createReport(body);
  }

  @Get()
  @ApiOperation({ summary: 'Lấy danh sách các hồ sơ sự cố' })
  async getAll() {
    return this.incidentsService.findAll();
  }

  @Get(':id')
  @ApiOperation({ summary: 'Xem chi tiết một hồ sơ sự cố' })
  async getOne(@Param('id') id: string) {
    return this.incidentsService.findOne(id);
  }
}
