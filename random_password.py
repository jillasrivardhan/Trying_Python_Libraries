import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}\\|;:'\",.<>/?`~ "

# chooses random number between 1 to 10

length = random.choice(range(1,10))

#joins the random characters with size of length

random_password = ''.join(random.choices(characters, k=length))

print(random_password)