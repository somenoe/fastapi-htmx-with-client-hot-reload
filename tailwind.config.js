/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.{html,js,css}",
    "./static/**/*.{html,js}",
  ],
  theme: {
    extend: {
      keyframes: {
        rainbow: {
          '0%': { color: '#ff0000' },
          '14.28%': { color: '#ff7f00' },
          '28.56%': { color: '#ffff00' },
          '42.84%': { color: '#48ff00' },
          '57.12%': { color: '#008cff' },
          '71.4%': { color: '#3549ff' },
          '85.68%': { color: '#8732fe' },
          '100%': { color: '#ff0000' },
        },
      },
      animation: {
        rainbow: 'rainbow 3s linear infinite',
      },
    },
  },
  plugins: [],
}
