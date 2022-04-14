import logo from './logo.svg';
import './App.css';
import React, { useState } from "react";

function App() {
  var counterVal = 0;
  function increment() {
    counterVal++;
    document.getElementById("count").innerHTML = (counterVal);
  }
  function decrement() {
    counterVal--;
    document.getElementById("count").innerHTML = (counterVal);
  }

  return (
    <div className="App">
      <header className="App-header">
        <button 
          type="button" onClick={() => increment()}>+
        </button>
        <button 
          type="button" onClick={() => decrement()}>-
        </button>
        <p><h3 id="count">0</h3></p>
      </header>
    </div>
  );
}

export default App;
