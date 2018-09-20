# /usr/local/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf

import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, msg):
    print("Respuesta del topico: "+str(msg.payload.decode("UTF-8")))
    # Funcion recursiva que muestra la respuesta dada por el servidor de MQTT de OM2M despues de que se envia cada
    # payload


# enter username and password
authenticate = """ "username:password" """

topic = "/oneM2M/req/Temp_cocina/in-cse/json"
payload_lista = []
payload1 = """{"m2m:rqp": {"m2m:fr": "Temp_cocina","m2m:to": "/in-cse","m2m:op": 2,"m2m:rqi": 123456}}"""
# Payload de prubea

payload2 = """{"m2m:rqp": {
"m2m:fr" : """+authenticate+""",
"m2m:to" : "/in-cse/in-name",
"m2m:op" : 1,
"m2m:rqi": 123456,
"m2m:pc": {
"m2m:ae": {
     "api": "app-sensor",
     "rr": "false",
     "lbl": ["Type/sensor", "Category/temperature", "Location/home"],
     "rn": "Temp_cocina"}},
"m2m:ty": 2}}"""
# payload para crear la aplicacion con el nombre temp_cocina

payload3="""{"m2m:rqp": {
"m2m:fr" : """+authenticate+""",
"m2m:to" : "/in-cse/in-name/Temp_cocina",
"m2m:op" : 1,
"m2m:rqi": 123456,
"m2m:pc": {"m2m:cnt": {"rn": "DESCRIPTOR"}},
"m2m:ty": 3}}"""
# payload para crear el contenedor descriptor en la aplicacion.

payload4="""{"m2m:rqp": {
"m2m:fr" : """+authenticate+""",
"m2m:to" : "/in-cse/in-name/Temp_cocina",
"m2m:op" : 1,
"m2m:rqi": 123456,
"m2m:pc": {"m2m:cnt": {"rn": "Healthcheck"}},
"m2m:ty": 3}}"""
# payload para crear el contenedor Healthcheck en la aplicacion.

payload5="""{"m2m:rqp": {
"m2m:fr" : """+authenticate+""",
"m2m:to" : "/in-cse/in-name/Temp_cocina",
"m2m:op" : 1,
"m2m:rqi": 123456,
"m2m:pc": {"m2m:cnt": {"rn": "DATA"}},
"m2m:ty": 3}}"""
# payload para crear el contenedor DATA en la aplicacion.

payload6="""{"m2m:rqp": {
"m2m:fr" : """+authenticate+""",
"m2m:to" : "/in-cse/in-name/Temp_cocina/DATA",
"m2m:op" : 1,
"m2m:rqi": 123454,
"m2m:pc": {
   "m2m:cin": {"cnf":"message",
   "con":"55 C"
   }
},
"m2m:ty": 4}}"""
# este payload crea un dato en el contenedor DATA


payload7="""{"m2m:rqp": {
"m2m:fr" : """+authenticate+""",
"m2m:to" : "/in-cse/in-name/Temp_cocina/Healthcheck",
"m2m:op" : 1,
"m2m:rqi": 123454,
"m2m:pc": {
   "m2m:cin": {"cnf":"message",
   "con":"1s"
   }
},
"m2m:ty": 4}}"""
# este payload crea un dato en el contenedor Healthcheck

payload_lista.append(payload1)
payload_lista.append(payload2)
payload_lista.append(payload3)
payload_lista.append(payload4)
payload_lista.append(payload5)
payload_lista.append(payload6)
payload_lista.append(payload7)
# Despues de creada la aplicacion, si solo desean enviar datos, agregar comentarios al append de payload 1 al 5.

# while True:
for payload in payload_lista:
    client = mqtt.Client("OM2M_MQTT")
    client.on_message = on_message
    client.connect("13.58.183.185", 1883)

    client.loop_start()
    client.subscribe("/oneM2M/resp/in-cse/Temp_cocina/json")
    print("prueba del MQTT: "+payload)
    print()
    client.publish(topic, payload)
    time.sleep(1)
    client.on_message = on_message
    client.loop_stop()