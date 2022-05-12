# Proyecto LED

Colección de scripts tipo "Hello World" para Raspberry Pi Zero W.
En el directorio raiz, un par de scripts básicos tipo _blink_. y tambien un script PIR con un buzzer como alarma.

Dentro del directorio cam, varios programas para controlar una camara con filtro de corte IR motorizado.

Debido a las limitaciones de la RPiZero, el modo ideal para su uso es mediante un setup headless, de modo que es necesario acceder a un webserver mediante un navegador para ver el vídeo. El script _web2.py_ permite justo esto, además pulsando enter mientras se ejecuta se puede alternar el filtro IR de la cámara. Simulando en un ordenador una webcam con obs e importando como fuente de video la ip de la raspberry, esta se puede usar de webcam con capacidad de imagen nocturna.

Por último, el script _getir.py_ procesa un par de imágenes tomadas por _irnoirbalanced.py_ para generar una imagen con el índice NDVI. No esta probado completamente, debido a las dificultades de mantener la cámara estática y a la ausencia de un filtro azul para la cámara.

