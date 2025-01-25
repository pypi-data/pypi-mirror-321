import os
from typing import Union, List


class InputFile:
    def __init__(
        self,
        file: Union[str, bytes, None] = None,
        file_id: str | None = None,
        is_image: bool = True,
        as_document: bool = False,
    ):
        """
        Represents a file to be sent to Mattermost.

        :param file: Path to the file, bytes of the file, or None.
        :param file_id: Existing file ID in Mattermost (if already uploaded).
        :param is_image: Whether the file is an image.
        :param as_document: Whether to send the image as a document.
        """
        if not file and not file_id:
            raise ValueError("Either 'file' or 'file_id' must be provided.")

        self.file = file
        self.file_id = file_id
        self.is_image = is_image
        self.as_document = as_document

        if isinstance(file, str) and not os.path.isfile(file):
            raise ValueError(
                f"The file path '{file}' does not exist or is not a file."
            )

    def is_uploaded(self) -> bool:
        """Check if the file is already uploaded (identified by file_id)."""
        return self.file_id is not None

    def is_file_path(self) -> bool:
        """Check if the file is a valid file path."""
        return isinstance(self.file, str) and os.path.isfile(self.file)


class InputFileGroup:
    def __init__(self, files: List[InputFile]):
        """
        Represents a group of InputFile objects to be sent as attachments.

        :param files: List of InputFile objects.
        """
        if not files:
            raise ValueError(
                "InputFileGroup must contain at least one InputFile."
            )

        self.files = files

    def get_uploaded_file_ids(self) -> List[str]:
        """Retrieve file IDs of already uploaded files."""
        return [file.file_id for file in self.files if file.is_uploaded()]

    def get_unuploaded_files(self) -> List[InputFile]:
        """Retrieve files that need to be uploaded."""
        return [file for file in self.files if not file.is_uploaded()]
