#added enumerated type in loop, also comments belong above statements for legibility, practiced f-strings

def first_negative_number(list_of_numbers):
    
    #enumerate() and for index cycle through list
    for index, number in enumerate(list_of_numbers): 
        if number < 0:
            return f"Index {index}: {number}"
        
    #message to output in terminal if no negative numbers
    return "No negative numbers in this list" 
    
print(first_negative_number([3, 5, 2, -1]))
