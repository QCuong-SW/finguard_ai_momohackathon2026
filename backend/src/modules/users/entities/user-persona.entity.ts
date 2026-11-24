import { Entity, PrimaryGeneratedColumn, Column, UpdateDateColumn, OneToOne, JoinColumn } from 'typeorm';
import { User } from './user.entity';

@Entity('user_personas')
export class UserPersona {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column('uuid')
  user_id: string;

  @OneToOne(() => User, (user) => user.persona, { onDelete: 'CASCADE' })
  @JoinColumn({ name: 'user_id' })
  user: User;

  @Column('numeric', { precision: 15, scale: 2, default: 0 })
  monthly_income: number;

  @Column('numeric', { precision: 15, scale: 2, default: 0 })
  safe_spending_limit: number;

  @Column({ default: 'MODERATE' })
  risk_appetite: string; // LOW, MODERATE, HIGH

  @Column('jsonb', { default: [] })
  spending_habits: string[];

  @Column({ default: 3 })
  emergency_fund_months: number;

  @UpdateDateColumn({ type: 'timestamp with time zone' })
  updated_at: Date;
}
