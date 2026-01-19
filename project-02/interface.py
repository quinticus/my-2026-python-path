'''
Interface.py handles the fancy look of the app
'''
import os
from pathlib import Path
import questionary
from rich.console import Console
import logic

console = Console()

def get_path() -> str:
  while True:
    console.clear()
    entered_directory = questionary.path("Enter path: ").ask()

    confirmed = questionary.confirm(f"Is \"{entered_directory}\" correct?").ask()
    if confirmed:
      console.clear()
      return entered_directory

def file_picker(directory: Path) -> list[Path]:
  files = logic.get_items_from_directory(directory)
  if len(files) == 0:
    # If there's nothing here, then we'll add a safeguard.
    # I'm too lazy to add that as of now.
    return
  
  file_dictionary: dict[str, Path] = {}

  for file in files:
    file_dictionary[file.name] = file
  
  file_choices = list(file_dictionary.keys())
  
  while True:
    selected_files = questionary.checkbox(
      "Select files: ",
      choices=file_choices
    ).ask()
    
    confirmed = questionary.confirm(f"Will you select these files? ({selected_files})").ask()
    console.clear()
    if confirmed:
      break

  if not selected_files:
    return []

  return [file_dictionary[name] for name in selected_files]

def mode_select() -> str:
  # `transfer_file` in logic.py handles the logic, just ask the user
  modes = ["Move", "Copy"]
  selected_mode = questionary.select(
    "Would you like to move or copy files?",
    choices=modes
  )
  return selected_mode.ask().lower()