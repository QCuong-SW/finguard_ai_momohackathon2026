import { NestFactory } from '@nestjs/core';
import { ValidationPipe } from '@nestjs/common';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // Bật CORS cho Frontend Next.js
  app.enableCors({
    origin: '*',
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
    credentials: true,
  });

  // Global prefix cho API
  app.setGlobalPrefix('api/v1');

  // Validation pipe tự động kiểm tra DTO
  app.useGlobalPipes(
    new ValidationPipe({
      whitelist: true,
      forbidNonWhitelisted: true,
      transform: true,
    }),
  );

  // Cấu hình Swagger API Documentation
  const config = new DocumentBuilder()
    .setTitle('FinGuard AI API Documentation')
    .setDescription('Backend REST API cho hệ thống Trợ lý Tài chính & Chống Lừa Đảo FinGuard AI')
    .setVersion('1.0')
    .addBearerAuth()
    .build();
  const document = SwaggerModule.createDocument(app, config);
  SwaggerModule.setup('api/docs', app, document);

  const port = process.env.BACKEND_PORT || 4000;
  await app.listen(port);
  console.log(`🛡️ FinGuard Backend running at: http://localhost:${port}/api/v1`);
  console.log(`📚 Swagger Docs available at: http://localhost:${port}/api/docs`);
}
bootstrap();
