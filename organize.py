import os
from pathlib import Path
import click


DIRECTORIES = {
	"Videos" : ['.mp4', '.mov', '.wmv', '.avi', '.flv'],
	"Audio"  : ['.mp3', '.oog', '.wav', '.wma'],
	"Pictures" : ['.jpg', '.gif', '.tif', '.png'],
	"Documents" : ['.txt', '.pdf', '.doc', '.bat', '.odt', '.docx', '.tex'],
	"Zipped" : ['.rar', '.zip', '.7z', '.gz'],
	"Code" : ['.py', '.java', '.cpp', '.c', '.mat'],
	}


def pickDirectory(item_type):
	for category, suffixes in DIRECTORIES.items():
		for suffix in suffixes:
			if suffix == item_type:
				return category
	return 'Unknown'


@click.command()
@click.option('-path', required=True, help='path of directory to clean')
def organize_dir(path):
	for item in os.scandir(path): 
		if not item.is_dir():
			item_path = Path(item)
			item_type = item_path.suffix.lower()
			directory_type = pickDirectory(item_type)
			directory = Path(path).joinpath(pickDirectory(item_type))
			if not os.path.exists(directory):
				directory.mkdir()
			new_file_path = f"{directory}/{item.name}"
			os.replace(item_path, new_file_path)
			
