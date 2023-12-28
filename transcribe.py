from deepgram import Deepgram
import asyncio, json
import os
from pathlib import Path
import nltk
from nltk.tokenize import sent_tokenize

DEEPGRAM_API_KEY = os.environ["DEEPGRAM_API_KEY"]
FILE = "./audio.opus"
MIMETYPE = "audio/opus"


async def main():
    deepgram = Deepgram(DEEPGRAM_API_KEY)

    with open(FILE, "rb") as audio:
        source = {"buffer": audio, "mimetype": MIMETYPE}

        response = await asyncio.create_task(
            deepgram.transcription.prerecorded(
                source,
                {
                    "smart_format": True,
                    "model": "nova-2",
                },
            )
        )

    with open("transcript.json", "w") as f:
        print(json.dumps(response, indent=4), file=f)

def postprocess():
    nltk.download('punkt')

    with open("transcript.json") as f:
        res = json.load(f)

    text = res['results']['channels'][0]['alternatives'][0]['transcript']
    sentences = sent_tokenize(text)

    with open("transcript.txt", "w") as f:
        for s in sentences:
            print(s, file=f)


if __name__ == "__main__":
    transcript = Path('transcript.json')
    if not transcript.exists():
        asyncio.run(main())

    postprocess()
