import yt_dlp
import os
import os
os.environ['FFMPEG_BINARY'] = '/opt/homebrew/bin/ffmpeg'

def download_video(url, quality):
    try:
        ydl_opts = {
            'format': f'bestvideo[height<={quality}]+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': True,
            'merge_output_format': 'mp4',
            'geo_bypass': True,
            'ffmpeg_location': '/opt/homebrew/bin/ffmpeg',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from {url}...")
            ydl.download([url])
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def download_audio(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': True,
            'geo_bypass': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading audio from {url}...")
            ydl.download([url])
        print("Audio downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

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

if __name__ == "__main__":
    main()