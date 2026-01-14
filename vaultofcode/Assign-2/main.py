# write a program to count frequencies in a given text


from collections import Counter
text = input("Enter some text: ")

words = text.split()

freq = Counter(words)

print("Word Frequencies:")
for word, count in freq.items():
    print(f"{word}: {count}")

# palindrome check

text = input("Enter a word: ")

if text == text[::-1]:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")


# squre of number in list
numbers = [1, 2, 3, 4, 5]

squares = [n**2 for n in numbers]

print("Original list:", numbers)
print("Squares:", squares)

