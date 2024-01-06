// src/components/UserProfile.js
import React, { useEffect, useState } from 'react';
import { fetchUserData } from '../services/api';

const UserProfile = ({ userId }) => {
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    setError(null);
    const loadUserData = async () => {
      try {
        const data = await fetchUserData(userId);
        setUserData(data);
      } catch (error) {
        setError('Failed to load user data.');
      } finally {
        setLoading(false);
      }
    };

    loadUserData();
  }, [userId]);

  return (
    <div>
      {error && <p className="error">{error}</p>}
      {loading ? (
        <p>Loading user data...</p>
      ) : userData ? (
        <div>
          <h1>{userData.name}</h1>
          {/* Render other user data */}
        </div>
      ) : (
        <p>No user data found.</p>
      )}
    </div>
  );
};

export default UserProfile;
