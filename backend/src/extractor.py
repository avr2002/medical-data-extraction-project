from pdf2image import convert_from_path
import pytesseract
import util

from prescription_parser import PrescriptionParser
from patient_details_parser import PatientDetailsParser


pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
POPPLER_PATH = r"C:\Users\Amit Vikram Raj\poppler-22.12.0\Library\bin"


def extract(file_path, file_format):
    # step 1: extracting text from pdf file

    # convert pdf file to image
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''
    for page in pages:
        processed_img = util.pre_process_img(page)
        text = pytesseract.image_to_string(processed_img, lang='eng')
        document_text += '\n' + text

    # step 2: extract fields from text

    if file_format == 'prescription':
        # extract data from prescription
        extracted_data = PrescriptionParser(document_text).parse()
    elif file_format == 'patient_details':
        # extract data from patienet_details
        extracted_data = PatientDetailsParser(document_text).parse()
    else:
        raise Exception(f"Invalid Document Format: {file_format}")

    return extracted_data


if __name__ == '__main__':
    # data = extract('../resources/prescription/pre_2.pdf', 'prescription')
    data = extract('../resources/patient_details/pd_2.pdf', 'patient_details')
    print(data)

