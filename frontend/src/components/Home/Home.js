// src/components/Home/Home.js
import React from 'react';
import './Home.css'; // Importa el archivo CSS para estilos

const Home = () => {
    return (
        <div className="home-container">
            <header className="header">
                <h1>Bienvenido a Reservas de Escenarios</h1>
                <p>¡Descubre, reserva y disfruta de experiencias inolvidables!</p>
                <button className="btn-primary">Comienza Ahora</button>
            </header>

            <section className="services">
                <h2>Nuestros Servicios</h2>
                <div className="service-cards">
                    <div className="service-card">
                        <img src="https://via.placeholder.com/150" alt="Servicio 1" />
                        <h3>Servicio 1</h3>
                        <p>Descripción breve del servicio 1.</p>
                    </div>
                    <div className="service-card">
                        <img src="https://via.placeholder.com/150" alt="Servicio 2" />
                        <h3>Servicio 2</h3>
                        <p>Descripción breve del servicio 2.</p>
                    </div>
                    <div className="service-card">
                        <img src="https://via.placeholder.com/150" alt="Servicio 3" />
                        <h3>Servicio 3</h3>
                        <p>Descripción breve del servicio 3.</p>
                    </div>
                </div>
            </section>

            <section className="testimonial">
                <h2>Testimonios</h2>
                <p>"Una experiencia increíble, ¡definitivamente volveré!" - Cliente Satisfecho</p>
            </section>

            {/* Elimina el footer de aquí */}
            {/* <footer className="footer">
                <p>&copy; 2024 Reservas de Escenarios. Todos los derechos reservados.</p>
            </footer> */}
        </div>
    );
};

export default Home;
