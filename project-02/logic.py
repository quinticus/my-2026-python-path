'''
Logic.py handles the files and folders
'''
import shutil
from pathlib import Path

def validate_directory(path_string: str) -> Path | None:
  directory: Path = Path(path_string)

  if directory.exists() and directory.is_dir():
    return directory
  
  return None

def get_items_from_directory(directory: Path) -> list[path]:
  files: list[Path] = []

  for item in directory.iterdir():
    if item.is_file():
      files.append(item)
  
  return files

def transfer_file(files: list[Path], destination: Path, mode: str):
  mode = mode.lower()
  for file in files:
    target_destination = destination / file.name

    file_already_exists = target_destination.exists()
    if file_already_exists:
      # Has the potential to overwrite original file!
      # To avoid this, let's skip it for now.
      continue

    if mode == 'move':
      shutil.move(file, target_destination)
    elif mode == 'copy':
      shutil.copy2(file, target_destination)