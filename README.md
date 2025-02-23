# Transcript Combiner

<div align="center">

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/yourusername/transcript-combiner/issues)

</div>

## 📝 Descripción

Transcript Combiner es una herramienta potente y flexible diseñada para mejorar la calidad de las transcripciones mediante la combinación inteligente de múltiples fuentes. Actualmente soporta:

- Transcripciones de YouTube
- Transcripciones del Pixel 6 (grabadora de Google)

## ✨ Características

- Combinación inteligente de transcripciones
- Soporte para múltiples formatos de entrada
- Procesamiento de texto avanzado con spaCy
- Fácil integración con otros sistemas
- Salida en múltiples formatos

## 🚀 Inicio Rápido

### Prerrequisitos

- Python 3.8 o superior
- pip
- Acceso a Internet (para la instalación inicial)

### Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/transcript-combiner.git
cd transcript-combiner
```

2. Crea y activa un entorno virtual:
```bash
python -m venv env
# En Unix o MacOS:
source env/bin/activate
# En Windows:
env\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Instala el modelo de spaCy:
```bash
python -m spacy download es_core_news_sm
```

## 📖 Uso

1. Coloca tus archivos de entrada en los directorios correspondientes:
```
data/
├── input/
│   ├── youtube_subtitles/
│   └── pixel_6_translation/
```

2. Ejecuta el script principal:
```bash
python -m src.main
```

3. Encuentra los resultados en el directorio de salida:
```
data/output/
```

## 🏗️ Estructura del Proyecto

```
transcript-combiner/
├── data/
│   ├── input/
│   │   ├── youtube_subtitles/
│   │   └── pixel_6_translation/
│   └── output/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── process_files.py
│   ├── config.py
│   └── utils/
│       ├── __init__.py
│       ├── text_utils.py
│       └── spacy_utils.py
├── tests/
│   ├── __init__.py
│   └── test_basic.py
├── docs/
├── requirements.txt
├── setup.py
└── README.md
```

## 🧪 Tests

Para ejecutar la suite completa de tests:

```bash
pytest tests/
```

Para tests específicos:

```bash
pytest tests/test_basic.py
```

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Sigue estos pasos:

1. Fork el proyecto
2. Crea tu rama de feature (`git checkout -b feature/AmazingFeature`)
3. Realiza tus cambios y haz commit (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

Por favor, asegúrate de actualizar los tests según corresponda y sigue las guías de contribución del proyecto.

## 📄 Licencia

Este proyecto está distribuido bajo la Licencia MIT. Ver el archivo `LICENSE` para más información.

## ✍️ Autores

* **Tu Nombre** - *Trabajo Inicial* - [@tu-usuario](https://github.com/tu-usuario)

Ver también la lista de [contribuidores](https://github.com/tu-usuario/transcript-combiner/contributors) que han participado en este proyecto.

## 🙏 Agradecimientos

* Agradecimiento especial a todos los contribuidores
* Inspirado en la necesidad de mejorar la calidad de las transcripciones automáticas
* Basado en las mejores prácticas de procesamiento de lenguaje natural

## 📞 Soporte

Si encuentras un bug o tienes una sugerencia, por favor abre un issue:
https://github.com/tu-usuario/transcript-combiner/issues