// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home/Home';
import Header from './components/Header';
import Footer from './components/Footer';
import Departamentos from './pages/Departamentos';
import 'bootstrap/dist/css/bootstrap.min.css';
import Espacios from './components/Espacios';
import Reservas from './components/Reservas';

const App = () => {
    return (
        <Router>
            <div>
                <Header />
                <br></br>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/departamentos" element={<Departamentos />} />
                    <Route path="/espacios" element={<Espacios />} />
                    <Route path="/reservas" element={<Reservas />} />
                </Routes>
                <Footer />
            </div>
        </Router>
    );
};

export default App;
