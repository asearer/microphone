import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

audio = pyaudio.PyAudio()

# Get the default microphone input device
default_device_index = audio.get_default_input_device_info()["index"]

stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=default_device_index,
                    frames_per_buffer=CHUNK)

print("Recording started...")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording finished.")

stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a WAV file
wave_file = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wave_file.setnchannels(CHANNELS)
wave_file.setsampwidth(audio.get_sample_size(FORMAT))
wave_file.setframerate(RATE)
wave_file.writeframes(b''.join(frames))
wave_file.close()

print(f"Audio saved to {WAVE_OUTPUT_FILENAME}")
