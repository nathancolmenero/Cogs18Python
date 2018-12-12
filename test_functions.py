import pytest
from my_module.functions import select_language

def test_select_language_english():
    assert select_language('english') == 'english'

def test_select_language_invalid():
    with pytest.raises(ValueError) as e:        
        select_language('menglish')

def test_select_languagee_swedish():
        assert select_language('swedish') == 'swedish'