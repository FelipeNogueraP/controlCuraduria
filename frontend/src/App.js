// src/App.js
import React from 'react';
import UserProfile from './components/UserProfile';

function App() {
  return (
    <div className="App">
      <UserProfile userId="1" /> {/* Example user ID */}
    </div>
  );
}

export default App;
