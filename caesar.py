def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    
    alphaSize = len(lowers)
    dict = {}
    for i in range(alphaSize):
        dict[ lowers[i] ] = lowers[(i + shift) % alphaSize]
        dict[ uppers[i] ] = uppers[(i + shift) % alphaSize]
    
    return dict

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    cipText = ''
    dict = coder
    for char in text:
        if char in dict:
            cipText += dict[char]
        else:
            cipText += char
    
    return cipText  


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return applyCoder(text, buildCoder(shift))

def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    
    text = text.split(' ')
    bestShift = 0
    maxFoundWords = 0
    for shift in range(26):
        decryptedWords = []
        
        for word in text:
            decrypted = applyShift(word, shift)
            decryptedWords.append(decrypted)
        
        foundWords = 0
        for word in decryptedWords:
            if isWord(wordList, word):
                foundWords += 1
        
        if foundWords > maxFoundWords:
            maxFoundWords = foundWords
            bestShift = shift
        
    return bestShift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    ### TODO
    wordList = loadWords()
    story = getStoryString()
    bestShift = findBestShift(wordList, story)
    return applyShift(story, bestShift)

print decryptStory()

