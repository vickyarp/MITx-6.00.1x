#The player starts with a hand, a set of letters. As the player spells out words, 
#letters from this set are used up. For example, the player could start out with the following hand: 
#    a, q, l, m, u, i, l. The player could choose to spell the word quail . 
#    This would leave the following letters in the player's hand: l, m. 
#    Your task is to implement the function updateHand, which takes in two inputs - a hand and a word (string). 
#    updateHand uses letters from the hand to spell the word, and then returns a copy of the hand, 
#    containing only the letters remaining. For example:
#>>> hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
#>>> displayHand(hand) # Implemented for you
#a q l l m u i
#>>> hand = updateHand(hand, 'quail') # You implement this function!
#>>> hand
#{'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
#>>> displayHand(hand)
#l m  

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    dict=hand.copy()
    for letter in word:
        if letter in dict:
            dict[letter]-=1
    return (dict)