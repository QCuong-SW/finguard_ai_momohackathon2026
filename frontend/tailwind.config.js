/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        finguard: {
          primary: '#8b0051', // Màu hồng đậm biểu trưng MoMo
          secondary: '#b30068',
          dark: '#0f172a',
          card: '#1e293b',
          accent: '#10b981',
          danger: '#ef4444',
          warning: '#f59e0b',
        },
      },
    },
  },
  plugins: [],
};
