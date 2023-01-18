import re
from backend.src.generic_parser import MedicalDocParser


class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__int__(self, text=text)
        # super().__int__(text=text)

    def parse(self):
        """
        parse() returns the required info. of patient in JSON format
        from prescription text obtained by using pytesserect.
        """
        return {
            'patient_name': self.get_field('patient_name'),
            'patient_address': self.get_field('patient_address'),
            'medicines': self.get_field('medicines'),
            'dosage_direction': self.get_field('dosage_direction'),
            'refill_amount': self.get_field('refill_amount')
        }

    def get_field(self, field_name):
        """
        Uses regex to return the required patient details in prescription text.
        """
        pattern_dict = {
            'patient_name': {'pattern': "Name: (.*) Date:", 'flags': 0},
            'patient_address': {'pattern': "Address: (.*)\n", 'flags': 0},
            'medicines': {'pattern': "Address:[^\n]*(.*)Directions:", 'flags': re.DOTALL},
            'dosage_direction': {'pattern': "Directions:(.*)Refill:", 'flags': re.DOTALL},
            'refill_amount': {'pattern': "Refill:(.*)times", 'flags': 0}
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
            if len(matches) > 0:
                return matches[0].strip()


if __name__ == '__main__':
    document_text = """Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

K

Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times
"""
    pp = PrescriptionParser(document_text)
    print(pp.parse())
