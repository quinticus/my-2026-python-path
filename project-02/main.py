import typer
from rich.progress import track
import logic
import interface

source_dir_str = interface.get_path()
source_dir = logic.validate_directory(source_dir_str)

selected_files = interface.file_picker(source_dir)

dir_destination_str = interface.get_path()
dir_destination = logic.validate_directory(dir_destination_str)

mode = interface.mode_select()
logic.transfer_file(selected_files, dir_destination, mode)