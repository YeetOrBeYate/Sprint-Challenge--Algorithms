'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

word = "abcthxyz"



def count_th(word):
    
    value = "th"

    n1 = len(word)
    n2 = len(value)

    if n1 == 0:
        return 0
    
    # if the first two letters of the string have it, add one to the return
    if word[0 :n2] == value:
        # move 1 leter over and repeat
        return count_th(word[n2-1:]) + 1
    else:
        #move 1 leter over and repeat
        return count_th(word[n2-1:])

print(count_th(word))