# Write to file called John Doe.txt and it should contain data about John Doe.

f = open("John Doe.txt", "w")

string = '''
John Doe is a nice guy and he is from New York. He works with python and his favorite library is Pandas.
'''
f.write(string)

f.close()
