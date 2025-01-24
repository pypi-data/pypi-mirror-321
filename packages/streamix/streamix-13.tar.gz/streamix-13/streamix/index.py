import yt_dlp
import os
import shutil

# Function to check if ffmpeg is installed
def is_ffmpeg_installed():
    return shutil.which("ffmpeg") is not None

# Function to get the Desktop path
def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), "Desktop")

# Function to download video
def download_video(url, quality):
    try:
        # Path to the Desktop
        download_path = get_desktop_path()
        if not os.path.exists(download_path):
            raise Exception(f"Desktop path not found: {download_path}")

        ydl_opts = {
            'format': f'bestvideo[height<={quality}]+bestaudio/best',
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Save to Desktop
            'quiet': True,
            'merge_output_format': 'mp4',
            'geo_bypass': True,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            },
        }

        if is_ffmpeg_installed():
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }]
        else:
            print("Warning: FFmpeg is not installed. Video and audio may not be merged.")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from {url}...")
            ydl.download([url])
        print(f"Video downloaded successfully to {download_path}!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to download audio
def download_audio(url):
    try:
        # Path to the Desktop
        download_path = get_desktop_path()
        if not os.path.exists(download_path):
            raise Exception(f"Desktop path not found: {download_path}")

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Save to Desktop
            'quiet': True,
            'geo_bypass': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }] if is_ffmpeg_installed() else None
        }

        if not is_ffmpeg_installed():
            print("Warning: FFmpeg is not installed. Audio may not be converted to MP3 format.")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading audio from {url}...")
            ydl.download([url])
        print(f"Audio downloaded successfully to {download_path}!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    print("Welcome to Streamix!")
    print("1. Download Video")
    print("2. Download Audio")

    choice = input("Choose an option (1/2): ").strip()

    if choice == '1':
        print("Video Quality Options:")
        print("1. 240p\n2. 360p\n3. 480p\n4. 720p\n5. 1080p")
        quality_map = {'1': '240', '2': '360', '3': '480', '4': '720', '5': '1080'}
        quality = quality_map.get(input("Select quality (1-5): ").strip(), '720')
        url = input("Enter the YouTube URL: ").strip()
        download_video(url, quality)

    elif choice == '2':
        url = input("Enter the YouTube URL: ").strip()
        download_audio(url)
    else:
        print("Invalid option. Exiting.")

# Entry point
if __name__ == "__main__":
    main()