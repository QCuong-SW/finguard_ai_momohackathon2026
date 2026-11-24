import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { ScamController } from './scam.controller';
import { ScamService } from './scam.service';
import { ScamScan } from './entities/scam-scan.entity';
import { AiBridgeService } from '../ai-bridge/ai-bridge.service';

@Module({
  imports: [TypeOrmModule.forFeature([ScamScan])],
  controllers: [ScamController],
  providers: [ScamService, AiBridgeService],
  exports: [ScamService],
})
export class ScamModule {}
