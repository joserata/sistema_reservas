// Reservas.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Departamentos.css';

const Reservas = () => {
    const [reservas, setReservas] = useState([]);
    const [filteredReservas, setFilteredReservas] = useState([]);
    const [error, setError] = useState('');
    const [searchTerm, setSearchTerm] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const itemsPerPage = 5; 
    const [editingReserva, setEditingReserva] = useState(null);
    const [newComments, setNewComments] = useState('');

    useEffect(() => {
        const fetchReservas = async () => {
            try {
                const response = await axios.get('http://localhost:8000/reservas/');
                setReservas(response.data);
                setFilteredReservas(response.data); 
            } catch (err) {
                setError('Error al cargar las reservas');
            }
        };
        fetchReservas();
    }, []);

    useEffect(() => {
        setFilteredReservas(
            reservas.filter(reserva =>
                reserva.comentarios.toLowerCase().includes(searchTerm.toLowerCase())
            )
        );
    }, [searchTerm, reservas]);

    const handleEdit = (reserva) => {
        setEditingReserva(reserva);
        setNewComments(reserva.comentarios); 
    };

    const handleUpdate = async () => {
        try {
            await axios.put(`http://localhost:8000/reservas/${editingReserva.id_reserva}/`, {
                ...editingReserva,
                comentarios: newComments 
            });
            setReservas(reservas.map(reserva =>
                reserva.id_reserva === editingReserva.id_reserva ? { ...reserva, comentarios: newComments } : reserva
            ));
            setFilteredReservas(filteredReservas.map(reserva =>
                reserva.id_reserva === editingReserva.id_reserva ? { ...reserva, comentarios: newComments } : reserva
            ));
            setEditingReserva(null);
        } catch (err) {
            setError('Error al actualizar la reserva');
        }
    };

    const handleDelete = async (id) => {
        if (window.confirm('¿Estás seguro de que deseas eliminar esta reserva?')) {
            try {
                await axios.delete(`http://localhost:8000/reservas/${id}/`);
                setReservas(reservas.filter(reserva => reserva.id_reserva !== id));
                setFilteredReservas(filteredReservas.filter(reserva => reserva.id_reserva !== id));
            } catch (err) {
                setError('Error al eliminar la reserva');
            }
        }
    };

    const indexOfLastItem = currentPage * itemsPerPage;
    const indexOfFirstItem = indexOfLastItem - itemsPerPage;
    const currentItems = filteredReservas.slice(indexOfFirstItem, indexOfLastItem);
    const totalPages = Math.ceil(filteredReservas.length / itemsPerPage);

    return (
        <div className="departamentos">
            <h1>Reservas</h1>
            {error && <p className="error">{error}</p>}

            <input
                type="text"
                placeholder="Buscar por comentario..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
            />

<table className="departamentos-table">
    <thead>
        <tr>
            <th>ID</th>
            <th>Usuario</th>
            <th>Espacio</th>
            <th>Fecha Reserva</th>
            <th>Hora Inicio</th>
            <th>Hora Fin</th>
            <th>Estado</th>
            <th>Comentarios</th>
            <th>Acciones</th>
        </tr>
    </thead>
    <tbody>
        {currentItems.map(reserva => (
            <tr key={reserva.id_reserva}>
                <td>{reserva.id_reserva}</td>
                <td>{reserva.id_usuario.nombre}</td>
                <td>{reserva.id_espacio.name}</td>
                <td>{reserva.fecha_reserva}</td>
                <td>{reserva.hora_inicio}</td>
                <td>{reserva.hora_fin}</td>
                <td>{reserva.estado}</td>
                <td>{reserva.comentarios}</td>
                <td>
                    <button onClick={() => handleEdit(reserva)}>Editar</button>
                    <button onClick={() => handleDelete(reserva.id_reserva)}>Eliminar</button>
                </td>
            </tr>
        ))}
    </tbody>
</table>

            {editingReserva && (
                <div className="edit-form">
                    <h2>Editar Reserva</h2>
                    <input
                        type="text"
                        value={newComments}
                        onChange={(e) => setNewComments(e.target.value)}
                        placeholder="Nuevos comentarios"
                    />
                    <button onClick={handleUpdate}>Guardar</button>
                    <button onClick={() => setEditingReserva(null)}>Cancelar</button>
                </div>
            )}

            <div className="pagination">
                {Array.from({ length: totalPages }, (_, index) => (
                    <button
                        key={index + 1}
                        onClick={() => setCurrentPage(index + 1)}
                        className={currentPage === index + 1 ? 'active' : ''}
                    >
                        {index + 1}
                    </button>
                ))}
            </div>
        </div>
    );
};

export default Reservas;
