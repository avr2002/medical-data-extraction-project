import re
from backend.src.generic_parser import MedicalDocParser


class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        # MedicalDocParser.__init__(self, text=text)
        super().__int__(text=text)

    def parse(self):
        return {
            'patient_name': self.get_patient_name(),
            'phone_number': self.get_patient_phone_number(),
            'hepatitis_b_vaccination': self.get_hepatitis_b_vaccination(),
            'medical_problems': self.get_medical_problems()
        }

    def get_patient_name(self):
        pattern = "Patient Information(.*?)\(\d{3}\)"
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        name = ''

        if matches:
            name = self.remove_noise_from_name(matches[0])

        return name

    def remove_noise_from_name(self, name: str):
        name = name.strip()
        name = name.replace('Birth Date', '').strip()

        pattern = '((Jan|Feb|March|April|May|June|Ju1y|Aug|Sep|Oct|Nov|Dec)[ \d]+)'

        date_matches = re.findall(pattern, name)
        if date_matches:
            date = date_matches[0][0]
            name = name.replace(date, '').strip()
        return name

    def get_patient_phone_number(self):
        pattern = "Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})"
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        return matches[0][1]

    def get_hepatitis_b_vaccination(self):
        pattern = "Have you had the Hepatitis B vaccination\?.*?(Yes|No)"
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        return matches[0]

    def get_medical_problems(self):
        # pattern = "List any Medical Problems \(asthma, seizures, headaches\}:[\n]*(.*)|List any Medical Problems \(asthma, seizures, headaches\):[\n]*(.*)"
        pattern = "List any Medical Problems .*?:[\n]*(.*)"
        matches = re.findall(pattern, self.text)

        # if matches:
        #     t = matches[0]  # we get a tuple
        #     if t[0] != '':
        #         return t[0].strip()
        #     else:
        #         return t[1].strip()

        return matches[0].strip()


if __name__ == '__main__':
    document_text = '''17/12/2020

Patient Medical Record

Patient Information Birth Date

Kathy Crawford May 6 1972

(737) 988-0851 Weight’

9264 Ash Dr 95

New York City, 10005 '

United States Height:
190

In Case of Emergency
ee J
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone
Genera! Medical History
nn ee
Chicken Pox (Varicella): Measies:
IMMUNE

IMMUNE
Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches}:

Migraine

.

‘Name of Insurance Company:

Random Insuarance Company - 4789 Bollinger Rd
Jersey City, New Jersey, 07030

a Policy Number:
71 1520731 3 Expiry Date:

. 30 December 2020
Do you have medical insurance?

Yes:

Medical Insurance Details

List any allergies:

Peanuts

List any medication taken regularly:
Triptans'''

    pd = PatientDetailsParser(document_text)
    print(pd.parse())
