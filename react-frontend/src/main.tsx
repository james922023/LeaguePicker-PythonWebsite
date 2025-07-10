import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Role from './Role.tsx'
import Details from './Details.tsx';
import CreateBuild from './CreateBuild.tsx';
createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/roles" element={<Role />} />
        <Route path="/details" element={<Details />} />
        <Route path="/createbuild" element={<CreateBuild/>} />
      </Routes>
    </BrowserRouter>
  </StrictMode>,
)
