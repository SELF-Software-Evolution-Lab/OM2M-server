# OM2M-server
This repository contains code to simulate an IoT device connected to an OM2M  server. Also how to get the last data sent from a device.

The python file mqtt_om2m.py, simulates an IoT device that registers and send data to OM2M via MQTT protocol. Feel free to modify this code to change the application name or to configure the program just to send data, not to create the application. The Paho-mqtt library is required to execute this code.

The python file read_la.py, uses the API REST of OM2M to read the last data sent by the IoT device through a get request. This code requires the Request and JSON libraries.

On both files you must configure username and password.

The server IP is http://13.58.183.185/webpage/ and you can see the server content in your browser.

Aditional information can be found in https://wiki.eclipse.org/OM2M/one#Getting_started and https://wiki.eclipse.org/OM2M/one/REST_API.

## Libraries requirements.

requests==2.19.1

paho-mqtt==1.3.1
