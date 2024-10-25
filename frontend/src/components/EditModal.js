// src/components/EditModal.js
import React, { useState, useEffect } from 'react';
import './EditModal.css'; // Asegúrate de tener estilos para el modal

const EditModal = ({ isOpen, onClose, departamento, onEdit }) => {
    const [name, setName] = useState('');

    useEffect(() => {
        if (departamento) {
            setName(departamento.name); // Asigna el nombre actual al estado
        }
    }, [departamento]);

    const handleSubmit = (e) => {
        e.preventDefault();
        onEdit({ ...departamento, name }); // Llama a la función de edición con el nuevo nombre
        onClose(); // Cierra el modal después de editar
    };

    if (!isOpen) return null; // No renderiza el modal si no está abierto

    return (
        <div className="modal">
            <div className="modal-content">
                <span className="close" onClick={onClose}>&times;</span>
                <h2>Editar Departamento</h2>
                <form onSubmit={handleSubmit}>
                    <div>
                        <label>Nombre:</label>
                        <input
                            type="text"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                            required
                        />
                    </div>
                    <button type="submit">Guardar</button>
                </form>
            </div>
        </div>
    );
};

export default EditModal;
