def check_palindrome(sequence):
  #simplest way to return and ignore spaces and punctuation 
  empty = "" 

  for char in sequence: 
    # isalnum() checks if is a letter or number - helps ignore spaces and punctuation
    if char.isalnum():
      empty += char.lower()

  #returns true or false - empty[start:stop:step] [::-1] is empty start stop and then step is going through backwards
  return empty == empty[::-1]


def main():
  sequence = input("Enter a word: ")
  print(check_palindrome(sequence))

if __name__ == "__main__": 
  main()
