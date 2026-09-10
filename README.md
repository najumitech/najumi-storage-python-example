# Najumi Storage Python Example

An enterprise-grade Python example application demonstrating secure file upload and storage operations using Najumi Storage SDK.

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone [https://github.com/najumitech/najumi-storage-python-example.git](https://github.com/najumitech/najumi-storage-python-example.git)
cd najumi-storage-python-example

2. Install Dependencies

​To install the Najumi Storage SDK and required packages, run:
pip install -r requirements.txt

3. Configure Environment Variables

​Create a .env file in the root directory and add your Najumi Storage credentials:
NAJUMI_BASE_URL=[https://storage-api.najumitech.com](https://storage-api.najumitech.com)
NAJUMI_BUCKET_ID=njs_bucket_xxxxx
NAJUMI_ACCESS_KEY=your_access_key
NAJUMI_SECRET_KEY=your_secret_key

4. Run the Application

​Make sure you have a sample file named sample.jpg in your directory, then run:python main.py
📦 Code Implementation (main.py)
​Here is how simple it is to initialize the client and upload a file using the Python SDK:

python main.py
📦 Code Implementation (main.py)
​Here is how simple it is to initialize the client and upload a file using the Python SDK:
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

🛡️ Security Best Practices
​Never hardcode your NAJUMI_SECRET_KEY directly into your source code. Always use environment variables or a secure secrets manager.
​📄 License
​This project is licensed under the MIT License - see the LICENSE file for details.
​<p align="center">
Built with precision by <a href="https://najumitech.com">Najumi Tech Ltd</a>.
</p>
