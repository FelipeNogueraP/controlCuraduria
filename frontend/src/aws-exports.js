// src/aws-exports.js
const awsExports = {
    Auth: {
        Cognito:{
            userPoolId: process.env.REACT_APP_COGNITO_POOL_ID,
            userPoolClientId: process.env.REACT_APP_COGNITO_POOL_CLIENT_ID,
        }
    },
};

export default awsExports;
