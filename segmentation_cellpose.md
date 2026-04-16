# Taller: Segmentación 3D con Aprendizaje Profundo - Guía paso a paso

Esta guía te llevará a través de los materiales del taller y los ejercicios prácticos.

### Segmentación 3D con Cellpose

**Descripción general**: Este cuaderno demuestra cómo usar Cellpose para la segmentación celular 3D con visualización en Napari.

**Pasos para abrir y ejecutar**:

1. Desde la terminal dentro de la carpeta del taller:
   ```bash
   pixi run cellpose
   ```
   
   Alternativamente, si usás VS Code con la extensión Jupyter:
   - Abrí VS Code en la carpeta del taller
   - Hacé clic en `notebooks/cellpose_napari_3d.ipynb` en el explorador de archivos
   - Seleccioná el kernel de Pixi cuando se te solicite

2. **Seguí las celdas del cuaderno en orden**:
   - Leé la introducción y comprendé el modelo Cellpose
   - Cargá el conjunto de datos `Lund.tif`
   - Ejecutá el modelo de segmentación en el volumen 3D
   - Visualizá los resultados en Napari
   - Explorá los distintos parámetros y sus efectos

3. **Salidas esperadas**:
   - Una máscara de segmentación que muestra las células identificadas
   - Visualización 3D interactiva en el visor de Napari
   - Métricas de rendimiento y tiempo de procesamiento

### Segmentación 3D con StarDist

**Descripción general**: Este cuaderno demuestra cómo usar StarDist para la segmentación 3D, un enfoque alternativo que usa polígonos estrella-convexos.

**Pasos para abrir y ejecutar**:

1. Desde la terminal con el entorno Pixi activado, iniciá Jupyter:
   ```bash
   pixi run stardist
   ```
   
   O abrilo directamente en VS Code mediante la extensión Jupyter.

2. **Seguí las celdas del cuaderno en orden**:
   - Comprendé la arquitectura del modelo StarDist
   - Cargá el conjunto de datos `lund1051_resampled.tif`
   - Ejecutá el modelo StarDist 3D
   - Comparará los resultados con Cellpose
   - Visualizá y analizá la salida de segmentación

3. **Salidas esperadas**:
   - Máscaras de segmentación de StarDist
   - Visualización 3D interactiva
   - Métricas de comparación entre modelos

## Próximos pasos: Probar PlantSeg en BioImage.io

Después de completar los cuadernos, explorá modelos de segmentación adicionales en **[BioImage.io](https://bioimage.io/)**:

1. Visitá [https://bioimage.io/](https://bioimage.io/)
2. Podés probar los modelos en la página web iniciando sesión y haciendo clic en "test run model".
3. Podés:
   - Leer la documentación del modelo y las referencias de los artículos
   - Ver segmentaciones de ejemplo y visualizaciones 3D
   - Descargar el modelo para usarlo en tus propios proyectos
   - Probar el modelo de forma interactiva si está disponible
   - Este [cuaderno](https://github.com/bioimage-io/core-bioimage-io-python/blob/main/example/model_usage.ipynb) puede ayudarte a descargar un modelo de BioImage y ejecutarlo por tu cuenta.

PlantSeg es un excelente ejemplo de cómo los modelos especializados de aprendizaje profundo pueden desarrollarse y compartirse para aplicaciones específicas de imágenes biológicas. Explorá cómo se compara con los modelos de uso general Cellpose y StarDist que usaste en este taller.

## Consejos para el éxito

- **Comenzá con Cellpose**: Suele ser más amigable para principiantes
- **Experimentá con los parámetros**: Probá diferentes umbrales y configuraciones para ver cómo afectan los resultados
- **Usá las funciones de Napari**: Zoom, rotación y alternar capas para entender la estructura 3D
- **Comparí los modelos**: Ejecutá ambos cuadernos con los mismos datos para ver cómo difieren los distintos enfoques
- **Revisá las salidas intermedias**: La mayoría de los cuadernos guardan resultados intermedios para inspección

## Objetivos clave de aprendizaje

Al finalizar estos cuadernos, deberías comprender:
- Cómo funcionan los modelos de aprendizaje profundo para segmentación celular
- Las diferencias entre los enfoques Cellpose y StarDist
- Cómo usar Napari para visualización 3D
- Cómo evaluar y comparar resultados de segmentación

## Solución de problemas

- Si Napari no se muestra correctamente, asegurate de que los controladores gráficos estén actualizados
- Si ocurren problemas de memoria, los cuadernos pueden modificarse para procesar cortes más pequeños
- Contactá al instructor del taller si encontrás algún problema

---

¡Feliz segmentación! 🔬
