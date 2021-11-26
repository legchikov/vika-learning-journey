import os
from hello import hello


# -------------------------------------------------------------------
def test_validInput():

    assert hello("dima") == "Hello, Dima!"

      
# -------------------------------------------------------------------

def test_invalidInput():

    assert hello("125 545") == "ERROR: Invalid Input data. Please use only string!"

# -------------------------------------------------------------------

def test_validInput1():

    assert hello("Dima") == "Hello, Dima!"
      
# -------------------------------------------------------------------