# Workshop: Píxel a cuantificación

Bienvenido al taller de Análisis de Bioimágenes: Píxel a cuantificación. En este taller de 2 horas aprenderás a realizar segmentación y cuantificación de imágenes 3D utilizando Napari y herramientas de análisis de imágenes basadas en Python.

## Descripción del taller

El taller se divide en dos secciones, cada una con una parte teórica:

### Sección 1: Fundamentos de Segmentación (2 horas)
- **Clase teórica**: Principios de segmentación de imágenes, métodos de umbralización y operaciones morfológicas
- **Práctica: Segmentación con Napari** (90 minutos): Segmentación interactiva usando Napari con el asistente de segmentación
  - Ver [Guía de Segmentación en Napari](./segmentation_napari.md) para instrucciones detalladas

### Sección 2: Métodos Avanzados de Segmentación (extra pára poder seguir desde casa)
- **Clase teórica**: Segmentación basada en aprendizaje profundo y descripción general de CellPose
- **Práctica: Segmentación con CellPose**: Aplicación práctica de CellPose para segmentación celular automatizada
  - Ver [Guía de Segmentación con CellPose](./segmentation_cellpose.md) para instrucciones detalladas

## Material de las clases

Descargá las diapositivas de la presentación y recursos adicionales desde **[Zenodo](https://zenodo.org/records/18717816)**.

## Configuración del entorno

### Requisitos previos

Instalá [Pixi](https://pixi.sh/) — un gestor de paquetes para entornos Python entre otros.

### Instalación y descargar datos

1. Cloná o descargá este repositorio
2. Abrí una terminal en el directorio del repositorio (shift + click derecho > Abrir terminal aquí)
3. Instalá el entorno:
   ```bash
   pixi install --all
   pixi run descargar-datos
   ```

*Nota:* Si no pudiste descargar los datos, abajo se encuentra el link.

## Datos de ejemplo

Descargá las imágenes de ejemplo desde Zenodo:
- **Imagen 3D**: `Lund.tif` - Pila 3D completa para este taller

https://zenodo.org/records/17986091

## Ejecutar el taller

### Iniciar Napari con el plugin Asistente

```bash
pixi run assistant
```

Esto abre Napari con el panel del asistente de segmentación que te guía a través del flujo de trabajo.

## Consejos y trucos

- **Alternar 2D/3D**: Hacé clic en el botón de la esquina inferior izquierda para cambiar entre corte 2D y renderizado 3D
- **Vistas ortogonales**: Hacé clic en el botón de orden de ejes para ver los planos XY, XZ e YZ simultáneamente
- **Ajuste de parámetros**: Los parámetros como el radio de erosión deben ajustarse según tu imagen
  - Radio mayor = erosión más agresiva (mejor separación, pero puede perder objetos pequeños)
  - Radio menor = erosión conservadora (conserva más detalles, pero puede no separar adecuadamente)
- **Memoria**: Trabajar con pilas 3D grandes puede ser intensivo en memoria. Considerá submuestrear o trabajar con subconjuntos si es necesario

## Solución de problemas

### Napari no abre
- Asegurate de que todas las dependencias estén correctamente instaladas: `pixi install`
- Probá limpiar la caché de pixi: `pixi clean cache`

### Segmentación deficiente
- Probá diferentes métodos de preprocesamiento:
  - Usá diferentes métodos de umbralización (Otsu, Li, Isodata)
  - Ajustá los parámetros de erosión/dilatación
  - Aumentá/disminuí el radio del Sombrero de Copa Blanco (White Top Hat)
  - Aplicá suavizado gaussiano antes de la umbralización (disponible en el asistente)

### Problemas de memoria con pilas grandes
- Abrí solo la región de interés (ROI)
- Submuestreá las dimensiones espaciales
- Procesá cortes individualmente y combinalos

## Para seguir aprendiendo

- [Documentación de Napari](https://napari.org)
- [Filtros de scikit-image](https://scikit-image.org/docs/stable/api/skimage.filters.html)
- [napari-assistant](https://github.com/napari-assistant/napari-assistant)
- [Taller completo de Microscopía de Lámina de Luz](https://bruvellu.github.io/light-sheet-image-analysis-workshop-2026/)

## Referencias

- Cuenca, M., et al. - Taller práctico de segmentación
- Datos de: https://zenodo.org/records/17986091

## Licencia

Este trabajo está licenciado bajo [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

