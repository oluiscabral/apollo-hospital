import React from 'react';
import { Route, BrowserRouter, Switch } from 'react-router-dom';

// import ProtectedRoute from './ProtectedRoute';

import Login from './pages/login/Login';
import Dashboard from './pages/dashboard/Dashboard';


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route path="/login" component={Login} />
          <Route path="/dashboard" component={Dashboard} />
          {/* <ProtectedRoute component={Dashboard} /> */}
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
