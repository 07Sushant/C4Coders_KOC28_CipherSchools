from termcolor import colored

print("\n")
# function to create acronym
bar = 20
print("==" * bar)
print("Print Acronym of Given String\n")

def mainFn(stng):
    # add first letter
    output = stng[0]
    # iterate over string
    for i in range(1, len(stng)):
        if stng[i-1] == ' ':
           
            # add letter next to space
            output += stng[i]
             
    # uppercase output
    output = output.upper()
    return output

number_of_string = input("Total number of strings: ")
print("\n")

if number_of_string.isnumeric() == True:

    strings = []
    for x in range(int(number_of_string)):
        strings.append(input('Enter String '+str(int(x+1))+": "))

    print("\n")

    for y in range(len(strings)):
        print(colored(strings[y] + mainFn(":  "+strings[y]+ " "),"red","on_white"))
else:
    print(colored("Enter any positive integer","white","on_red"))

print("\n==========================================")