import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  base: "/",
  // Put the dist folder into the backend to enable easier deployment
  build: {
    outDir: '../backend/dist',
    emptyOutDir: true, // also necessary
  }
})

