import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { FinanceController } from './finance.controller';
import { FinanceService } from './finance.service';
import { Transaction } from './entities/transaction.entity';
import { UserPersona } from '../users/entities/user-persona.entity';
import { AiBridgeService } from '../ai-bridge/ai-bridge.service';

@Module({
  imports: [TypeOrmModule.forFeature([Transaction, UserPersona])],
  controllers: [FinanceController],
  providers: [FinanceService, AiBridgeService],
  exports: [FinanceService],
})
export class FinanceModule {}
