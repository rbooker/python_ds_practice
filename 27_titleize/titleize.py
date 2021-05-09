def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase_list = phrase.split(' ')
    capital_phrase = ""
    for word in phrase_list:
    	capital_phrase += word.capitalize() + " "
    return capital_phrase.rstrip()

