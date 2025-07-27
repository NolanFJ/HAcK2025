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
  const [currentImage, setCurrentImage] = useState(null);

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
    });

    // set picture connection, and update currentPicture
    socket.on('picture_taken', data => {
      setPictureStatus(data.message);
      if (data.success) {
        const timestamp = new Date().getTime();
        const imagePath = `/downloaded_image.jpg?t=${timestamp}`;
        console.log('Setting image path to: ', imagePath)
        setCurrentImage(imagePath);
      }
      setTimeout(() => setPictureStatus(""), 3000);
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
      alert("Please enter a message");
    }
  }

  // handle enter key input
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      sendMessage();
    }
  }

  return (
    <div className="dashboard">
      <div className="dashboard-container">
        <div className="main-grid">
          {/* Display sensor data */}
          <div className="sensor-section">
            <h2 className="section-header">
              Sensor Readings
            </h2>
            <div className="sensor-grid">
              <div className="sensor-card temperature">
                <div className="sensor-label">Temperature (F)</div>
                <div className="sensor-value">{temp || 'No data'}</div>
              </div>
              <div className="sensor-card humidity">
                <div className="sensor-label">Humidity (%)</div>
                <div className="sensor-value">{humidity || 'No data'}</div>
              </div>
              <div className="sensor-card light">
                <div className="sensor-label">Light (lumens)</div>
                <div className="sensor-value">{light || 'No data'}</div>
              </div>
              <div className="sensor-card ultrasonic">
                <div className="sensor-label">Distance (cm)</div>
                <div className="sensor-value">{ultrasonic || 'No data'}</div>
              </div>
            </div>
          </div>

          {/* Camera Section */}
          <div className="camera-section">
            <h2 className="section-header">
              Camera Control
            </h2>

            <div className="camera-controls">
              <button onClick={handlePicture} className="take-picture-btn">
                Take Picture
              </button>
              {pictureStatus && <p className="picture-status">{pictureStatus}</p>}
            </div>

            {/* Display the current image */}
            {currentImage && (
              <div className="image-container">
                <h3 className="image-title">Latest Picture:</h3>
                <div className="image-wrapper">
                  <img
                    src={currentImage}
                    alt="Latest capture"
                    className="captured-image"
                    onError={() => {
                      console.log('Image failed to load');
                      setCurrentImage(null);
                    }}
                  />
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Message input section */}
        <div className="message-section">
          <h2 className="section-header">
            Send Message to Pico
          </h2>
          <div className="message-form">
            <input
              type="text"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              onKeyDown={handleKeyPress}
              placeholder="Type message for Pico..."
              className="message-input"
            />
            <button onClick={sendMessage} className="send-btn">
              Send
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;