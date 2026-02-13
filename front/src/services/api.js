import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Health check service
export const healthCheck = async () => {
  try {
    const response = await api.get('/health');
    return response.data;
  } catch (error) {
    throw error.response?.data || error.message;
  }
};

// Test endpoint service
export const testApi = async () => {
  try {
    const response = await api.get('/test');
    return response.data;
  } catch (error) {
    throw error.response?.data || error.message;
  }
};

// Sample data service
export const getSampleData = async () => {
  try {
    const response = await api.get('/data');
    return response.data;
  } catch (error) {
    throw error.response?.data || error.message;
  }
};

export default api;