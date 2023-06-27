# ZZA_EDR

La herramienta ZZA EDR (Endpoint Detection and Response) tiene como objetivo monitorear un directorio específico en busca de eventos relacionados con archivos, como creación, eliminación, modificación y acceso. Proporciona una capa adicional de seguridad al permitirte detectar y responder rápidamente a posibles amenazas en tus endpoints.

El funcionamiento de la herramienta es el siguiente:

Se inicia ejecutando el script zza_edr.py en un entorno de Python.

Se te solicitará responder una serie de preguntas para personalizar la configuración de monitoreo de la herramienta. Estas preguntas determinarán qué eventos específicos deseas monitorear.

Una vez que se haya completado la configuración, ZZA EDR comenzará a monitorear el directorio especificado.

A medida que se produzcan eventos en el directorio (por ejemplo, creación, eliminación, modificación o acceso a archivos), la herramienta mostrará información sobre dichos eventos en la consola.

Además de la visualización de eventos, la herramienta también ejecutará acciones de respuesta según la configuración y la lógica que hayas implementado. Por ejemplo, puedes enviar notificaciones, generar registros detallados, bloquear archivos sospechosos o iniciar análisis adicionales.

En resumen, ZZA EDR monitorea un directorio en busca de eventos relacionados con archivos y proporciona información detallada sobre esos eventos. También puede ejecutar acciones de respuesta personalizadas según tus necesidades.

Para ejecutar la herramienta, sigue estos pasos:

Asegúrate de tener Python instalado en tu sistema.

Descarga el archivo zza_edr.py y guárdalo en una ubicación de tu elección.

Abre una terminal o línea de comandos y navega hasta la ubicación donde guardaste el archivo zza_edr.py.

Asegúrate de tener instalada la biblioteca pyinotify. Si no la tienes instalada, puedes ejecutar el siguiente comando en la terminal:

pip install pyinotify

Una vez que tengas la biblioteca instalada, ejecuta el siguiente comando para iniciar la herramienta:

python zza_edr.py

Responde las preguntas interactivas para personalizar la configuración de monitoreo.

La herramienta comenzará a monitorear el directorio especificado y mostrará información sobre los eventos detectados en la consola.

Recuerda reemplazar "/path/to/directory" en el código con la ruta real del directorio que deseas monitorear.


