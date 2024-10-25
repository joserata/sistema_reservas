import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Departamentos.css';

const Departamentos = () => {
    const [departamentos, setDepartamentos] = useState([]);
    const [filteredDepartamentos, setFilteredDepartamentos] = useState([]);
    const [error, setError] = useState('');
    const [searchTerm, setSearchTerm] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const itemsPerPage = 5; // Cambia esto si quieres mostrar más o menos elementos por página
    const [editingDepartamento, setEditingDepartamento] = useState(null);
    const [newName, setNewName] = useState('');

    useEffect(() => {
        const fetchDepartamentos = async () => {
            try {
                const response = await axios.get('http://localhost:8000/departamentos/');
                setDepartamentos(response.data);
                setFilteredDepartamentos(response.data); // Inicializa los departamentos filtrados
            } catch (err) {
                setError('Error al cargar los departamentos');
            }
        };
        fetchDepartamentos();
    }, []);

    useEffect(() => {
        // Filtrar departamentos según el término de búsqueda
        setFilteredDepartamentos(
            departamentos.filter(departamento =>
                departamento.name.toLowerCase().includes(searchTerm.toLowerCase())
            )
        );
    }, [searchTerm, departamentos]);

    // Función para manejar la edición
    const handleEdit = (departamento) => {
        setEditingDepartamento(departamento);
        setNewName(departamento.name); // Establecer el nombre actual del departamento para editar
    };

    // Función para manejar la actualización
    const handleUpdate = async () => {
        try {
            await axios.put(`http://localhost:8000/departamentos/${editingDepartamento.id}/`, {
                ...editingDepartamento,
                name: newName // Actualizar el nombre
            });
            // Actualizar la lista de departamentos
            setDepartamentos(departamentos.map(departamento =>
                departamento.id === editingDepartamento.id ? { ...departamento, name: newName } : departamento
            ));
            setFilteredDepartamentos(filteredDepartamentos.map(departamento =>
                departamento.id === editingDepartamento.id ? { ...departamento, name: newName } : departamento
            ));
            setEditingDepartamento(null); // Cerrar el formulario de edición
        } catch (err) {
            setError('Error al actualizar el departamento');
        }
    };

    // Función para manejar la eliminación
    const handleDelete = async (id) => {
        if (window.confirm('¿Estás seguro de que deseas eliminar este departamento?')) {
            try {
                await axios.delete(`http://localhost:8000/departamentos/${id}/`);
                // Actualizar la lista de departamentos después de eliminar
                setDepartamentos(departamentos.filter(departamento => departamento.id !== id));
            } catch (err) {
                setError('Error al eliminar el departamento');
            }
        }
    };

    // Paginación
    const indexOfLastItem = currentPage * itemsPerPage;
    const indexOfFirstItem = indexOfLastItem - itemsPerPage;
    const currentItems = filteredDepartamentos.slice(indexOfFirstItem, indexOfLastItem);
    const totalPages = Math.ceil(filteredDepartamentos.length / itemsPerPage);

    return (
        <div className="departamentos">
            <h1>Departamentos</h1>
            {error && <p className="error">{error}</p>}

            {/* Barra de búsqueda */}
            <input
                type="text"
                placeholder="Buscar departamentos..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
            />

            <table className="departamentos-table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nombre</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {currentItems.map(departamento => (
                        <tr key={departamento.id}>
                            <td>{departamento.id}</td>
                            <td>{departamento.name}</td>
                            <td>
                                <button onClick={() => handleEdit(departamento)}>Editar</button>
                                <button onClick={() => handleDelete(departamento.id)}>Eliminar</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>

            {/* Formulario de Edición */}
            {editingDepartamento && (
                <div className="edit-form">
                    <h2>Editar Departamento</h2>
                    <input
                        type="text"
                        value={newName}
                        onChange={(e) => setNewName(e.target.value)}
                        placeholder="Nuevo nombre del departamento"
                    />
                    <button onClick={handleUpdate}>Guardar</button>
                    <button onClick={() => setEditingDepartamento(null)}>Cancelar</button>
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

export default Departamentos;
