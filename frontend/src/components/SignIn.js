// src/components/SignIn.js
import React, { useState } from 'react';
import { Form, Button, Card, Container, Spinner } from 'react-bootstrap';
import { signIn } from 'aws-amplify/auth';

function SignIn(){
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [authError, setAuthError] = useState(null);
    const [isLoading, setIsLoading] = useState(false);


    const handleSubmit = async (event) => {
        event.preventDefault();
        setIsLoading(true); // Start loading
        try {
            const signInResponse = await signIn({ 
                username, // Use the state directly
                password  // Use the state directly
            });
    
            console.log('Sign in successful!', signInResponse);
            // Handle the successful sign-in
            setIsLoading(false); // Stop loading on success
            setAuthError(null); // Delete authentication message in case its present

        } catch (error) {
            console.error('Error signing in:', error);
            setAuthError(error.message || 'Authentication failed');
            // Handle sign-in errors
            setIsLoading(false); // Stop loading on failure
        }
    };


    return (
        <Container className="d-flex justify-content-center align-items-center" style={{ height: '100vh' }}>
            <Card style={{ width: '300px' }}>
                <Card.Body>
                     <Form onSubmit={handleSubmit}>
                        <Form.Group className="mb-3" controlId="formBasicEmail">
                            <Form.Label>Username</Form.Label>
                            <Form.Control type="text" placeholder="Enter username" value={username} onChange={e => setUsername(e.target.value)} />
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="formBasicPassword">
                            <Form.Label>Password</Form.Label>
                            <Form.Control type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
                        </Form.Group>
                        
                        {authError && <div className="alert alert-danger alert-dismissible fade show" role="alert"> {authError} 
                                            <button type="button" className="btn-close" data-bs-dismiss="alert" aria-label="Close" onClick={() => setAuthError(null)}>
                                            </button>
                                    </div>}
                        
                        {isLoading ? (
                            <Button variant="primaty" disabled>
                                <Spinner as="span" animation="border" size="sm" role="status" aria-hidden="true" />
                                <span className="sr-only">Signin in</span>    
                            </Button>
                        ):(
                            <Button variant="primary" type="submit">
                                Sign In
                            </Button>
                            
                        )}
                     </Form>
                </Card.Body>
            </Card>
        </Container>
    );
}

export default SignIn;