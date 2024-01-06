// src/services/api.js
import axios from 'axios';

const API = axios.create({
  baseURL: process.env.REACT_APP_BACKEND_URL || 'http://backend:8000',
  headers: {
    'Content-Type': 'application/json'
  }
});

export default API;

export const fetchUserData = async (userId) => {
  try {
    const response = await API.get(`/users/${userId}`);
    return response.data;
  } catch (error) {
    // Handle error (e.g., logging or displaying a message)
    console.error('Error fetching user data:', error);
    throw error;
  }
};
