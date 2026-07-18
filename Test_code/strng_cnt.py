def strng_count(words):
    count=0
    for word in words:
        if len(word)>=2 and word[0]==word[-1]:
            count+=1

    return count

str_lis=['a','aa','abc','abba','dafae','cccc']
final=strng_count(str_lis)
print('The final count is ',final)