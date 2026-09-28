import validation
import analysis


def test_validation():
    x = validation.check("ATGC")
    assert x[0] == True

    x = validation.check("ATGX")
    assert x[0] == False


def test_count():
    x = analysis.count("AATGCC")
    assert x == (2, 1, 1, 2)


def test_analysis():
    x = analysis.do_analysis("ATGC")
    assert x["length"] == 4
    assert x["gc"] == 50.0


test_validation()
test_count()
test_analysis()

print("Tests passed.")
