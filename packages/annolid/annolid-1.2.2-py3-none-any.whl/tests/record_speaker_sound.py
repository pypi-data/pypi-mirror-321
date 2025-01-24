import sounddevice as sd
import numpy as np
import wave

def callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
    recorded_frames.append(indata.copy())

# Set the sample rate and duration
sample_rate = 44100  # You can adjust this based on your needs
duration = 10  # Recording duration in seconds

# Initialize a list to store the recorded frames
recorded_frames = []

# Get default input device info
input_device_info = sd.query_devices(sd.default.device, 'input')
channels = input_device_info['max_input_channels']

# Open an input stream with the default input device settings
with sd.InputStream(callback=callback, channels=channels, samplerate=sample_rate):
    print(f"Recording for {duration} seconds...")
    sd.sleep(duration * 1000)  # Adjust sleep duration for buffer overrun

print("Recording complete.")

# Convert the list of frames to a numpy array
recording = np.concatenate(recorded_frames, axis=0)

# Save the recorded audio to a WAV file
output_filename = "output.wav"
with wave.open(output_filename, 'wb') as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(2)  # 16-bit audio
    wf.setframerate(sample_rate)
    wf.writeframes(recording.tobytes())

print(f"Audio saved to {output_filename}")
