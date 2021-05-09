def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    lst_from_str = list(phrase)
    lst_from_str.reverse()
    str_from_lst = "".join(lst_from_str)
    print(str_from_lst)
