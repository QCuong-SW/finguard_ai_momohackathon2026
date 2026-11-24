'use client';

import React, { useState, useEffect } from 'react';
import { apiService } from '@/services/api';
import { 
  ShieldAlert, 
  ShieldCheck, 
  AlertTriangle, 
  FileText, 
  Sparkles, 
  Search, 
  ExternalLink, 
  Lock, 
  FileDown, 
  TrendingDown, 
  DollarSign 
} from 'lucide-react';

export default function Dashboard() {
  const [activeTab, setActiveTab] = useState<'OVERVIEW' | 'SCAM' | 'FINANCE' | 'RAG' | 'ADVISOR'>('OVERVIEW');

  // State Scam
  const [scamInput, setScamInput] = useState('');
  const [scamResult, setScamResult] = useState<any>(null);
  const [isScanning, setIsScanning] = useState(false);

  // State Finance
  const [financeData, setFinanceData] = useState<any>(null);

  // State RAG
  const [ragResult, setRagResult] = useState<any>(null);
  const [analyzingDoc, setAnalyzingDoc] = useState(false);

  // State Advisor
  const [spendAmount, setSpendAmount] = useState('4200000');
  const [advisorResult, setAdvisorResult] = useState<any>(null);
  const [gettingAdvice, setGettingAdvice] = useState(false);

  // Load finance data on mount
  useEffect(() => {
    apiService.getFinancialHealth().then(setFinanceData);
  }, []);

  const handleScanScam = async () => {
    if (!scamInput.trim()) return;
    setIsScanning(true);
    try {
      const res = await apiService.scanContent('TEXT', scamInput);
      setScamResult(res);
    } finally {
      setIsScanning(false);
    }
  };

  const handleAnalyzeMockDoc = async () => {
    setAnalyzingDoc(true);
    try {
      const res = await apiService.analyzeDocument('Hop_Dong_Vay_Tieu_Dung_Nhanh.pdf');
      setRagResult(res);
    } finally {
      setAnalyzingDoc(false);
    }
  };

  const handleGetAdvice = async () => {
    setGettingAdvice(true);
    try {
      const res = await apiService.getAdvisorDecision({
        amount: Number(spendAmount),
        category: 'Mua sắm / Điện tử',
        notes: 'Mua trả góp',
      });
      setAdvisorResult(res);
    } finally {
      setGettingAdvice(false);
    }
  };

  return (
    <div className="space-y-6">
      {/* Navigation Tabs */}
      <div className="flex gap-2 overflow-x-auto pb-2 border-b border-slate-800 text-sm">
        <button
          onClick={() => setActiveTab('OVERVIEW')}
          className={`px-3 py-1.5 rounded-lg font-medium transition ${
            activeTab === 'OVERVIEW' ? 'bg-pink-600 text-white' : 'text-slate-400 hover:bg-slate-900'
          }`}
        >
          📊 Tổng quan
        </button>
        <button
          onClick={() => setActiveTab('SCAM')}
          className={`px-3 py-1.5 rounded-lg font-medium transition ${
            activeTab === 'SCAM' ? 'bg-pink-600 text-white' : 'text-slate-400 hover:bg-slate-900'
          }`}
        >
          🛡️ Quét Lừa đảo (AI Scam)
        </button>
        <button
          onClick={() => setActiveTab('FINANCE')}
          className={`px-3 py-1.5 rounded-lg font-medium transition ${
            activeTab === 'FINANCE' ? 'bg-pink-600 text-white' : 'text-slate-400 hover:bg-slate-900'
          }`}
        >
          🚨 Radar Biến động Dòng tiền
        </button>
        <button
          onClick={() => setActiveTab('RAG')}
          className={`px-3 py-1.5 rounded-lg font-medium transition ${
            activeTab === 'RAG' ? 'bg-pink-600 text-white' : 'text-slate-400 hover:bg-slate-900'
          }`}
        >
          📚 RAG Bóc tách Hợp đồng
        </button>
        <button
          onClick={() => setActiveTab('ADVISOR')}
          className={`px-3 py-1.5 rounded-lg font-medium transition ${
            activeTab === 'ADVISOR' ? 'bg-pink-600 text-white' : 'text-slate-400 hover:bg-slate-900'
          }`}
        >
          🤖 Cố vấn Chi tiêu (Persona)
        </button>
      </div>

      {/* TAB 1: OVERVIEW */}
      {activeTab === 'OVERVIEW' && (
        <div className="space-y-6">
          {/* Hero Banner */}
          <div className="bg-gradient-to-r from-pink-950/60 to-slate-900 border border-pink-900/40 rounded-2xl p-6">
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
              <div>
                <span className="text-xs uppercase tracking-wider text-pink-400 font-bold">Lá chắn tài chính thông minh</span>
                <h2 className="text-2xl font-bold text-white mt-1">Sức khỏe & An toàn Tài chính: 85/100</h2>
                <p className="text-slate-400 text-sm mt-1">Đang chủ động bảo vệ trước 2 tín hiệu bất thường trong ngày.</p>
              </div>
              <button
                onClick={() => setActiveTab('SCAM')}
                className="px-4 py-2.5 rounded-xl bg-pink-600 hover:bg-pink-500 font-semibold text-white flex items-center gap-2 shadow-lg shadow-pink-600/30 transition text-sm"
              >
                <Search size={16} /> Quét nhanh tin nhắn / link lạ
              </button>
            </div>
          </div>

          {/* Quick Metrics Grid */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="bg-slate-900 border border-slate-800 rounded-xl p-4">
              <div className="flex items-center justify-between text-slate-400 text-xs mb-2">
                <span>RADAR BIẾN ĐỘNG DÒNG TIỀN</span>
                <AlertTriangle size={16} className="text-amber-500" />
              </div>
              <div className="text-xl font-bold text-amber-400">2 khoản chi lạ</div>
              <p className="text-xs text-slate-400 mt-1">Giao dịch 2.500.000đ phát sinh lúc 02:15 sáng.</p>
            </div>

            <div className="bg-slate-900 border border-slate-800 rounded-xl p-4">
              <div className="flex items-center justify-between text-slate-400 text-xs mb-2">
                <span>TỐC ĐỘ TIÊU NGÂN SÁCH (BURN RATE)</span>
                <TrendingDown size={16} className="text-rose-500" />
              </div>
              <div className="text-xl font-bold text-rose-400">72% / 12 ngày</div>
              <p className="text-xs text-slate-400 mt-1">Cảnh báo: Tiêu nhanh hơn mức trung bình 32%.</p>
            </div>

            <div className="bg-slate-900 border border-slate-800 rounded-xl p-4">
              <div className="flex items-center justify-between text-slate-400 text-xs mb-2">
                <span>HỒ SƠ USER PERSONA</span>
                <Sparkles size={16} className="text-emerald-400" />
              </div>
              <div className="text-xl font-bold text-emerald-400">Thận trọng vừa phải</div>
              <p className="text-xs text-slate-400 mt-1">Ngưỡng chi tiêu an toàn: 5.000.000đ/khoản.</p>
            </div>
          </div>
        </div>
      )}

      {/* TAB 2: SCAM SCANNER */}
      {activeTab === 'SCAM' && (
        <div className="space-y-4">
          <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
            <h3 className="font-bold text-lg flex items-center gap-2 text-white">
              <ShieldAlert className="text-pink-500" /> Máy quét Lừa đảo & Thao túng Tâm lý (AI Scam Intelligence)
            </h3>
            <p className="text-sm text-slate-400">
              Dán nội dung tin nhắn, SMS Brandname, đường dẫn URL hoặc đoạn chat để AI giải mã bẫy tâm lý.
            </p>

            <textarea
              rows={4}
              value={scamInput}
              onChange={(e) => setScamInput(e.target.value)}
              placeholder="Ví dụ: Em là cán bộ CSGT thông báo phạt nguội 5 triệu, bấm link http://tra-cuu-phat-nguoi.online/pay nộp ngay trong 24h nếu không sẽ khóa tài khoản..."
              className="w-full bg-slate-950 border border-slate-800 rounded-xl p-3 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-pink-500 transition"
            />

            <div className="flex gap-2">
              <button
                onClick={handleScanScam}
                disabled={isScanning}
                className="px-4 py-2 rounded-xl bg-pink-600 hover:bg-pink-500 font-semibold text-white text-sm flex items-center gap-2 transition disabled:opacity-50"
              >
                {isScanning ? 'Đang phân tích kịch bản...' : 'Quét ngay với AI'}
              </button>
              <button
                onClick={() => setScamInput('Em là CSGT thông báo phạt nguội 5.000.000đ, bấm link http://tra-cuu-phat-nguoi-cand.online/pay nộp ngay trong 24h nếu không sẽ khởi tố!')}
                className="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs text-slate-300 transition"
              >
                Nạp mẫu lừa đảo giả danh công an
              </button>
            </div>
          </div>

          {/* Scam Result Box */}
          {scamResult && (
            <div className="bg-slate-900 border border-red-500/40 rounded-2xl p-5 space-y-4">
              <div className="flex items-center justify-between">
                <span className="px-3 py-1 rounded-full bg-red-500/10 text-red-400 border border-red-500/30 text-xs font-bold uppercase tracking-wider">
                  Mức độ nguy hiểm: {scamResult.risk_level} ({scamResult.risk_score}/100)
                </span>
                <span className="text-xs text-slate-500">Scan ID: {scamResult.scan_id}</span>
              </div>

              <h4 className="font-semibold text-white text-base">{scamResult.summary}</h4>

              {/* Explainable AI Badges */}
              <div className="space-y-2">
                <p className="text-xs font-semibold text-pink-400 uppercase tracking-wider">Chiêu trò thao túng tâm lý phát hiện:</p>
                <div className="space-y-2">
                  {scamResult.psychological_manipulation?.map((item: any, idx: number) => (
                    <div key={idx} className="bg-slate-950 border border-slate-800 p-3 rounded-xl text-xs space-y-1">
                      <div className="font-bold text-amber-400">{item.tactic}</div>
                      <div className="text-slate-400 italic">" {item.evidence} "</div>
                      <div className="text-slate-300">{item.explanation}</div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Action Checklist */}
              <div className="bg-slate-950/80 border border-emerald-500/20 p-4 rounded-xl space-y-2">
                <p className="text-xs font-bold text-emerald-400 uppercase">Checklist hành động an toàn ngay lúc này:</p>
                <ul className="text-xs text-slate-300 space-y-1 list-disc list-inside">
                  {scamResult.actionable_checklist?.map((action: string, idx: number) => (
                    <li key={idx}>{action}</li>
                  ))}
                </ul>
              </div>
            </div>
          )}
        </div>
      )}

      {/* TAB 3: FINANCE RADAR */}
      {activeTab === 'FINANCE' && financeData && (
        <div className="space-y-4">
          <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
            <h3 className="font-bold text-lg text-white">Radar Phát hiện Biến động Bất thường & Tốc độ Tiêu Ngân sách</h3>
            
            <div className="bg-amber-500/10 border border-amber-500/30 p-4 rounded-xl text-amber-300 text-sm">
              ⚠️ {financeData.burn_rate?.message}
            </div>

            <div className="space-y-3">
              <h4 className="text-xs font-semibold uppercase text-slate-400">Các giao dịch lệch chuẩn cần kiểm tra:</h4>
              {financeData.recent_transactions?.filter((t: any) => t.is_anomaly).map((tx: any) => (
                <div key={tx.id} className="bg-slate-950 border border-slate-800 p-4 rounded-xl flex items-center justify-between">
                  <div>
                    <div className="font-bold text-white text-sm">{tx.recipient}</div>
                    <div className="text-xs text-red-400 mt-0.5">{tx.anomaly_reason}</div>
                    <div className="text-xs text-slate-500 mt-1">{tx.timestamp}</div>
                  </div>
                  <div className="text-right">
                    <span className="text-base font-bold text-white">{Number(tx.amount).toLocaleString('vi-VN')} đ</span>
                    <button className="block mt-2 text-xs text-pink-400 hover:underline">Xác nhận chính chủ</button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* TAB 4: RAG DOCUMENT */}
      {activeTab === 'RAG' && (
        <div className="space-y-4">
          <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
            <h3 className="font-bold text-lg text-white flex items-center gap-2">
              <FileText className="text-pink-500" /> RAG Studio – Bóc tách Hợp đồng & Chỉ điểm "Bẫy chữ nhỏ"
            </h3>
            <p className="text-sm text-slate-400">
              Công nghệ Retrieval-Augmented Generation đọc sâu từng trang hợp đồng vay, điều khoản thẻ tín dụng để vạch trần lãi suất ngầm và phí phạt cao.
            </p>

            <button
              onClick={handleAnalyzeMockDoc}
              disabled={analyzingDoc}
              className="px-4 py-2.5 rounded-xl bg-pink-600 hover:bg-pink-500 text-white font-semibold text-sm transition"
            >
              {analyzingDoc ? 'Đang đọc và phân tích RAG...' : 'Bóc tách file mẫu: Hop_Dong_Vay_Tieu_Dung.pdf'}
            </button>
          </div>

          {ragResult && (
            <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
              <div className="flex items-center justify-between">
                <h4 className="font-bold text-white">{ragResult.document_name}</h4>
                <span className="px-2.5 py-1 rounded-full bg-red-500/10 text-red-400 text-xs font-bold border border-red-500/20">
                  {ragResult.risk_rating}
                </span>
              </div>
              <p className="text-xs text-slate-300">{ragResult.summary}</p>

              <div className="space-y-2">
                <p className="text-xs font-bold uppercase text-amber-400">Bẫy chữ nhỏ phát hiện được:</p>
                {ragResult.hidden_traps?.map((trap: any, idx: number) => (
                  <div key={idx} className="bg-slate-950 border border-slate-800 p-3 rounded-xl text-xs space-y-1">
                    <div className="font-bold text-red-400">{trap.category}</div>
                    <div className="text-slate-400 italic">" {trap.clause_snippet} "</div>
                    <div className="text-amber-300">{trap.trap_warning}</div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      )}

      {/* TAB 5: PERSONA ADVISOR */}
      {activeTab === 'ADVISOR' && (
        <div className="space-y-4">
          <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
            <h3 className="font-bold text-lg text-white flex items-center gap-2">
              <Sparkles className="text-pink-500" /> Cố vấn Quyết định & Chi tiêu (Dựa trên Đặc trưng User Persona)
            </h3>
            <p className="text-sm text-slate-400">
              Nhập khoản chi hoặc gói tài chính bạn đang đắn đo. AI sẽ đối chiếu với thu nhập và chu kỳ hóa đơn của bạn để đưa ra lời khuyên.
            </p>

            <div className="flex gap-2">
              <input
                type="number"
                value={spendAmount}
                onChange={(e) => setSpendAmount(e.target.value)}
                className="bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-sm text-white focus:outline-none focus:border-pink-500"
                placeholder="Số tiền dự chi..."
              />
              <button
                onClick={handleGetAdvice}
                disabled={gettingAdvice}
                className="px-4 py-2 rounded-xl bg-pink-600 hover:bg-pink-500 text-white font-semibold text-sm transition"
              >
                {gettingAdvice ? 'Đang tính toán...' : 'Xin lời khuyên của FinGuard'}
              </button>
            </div>
          </div>

          {advisorResult && (
            <div className="bg-slate-900 border border-pink-500/40 rounded-2xl p-5 space-y-4">
              <span className="px-3 py-1 rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/30 text-xs font-bold">
                Khuyến nghị: {advisorResult.recommendation}
              </span>
              <h4 className="font-bold text-white text-base">{advisorResult.headline}</h4>
              <div className="bg-slate-950 p-4 rounded-xl text-xs text-slate-300 space-y-1.5">
                <p>• {advisorResult.personalized_analysis?.current_budget_status}</p>
                <p>• {advisorResult.personalized_analysis?.upcoming_obligations}</p>
                <p>• {advisorResult.personalized_analysis?.emergency_fund_impact}</p>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
