import React from 'react';
import { Amplify } from 'aws-amplify';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import SignIn from './components/SignIn';
import awsExports from './aws-exports';


Amplify.configure(awsExports);

// You can get the current config object
const currentConfig = Amplify.getConfig();

console.log(currentConfig)

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/signin" element={<SignIn />} />
        {/* Other routes */}
      </Routes>
    </Router>
  );
}

export default App;
