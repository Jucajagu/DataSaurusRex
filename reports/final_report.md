# 1. Marco Teórico -SRC
## Uso, procesamiento y clasificación de imágenes
Una imagen en un plano bidimensional se puede definir como una función de dos variables, un ejemplo de esto podría ser $a(x,y)$ siendo $a$ el brillo de una imagen en la coordenada $(x,y)$, el caso de una imagen digital no es fundamentalmente diferente ya que esta se divide en $N$ filas y $M$ columnas, donde sus intersección es definida como un pixel (Young et al., 1995).  

Una de las variables que considera la función de una imagen es el color o longitud de onda ($\lambda$), esta es percibida por los seres humanos gracias los tres pigmentos de colores que se encuentran en la retina (Young et al., 1995). En imágenes digitales estas se representan de una manera similar en términos de las combinaciones de colores primarios -generalmente siendo rojo, verde y azul- donde cada canal representa la intensidad del respectivo color entre 0 y 255. En otras palabras, las imágenes en RGB están realmente compuestas por 3 canales.

## Antecedentes -SRC

# 2. Contexto y Objetivo del Proyecto -SRC
## Objetivo de clasificar imágenes relacionadas a elementos artísticos
## Justificación y uso para la clasificación automatizada de piezas artísticas, casos de uso

# 3. Colección de Datos -SRC
## Descripción de dónde salieron los datos y qué contienen

# 4. Análisis Exploratorio -SRC
## Highlights y procedimiento corto de EDA con hallazgos

# 5. Modelo de Clasificación -JC
## Explicación de Modelo Neuronal
## Visualización 3D
## Embedding de imágenes

# 6. Carga de Datos -DP
## Explicación de RDS Amazon y su uso
## Carga de embeddings de imágenes
## Conexión con sistema

# 7. Infraestructura y Despliegue -DP & JC
## Diagrama y explicación de procesamiento
## Explicación breve de cómo procede FastAPI (Backend)
## Explicación breve de Dash

# 8. Solución / Herramientas - DP
## Demo
## Pruebas Unitarias
## Explicación de uso

# 9. Discusión y Conclusiones - UN POCO TODOS
Los resultados encontrados en el análisis exploratorio nos permiten visualizar algunas de la diferencias que existen entre las distribuciones de intensidad por canal de colores para cada clase de imagen. Por ejemplo, se pudo visualizar las semejanzas en esta distribución entre las clases de dibujo y 
# 10. Limitaciones - UN POCO TODOS

# 11. Referencias
Young, I. T., Gerbrands, J. J., & Van Vliet, L. J. (1995). Fundamentals of Image Processing.