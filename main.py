HF_TOKEN = "" # TODO: add your token
from pydub import AudioSegment
import os
from pyannote.audio import Pipeline
from pyannote.audio.pipelines.utils.hook import ProgressHook

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    use_auth_token=HF_TOKEN)

# apply pretrained pipeline (with optional progress hook)
with ProgressHook() as hook:
    diarization = pipeline("example.wav", hook=hook)

# Create a dictionary to map speaker IDs to folders
speaker_folders = {}
speaker_count = 0

# print the result
for turn, track, speaker in diarization.itertracks(yield_label=True):
    if speaker not in speaker_folders:
        folder_name = f"{speaker_count:02d}_speaker"
        speaker_folders[speaker] = folder_name
        os.makedirs(folder_name, exist_ok=True)
        speaker_count += 1

# Load the audio file
audio = AudioSegment.from_wav("example.wav")

current_speaker = None
current_segment = None
current_start_ms = None
current_end_ms = None

for turn, track, speaker in diarization.itertracks(yield_label=True):
    # Extract the segment
    start_ms = int(turn.start * 1000)  # Convert to milliseconds
    end_ms = int(turn.end * 1000)
    segment = audio[start_ms:end_ms]
    print(f"Segment from {start_ms} to {end_ms} : speaker {speaker}")
    
    # If this is a new speaker or first segment
    if speaker != current_speaker:
        # Save previous segment if it exists
        if current_segment is not None:
            folder = speaker_folders[current_speaker]
            output_path = f"{folder}/segment_{current_start_ms}_{current_end_ms}.wav"
            current_segment.export(output_path, format="wav")
        
        # Start new segment
        current_speaker = speaker
        current_segment = segment
        current_start_ms = start_ms
        current_end_ms = end_ms
    else:
        # Append to current segment
        current_segment = current_segment + segment
        current_end_ms = end_ms

# Save the final segment
if current_segment is not None:
    folder = speaker_folders[current_speaker]
    output_path = f"{folder}/segment_{current_start_ms}_{current_end_ms}.wav"
    current_segment.export(output_path, format="wav")