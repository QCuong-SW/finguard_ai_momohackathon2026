import { Entity, PrimaryGeneratedColumn, Column, ManyToOne, JoinColumn, CreateDateColumn } from 'typeorm';
import { User } from '../../users/entities/user.entity';

@Entity('transactions')
export class Transaction {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column('uuid')
  user_id: string;

  @ManyToOne(() => User, (user) => user.transactions, { onDelete: 'CASCADE' })
  @JoinColumn({ name: 'user_id' })
  user: User;

  @Column('numeric', { precision: 15, scale: 2 })
  amount: number;

  @Column()
  category: string; // Ăn uống, Mua sắm, Sinh hoạt, Giải trí, Đầu tư, Chuyển khoản...

  @Column({ nullable: true })
  description: string;

  @Column({ nullable: true })
  recipient: string;

  @Column({ default: false })
  is_anomaly: boolean;

  @Column({ type: 'text', nullable: true })
  anomaly_reason: string;

  @CreateDateColumn({ type: 'timestamp with time zone' })
  transaction_time: Date;
}
