import pytest
import ai

def test_tah_chyba():
    with pytest.raises(ValueError):
        ai.tah_pocitace('oxoxoxoxoxoxoxoxoxox')