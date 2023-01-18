import re
from backend.src.generic_parser import MedicalDocParser


class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        # MedicalDocParser.__init__(self, text=text)
        super().__int__(text=text)

    def parse(self):

        return {
            'patient_name': self.get_field('patient_name'),
            'phone_number': self.get_field('phone_number'),
            'HB_status': self.get_field('HB_status'),
            'any_med_prob': self.get_field('any_med_prob')
        }

    def get_field(self, field_name):
        pattern_dict = {
            'patient_name': {'pattern': "Date[\n]*(.*) [a-zA-Z]+ \d \d{4}", 'flags': 0},
            'phone_number': {'pattern': "\d{4}[\n]*(\(\d{3}\) \d{3}-\d{4})", 'flags': 0},
            'HB_status': {'pattern': "Have you had the Hepatitis B vaccination\?[\n]*(\w+|‘\w+)", 'flags': 0},
            'any_med_prob': {
                'pattern': "List any Medical Problems \(asthma, seizures, headaches\}:[\n]*(.*)|List any Medical Problems \(asthma, seizures, headaches\):[\n]*(.*)",
                'flags': 0}
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
            if field_name == 'any_med_prob':
                if len(matches) > 0:
                    t = matches[0]
                    if t[0] == '':
                        return t[1].strip()
                    else:
                        return t[0].strip()
            else:
                if len(matches) > 0:
                    return matches[0].strip()


if __name__ == '__main__':
    document_text = '''Patient Medical Record

Patient Information Birth Date

Jerry Lucas May 2 1998

(279) 920-8204 Weight:

4218 Wheeler Ridge Dr 57

Buffalo, New York, 14201 Height:

United States gnt
170

In Case of Emergency

- eee

Joe Lucas . 4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone United States
Work phone

General Medical History

Chicken Pox (Varicelia): Measles: ..

IMMUNE NOT IMMUNE

Have you had the Hepatitis B vaccination?

‘Yes

| List any Medical Problems (asthma, seizures, headaches):
N/A

7?
v

17/12/2020


_—

Name of Insurance Company:
Random Insuarance Company

Policy Number:
5638746258

Do you have medical insurance?

_ Yes

Medical Insurance Details

List any allergies:
N/A

List any medication taken regularly:

N/A

4218 Smeeler Ridge Dr
Buffalo, New York, 14206
United States

Expiry Date:
31 December 2020'''

    pd = PatientDetailsParser(document_text)
    print(pd.parse())
