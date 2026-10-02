import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://alsalafiyyah.github.io',
  base: '/fawaid',
  trailingSlash: 'never',
  build: {
    format: 'directory'
  }
});