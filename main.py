import whisper
import os

def check(path, model):
    if not os.path.exists(path):
        print("The path doesn't exist. Exiting...")
        exit()
    
    if os.path.isdir(path):
        for x in os.listdir(path):
            full_path = os.path.join(path, x)

            if os.path.isdir(full_path):  
                check(full_path, model)

            elif full_path.lower().endswith(("mp4", "mp3", "m4a", "amr")):  
                print(f"Transcribing: {full_path}")
                result = model.transcribe(full_path) 
                txt_path = os.path.join(path, f"{os.path.splitext(x)[0]}.txt")
                with open(txt_path, "w") as file:
                    file.write(result["text"]) 
                
                print(f"Saved transcript: {txt_path}")

if __name__ == "__main__":
    model = whisper.load_model("base")
    path = input("Enter the path (default: 'D:\\OneDrive\\Desktop\\internshala'): ") or r"D:\OneDrive\Desktop\internshala"

    try:
        check(path, model)
    except Exception as e:
        print(f"There was an error: {e}")
