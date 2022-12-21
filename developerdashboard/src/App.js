import './App.css';
import Dashboard from './components/Dashboard';
import { useEffect } from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import DetailedView from './components/DetailedView';
import Results from './components/Results';

export const eel = window.eel
if(eel !== null && eel !== undefined){
  eel.set_host('ws://localhost:8080')
}

function App() {

useEffect(() => {
},[])

  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<Dashboard />} />
        <Route path="results/:pricelow/:pricehigh/:" element={<Results />} />
        <Route path="detailedView" element={<DetailedView />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
