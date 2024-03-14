/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '**/**/**/**/*.html',
  ],
  theme: {
    extend: {
      backgroundImage: theme => ({
        'sea': "url('/static/img/background.jpg')",
      }),
      
    },
  },
  plugins: [],
}

