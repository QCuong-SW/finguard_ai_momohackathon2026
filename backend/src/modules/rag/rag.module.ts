import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { RagController } from './rag.controller';
import { RagService } from './rag.service';
import { UserDocument } from './entities/user-document.entity';
import { AiBridgeService } from '../ai-bridge/ai-bridge.service';

@Module({
  imports: [TypeOrmModule.forFeature([UserDocument])],
  controllers: [RagController],
  providers: [RagService, AiBridgeService],
  exports: [RagService],
})
export class RagModule {}
