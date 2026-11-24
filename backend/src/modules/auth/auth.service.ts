import { Injectable, UnauthorizedException, ConflictException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { JwtService } from '@nestjs/jwt';
import * as bcrypt from 'bcrypt';
import { User } from '../users/entities/user.entity';
import { UserPersona } from '../users/entities/user-persona.entity';

@Injectable()
export class AuthService {
  constructor(
    @InjectRepository(User)
    private userRepo: Repository<User>,
    @InjectRepository(UserPersona)
    private personaRepo: Repository<UserPersona>,
    private jwtService: JwtService,
  ) {}

  async register(dto: any) {
    const existing = await this.userRepo.findOne({ where: { email: dto.email } });
    if (existing) throw new ConflictException('Email đã tồn tại trong hệ thống');

    const hashedPassword = await bcrypt.hash(dto.password || 'password123', 10);
    const user = this.userRepo.create({
      email: dto.email,
      password_hash: hashedPassword,
      full_name: dto.full_name || 'Người dùng FinGuard',
      phone_masked: dto.phone ? dto.phone.replace(/(\d{3})\d{4}(\d{3})/, '$1****$2') : '098****123',
    });
    await this.userRepo.save(user);

    // Tạo hồ sơ Persona mặc định
    const persona = this.personaRepo.create({
      user_id: user.id,
      monthly_income: dto.monthly_income || 15000000,
      safe_spending_limit: dto.safe_spending_limit || 5000000,
      risk_appetite: 'MODERATE',
      spending_habits: ['Ăn uống', 'Mua sắm trực tuyến', 'Dịch vụ số'],
    });
    await this.personaRepo.save(persona);

    const token = this.jwtService.sign({ sub: user.id, email: user.email });
    return {
      user: { id: user.id, email: user.email, full_name: user.full_name },
      token,
    };
  }

  async login(dto: any) {
    const user = await this.userRepo
      .createQueryBuilder('user')
      .addSelect('user.password_hash')
      .where('user.email = :email', { email: dto.email })
      .getOne();

    if (!user) throw new UnauthorizedException('Email hoặc mật khẩu không chính xác');

    const isMatch = await bcrypt.compare(dto.password, user.password_hash);
    if (!isMatch) throw new UnauthorizedException('Email hoặc mật khẩu không chính xác');

    const token = this.jwtService.sign({ sub: user.id, email: user.email });
    return {
      user: { id: user.id, email: user.email, full_name: user.full_name },
      token,
    };
  }
}
