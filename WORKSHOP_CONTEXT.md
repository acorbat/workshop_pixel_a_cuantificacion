# Contexto del Taller: Introducción al Análisis de Bioimágenes

## Descripción general

Este taller introduce los conceptos fundamentales del análisis de bioimágenes, con foco en la segmentación y cuantificación de imágenes 3D usando Napari y herramientas basadas en Python. Los participantes aprenderán técnicas prácticas de análisis de imágenes a través de la experiencia directa con datos reales de bioimágenes.

## Objetivos de aprendizaje

Al finalizar este taller, serás capaz de:

### Visualización de imágenes
- Cargar y visualizar pilas de imágenes 3D en Napari
- Navegar entre los modos de visualización 2D y 3D
- Crear proyecciones ortogonales para una mejor comprensión espacial
- Ajustar configuraciones de visualización (brillo, contraste, mapas de color)

### Preprocesamiento de imágenes
- Comprender la eliminación de fondo y su importancia
- Aplicar el filtro Sombrero de Copa Blanco (White Top Hat) para corregir iluminación no uniforme
- Identificar y eliminar ruido usando filtros de suavizado
- Evaluar el impacto del preprocesamiento en los resultados de segmentación

### Segmentación de imágenes
- Comprender los conceptos y métodos de umbralización
- Aplicar técnicas de umbralización global y local
- Crear máscaras binarias a partir de imágenes de intensidad
- Comparar diferentes algoritmos de umbralización (Yen, Otsu, Li, Isodata)

### Generación y refinamiento de etiquetas
- Generar etiquetas de componentes conexos a partir de máscaras binarias
- Comprender la conectividad y su impacto en el etiquetado
- Aplicar operaciones morfológicas (erosión, dilatación, rellenado de huecos)
- Refinar la segmentación mediante flujos de trabajo de refinamiento iterativo
- Manejar objetos superpuestos/tocantes mediante refinamiento morfológico

### Cuantificación
- Extraer medidas morfológicas de objetos segmentados
- Comprender las propiedades de región (área, perímetro, circularidad, ajuste de elipse)
- Medir características de intensidad a partir de los datos originales
- Exportar resultados para análisis posteriores

### Visualización y análisis
- Crear visualizaciones con mapas de color de las mediciones
- Interpretar distribuciones de mediciones
- Filtrar objetos según criterios morfológicos
- Preparar datos para análisis estadístico

## Estructura del taller

### Parte 1: Introducción (30 minutos)
- Descripción general del flujo de trabajo de análisis de bioimágenes
- Introducción a la interfaz de Napari
- Demostración del pipeline de segmentación

### Parte 2: Práctica (90 minutos)
- Cargar y visualizar imagen 3D de muestra
- Ejecutar pasos de preprocesamiento
- Realizar el flujo de trabajo de segmentación
- Refinar y medir resultados
- Explorar y visualizar mediciones

### Parte 3: Temas avanzados (30 minutos)
- Resolución de problemas comunes de segmentación
- Ajuste de parámetros para tus propias imágenes
- Introducción a la automatización y procesamiento por lotes
- Recursos para seguir aprendiendo

## Conceptos clave

### Pipeline de segmentación

```
Imagen cruda
    ↓
Preprocesamiento: Eliminar fondo y ruido
    ↓ 
Binarización: Convertir a primer plano/fondo
    ↓
Etiquetado: Asignar IDs únicos a los objetos
    ↓
Refinamiento: Mejorar la calidad de las etiquetas mediante morfología
    ↓
Cuantificación: Extraer medidas morfológicas y de intensidad
    ↓
Análisis: Análisis estadístico y visualización
```

### Filtrado por Sombrero de Copa Blanco (White Top Hat)

- Elimina la iluminación de fondo no uniforme (sombreado)
- Aísla objetos pequeños mientras suprime características de fondo más grandes
- El parámetro de radio debe ser mayor que la estructura de fondo más grande pero menor que los objetos de primer plano más pequeños

### Umbralización

- **Umbralización global**: Usa un único umbral para toda la imagen
  - Rápida pero falla con iluminación no uniforme
  - Mejor para imágenes de alto contraste

- **Umbralización local**: Calcula el umbral para el vecindario alrededor de cada píxel
  - Se adapta a variaciones locales de intensidad
  - Requiere mayor costo computacional
  - Mejor para imágenes con sombreado o iluminación no uniforme

### Etiquetado de componentes conexos

- Convierte la máscara binaria en una imagen de etiquetas enteras
- Cada región de primer plano conectada recibe una etiqueta única (1, 2, 3, ...)
- La conectividad puede ser de 4 o 8 vecinos (2D) o de 6/26 vecinos (3D)
- Base para el análisis basado en objetos

### Operaciones morfológicas

- **Erosión**: Elimina objetos pequeños y separa regiones tocantes
  - Encoge todos los píxeles de primer plano por radio
  - Efectiva para romper conexiones débiles

- **Dilatación**: Expande los objetos restantes hacia su tamaño original
  - Hace crecer las regiones de primer plano por radio
  - Restaura la forma aproximada original después de la erosión

- **Ciclo de erosión-dilatación (Apertura)**: Elimina ruido pequeño conservando estructuras más grandes

### Propiedades de región

Medidas típicas extraídas de objetos segmentados:

**Geométricas:**
- Área: Número de píxeles en el objeto
- Perímetro: Longitud del borde
- Circularidad: Qué tan redondo es el objeto (1.0 = círculo perfecto)
- Excentricidad: Alargamiento de la elipse de mejor ajuste
- Solidez: Qué tan "relleno" está el objeto

**Posicionales:**
- Centroide: Posición del centro de masa
- Caja delimitadora: Rectángulo más pequeño que contiene al objeto
- Orientación: Ángulo del eje principal

**Intensidad (de la imagen original):**
- Media, mediana, desviación estándar
- Intensidad mínima/máxima
- Intensidad integrada

## Herramientas y librerías

### Napari
- Visor de imágenes interactivo con visualización avanzada
- Arquitectura de plugins para extensiones
- **napari-assistant**: Herramienta de recomendación de flujo de trabajo que sugiere los siguientes pasos de procesamiento

### Librerías Python
- **scikit-image**: Algoritmos de procesamiento de imágenes (filtros, morfología, segmentación)
- **scipy**: Computación científica incluyendo operaciones morfológicas
- **pandas**: Manipulación de datos (para tablas de mediciones)
- **imageio/tifffile**: Lectura/escritura de archivos de imagen

## Ejemplo de flujo de trabajo práctico

Trabajando con `Lund.tif` (imagen confocal de lámina de luz de estructura biológica):

1. **Visualización**: Abrir en Napari, inspeccionar en 3D
2. **Preprocesamiento**: Aplicar White Top Hat (r=10) para eliminar fondo
3. **Umbralización**: Usar el método Yen para crear máscara binaria
4. **Etiquetado**: Etiquetado de componentes conexos en la imagen binaria
5. **Refinamiento**: Erosión (r=3) → Re-etiquetado → Dilatación (r=3) para separar objetos tocantes
6. **Medición**: Extraer características de área, volumen, forma e intensidad
7. **Análisis**: Filtrar por tamaño, visualizar distribución, exportar para análisis adicional

## Resultados de aprendizaje

### Conocimiento
- Comprensión de los principios de segmentación de imágenes
- Familiaridad con estrategias de preprocesamiento, umbralización y etiquetado
- Conocimiento de las operaciones morfológicas y sus efectos

### Habilidades
- Capacidad práctica para realizar segmentación en Napari
- Optimización de parámetros para diferentes tipos de imágenes
- Visualización de resultados y evaluación de calidad
- Exportación de datos para análisis posterior

### Competencia
- Capacidad para segmentar imágenes biológicas 3D sencillas
- Capacidad para resolver problemas comunes de segmentación
- Comprensión de cuándo/cómo aplicar preprocesamiento y refinamiento
- Base para aprender técnicas avanzadas (segmentación por aprendizaje automático, tracking, etc.)

## Próximos pasos después del taller

### Aplicaciones inmediatas
- Aplicar el flujo de trabajo a tus propios datos de imagen
- Ajustar parámetros para tus condiciones de adquisición específicas
- Experimentar con diferentes métodos de preprocesamiento y umbralización

### Para seguir aprendiendo
- Explorar segmentación avanzada (basada en aprendizaje automático)
- Aprender técnicas de cuantificación avanzadas
- Estudiar tracking de células/objetos en datos de series temporales
- Investigar clasificación de objetos segmentados

### Automatización
- Programar flujos de trabajo repetitivos usando Python
- Procesar múltiples imágenes por lotes
- Crear pipelines de análisis reproducibles

## Recursos

- **Tutoriales de Napari**: https://napari.org/stable/tutorials/
- **Galería de scikit-image**: https://scikit-image.org/docs/stable/auto_examples/
- **Curso de Análisis de Bioimágenes**: https://bruvellu.github.io/light-sheet-image-analysis-workshop-2026/
- **Guía de Segmentación de ImageJ/Fiji**: https://imagej.net/
- **Python para Bioimágenes**: Libros y tutoriales de la comunidad

## Contacto y soporte

Para preguntas durante el taller:
- Consultá el README.md para instrucciones paso a paso
- Revisá la sección de Solución de problemas para problemas comunes
- Consultá la documentación de Napari/scikit-image
- Explorá las referencias y recursos de aprendizaje proporcionados

---

**Versión del taller**: 0.1.0  
**Última actualización**: Febrero 2026
