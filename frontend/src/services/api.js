// src/services/api.js
import axios from 'axios';

// Configura la URL base de tu backend de Django
const api = axios.create({
  baseURL: 'http://localhost:8000/', // Cambia la URL según la configuración de tu backend
});

// Puedes agregar otras configuraciones globales si lo necesitas

export default api;
