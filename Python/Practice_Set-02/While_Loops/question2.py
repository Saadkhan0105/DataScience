# Write a program that keeps asking the user to enter a password until they enter the correct one.

password = "secret"
entered_pass = input("Enter the password: ")

while(entered_pass != password):
    entered_pass = input("Wrong Password! Try again and Enter the password: ")
    
print("Success! You are logged in.")