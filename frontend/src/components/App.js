import React from 'react';
import './App.css';
import ServerStatus from './components/ServerStatus';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>Server Monitoring Dashboard</h1>
                <ServerStatus />
            </header>
        </div>
    );
}

export default App;
