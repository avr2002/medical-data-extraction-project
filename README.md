# medical-data-extraction-project

This is a basic python project using **OpenCV**, **FastAPI**, and **Regex** that extracts required data from medical documents like patient details and prescription details. This project uses **FastAPI** server in the backend which uses **very basic computer vision** and extracts medical information from pdfs using **pytesseract**. As of now I've not developed any fronted but it was successfully tested using **Postman**.



- Python backend was built using pytesseract, OpenCV, Regular expressions and FastAPI as a web serving framework 

- Auto extracted important fields from patient details and medical prescriptions. Image processing was performed in OpenCV and then pytesseract was used for image to text conversion. The last step was to use Regular Expression (Regex) for extracting important fields from the text



All the project related code and files are in the backend folder

Run `main.py`
