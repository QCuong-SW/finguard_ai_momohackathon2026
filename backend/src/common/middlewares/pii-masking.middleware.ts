import { Injectable, NestMiddleware } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';

@Injectable()
export class PiiMaskingMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    if (req.body && typeof req.body === 'object') {
      req.body = this.maskSensitiveData(req.body);
    }
    next();
  }

  private maskSensitiveData(data: any): any {
    if (typeof data === 'string') {
      return this.maskString(data);
    }

    if (Array.isArray(data)) {
      return data.map((item) => this.maskSensitiveData(item));
    }

    if (typeof data === 'object' && data !== null) {
      const maskedObj: Record<string, any> = {};
      for (const [key, value] of Object.entries(data)) {
        // Không mask password hash nội bộ
        if (key === 'password' || key === 'password_hash') {
          maskedObj[key] = value;
        } else {
          maskedObj[key] = this.maskSensitiveData(value);
        }
      }
      return maskedObj;
    }

    return data;
  }

  private maskString(text: string): string {
    let result = text;

    // Mask số tài khoản ngân hàng / thẻ tín dụng (dãy 12-19 chữ số)
    result = result.replace(/\b(\d{4})[ -]?(\d{4,11})[ -]?(\d{4})\b/g, '$1 **** **** $3');

    // Mask số điện thoại Việt Nam (10 số, bắt đầu bằng 0 hoặc +84)
    result = result.replace(/(\+84|0)(\d{2,3})(\d{3})(\d{3})/g, '$1$2 **** $4');

    // Mask số Căn cước công dân (12 chữ số)
    result = result.replace(/\b\d{3}(\d{6})\d{3}\b/g, '***$1***');

    // Mask mã OTP (4-6 chữ số liền sau từ khóa OTP)
    result = result.replace(/(otp[:\s]+)(\d{4,6})/gi, '$1******');

    return result;
  }
}
