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
      fontFamily: {
        'baloo-bhai': ['"Baloo Bhai 2"', 'cursive'],
        'baloo-bhaina': ['"Baloo Bhaina 2"', 'cursive'],
        'baloo-thambi': ['"Baloo Thambi 2"', 'cursive'],
      },
      
    },
  },
  plugins: [],
}

