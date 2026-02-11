from faster_whisper import WhisperModel
from pathlib import Path
from typing import Optional


class WhisperService:
    def __init__(self):
        # small ist guter Kompromiss zwischen Speed & Qualität
        print("Loading Whisper model...")
        self.model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8"
        )
        print("Model loaded.")

    def transcribe(self, wav_path: Path, language: Optional[str] = "de") -> str:
        segments, info = self.model.transcribe(
            str(wav_path),
            language=language,
            vad_filter=True,
            beam_size=5,
            condition_on_previous_text=False
        )

        text_parts = []
        for segment in segments:
            text_parts.append(segment.text.strip())

        return " ".join(text_parts)
