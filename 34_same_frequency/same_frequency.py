def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str1 = str(num1)
    str2 = str(num2)
    if len(str1) != len(str2):
    	return False
    
    digitcount1 = {digit:str1.count(digit) for digit in str1}
    digitcount2 = {digit:str2.count(digit) for digit in str2}

    if set(digitcount1.items()) == set(digitcount2.items()):
    	return True
    else:
    	return False