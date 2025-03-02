Media File Transcriber
This Python script uses OpenAI's Whisper model to transcribe audio and video files into text. It processes all media files in a given directory (including subdirectories) and saves the transcriptions as text files in the same folder.

Features
Automatically detects and transcribes media files (.mp3, .wav, .mp4, .mkv, .mov, .flv, .aac, .m4a, .amr).
Recursively processes all subdirectories.
Saves transcriptions as .txt files with the same name as the media file.
Uses OpenAI's Whisper model for accurate transcription.
Requirements
1. Install Dependencies
Before running the script, ensure you have Python installed and then install the required dependencies using:

bash
Copy
Edit
pip install openai-whisper ffmpeg
Note: The ffmpeg package is required for Whisper to process certain file formats. You can install it using:

Windows: Download from FFmpeg official website and add it to your system PATH.
Linux/macOS: Install using:
bash
Copy
Edit
sudo apt install ffmpeg  # Ubuntu/Debian  
brew install ffmpeg       # macOS  
Usage
Clone this repository or download the script:

bash
Copy
Edit
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Run the script:

bash
Copy
Edit
python transcriber.py
Enter the path to the directory containing your media files when prompted. (Press Enter to use the default path.)

Example Output
mathematica
Copy
Edit
Enter the path (default: 'D:\OneDrive\Desktop\internshala'):  
 
----| current working directory : D:\OneDrive\Desktop\internshala |----  

Transcribing: D:\OneDrive\Desktop\internshala\audio.mp3  
Saved transcript: D:\OneDrive\Desktop\internshala\audio.txt  

Transcribing: D:\OneDrive\Desktop\internshala\video.mp4  
Saved transcript: D:\OneDrive\Desktop\internshala\video.txt  
Customization
You can change the Whisper model in the script by modifying this line:

python
Copy
Edit
model = whisper.load_model("base")  
Available models: "tiny", "base", "small", "medium", "large".

Change the default path by modifying:

python
Copy
Edit
path = input("Enter the path (default: 'D:\\OneDrive\\Desktop\\internshala'): ") or r"D:\OneDrive\Desktop\internshala"
Contributing
Feel free to open issues or submit pull requests to improve the script.
