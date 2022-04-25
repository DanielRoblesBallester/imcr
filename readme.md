# Como usar

Para usar el programa tendremos que crear un servidor desde python y tener nuestro ordenador y el teléfono conectados a una misma red.

## Conect.py

1. Iniciamos el programa y ponemos la IP que tenga nuestro ordenador en la red local. 

## SensorStreamer

1. Descargar aplicación [SensorStreamer](https://play.google.com/store/apps/details?id=cz.honzamrazek.sensorstreamer) .
2. Dentro de la aplicación en el menú izquierdo, en manage connections, creamos una nueva conexión de tipo tcp client. Dentro de hostName ponemos la ip de nuestro ordenador en la red local y en el puerto ponemos el 8080.
3. Abrimos el menú de la izquierda y entramos en el apartado de packets. Dentro de este creamos un nuevo paquete de tipo JSON que transmita los datos del acelerómetro.
4. volvemos al menú principal y cuando el servidor de python esté en marcha le damos a start.
