// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home/Home';
import Header from './components/Header';
import Footer from './components/Footer';
import Departamentos from './pages/Departamentos';

const App = () => {
    return (
        <Router>
            <div>
                <Header />
                <br></br>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/departamentos" element={<Departamentos />} />
                </Routes>
                <Footer />
            </div>
        </Router>
    );
};

export default App;
