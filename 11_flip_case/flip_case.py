def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    if to_swap.islower():
    	to_swap_flipped = to_swap.upper()
    else:
    	to_swap_flipped = to_swap.lower()
    flipped_list = []
    for x in phrase:
    	if x == to_swap or x == to_swap_flipped:
    		if x.islower():
    			flipped_list.append(x.upper())
    		else:
    			flipped_list.append(x.lower())
    	else:
    		flipped_list.append(x)
    return ''.join(flipped_list)

