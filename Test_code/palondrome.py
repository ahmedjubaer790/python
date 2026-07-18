def pal(words):
    rvtrn=words[::-1]

    if words==rvtrn:
        print(words,' is a palindrome')
    else:
        print(words,' is not a palindrome')

pal('madam')