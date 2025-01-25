import argparse
import PyPDF2
import os, sys
from pathlib import Path
from gtts import gTTS


class MergePDFCommand:
    def execute(self, arguments):
        src = arguments.src
        self.method_name(src)
        pdf_merger = PyPDF2.PdfMerger()
        files = os.listdir(src)
        sorted_files = sorted(files)
        for file in sorted_files:
            with open(os.path.join(src, file), "rb") as f:
                pdf_reader = PyPDF2.PdfReader(f)
                pdf_merger.append(pdf_reader)
        with open(arguments.dest, "wb") as f:
            pdf_merger.write(f)

    def method_name(self, src):
        dir_path = Path(src)
        if not dir_path.exists():
            raise FileNotFoundError(f"Error: File not found at {src}")


class CreateAudioCommand:
    def execute(self, arguments):
        tts = gTTS(arguments.text, lang='en', tld='us')
        tts.save(arguments.dest)


class CommandFactory:

    @staticmethod
    def create_command(name):
        if name == "merge-pdf":
            return MergePDFCommand()
        if name == "create-audio":
            return CreateAudioCommand()
        return None


def create_parser(args):
    parser = argparse.ArgumentParser(prog='Shining Brain')
    subparsers = parser.add_subparsers(dest='command')
    pdf = subparsers.add_parser("merge-pdf", help="Merge PDFs from the given directory to the given destination.")
    pdf.add_argument("src", type=str, help="directory")
    pdf.add_argument("dest", type=str, help="file path")

    audio = subparsers.add_parser("create-audio", help="Create an audio from the given text.")
    audio.add_argument("text", type=str, help="string")
    audio.add_argument("dest", type=str, help="file path")


    return parser.parse_args(args)


if __name__ == "__main__":
    args = create_parser(sys.argv[1:] if len(sys.argv[1:]) != 0 else ["-h"])
    command = CommandFactory.create_command(args.command)
    command.execute(args)
