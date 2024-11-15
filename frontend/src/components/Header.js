import React from 'react';
import './Header.css'; 

const Header = () => {
    return (
        <header className="header">
            <div className="logo">Sistema de Reservas</div>
            <nav className="nav">
                <ul>
                    <li><a href="/">Inicio</a></li>
                    <li><a href="/departamentos">Departamentos</a></li>
                    <li><a href="/espacios">Espacios</a></li>
                    <li><a href="/reservas">Reservas</a></li>
                    <li><a href="/contacto">Contacto</a></li>
                </ul>
            </nav>
        </header>
    );
};

export default Header;
