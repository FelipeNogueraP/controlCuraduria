import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import SignIn from './components/SignIn';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/signin" component={SignIn} />
        {/* Other routes */}
      </Switch>
    </Router>
  );
}

export default App;
