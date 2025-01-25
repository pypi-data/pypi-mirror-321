# llamarker/file_to_pdf_converter.py
import logging
import subprocess
import tempfile
from pathlib import Path
from typing import List, Tuple
from pypdf import PdfReader
import matplotlib.pyplot as plt
import shutil


class FileToPDFConverter:
    """
    Converts supported files (txt, docx, pdf, rtf, odt, xls, xlsx, csv, ods, ppt, pptx, odp) to PDFs using LibreOffice.
    Files are stored temporarily unless explicitly saved to a user-defined folder.
    """

    def __init__(self, input_dir: str = None, file_path: str = None, temp_dir: str = None, save_dir: str = None, logger: logging.Logger = None):
        """
        Args:
            input_dir (str): Path to the input directory with files.
            file_path (str): Path to a single file to process.
            save_dir (str): Optional path to save the converted PDFs permanently.
            logger (logging.Logger): Logger instance for logging progress.
        """
        if not (input_dir or file_path):
            raise ValueError("Either 'input_dir' or 'file_path' must be provided.")

        self.input_dir = Path(input_dir) if input_dir else None
        self.file_path = Path(file_path) if file_path else None
        self.logger = logger or logging.getLogger(__name__)
        self.temp_dir = Path(temp_dir) if temp_dir else Path(tempfile.mkdtemp())
        self.save_dir = Path(save_dir) if save_dir else None

        # Temporary folder to store converted PDFs
        self.logger.info(f"Temporary directory created at: {self.temp_dir}")

        # Validate input
        if self.file_path and not self.file_path.exists():
            raise FileNotFoundError(f"Input file not found: {self.file_path}")

        # Validate input directory only if it is provided
        if self.input_dir and not self.input_dir.exists():
            raise FileNotFoundError(f"Input directory not found: {self.input_dir}")

        self.results: List[Tuple[str, int]] = []

        # Creates pdf directory and cleans if needed
        self.clean_save_dir()

        # Validate LibreOffice installation
        self.libreoffice_path = self._validate_libreoffice()

    def get_temp_dir(self) -> str:
        """Returns the path to the temporary directory."""
        return str(self.temp_dir)

    def _validate_libreoffice(self) -> str:
        """Check if LibreOffice is installed and return the path."""
        libreoffice_path = shutil.which("libreoffice") or shutil.which("soffice")
        if not libreoffice_path:
            raise EnvironmentError(
                "LibreOffice is not installed. Please install it from https://www.libreoffice.org/download/"
            )
        self.logger.info(f"LibreOffice found at: {libreoffice_path}")
        return libreoffice_path
    
    def _process_file(self, file: Path):
        if file.suffix in [".txt", ".docx", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".rtf", ".odt", ".ods", ".odp"]:
            self._convert_to_pdf(file)

    def convert_and_count_pages(self) -> None:
        """
        Converts supported files (txt, docx, pdf, rtf, odt, xls, xlsx, csv, ods, ppt, pptx, odp) to PDF, counts pages, and handles file cleanup.
        """

        if self.file_path:
            self._process_file(self.file_path)
        elif self.input_dir:
            self.logger.info(f"Starting file conversion in: {self.input_dir}")
            for file in self.input_dir.rglob("*"):
                self._process_file(file)

        self.logger.info(f"Processing completed: {len(self.results)} files converted.")

    def _convert_to_pdf(self, input_file: Path) -> None:
        """Converts a file to PDF using LibreOffice."""
        output_file = self.temp_dir / input_file.with_suffix(".pdf").name
        command = [
            self.libreoffice_path,
            "--headless",
            "--convert-to", "pdf",
            "--outdir", str(output_file.parent),
            str(input_file)
        ]
        try:
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            pages = self._count_pdf_pages(output_file)
            self.results.append((str(output_file), pages))
            self.logger.info(f"Converted: {input_file} -> {output_file} ({pages} pages)")

            # Save to user-specified directory if provided
            if self.save_dir:
                self._save_to_user_directory(output_file)
        except Exception as e:
            self.logger.error(f"Failed to convert {input_file}: {e}")

    def _count_pdf_pages(self, pdf_file: Path) -> int:
        """Counts pages in a PDF file."""
        reader = PdfReader(pdf_file)
        return len(reader.pages)

    def _save_to_user_directory(self, temp_file: Path):
        """Saves the converted PDF to the user-specified directory."""
        dest_file = self.save_dir / temp_file.name
        shutil.copy2(temp_file, dest_file)
        self.logger.info(f"Saved PDF to: {dest_file}")

    def clean_save_dir(self):
        if self.save_dir.exists():
            self.logger.info(f"Cleaning existing PDFFiles directory: {self.save_dir}")
            for item in self.save_dir.iterdir():
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()
        else:
            self.save_dir.mkdir(exist_ok=True)

    def cleanup(self):
        """Cleans up the temporary directory."""
        try:
            shutil.rmtree(self.temp_dir)
            self.logger.info("Temporary directory cleaned up.")
        except Exception as e:
            self.logger.error(f"Failed to clean up temporary files: {e}")

    def get_results(self) -> List[Tuple[str, int]]:
        """Returns the list of converted PDFs and their page counts."""
        return self.results
    
    def plot_page_counts(self) -> None:
        """Plots a bar chart showing the number of pages across all processed files."""
        if not self.results:
            self.logger.warning("No files to plot. Please run `convert_and_count_pages` first.")
            return

        file_names, page_counts = zip(*[(Path(f).name, p) for f, p in self.results])

        plt.figure(figsize=(10, 6))
        plt.bar(file_names, page_counts, color="skyblue")
        plt.xlabel("Files", fontsize=12)
        plt.ylabel("Number of Pages", fontsize=12)
        plt.title("Page Count Across Files", fontsize=14)
        plt.xticks(rotation=45, ha="right", fontsize=10)
        plt.tight_layout()
        # plt.show()


if __name__ == "__main__":
     # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    logger = logging.getLogger("LlaMarker")

    convertor = FileToPDFConverter(file_path="/home/revdha/PycharmProjects/rag_app/database/PB-7.1.0-1_Beschaffung.docx", logger=logger)
    convertor.convert_and_count_pages()