# HACK 2025 PROJECT

## Cloning the project 

- Clone the repository by running 'git clone (url)'

## Backend and Frontend setup

- In the backend directory, create a file named '.env', and add the following:

- CONNECT_URL=mqtts://(your URL):(your port)

- MQTT_USER=(your user)

- MQTT_PASS=(your pass)

- Then, while in the backend directory, install the dependencies by running
### `npm install`
- You can start the backend by running 
### `node index.js`

- In a separate terminal, in the frontend directory, install the dependencies by running
### `npm install`
- You can start the frontend by running 
### `npm start`

## Using connections.py for your Pico 2W

- You will be able to use 2 functions in connections.py
    - One for connection to the MQTT broker (connect_mqtt) and one for connecting to WIFI (connect_internet)

    - connect_mqtt(mqtt_server, mqtt_user, mqtt_pass):

        - mqtt_server: the server url which you have obtained by making a free serverless MQTT Broker on HIVEMQ
            - Should look something like: '37##616##db7#bd1##cac997eb01##13.s1.eu.hivemq.cloud'

        - mqtt_user:
            - This is the name of the user you create when you make a credential
                - The purpose of this is just to have a unique user in which the MQTT Broker can understand where the message is coming from 
                - Ex: username = 'pico' when creating credentials for the Raspberry Pi Pico W to send something

        - mqtt_pass:
            - This is the password that goes along with your mqtt_user
            - Just for the broker to validate the user
            - Make this whatever you want, just write it down

        - RETURNS client, which you can use 
            - client.subscribe(b"topic") to subscribe to a topic of your choice
            - client.publish(b"topic", b"message") to publish a message with a topic of your choice
            - client

    - connect_internet( ssid, password ):
        
        - ssid: 
            - This is the name of the wi-fi network you are trying to connect to

        - password:
            - this is the password of the wi-fi network you are trying to connect to

## Cam_Setup folder

- Code to program the camera has been provided to you.
- Follow the instructions on the readme located within the Cam_Setup folder to set up your esp-32.\

## CAD folder

- Showcases all of the CAD files used to build the gadget.

## Circuits Schematics folder

- Contains diagram of what the gadget's circuit is wired like.
