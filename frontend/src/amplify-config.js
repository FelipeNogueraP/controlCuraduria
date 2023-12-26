// src/amplify-config.js
import Amplify from 'aws-amplify';

Amplify.configure({
    Auth: {
        region: process.env.REACT_APP_COGNITO_REGION,
        userPoolId: process.env.REACT_APP_COGNITO_USER_POOL_ID,
        userPoolWebClientId: process.env.REACT_APP_COGNITO_APP_CLIENT_ID
    }
});

export default Amplify;
