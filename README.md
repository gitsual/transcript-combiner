# Transcript Combiner

<div align="center">

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/yourusername/transcript-combiner/issues)

</div>

## 📝 Description

Transcript Combiner is a powerful and flexible tool designed to enhance transcription quality by intelligently combining multiple sources. Currently supports:

- Transcriptions from two input sources
- Processing and combining related texts

## ✨ Features

- Intelligent transcription combining
- Support for multiple input formats
- Advanced text processing with spaCy
- Seamless integration with other systems
- Multiple output formats

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/transcript-combiner.git
cd transcript-combiner
```

2. Create and activate a virtual environment:
```bash
python -m venv env
# On Unix or MacOS:
source env/bin/activate
# On Windows:
env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install the spaCy model:
```bash
python -m spacy download es_core_news_sm
```

## 📖 Usage

1. Run tests to verify functionality:
```bash
pytest tests/
```

2. Place your input files in the corresponding directory:
```
data/
└── input/
    └── source_1/
    └── source_2/
```

3. Run the main script:
```bash
python src/main.py
```

## 🏗️ Project Structure

```
transcript-combiner/
├── data/
│   └── input/
│       └── source_1/
│       └── source_2/
├── tests/
│   ├── __init__.py
│   ├── test_basic.py
│   ├── test_transcription.py
│   ├── input/
│   └── output/
└── requirements.txt
```

## 🧪 Tests

To run the complete test suite:

```bash
pytest tests/
```

For specific tests:

```bash
pytest tests/test_basic.py
```

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure you update tests as appropriate and follow the project's contribution guidelines.

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.

## ✍️ Authors

* **Gitsual** - *Initial Work* - [@gitsual](https://github.com/gitsual)

See also the list of [contributors](https://github.com/gitsual/transcript-combiner/contributors) who have participated in this project.

## 🙏 Acknowledgments

* Special thanks to all contributors
* Inspired by the need to improve automatic transcription quality
* Based on natural language processing best practices

## 📞 Support

If you find a bug or have a suggestion, please open an issue:
https://github.com/gitsual/transcript-combiner/issues