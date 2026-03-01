import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import monacoEditorPlugin from 'vite-plugin-monaco-editor';

const monacoEditorPluginDefault = (monacoEditorPlugin).default;

export default defineConfig({
  plugins: [vue(), monacoEditorPluginDefault({})],
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false
      }
    }
  }
})