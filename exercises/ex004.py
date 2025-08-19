v = input('Enter a value: ')
print('''
    Type: {}
    Is numeric?: {}
    Is alphabeth?: {}
    Is float?: {}
    Is alphanumeric?: {}
    Is capital: {}
    Is lowercase: {}
    Contains spaces?: {}
    Is capitalized?: {}
    

'''.format(type(v), v.isnumeric(), v.isalpha(), v.isdecimal(),v.isalnum(), v.isupper(), v.islower(), v.isspace(), v.istitle()))