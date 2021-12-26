from crownest import crownest

def test_check_a():
    assert crownest("cow") == "Ahoy, Captain, a cow off the larboard bow!"

#--------------------------------------------------------------------------

def test_check_an():
    assert crownest("apple") == "Ahoy, Captain, an apple off the larboard bow!"


#-----------------------------------------------------------------------------

def test_check_invalid(): 
    assert crownest("one1") == "ERROR: Invalid Input data. Please use only string!"


#-----------------------------------------------------------------------------

def test_check_notLatin():
    assert crownest("вася") == "ERROR: Invalid Input data. Please use only latin alphabet!"

#-----------------------------------------------------------------------------

def test_check_theCity():
    assert crownest("Havana") == "Ahoy, Captain, the Havana off the larboard bow!"

#-----------------------------------------------------------------------------

def test_check_theName():
    assert crownest("Alex") == "Ahoy, Captain, the Alex off the larboard bow!"

#-----------------------------------------------------------------------------

def test_check_theExption():
    assert crownest("universe") == "Ahoy, Captain, the universe off the larboard bow!"