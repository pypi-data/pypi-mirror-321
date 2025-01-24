# OuteAI Early Access API - TTS Client

A Python client for interacting with the OuteAI Text-to-Speech (TTS) API during early access. 

## Features

- **Customizable Parameters**: Adjust generation settings, including temperature, repeat penalty, and speaker selection.
- **Convenient Audio Handling**: Save audio outputs as `.wav` files with a simple interface.

## Installation
```bash
pip install outeai
```

## Usage

### Initializing the TTS Client

To use the TTS client, you need an API token from OuteAI. Replace `"your_api_token"` with your actual token.

```python
from outeai.api.v1 import TTSClient

# Initialize the client
client = TTSClient(token="your_api_token")
```

### Generating Speech

Provide the required parameters (text, model ID, speaker, etc.) to generate speech.

```python
audio_output = client.generate(
    text="Speech synthesis is the artificial production of human speech.",
    model_id="outetts-0.3-500m",
    speaker="en_male_1"
)

# Save the audio to a file
audio_output.save("output_audio.wav")
```

### Parameters

- **`text`**: The text to be converted into speech. (Required)
- **`model_id`**: The ID of the TTS model to use. (Required)
- **`temperature`**: Controls the randomness of the output. Value between `0.1` and `1.0`. (Default: `0.1`)
- **`repeat_penalty`**: Penalizes repeated sequences. Value between `1.0` and `2.0`. (Default: `1.1`)
- **`speaker`**: The speaker voice ID. (Default: `en_male_1`)
- **`show_notice`**: Whether to show API usage notices. (Default: `True`)

### Error Handling

The client raises clear exceptions for invalid inputs or API issues:

- **`ValueError`**: For invalid parameter values or API errors.
- **`requests.RequestException`**: For network-related issues.

### Example

```python
try:
    audio_output = client.generate(
        text="Speech synthesis is the artificial production of human speech.",
        model_id="outetts-0.3-500m",
        speaker="en_female_1",
        temperature=0.4,
        repeat_penalty=1.1
    )
    audio_output.save("speech.wav")
except Exception as e:
    print(f"An error occurred: {e}")
```