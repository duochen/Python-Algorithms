# Delete values in dictionary

dict = {'Name':'Zara', 'Age':7, 'Class':'First'}

del dict['Name']  # Delete entry with key 'Name'
dict.clear()      # Remove all entries
del dict          # Delete entir dictionary

print(f"dict['Age']:  {dict['Age']}")           # An exception is raised
print(f"dict['School']:  {dict['School']}")     # An exception is raised