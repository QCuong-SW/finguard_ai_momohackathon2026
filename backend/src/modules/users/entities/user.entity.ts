import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn, UpdateDateColumn, OneToMany, OneToOne } from 'typeorm';
import { UserPersona } from './user-persona.entity';
import { Transaction } from '../../finance/entities/transaction.entity';
import { ScamScan } from '../../scam/entities/scam-scan.entity';
import { UserDocument } from '../../rag/entities/user-document.entity';
import { IncidentReport } from '../../incidents/entities/incident-report.entity';

@Entity('users')
export class User {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ unique: true })
  email: string;

  @Column({ select: false })
  password_hash: string;

  @Column()
  full_name: string;

  @Column({ nullable: true })
  phone_masked: string;

  @OneToOne(() => UserPersona, (persona) => persona.user, { cascade: true })
  persona: UserPersona;

  @OneToMany(() => Transaction, (tx) => tx.user)
  transactions: Transaction[];

  @OneToMany(() => ScamScan, (scan) => scan.user)
  scam_scans: ScamScan[];

  @OneToMany(() => UserDocument, (doc) => doc.user)
  documents: UserDocument[];

  @OneToMany(() => IncidentReport, (incident) => incident.user)
  incidents: IncidentReport[];

  @CreateDateColumn({ type: 'timestamp with time zone' })
  created_at: Date;

  @UpdateDateColumn({ type: 'timestamp with time zone' })
  updated_at: Date;
}
