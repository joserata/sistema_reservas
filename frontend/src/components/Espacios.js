import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Departamentos.css';


const Espacios = () => {
    const BASE_URL = 'http://localhost:8000';
    const [espacios, setEspacios] = useState([]);
    const [filteredEspacios, setFilteredEspacios] = useState([]);
    const [error, setError] = useState('');
    const [searchTerm, setSearchTerm] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const itemsPerPage = 5; 
    const [editingEspacio, setEditingEspacio] = useState(null);
    const [newName, setNewName] = useState('');

    useEffect(() => {
        const fetchEspacios = async () => {
            try {
                const response = await axios.get('http://localhost:8000/espacios/');
                setEspacios(response.data);
                setFilteredEspacios(response.data); // Inicializa los espacios filtrados
            } catch (err) {
                setError('Error al cargar los espacios');
            }
        };
        fetchEspacios();
    }, []);

    useEffect(() => {
        // Filtrar espacios según el término de búsqueda
        setFilteredEspacios(
            espacios.filter(espacio =>
                espacio.name.toLowerCase().includes(searchTerm.toLowerCase())
            )
        );
    }, [searchTerm, espacios]);

    // edición
    const handleEdit = (espacio) => {
        setEditingEspacio(espacio);
        setNewName(espacio.name); // Establecer el nombre actual del departamento para editar
    };

    // actualización
    const handleUpdate = async () => {
        try {
            await axios.put(`http://localhost:8000/espacios/${editingEspacio.id}/`, {
                ...editingEspacio,
                name: newName // Actualizar el nombre
            });
            // Actualizar la lista de espacios
            setEspacios(espacios.map(espacio =>
                espacio.id === editingEspacio.id ? { ...espacio, name: newName } : espacio
            ));
            setFilteredEspacios(filteredEspacios.map(espacio =>
                espacio.id === editingEspacio.id ? { ...espacio, name: newName } : espacio
            ));
            setEditingEspacio(null); // Cerrar el formulario de edición
        } catch (err) {
            setError('Error al actualizar el Espacio');
        }
    };

    // eliminación
    const handleDelete = async (id) => {
        if (window.confirm('¿Estás seguro de que deseas eliminar este Escenario?')) {
            try {
                await axios.delete(`http://localhost:8000/espacios/${id}/`);
                // Actualizar la lista de espacios después de eliminar
                setEspacios(espacios.filter(espacio => espacio.id !== id));
            } catch (err) {
                setError('Error al eliminar el Escenario');
            }
        }
    };

    // Paginación
    const indexOfLastItem = currentPage * itemsPerPage;
    const indexOfFirstItem = indexOfLastItem - itemsPerPage;
    const currentItems = filteredEspacios.slice(indexOfFirstItem, indexOfLastItem);
    const totalPages = Math.ceil(filteredEspacios.length / itemsPerPage);

    return (
        <div className="departamentos">
            <h1>Escenarios</h1>
            {error && <p className="error">{error}</p>}

            {/* Barra de búsqueda */}
            <input
                type="text"
                placeholder="Buscar escenarios..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
            />

            <table className="departamentos-table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Imagen</th>
                        <th>Nombre</th>
                        <th>Ubicacion</th>
                        <th>Capacidad</th>
                        <th>Descripcion</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {currentItems.map(espacio => (
                        <tr key={espacio.id}>
                            <td>{espacio.id}</td>
                            <td>
                                <img
                                    src={`${BASE_URL}/static/images/${espacio.imagen}`}
                                    alt={espacio.nombre}
                                    width="100"
                                    height="100"
                                />
                            </td>
                            <td>{espacio.name}</td>
                            <td>{espacio.ubicacion}</td>
                            <td>{espacio.capacidad}</td>
                            <td>{espacio.descripcion}</td>
                            <td>
                                <button onClick={() => handleEdit(espacio)}>Editar</button>
                                <button onClick={() => handleDelete(espacio.id)}>Eliminar</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>

            {/* Formulario de Edición */}
            {editingEspacio && (
                <div className="edit-form">
                    <h2>Editar Escenario</h2>
                    <input
                        type="text"
                        value={newName}
                        onChange={(e) => setNewName(e.target.value)}
                        placeholder="Nuevo nombre del Escenario"
                    />
                    <button onClick={handleUpdate}>Guardar</button>
                    <button onClick={() => setEditingEspacio(null)}>Cancelar</button>
                </div>
            )}

            {/* Paginación */}
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

export default Espacios;
