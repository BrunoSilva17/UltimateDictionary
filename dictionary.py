print("Welcome to the ultimate Dictionary!")

word = input("Please type a word: ")

with open('bank.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

if word in open('bank.txt').read():
     with open('bank.txt', 'r') as f:
        for line in f:
            if word in line:                
                print (line)
                input("");
else:
       print("The word doesn't exist in the bank.")
       confirmation1 = input("Do you want to add this word to the bank (Yes/No): ")
       if confirmation1 == "Yes":
         definition = input("Please type the defenition of the word: ")
         f = open("bank.txt", "a")
         f.write("\n" + word + " " + "=" + " " + definition)
         f.close()
         
         

