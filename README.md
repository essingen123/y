# YouTube Video Downloader and Converter to MP3

A Python script to download YouTube videos and convert them to MP3 format.

## Disclaimer

* This script is for educational purposes only.
* It is intended to be used only if you have the rights to use it according to YouTube's terms of service and applicable laws.
* If you own the material, you may still be subject to license agreements and other restrictions that prohibit downloading or converting your own content.
* Use of this script may be subject to YouTube's policies on scraping, downloading, and converting content.
* In no event shall the authors or maintainers of this script be liable for any damages or consequences arising from its use, including but not limited to:
    + Copyright infringement
    + License agreement breaches
    + Intergalactic copyright disputes in the year 3050
    + Any other unforeseen consequences

By using this script, you acknowledge that you have read and understood these terms and will use the script responsibly and in accordance with applicable laws and regulations.


## Requirements

* Python 3.x
* pytube library (`pip install pytube`)
* ffmpeg (for audio conversion)

## Usage

1. Run the script in a Docker container for best results.
2. Provide the YouTube video URL as a command-line argument or input it when prompted.
3. The script will download the video and convert it to MP3 format.

## Notes

* This script may not work consistently due to changes in YouTube's URL patterns.
* A function to fix these patterns is included, but it may require manual updates.
* **Caution:** The script attempts to modify `cipher.py` to fix patterns. This may have unintended consequences. Use at your own risk.
* **Warning:** Running this script may interact with uncontrolled third-party tools. Use a sandboxed container for this script.
* **Important:** Due to frequent changes in the YouTube frontend, some JavaScript code may not match with this version of pytube. This may cause issues with video downloads.
* **Work in Progress:** This script is a work in progress and may not work as expected. Future updates may include an automatic hook for fixing `cipher.py` using a Large Language Model (LLM) like LLaMA 405B or Groq (Llama-3.1-70b-versatile) to dynamically update the cipher in real-time.

