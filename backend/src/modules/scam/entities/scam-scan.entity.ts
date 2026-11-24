import { Entity, PrimaryGeneratedColumn, Column, ManyToOne, JoinColumn, CreateDateColumn } from 'typeorm';
import { User } from '../../users/entities/user.entity';

@Entity('scam_scans')
export class ScamScan {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column('uuid', { nullable: true })
  user_id: string;

  @ManyToOne(() => User, (user) => user.scam_scans, { onDelete: 'SET NULL', nullable: true })
  @JoinColumn({ name: 'user_id' })
  user: User;

  @Column()
  input_type: string; // TEXT, IMAGE, URL

  @Column({ type: 'text' })
  original_content_masked: string;

  @Column('int')
  risk_score: number; // 0 - 100

  @Column()
  risk_level: string; // SAFE, SUSPICIOUS, CRITICAL

  @Column({ type: 'text', nullable: true })
  summary: string;

  @Column('jsonb', { default: [] })
  manipulation_tactics: any[];

  @Column('jsonb', { default: {} })
  xai_explanation: any;

  @Column('jsonb', { default: [] })
  actionable_checklist: string[];

  @CreateDateColumn({ type: 'timestamp with time zone' })
  scanned_at: Date;
}
