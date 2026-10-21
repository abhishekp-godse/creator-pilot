/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f0fdf4',
          500: '#22c55e',
          600: '#16a34a',
        },
        brand: {
          dark: '#0f172a',
          card: '#1e293b',
          border: '#334155',
          accent: '#6366f1'
        }
      }
    },
  },
  plugins: [],
}
