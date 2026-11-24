import { Module, MiddlewareConsumer, NestModule } from '@nestjs/common';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { TypeOrmModule } from '@nestjs/typeorm';
import { PiiMaskingMiddleware } from './common/middlewares/pii-masking.middleware';
import { AuthModule } from './modules/auth/auth.module';
import { ScamModule } from './modules/scam/scam.module';
import { FinanceModule } from './modules/finance/finance.module';
import { RagModule } from './modules/rag/rag.module';
import { IncidentsModule } from './modules/incidents/incidents.module';

import { User } from './modules/users/entities/user.entity';
import { UserPersona } from './modules/users/entities/user-persona.entity';
import { Transaction } from './modules/finance/entities/transaction.entity';
import { ScamScan } from './modules/scam/entities/scam-scan.entity';
import { UserDocument } from './modules/rag/entities/user-document.entity';
import { IncidentReport } from './modules/incidents/entities/incident-report.entity';

@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true }),
    TypeOrmModule.forRootAsync({
      imports: [ConfigModule],
      inject: [ConfigService],
      useFactory: (config: ConfigService) => ({
        type: 'postgres',
        host: config.get<string>('POSTGRES_HOST', 'localhost'),
        port: config.get<number>('POSTGRES_PORT', 5432),
        username: config.get<string>('POSTGRES_USER', 'finguard_admin'),
        password: config.get<string>('POSTGRES_PASSWORD', 'finguard_secret_pass_2026'),
        database: config.get<string>('POSTGRES_DB', 'finguard_db'),
        entities: [User, UserPersona, Transaction, ScamScan, UserDocument, IncidentReport],
        synchronize: true, // Auto-sync DB schema in dev mode for hackathon
      }),
    }),
    AuthModule,
    ScamModule,
    FinanceModule,
    RagModule,
    IncidentsModule,
  ],
})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    // Áp dụng PII Masking Middleware cho toàn bộ request để bảo vệ quyền riêng tư
    consumer.apply(PiiMaskingMiddleware).forRoutes('*');
  }
}
