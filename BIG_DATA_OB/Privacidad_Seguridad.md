![](https://www.devacademy.es/wp-content/uploads/2018/05/hacking-3112539_960_720.png)

# PRIVACIDAD Y SEGURIDAD
> Nunca se alcanza el 100%

## Ciclo de Big Data
- Generación de datos
    - Evistar la falsificación
    - Restringir el acceso
- Almacenamiento
    - Tecnicas de cifrado
        IBE(Identity Based Encryption)
        ABE (Attribute Based Encryption)
        Storage path encryption 
- Procesamiento
    - PPDP: Privacy Preserving Data Publishing

## Problemas principales
- Brechas de informacion: robo de datos.
- Venta incorrecta
- Discriminacion de datos
- No existe anonimato
- El analisis de datos no es 100% fiable
- Las patentes o copyright pierden su valor

## Buenas prácticas
- Utilizar frameworks de programación testados y seguros. (Hadoop)
- Asegurar tus datos no relacionales. 
    - Son Vulnerables a la inyección NoSQL, para contrarrestarlo fuzzing methods (HTTP)
- Asegurar el almacenamiento de datos y los registros de transacciones.
    - Destruir la info cuando ya utilizada
    - SUNDR : 
- Filtrado y validación de endpoints.
- Ajustarse a las normas y monitorización a tiempo real.
    - MDM: solo pueden acceder x dispositivos.
- Cifrado homomórfico.
    - Utilizar los datos sin necesidad de desencriptarlo antes.
- Criptografía de big data.
    - SSE (Protocolo búsqueda simétrica), IBE, ABE
- Control de acceso granular.
    - Dar y restringir accesos a las personas
- Auditorías.
- Procedencia de los datos.

## Hybrid EX
- Es un modelo de ejecución de confidencialidad y privacidad dentro del ámbito de la computación en la nube.
- Se hacen pruebas con datos menos sensibles de manera pública, para que lo más sensible se haga de manera privada.
Categorias
- Map Hybrid
- Vertical Partitioning
- Horizontal Partitioning
- Hybrid 