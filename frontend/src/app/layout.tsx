import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'FinGuard AI - Your Intelligent Financial Guardian',
  description: 'Trợ lý tài chính thông minh - Chủ động nhận diện lừa đảo và tối ưu dòng tiền cá nhân',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="vi">
      <body className="min-h-screen bg-slate-950 text-slate-100 flex flex-col">
        {/* Navigation Header */}
        <header className="sticky top-0 z-50 bg-slate-900/80 backdrop-blur-md border-b border-slate-800 px-4 py-3">
          <div className="max-w-5xl mx-auto flex items-center justify-between">
            <div className="flex items-center gap-2">
              <span className="text-2xl">🛡️</span>
              <div>
                <h1 className="font-bold text-lg text-pink-500 tracking-tight">FinGuard AI</h1>
                <p className="text-xs text-slate-400">MoMo Hackathon 2026</p>
              </div>
            </div>
            <div className="flex items-center gap-3 text-sm">
              <span className="px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 text-xs font-medium">
                ● Hệ thống An toàn
              </span>
              <div className="w-8 h-8 rounded-full bg-pink-600 flex items-center justify-center font-bold text-white text-xs">
                U
              </div>
            </div>
          </div>
        </header>

        {/* Main Content */}
        <main className="flex-1 max-w-5xl w-full mx-auto p-4 md:p-6 pb-20">
          {children}
        </main>
      </body>
    </html>
  );
}
