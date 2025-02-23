from pathlib import Path

# Rutas base
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output" / "processed_transcripts"
LOGS_DIR = BASE_DIR / "logs"

# Configuración de logging
LOG_FILE = LOGS_DIR / "application.log"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s" 