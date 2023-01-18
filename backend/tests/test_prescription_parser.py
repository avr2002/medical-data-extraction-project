from backend.src.prescription_parser import PrescriptionParser
import pytest


@pytest.fixture()
def doc_1_marta():
    document_text = \
        """
        Dr John Smith, M.D
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
    return PrescriptionParser(document_text)


@pytest.fixture()
def doc_2_amit():
    document_text = \
        """
        Dr Amit V Raj, M.D
        2 Non-Important Street,
        New York, Phone (000)-111-2222

        Name: Amit Vikram Raj Date: 5/11/2022

        Address: Singhmore, Hatia, Ranchi, 834003

        K

        Prednisone 20 mg
        Lialda 2.4 gram

        Directions:

        Prednisone, Taper 5 mg every 3 days,
        Finish in 2.5 weeks a
        Lialda - take 2 pill everyday for 1 month

        Refill: 2 times
        """
    return PrescriptionParser(document_text)


@pytest.fixture()
def doc_3_empty():
    return PrescriptionParser("")


def test_get_name(doc_1_marta, doc_2_amit, doc_3_empty):
    # pp = PrescriptionParser(document_text)
    assert doc_1_marta.get_field('patient_name') == "Marta Sharapova"
    assert doc_2_amit.get_field('patient_name') == "Amit Vikram Raj"
    assert doc_3_empty.get_field('patient_name') is None


def test_get_address(doc_1_marta, doc_2_amit, doc_3_empty):
    # pp = PrescriptionParser(document_text)
    assert doc_1_marta.get_field('patient_address') == "9 tennis court, new Russia, DC"
    assert doc_2_amit.get_field('patient_address') == "Singhmore, Hatia, Ranchi, 834003"
    assert doc_3_empty.get_field('patient_address') is None


def test_get_medicines(doc_1_marta, doc_2_amit, doc_3_empty):
    # assert doc_1_marta.get_field('medicines') == """K\n    \n        Prednisone 20 mg\n        Lialda 2.4 gram"""
    assert doc_3_empty.get_field('medicines') is None


def test_get_dosage_direction(doc_1_marta, doc_2_amit, doc_3_empty):
    # assert doc_1_marta.get_field('dosage_direction') == """Prednisone, Taper 5 mg every 3 days,
    #                                                        Finish in 2.5 weeks a
    #                                                        Lialda - take 2 pill everyday for 1 month"""
    assert doc_3_empty.get_field('dosage_direction') is None


def test_get_refill_amount(doc_1_marta, doc_2_amit, doc_3_empty):
    assert doc_1_marta.get_field('refill_amount') == '2'
    assert doc_3_empty.get_field('refill_amount') is None


def test_parse(doc_1_marta, doc_2_amit, doc_3_empty):
    record_marta = doc_1_marta.parse()
    assert record_marta['patient_name'] == "Marta Sharapova"
    assert record_marta['patient_address'] == "9 tennis court, new Russia, DC"

    record_empty = doc_3_empty.parse()
    assert record_empty == {
        'patient_name': None,
        'patient_address': None,
        'medicines': None,
        'dosage_direction': None,
        'refill_amount': None
    }
