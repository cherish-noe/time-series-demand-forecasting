import os
from dotenv import load_dotenv
import zipfile
import kaggle

# load environment variables from .env file
load_dotenv()

# kaggle configuration
kaggle_username = os.getenv('KAGGLE_USERNAME')
kaggle_key = os.getenv('KAGGLE_KEY')

kaggle.api.authenticate()

competition_name = "demand-forecasting-kernels-only"
file_name = "train.csv"
download_dir = "../data"

# create 'data' folder if it doesn't exist
os.makedirs(download_dir, exist_ok=True)

# download the dataset
kaggle.api.competition_download_file(
    competition=competition_name, 
    file_name=file_name, 
    path=download_dir, 
    force=True
)

# Unzip files
for file_name in os.listdir(download_dir):
    if file_name.endswith(".zip"):
        file_path = os.path.join(download_dir, file_name)
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(download_dir)

# Remove zip file after extracting
os.remove(file_path)




