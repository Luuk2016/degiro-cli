from degiro import DeGiro
from credentials import email, password

client = DeGiro(email, password)
print(client.auth())