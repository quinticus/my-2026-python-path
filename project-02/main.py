import typer
from rich.progress import track
import logic
import interface

src_path_str = interface.get_path()
dest_path_str = interface.get_path()

SOURCE_DIR = logic.validate_directory(src_path_str)
DESTINATION_DIR = logic.validate_directory(dest_path_str)

selected_src_files = interface.file_picker(SOURCE_DIR)
selected_dest_files = interface.file_picker(DESTINATION_DIR)