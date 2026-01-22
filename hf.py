from huggingface_hub import HfApi, login

# --- CONFIGURATION ---
# Paste your token between the quotes below
MY_TOKEN = "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" 
REPO_ID = "Sagnikroy/AutoCompleteMe-LongShort"
# Change this if your .pth files are in a different folder
SOURCE_FOLDER = "./" 

# 1. Log in programmatically
login(token=MY_TOKEN)

api = HfApi()

# 2. Create the repository (if it doesn't exist)
try:
    api.create_repo(repo_id=REPO_ID, repo_type="model", exist_ok=True)
    print(f"Success: Repository '{REPO_ID}' is ready.")
except Exception as e:
    print(f"Note: {e}")

# 3. Upload the specific .pth files
print("Uploading files... this may take a minute depending on file size.")

api.upload_folder(
    folder_path=SOURCE_FOLDER,
    repo_id=REPO_ID,
    repo_type="model",
    allow_patterns=["autocomplete_model.pth", "final_model_cpu.pth"],
    commit_message="Initial upload of autocomplete models"
)

print(f"Done! View your model here: https://huggingface.co/{REPO_ID}")