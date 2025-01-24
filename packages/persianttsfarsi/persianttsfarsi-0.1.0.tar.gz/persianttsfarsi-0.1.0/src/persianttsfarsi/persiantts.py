import websockets
import asyncio
import json
import time
import uuid
import librosa
import soundfile as sf
import noisereduce as nr

class PersianTTS:

    def __init__(self, voice="fa-IR-FaridNeural"):
        self.url = "wss://speech.platform.bing.com/consumer/speech/synthesize/readaloud/edge/v1?TrustedClientToken=6A5AA1D4EAFF4E9FB37E23D68491D6F4"
        self.default_voice = voice
        self.output_format = "audio-24khz-48kbitrate-mono-mp3"

    async def _synthesize(self, ssml_content, output_file):
        speech_config = {
            "context": {
                "synthesis": {
                    "audio": {
                        "metadataoptions": {
                            "sentenceBoundaryEnabled": "false",
                            "wordBoundaryEnabled": "false"
                        },
                        "outputFormat": self.output_format
                    }
                }
            }
        }
        speech_config_json = json.dumps(speech_config)

        headers = {
            "X-RequestId": "09c8b1578fbf256d23dcb20b6dd3eb6c",  # Generate a valid UUID
            "Content-Type": "application/json; charset=utf-8",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Origin": "chrome-extension://oajalfneblkfiejoadecnmodfpnaeblh",
        }

        try:
            async with websockets.connect(self.url, extra_headers=headers) as websocket:
                config_message = f"X-Timestamp: {time.time()}\r\nPath: speech.config\r\nContent-Type: application/json\r\n\r\n{speech_config_json}"
                await websocket.send(config_message)

                ssml_message = f"X-Timestamp: {time.time()}\r\nPath: ssml\r\nContent-Type: application/ssml+xml\r\n\r\n{ssml_content}"
                await websocket.send(ssml_message)
                audio_data = bytearray()
                while True:
                    response = await asyncio.wait_for(websocket.recv(), timeout=60)
                    if isinstance(response, bytes):
                        audio_data.extend(response)
                    elif isinstance(response, str) and 'Path:turn.end' in response:
                        break

                # Save the initial audio
                with open(output_file, "wb") as f:
                    f.write(audio_data)

                # Process the audio (denoising)
                y, sr = librosa.load(output_file, sr=None)
                denoised_audio = nr.reduce_noise(y=y, sr=sr)

                # Save the processed (denoised) audio
                processed_output_file = output_file.replace(".mp3", "_processed.wav")
                sf.write(processed_output_file, denoised_audio, sr)

                print(f"High-pass filtered and noise-reduced audio saved as {processed_output_file}")

        except Exception as e:
            raise RuntimeError(f"Error during synthesis: {e}")

    def synthesize(self, text, output_file="output.mp3", pitch="0%", rate="-20%", volume="70%", voice=None):
        selected_voice = voice if voice else self.default_voice
        ssml_content = f"""
        <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="fa-IR">
            <voice name="{selected_voice}">
                <prosody pitch="{pitch}" rate="{rate}" volume="{volume}">
                    {text}
                </prosody>
            </voice>
        </speak>
        """
        asyncio.run(self._synthesize(ssml_content, output_file))