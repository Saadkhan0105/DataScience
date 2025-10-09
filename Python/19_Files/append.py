# Append to an existing file called John Doe.txt and it should add more data about John Doe.

f = open("John Doe.txt", "a")

string = '''
John Doe initially used to stay in New York but now he moved to Delhi. And he is a very happy man. Currently he is working as a Data Scientist.
'''
f.write(string)

f.close()