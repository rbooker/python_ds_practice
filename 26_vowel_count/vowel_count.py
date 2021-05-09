def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    lowerphrase = phrase.lower()
    return {x:lowerphrase.count(x) for x in lowerphrase if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x =='u'}