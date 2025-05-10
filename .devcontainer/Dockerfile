# Basis-Image mit Python 3.11
FROM python:3.11-slim

# Setzt Umgebungsvariablen
ENV POETRY_VERSION=1.8.2 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    STREAMLIT_DISABLE_WELCOME_MESSAGE=true

# Installiert systemweite Abhängigkeiten (inkl. ps und netstat für Debugging)
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    git \
    procps \
    net-tools && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Setzt das Arbeitsverzeichnis
WORKDIR /app

# Kopiert nur die relevanten Dateien
COPY pyproject.toml poetry.lock* ./

# Installiert Python-Abhängigkeiten (nur Cache-Schicht)
RUN poetry config virtualenvs.create false && \
    poetry install --no-root

# Kopiert Quellcode und Konfiguration gezielt
COPY src/ ./src/

# Stellt sicher, dass Upload-/DB-Verzeichnisse existieren
RUN mkdir -p /app/uploads /app/data

# Legt die Streamlit credentials.toml an, um E-Mail-Abfrage zu unterdrücken
RUN mkdir -p /root/.streamlit && \
    echo "[general]\nemail = \"\"" > /root/.streamlit/credentials.toml
