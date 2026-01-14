import whisper
import os



def main(path, model):
    # checking the path if exists or not
    if not os.path.exists(path):
        print("The path doesn't exist. Exiting...")
        exit()
    
    print(f"\n\n ----| current working directory : {path} |---- \n\n")
    # checking if the path is a directory 
    if os.path.isdir(path):
        # getting the folder subelements
        for x in os.listdir(path):
            full_path = os.path.join(path, x)

            # if sub folder is a directory 
            if os.path.isdir(full_path):  
                main(full_path, model)     # going to check recursively 

            #  if the x is a media file Transcribing it to same folder
            elif full_path.lower().endswith((".mp3", ".wav", ".mp4", ".mkv", ".mov", ".flv", ".aac", ".m4a", ".amr")):  
                print(f"\nTranscribing: {full_path}")
                result = model.transcribe(full_path) 
                txt_path = os.path.join(path, f"{os.path.splitext(x)[0]}.txt")

                # making txt file with same media file name  
                with open(txt_path, "w") as file:
                    file.write(result["text"]) 
                
                # printing the where Transcribing file save  
                print(f"\nSaved transcript: {txt_path}")



if __name__ == "__main__":
    model = whisper.load_model("base")
    path = input("Enter the path (default: 'D:\\OneDrive\\Desktop\\internshala'): ") or r"D:\OneDrive\Desktop\internshala"

    try:
        main(path, model)
    except Exception as e:
        print(f"There was an error: {e}")



