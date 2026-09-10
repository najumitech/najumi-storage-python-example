import os
from dotenv import load_dotenv
from najumi_storage import Storage

# Load environment variables
load_dotenv()

# Initialize Najumi Storage client
storage = Storage(
    bucket_id=os.getenv("NAJUMI_BUCKET_ID"),
    access_key=os.getenv("NAJUMI_ACCESS_KEY"),
    secret_key=os.getenv("NAJUMI_SECRET_KEY")
)

def upload_sample_file():
    try:
        file_path = "sample.jpg" 
        print(f"Uploading {file_path} to Najumi Storage...")
        
        result = storage.upload(file_path)
        print("Upload successful!")
        print("Response data:", result)
        
    except Exception as e:
        print(f"Error during upload: {e}")

if __name__ == "__main__":
    upload_sample_file()

