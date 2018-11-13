# Program to remove emoticons.


string_with_emoticons = "Oh, hai! Can I haz cheezeberger? :D :D"

def remove_emoticons(string):
    """Remove emoticons from a string and return it.
    
    Postional arguments:
    string -- string to remove emoticons from.
    
    Returns:
    String without emoticons.
    
    >>> remove_emoticons("applause and laughter ;)")
    'applause and laughter '
    
    """
    emoticons = (':D', ':)', ':/', ':p', ';)')

    for emoticon in emoticons:
        string = string.replace(emoticon, "")
       
    return string
    
       
answer = remove_emoticons(string_with_emoticons)