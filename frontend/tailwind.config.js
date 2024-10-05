/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      fontFamily: {
        "display": ["Cambridge Round Regular", "sans-serif"],
        "sans": ["Workday Adelle Sans Regular", "Cambridge Round Regular", "sans-serif"]
      },
      colors: {
        "primary": "#0862be",
        "secondary": "#f28f08",
      }
    },
  },
  plugins: [],
}

