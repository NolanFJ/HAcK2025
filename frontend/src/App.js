import React, { useState, useEffect } from "react";
import io from 'socket.io-client';
import './App.css';

const socket = io('http://localhost:8000');

function App() {
  const [pictureStatus, setPictureStatus] = useState("");
  const [temp, setTemp] = useState(null);
  const [humidity, setHumidity] = useState(null);
  const [ultrasonic, setUltrasonic] = useState(null);
  const [light, setLight] = useState(null);
  const [message, setMessage] = useState("");

  useEffect(() => {
    socket.on('connect', () => console.log('Connected:', socket.id));

    // data connection establishers
    socket.on('temp', data => {
      setTemp(data);
    });

    socket.on('humidity', data => {
      setHumidity(data);
    });

    socket.on('ultrasonic', data => {
      setUltrasonic(data);
    });

    socket.on('light', data => {
      setLight(data)
    })

    socket.on('picture_taken', data => {
      setPictureStatus(data.message);
      setTimeout(() => setPictureStatus(""), 3000); // Clear status after 3 seconds
    });
    return () => {
      socket.off('temp');
      socket.off('humidity');
      socket.off('ultrasonic');
      socket.off('light');
      socket.off('picture_taken');
    };
  }, []);

  // frontend publishes picture topic
  const handlePicture = () => {
    console.log("Frontend requesting picture")
    setPictureStatus("Taking a Picture...")
    socket.emit('take_picture', 'Taking a Picture...')
  }

  // send a message to the pico
  const sendMessage = () => {
    if (message.trim()) {
      console.log("Sending message from frontend: ", message)
      socket.emit('display', message)
      setMessage(""); // clear input after sending
    }
    else {
      alert("Please enter a mesage");
    }
  }

  // handle enter key input
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      sendMessage();
    }
  }

  return (
    <div className="app">
      <p>             </p>
      {/* Display sensor data for testing */}
      <div>
        <p>Temperature: {temp || 'No data'}</p>
        <p>Humidity: {humidity || 'No data'}</p>
        <p>Light: {light || 'No data'}</p>
        <p>Ultrasonic: {ultrasonic || 'No data'}</p>

        <button onClick={handlePicture}>Take Picture</button>
        {pictureStatus && <p>{pictureStatus}</p>}

        <p>             </p>

        {/* Message input section */}
        <div>
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={handleKeyPress}
            placeholder="Type message for Pico..."
          />
          <button onClick={sendMessage}>Send to Pico</button>
        </div>
      </div>
    </div>
  )
}

export default App;
