# Program to remove emoticons.


string_with_emoticons = "Oh, hai! Can I haz cheezeberger? :D :D"

def remove_emoticons(string):
    emoticons = (':D', ':)', ':/', ':p', ';)')

    for emoticon in emoticons:
        string = string.replace(emoticon, "")
       
    return string
    
       
answer = remove_emoticons(string_with_emoticons)