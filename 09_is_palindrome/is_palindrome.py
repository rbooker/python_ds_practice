def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    lst = [x.lower() for x in phrase if x != " "]
    reverse_lst = lst.copy()
    reverse_lst.reverse()
    if lst == reverse_lst:
        print("True")
    else:
        print("False")
