const defaultTheme = require('tailwindcss/defaultTheme')
const plugin = require('tailwindcss/plugin')

module.exports = {
  content: [
    './templates/**/*.{html,js}',
    './projetointegrador/templates/**/*.{html,js}',
  ],
  theme: {
    screens: {
      'xsm': '400px',
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      'hdtv': '1450px',
      '2xl': '1536px',      
      'almostfullhd': '1800px',
      'fullhd': '1920px'
    },
    extend: {
      maxWidth: {
        '1920': '1920px',
      },
    },
  },
  plugins: [],
}
