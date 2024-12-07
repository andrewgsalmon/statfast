import './App.scss';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home/Home';
import League from './pages/League/League';

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="" element={<Home />} />
          <Route path="league" element={<League />} />
          <Route path="league/:idFromParams" element={<League />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
