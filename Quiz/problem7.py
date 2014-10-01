def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    Hint: use a guess and check approach.
    6a+9b+20c=n
    """
    a = 0
    b = 0
    c = 0
    while (6 * a + 9 * b + 20 * c - n) != 0:
