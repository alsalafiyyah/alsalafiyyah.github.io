/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './**/*.html',
    './**/*.md',
    './_layouts/**/*.html',
    './_layouts/**/*.liquid',
    './_posts/**/*.md',
    './_posts/*.md',
    './_pages/**/*.md',
    './_pages/**/*.html',
    './_pages/*.md',
    './_pages/*.html',
    './_includes/**/*.html',
    './_includes/**/*.liquid',
 ],
 darkMode: 'class',
  theme: {
    extend: {},
 },
  plugins: [require('@tailwindcss/typography')]
}
