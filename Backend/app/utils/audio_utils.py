
# Audio-Datei
# → FFmpeg starten
# → Konvertieren zu 16kHz Mono WAV
# → Fehler prüfen



from pathlib import Path
# Damit kannst du ein externes Programm starten.
import subprocess


def normalize_audio(input_path: Path, output_path: Path):

    #Erstelle den Zielordner, falls er nicht existiert.
    output_path.parent.mkdir(parents=True, exist_ok=True)


    #Der FFmpeg-Befehl in der commandline :  ffmpeg -y -i input.webm -ac 1 -ar 16000 -vn -c:a pcm_s16le output.wav

    command = [
        "ffmpeg",
        "-y",
        "-i", str(input_path),
        "-ac", "1",
        "-ar", "16000",
        "-vn",
        "-c:a", "pcm_s16le",
        str(output_path)
    ]

    #FFmpeg ausführen
    try:
        return  subprocess.run(command, capture_output=True, text=True)
    except FileNotFoundError:
        raise RuntimeError("FFmpeg not found. Please install and add it to PATH.")

