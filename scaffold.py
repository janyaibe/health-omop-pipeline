import os

# Define subfolder structure (no top-level folder this time)
folders = [
    "app",
    "app/templates",
    "data",
    "db",
    "etl",
    ".vscode"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create common empty files
files = {
    "run.py": "",
    "etl/mock_data_generator.py": "",
    "etl/transform_to_omop.py": "",
    "app/routes.py": "",
    ".gitignore": "__pycache__/\n*.pyc\n.env\n*.db\n",
    "requirements.txt": "flask\npandas\nsqlalchemy\nfaker\n",
    "README.md": "# Health OMOP Pipeline\n\nAn MVP to simulate a clinical data pipeline using Python, SQL, and the OMOP CDM.\n"
}

for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

print("✅ Folder structure and stub files created.")
