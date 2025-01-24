import os
from typing import Union

from solidipes.loaders.file import File, load_file
from solidipes.validators.validator import add_validation_error, validator


class SymLink(File):
    """Symbolic link (special file)"""

    def __init__(self, **kwargs):
        from ..viewers.symlink import SymLink as SymLinkViewer

        super().__init__(**kwargs)
        self.compatible_viewers[:0] = [SymLinkViewer]  # TODO: to binary or file info

    # TODO: as sequence, if path does not exist, treat as separate file with some infos
    @File.loadable
    def linked_file(self) -> Union[str, File]:
        from pathlib import Path

        _path = str(Path(self.file_info.path).resolve())
        if os.path.exists(_path):
            return load_file(_path)

        return _path

    @validator(description="Linked file is valid")
    def _is_linked_file_valid(self) -> bool:
        if isinstance(self.linked_file, File):
            return self.linked_file.is_valid

        add_validation_error(f"Linked file '{self.linked_file}' does not exist")
        return False
