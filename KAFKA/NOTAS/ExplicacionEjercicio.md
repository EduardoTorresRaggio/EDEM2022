# EJERCICIO CLASE KAFKA

1. Ejecución del docker compose
1.1 Mediante el docker compose, podremos ejecutar de manera local tanto kafka como zookeper (puertos)

2. Comprobacion todo correcto
- Para comprobar que zookeper está ok 
    ```
    docker-compose logs zookeper | Select-String binding
    ```
- Para comprobar que kafka está ok
    ```
    docker-compose logs kafka | Select-String started
    ```
3. Para crear un topic, con una replica y una particion
    ```
    docker-compose exec kafka kafka-topics --create --topic myTopic --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server host.docker.internal:9092
    ```
Poner dibujo de donde estamos actualmente
(asumo que es 1 producer, 2 brokers, con 1 particion, 1 consumidor)

4. Obtener informacion del topic que se ha creado
    ```
    docker-compose exec kafka kafka-topics --describe --topic myTopic --bootstrap-server host.docker.internal:9092
    ```
5. Entramos en el contenedor de kafka, y en la consola del productor y ejecutamos el mensaje
    ```
    docker-compose exec kafka kafka-console-producer --topic myTopic --broker-list localhost:9092
    ```

6. Entramos en el contenedor de kafa, y en la consola del consumidor y leemos el mensaje
    ```
    docker-compose exec kafka kafka-console-consumer --topic myTopic --from-beginning --bootstrap-server localhost:9092
    ```
