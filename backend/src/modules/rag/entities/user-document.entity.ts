import { Entity, PrimaryGeneratedColumn, Column, ManyToOne, JoinColumn, CreateDateColumn } from 'typeorm';
import { User } from '../../users/entities/user.entity';

@Entity('user_documents')
export class UserDocument {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column('uuid')
  user_id: string;

  @ManyToOne(() => User, (user) => user.documents, { onDelete: 'CASCADE' })
  @JoinColumn({ name: 'user_id' })
  user: User;

  @Column()
  doc_name: string;

  @Column({ nullable: true })
  file_path: string;

  @Column({ nullable: true })
  doc_type: string; // LOAN_CONTRACT, CREDIT_TERMS, INVESTMENT_PROPOSAL

  @Column({ nullable: true })
  risk_rating: string; // LOW_RISK, MEDIUM_RISK, HIGH_RISK

  @Column({ type: 'text', nullable: true })
  summary: string;

  @Column('jsonb', { default: [] })
  hidden_traps: any[];

  @Column('jsonb', { default: [] })
  suggested_questions: string[];

  @CreateDateColumn({ type: 'timestamp with time zone' })
  uploaded_at: Date;
}
