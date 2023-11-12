import React from 'react';
import './App.css';
import Gallery from './Gallery';

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <h1 className="gallery-header">React képgaléria</h1>
      </header>
      <main>
        <Gallery />
      </main>
    </div>
  );
}

export default App;
