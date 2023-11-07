import pytest
import funcionesp

#TEST PARCIAL

#Test comprobacion de ADN
@pytest.mark.parametrize("dna, res",[
    (["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"], True),
    (["AGTTGA","CCGTAC","TCCAGT","AGATCG","CAACTA","TTAGTG"],True),
    (["AATCCG","TTATAC","TGGACT","ATCATG","CAGGTC","ACAGTG"],False),
    (["TTTCGA","TACGAC","AGCCGT","ACTATG","CATATC","CCAGTG"],False)
])
def test_is_mutant(dna, res):
    assert funcionesp.is_mutant(dna) == res

#Test comprobacion de letra
@pytest.mark.parametrize("letter, res",[
    ("A", True),
    ("B",False),
    ("d",False),
    ("G",True)
])
def test_check_letter(letter, res):
    assert funcionesp.check_letter(letter) == res

#Test comprobacion de secuencia de letras
@pytest.mark.parametrize("sequence, res",[
    ("TTTA", False),
    ("AAAA",True),
    ("CCCC",True),
    ("GTTC", False)
])
def test_check_sequence(sequence, res):
    assert funcionesp.check_sequence(sequence) == res
