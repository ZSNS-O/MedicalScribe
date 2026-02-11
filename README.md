# 🩺 MedicalScribe – Backend

## 📌 Projektübersicht

MedicalScribe ist ein AI-gestützter Medical Scribe.

Das System:

1. Nimmt Audio auf
2. Normalisiert das Audio (16kHz Mono WAV)
3. Transkribiert es lokal mit Faster-Whisper
4. (später) verarbeitet es weiter zu strukturierten medizinischen Daten

**Stack:**

- Python 3.13+
- FastAPI
- FFmpeg
- Faster-Whisper
- uv als Package Manager

---

## 🏗️ Projektstruktur

```
MedicalScribe/
├── .venv/
├── audios/
│   ├── Recording.m4a
│   └── normalized/
│       └── test_output.wav
├── Backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── utils/
│   │   │   └── audio_utils.py
│   │   ├── services/
│   │   │   └── whisper_service.py
│   │   └── test/
│   │       ├── test_normalize.py
│   │       └── test_whisper_service.py
│   └── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## 🔊 Audio Normalisierung

Vor der Transkription wird das Audio standardisiert:

- Mono (`-ac 1`)
- 16 kHz (`-ar 16000`)
- PCM 16-bit WAV (`pcm_s16le`)
- Keine Videospur (`-vn`)

Dies erfolgt über **FFmpeg**.

**Warum?** Whisper erwartet 16 kHz Mono Audio. Browser-Aufnahmen sind oft `.m4a` oder `.webm`, daher ist die Konvertierung notwendig.

---

## 🧠 Whisper Transkription

**Verwendete Modelle:**

- `tiny` (~75 MB) – schnell, geringere Qualität
- `base` (~150 MB)
- `small` (~500 MB) – bessere Qualität

**Für Entwicklung empfohlen:**

```python
WhisperModel("tiny", device="cpu", compute_type="int8")
```

**Pipeline:**  
Audio → FFmpeg Normalisierung → Faster-Whisper → Text

---

## ⚙️ Installation

### 1. Python installieren

Python 3.10 oder höher. Von [python.org](https://www.python.org/downloads/) herunterladen und bei der Installation **„Add python.exe to PATH“** aktivieren.

### 2. uv installieren

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

Oder mit pip:

```powershell
pip install uv
```

Anschließend ein neues Terminal öffnen.

### 3. Virtual Environment und Dependencies

```powershell
cd MedicalScribe
uv venv
uv sync
```

### 4. FFmpeg installieren (Windows)

**Option A – winget:**

```powershell
winget install ffmpeg
```

**Option B – manuell:**

1. Download: [gyan.dev/ffmpeg/builds](https://www.gyan.dev/ffmpeg/builds/)
2. `ffmpeg-7.x.x-essentials_build.zip` entpacken nach `C:\ffmpeg`
3. `C:\ffmpeg\bin` zur PATH-Variable hinzufügen

**Test:**

```powershell
ffmpeg -version
```

---

## 🧪 Tests ausführen

**Wichtig:** Tests müssen aus dem `Backend`-Verzeichnis ausgeführt werden, damit das Modul `app` gefunden wird.

```powershell
cd Backend
```

### Audio Normalisierung testen

```powershell
uv run python -m app.test.test_normalize
```

### Whisper testen

```powershell
uv run python -m app.test.test_whisper_service
```

> **Hinweis:** Beim ersten Start wird das Whisper-Modell von Hugging Face heruntergeladen. Das kann einige Minuten dauern. Danach wird es lokal gecacht.

---

## 🚀 FastAPI starten

```powershell
cd Backend
uv run uvicorn app.main:app --reload
```

API erreichbar unter: http://127.0.0.1:8000

---

## 📋 Zusammenfassung – Häufige Probleme und Lösungen

| Problem | Ursache | Lösung |
|--------|---------|--------|
| `Attribute "app" not found in module "main"` | Uvicorn sucht `app` im falschen Modul | `uvicorn app.main:app` statt `main:app` verwenden |
| `ffmpeg` / `python` / `uv` nicht erkannt | Nicht im PATH oder Terminal nicht neu gestartet | Installation prüfen, neuen Pfad in PATH eintragen, Terminal neu öffnen |
| `ModuleNotFoundError: No module named 'app'` | Tests vom Projekt-Root ausgeführt | Aus `Backend`-Verzeichnis ausführen: `cd Backend` |
| `fast-whisper` nicht gefunden | Falscher Paketname | Paket heißt `faster-whisper` (mit „er“) |
| Whisper-Download dauert lange | Erstes Laden des Modells von Hugging Face | Warten – nach dem ersten Download wird lokal gecacht |
| `[tool.uv.scripts]` unknown field | uv unterstützt dieses Feld nicht | Stattdessen Befehle direkt mit `uv run` ausführen |
