from pathlib import Path
from app.services.whisper_service import WhisperService

base_dir = Path(__file__).resolve().parents[3]

normalized_audio = base_dir / "audios" / "normalized" / "test_output.wav"

if not normalized_audio.exists():
    raise FileNotFoundError(f"File not found: {normalized_audio}")

whisper = WhisperService()

result = whisper.transcribe(normalized_audio, language="de")

print("Transcription:\n")
print(result)
