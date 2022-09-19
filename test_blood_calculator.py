"""
def test_check_HDL_Normal():
    from blood_calculator import check_HDL
    answer = check_HDL(85)
    expected = "Normal"
    assert answer == expected

def test_check_HDL_BorderlineLow():
    from blood_calculator import check_HDL
    answer = check_HDL(50)
    expected = "Borderline Low"
    assert answer == expected

def test_check_HDL_Low():
    from blood_calculator import check_HDL
    answer = check_HDL(35)
    expected = "Low"
    assert answer == expected
"""

# A more condense way of doing the above code
import pytest
@pytest.mark.parametrize("HDL_input, expected",
    [(85, "Normal"), 
    (50, "Borderline Low"), 
    (35, "Low")])
def test_check_HDL(HDL_input,expected):
    from blood_calculator import check_HDL
    answer = check_HDL(HDL_input)
    assert answer == expected

# Write a test for LDL and Total Cholesterol
import pytest
@pytest.mark.parametrize("LDL_input, expected",
    [(125, "Normal"), 
    (140, "Borderline High"), 
    (170, "High"),
    (200, "Very High")])
def test_check_LDL(LDL_input,expected):
    from blood_calculator import check_LDL
    answer = check_LDL(LDL_input)
    assert answer == expected

import pytest
@pytest.mark.parametrize("Chol_input, expected",
    [(185, "Normal"), 
    (220, "Borderline High"), 
    (250, "High")])
def test_check_Chol(Chol_input,expected):
    from blood_calculator import check_Chol
    answer = check_Chol(Chol_input)
    assert answer == expected