import { Entity, PrimaryGeneratedColumn, Column, ManyToOne, JoinColumn, CreateDateColumn } from 'typeorm';
import { User } from '../../users/entities/user.entity';

@Entity('incident_reports')
export class IncidentReport {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column('uuid')
  user_id: string;

  @ManyToOne(() => User, (user) => user.incidents, { onDelete: 'CASCADE' })
  @JoinColumn({ name: 'user_id' })
  user: User;

  @Column({ unique: true })
  incident_code: string;

  @Column({ default: 'DRAFT' })
  status: string; // DRAFT, EXPORTED, SUBMITTED

  @Column('numeric', { precision: 15, scale: 2, default: 0 })
  total_financial_loss: number;

  @Column({ type: 'text', nullable: true })
  executive_summary: string;

  @Column('jsonb', { default: [] })
  timeline_events: any[];

  @Column('jsonb', { default: [] })
  attached_scam_ids: string[];

  @Column('jsonb', { default: [] })
  attached_transaction_ids: string[];

  @Column({ nullable: true })
  pdf_file_path: string;

  @CreateDateColumn({ type: 'timestamp with time zone' })
  created_at: Date;
}
