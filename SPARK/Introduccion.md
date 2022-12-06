# SPARK
## Qué es
- Es un frameworl de desarrollo de procesos de Big Data
- Se encarga de la velocidad de procesamiento
- Hadoop se encarga de la CANTIDAD de datos, tiene un problema de la velocidad ya que lo hace en el disco duro y tarda más. En cambio Spark lo trabaja desde la RAM.

## Qué no es
- No es una base de datos

## Spark VS Hadoop
- Spark se enfoca en el precsamiento de datos desde RAM
- Posee un metodo de grafos

## Características de los RDD:

- Principal abstracción de datos: Es la unidad básica, existen desde su inicio hasta su versión 3.0.
- Distribución: Los RDD se dritribuyen y particionan a lo largo del clúster.
- Creación simple: Al no poseer estructura formalmente, adoptan las más intuitiva.
- Inmutabilidad: Posterior a su creación no se pueden modificar
- Ejecución perezosa: A menos que se realice una acción.

## Características de los DataFrame

- Formato: A diferencia de un RDD poseen columnas, lo cual les otorga tipos de datos.
- Optimización: Poseen una mejor implementación, lo cual los hace preferibles.
- Facilidad de creación: Se pueden crear desde una base de datos externa, archivo o RDD existente.
- ¿Cuándo usar un RDD?

## Cuando te interesa controlar el flujo de Spark.
- Si eres usuario Python, convertir a RDD un conjunto permite mejor control de datos.
- Estás conectándote a versiones antiguas de spark.

## ¿Cuándo usar DataFrames?

- Si poseemos semánticas de datos complicadas.
- Vamos a realizar tareas de alto nivel como filtros, mapeos, agregaciones, promedios o sumas.
- Si vamos a usar sentencias SQL.