# Program to remove emoticons.


string_with_emoticons = "Oh, hai! Can I haz cheezeberger? :D :D"

def get_emoticons():
    """Reads an emoticon file.
   
    Returns:
    List of emoticon strings.
    
    >>> get_emoticons()
    [':D', ':)', ':/', ':p', ';)']
    
    >>> a = get_emoticons()
    >>> type(a)
    <class 'list'>
    
    """
    f = open('emoticons.txt') 
    emoticons =  f.read().split(",")
    return emoticons
    

    
def remove_emoticons(string):
    """Remove emoticons from a string and return it.
    
    Postional arguments:
    string -- string to remove emoticons from.
    
    Returns:
    String without emoticons.
    
    >>> remove_emoticons("applause and laughter ;)")
    'applause and laughter '
    
    """
    emoticons = get_emoticons()

    for emoticon in emoticons:
        string = string.replace(emoticon, "")
       
    return string
    
       
answer = remove_emoticons(string_with_emoticons)

print("string_with_emoticons: \"", string_with_emoticons, "\"", sep='')
print("string_with_emoticons removed: \"", answer, "\"", sep='')
