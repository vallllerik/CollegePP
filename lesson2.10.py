phoneNumber = input()
phoneNumber = phoneNumber.replace('(', '')
phoneNumber = phoneNumber.replace(')', '')
phoneNumber = phoneNumber.replace('-', '')
phoneNumber = phoneNumber.replace(' ', '')
print(phoneNumber)
