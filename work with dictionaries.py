# Creating a dictionary and adding values

acronyms = {}
acronyms['LOL']= 'laugh out loud'
acronyms['IDK']= "I don't know"
acronyms['TBH']= 'to be honest'


print(acronyms['LOL'])

# To update a dictionary definition
acronyms['IDK'] = "New definition"

# To remove a dictionary item
del acronyms['LOL']


# If you access an empty key
# "KeyError: <ref> "

# To avoid key error use the get method
acronyms.get('ref')


# e.g. 
definition = acronyms.get('BTW')
if definition: #is true
    print(definition)
else:
    print("Key doesn't exist")

