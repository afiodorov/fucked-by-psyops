# fucked-by-psyops

Transcript of https://media.ccc.de/v/37c3-12326-you_ve_just_been_fucked_by_psyops

```.bash
wget https://berlin-ak.ftp.media.ccc.de/congress/2023/webm-hd/37c3-12326-eng-deu-YOUVE_JUST_BEEN_FUCKED_BY_PSYOPS_webm-hd.webm -O video.webm
ffmpeg -i video.webm -vn -c:a libopus -b:a 128k audio.opus
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python transcribe.py
```
