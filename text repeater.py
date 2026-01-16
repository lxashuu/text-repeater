''' text repeater by ashu '''
print("Enter your word:")
text = str(input())

print('How many times do you want to repeat:', text)
time = int(input())

output = (text + " ") * time
print(output.strip())


