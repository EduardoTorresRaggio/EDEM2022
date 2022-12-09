https://www.youtube.com/watch?v=nAJ-qlL0hNs&ab_channel=KeepCoding-TechSchool


# KAFKA
## Introduccion
Es un sistema de mensajeria entre un/unos productor/es y un/os consumidor/es

## Tipos de sistemas
### Colas
Los mensajes del productor se reparten de manera orientativa, repartiendo la carga a la hora de consumir

### Suscriptor
Cada mensaje que envia el productor, es atentido por cada suscriptor

## Kafka broker
Una cola de mensaje es un topic

### Topic
Un topic puede tener particiones, que sirve para dividir un topic a lo largo de varios brokers y separar la infromacion
Cada menaje tiene un identificador unico que es el offset
Los ficheros son denominados logs

### Logs


## Escalar Kafka
- Si tenemos un kafka broker, por mucha particiones que le hagamos no aumentará su capacidad, por lo que es necesario incoporar otro para poder ser capaces de procesar los mensajes que le mande el producer

### Escalar horizontal
Replicas: sirve par conseguir una alta disponibilidad del servicio.
- Las replicas se consiguen mediante la duplicacion de las particiones en distintos brokers.

Ventajas:
- Con esto conseguimos que si una particion lider de un kafka browser no estuviera disponible, se le asigna el lider a su copia, de manera que el sistema pueda seguir funcionando.

Desventajas:
- Estamos duplicando datos por lo que ocupa el ancho de banda de los brokers
- Las replicas provocan la disminución de la tasa de producción de mensajes por segundos a un topic, si se activa el asentamiento por replica
> No puedo poner más réplicas que brokers

## Mensajes
Conformado por:
- Headers
- Timestamp
- Clave: suele ser usada para decidir a que participación se envía el mensaje
- Valor

## Creación de topics
```bash
kafka-topic.sh --zookeeper localhost:2181 --create --topic topictest --partitions 4 --replication-factor 2 -config x=y

```
- Numero de particiones
- Numero de replicas
- Opcional: configuraciones de topic

## Productores
- Son los que mandan mensajes a los distintos topics
- Siempre envia el mensaje a la particion lider y por tanto, estas particiones deben de estar distribuidos en el cluster, no en un broker para balancear la carga
- Normalmente se utiliza una clave para relacionarlo el topic con los consumidores
- Los mensajes se puede enviar por lotes: 
    - basado en tiempo: menor latencia
    - basado en numero: mayor interaccion

### Configuracion productor
> ESTOS TIENEN QUE ESTAR SÍ O SÍ
- bootstrap.servers: lista de brokers separados con comas indicando los puertos
- key.serializer: clase utilizada para serializar las claves de los mensajes (string, long, custom, json)
- value.deserializer: clase utilizada para deserializar el payload del mensaje.
- group.id: se utiliza para indicar que un consumidor pertenece a un grupo de consumidores

## Consumidores
- Son los que reciben el mensaje
- Utilizan un topic especial denominado __consumer_offsets para guardar donde se encuentran las particiones y guardar por donde van en los offsets
> nº de consumidores <= nº particiones

### Configuracion consumidor
> ESTOS TIENEN QUE ESTAR SÍ O SÍ
- bootstrap.server: lista de brokers separados con comas indicando los puertos
- key.deserializer : clase utilizada para deserializar las claves de los mensajes
- value.deserializer : clase utilizada para deserializar el payload del mensaje
- group.id. :se utliliza para indicar que un consumidr pertenece a un grupo de consumidores

# EJEMPLOS

Distribucion Kafka con:
- 1 Producer
- 1 broker
- 3 topics
- n paticiones
- n consumidores

![](https://www.cloudkarafka.com/img/blog/apache-kafka-partition.png)

![](https://miro.medium.com/max/1400/1*RQLzIEav1nSkSIbWH2KKwA.png)
