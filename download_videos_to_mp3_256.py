

'''

2024 Aug
Working, nope:
https://www.youtube.com/watch?v=cXCBsJAJSMk
https://www.youtube.com/watch?v=y5jQJrp4jQY

Working, yep:
https://www.youtube.com/watch?v=0na9-kpFWmk


'''
import subprocess
import os
import re
import sys
print("Run in a Docker for best results. May not work consistently.") 
print("Use a sandboxed container for this script. May interact with uncontrolled third-party tools.")

# Function to ensure pytube is installed
def ensure_pytube_installed():
    try:
        global YouTube
        from pytube import YouTube
    except ImportError:
        print("pytube not found, installing it now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pytube"])
        from pytube import YouTube
        print("pytube installed successfully.")

# Function to download video and convert to MP3
def download_video_to_mp3(url, target_path='.'):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        downloaded_file = stream.download(output_path=target_path)

        # Convert to MP3
        base, ext = os.path.splitext(downloaded_file)
        new_file = base + '.mp3'
        subprocess.run(['ffmpeg', '-i', downloaded_file, '-b:a', '256k', new_file], check=True)

        # Remove original download
        os.remove(downloaded_file)
        print(f'Downloaded & converted to MP3: {new_file}')
    except Exception as e:
        print(f'Failed to download {url}: {e}')

def fix_patterns():
    print("cipher.py-fix:")

    pattern_to_fix_into = ['''
        r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)','''
    ]

    pattern_to_fix = ['''
        r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*',
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)','''
    ]
    print("YouTube URLs change frequently. Would you like to try a fix the file cipher.py if previous attempts failed.")
    print("In the future this would benefit from being fixed by a LLM for each new variation by youtube :)")
    response = input("Do you want to try to fix the patterns? (y/n): ")
    if response.lower() == 'y':
        files_to_edit = []
        cmd = "sudo find ~ -name cipher.py"
        output = subprocess.check_output(cmd, shell=True)
        files_to_edit = [line.decode('utf-8').strip() for line in output.splitlines()]

        for file in files_to_edit:
            print(f"Found file: {file}")
            with open(file, 'r') as f:
                lines = f.readlines()
            updated_lines = lines[:]  # Create a copy of the original lines

            for pattern in pattern_to_fix:
                for i, line in enumerate(lines):
                    if re.search(pattern, line):
                        updated_lines[i] = '#' + pattern + '\n' + pattern_to_fix_into[0]

            with open(file + '_BACKUP_BEFORE_EDIT_', 'w') as f:
                f.writelines(lines)
            with open(file, 'w') as f:
                f.writelines(updated_lines)
    else:
        print("Skipping pattern fix.")

def main():
    ensure_pytube_installed()  # Ensure pytube is installed
    fix_patterns()

    video_url = sys.argv[1] if len(sys.argv) > 1 else input("Enter the YouTube video URL (ENTER for a test that previously worked): ")
    if(video_url == ''): video_url = 'https://www.youtube.com/watch?v=0na9-kpFWmk'
    download_video_to_mp3(video_url)

if __name__ == "__main__":
    main()
