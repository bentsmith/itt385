#this program displays the use of dictionaries
spanish = {"hello" : "hola", "yes" : "si", "bye" : "adios" }
run = True
exit = "exit"
while (run):
    engword = input("enter a english word, or enter exit to cancel: ")
    if engword in spanish.keys():
        print(engword, "in Spanish is", spanish[engword] )
    elif engword == exit:
        print("goodbye")
        run = False
    else:
        print("this word is not in the dictionary")