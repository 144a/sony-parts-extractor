# sony-parts-extractor
A script for extracting part numbers and specs from Sony Service Manuals using OCR

The script requires the PyPDF2 Library to function properly.

Usage:
python3 extract_components.py File_Path_Here

At the moment, this script will create an output.txt file with the listed capacitors sorted by board.

In the future, this will be expanded to other parts as well, once the Regex is written for them.
