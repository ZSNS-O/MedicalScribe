from pathlib import Path

from app.utils.audio_utils import normalize_audio

base_dir = Path(__file__).resolve().parents[3]

input_file = base_dir / "audios" / "Recording.m4a"
output_file = base_dir / "audios" / "normalized" / "test_output.wav"



if not input_file.exists():
    raise FileNotFoundError(f"Input file not found: {input_file}")


result= normalize_audio(input_path=input_file,output_path=output_file)

print("Return Code:",result.returncode)

if result.returncode == 0:
    print("Normalization successful ✅")

else:
    print("Error ❌ ")
    print(result.stderr)