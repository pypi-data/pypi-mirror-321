import base64
import requests
from dataclasses import dataclass
from loguru import logger
from typing import Generator
import json
from tqdm import tqdm

API_URL = "https://outeai.com/api/v1/tts-stream" 

@dataclass
class AudioOutput:
    """Class for handling the audio output from the TTS API."""
    audio_bytes: bytes
    sample_rate: int = 44100
    
    def save(self, path: str) -> None:
        with open(path, "wb") as wav_file:
            if not path.endswith(".wav"):
                path += ".wav"
            wav_file.write(self.audio_bytes)
            logger.info(f"File saved in: {path}")


class TTSClient:
    """Client for interacting with the OuteTTS API."""
    
    def __init__(self, token: str):
        """Initialize the TTS client.
        
        Args:
            token: API token for authentication
        """
        self.token = token
        self.session = requests.Session()
    
    def generate(
        self,
        text: str,
        model_id: str,
        temperature: float = 0.1,
        repeat_penalty: float = 1.1,
        speaker: str = "en_male_1",
        show_notice: bool = True
    ) -> Generator[dict, None, None]:
        """Generate speech from text with streaming.
        
        Args:
            text: Text to convert to speech
            model_id: ID of the model to use
            temperature: Generation temperature (default: 0.1)
            repeat_penalty: Penalty for repetition (default: 1.1)
            speaker: Speaker ID (default: "en_male_1")
        
        Yields:
            A dictionary containing partial generation data from the API
            (e.g., generated tokens and final audio when request is finished)
        
        Raises:
            ValueError: If the API request fails
            requests.RequestException: If there's a network error
        """

        if not text:
            raise ValueError("The 'text' parameter is required and cannot be empty.")
        if not model_id:
            raise ValueError("The 'model_id' parameter is required and cannot be empty.")
        if not speaker:
            raise ValueError("The 'speaker' parameter is required and cannot be empty.")
        if not (0.1 <= temperature <= 1.0):
            raise ValueError("The 'temperature' parameter must be between 0.1 and 1.0.")
        if not (1.0 <= repeat_penalty <= 2.0):
            raise ValueError("The 'repeat_penalty' parameter must be between 1.0 and 2.0.")
        
        payload = {
            "token": self.token,
            "text": text,
            "model_id": model_id.lower().strip(),
            "temperature": temperature,
            "repeat_penalty": repeat_penalty,
            "speaker": speaker.lower().strip()
        }

        audio_bytes = None
        
        try:
            MAX_PER_TEXT = 250
            if len(text) > MAX_PER_TEXT:
                logger.warning(f"Text exceeds the maximum length of {len(text)}/{MAX_PER_TEXT} characters and will be truncated automatically by the API.")

            if show_notice:
                logger.warning("Early access: Certain limitations and usage caps are in place.\n"
                               "Dynamic resource allocation includes inactivity timeout, after which resources may require reinitialization (cold start) when accessed again.\n"
                               "To disable this notice, pass 'show_notice=False' in the 'generate' function.")

            with self.session.post(API_URL, json=payload, stream=True) as response:
                response.raise_for_status()
                gen = tqdm(response.iter_lines(decode_unicode=True))
                for line in gen:
                    if line.strip():
                        try:
                            chunk = line.strip()
                            data = json.loads(chunk)

                            if data.get("data", {}).get("request_finished", False):
                                audio_bytes = data.get("data", {}).get("audio_bytes", None)
                            else:
                                gen.set_postfix({"generated_tokens": data.get("data", {}).get("generated_tokens", 0)})

                        except ValueError as e:
                            logger.error(f"Failed to parse chunk: {e}")
                            continue
        except requests.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise

        if audio_bytes is not None:
            audio_bytes = base64.b64decode(audio_bytes)

        return AudioOutput(audio_bytes)
