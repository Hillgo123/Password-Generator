import numpy as np

class generator():
    def length(self):
        return int(input("How long should your password be?")) #Asks for requested password length

    def create_password(self):
        possible_password_characters = np.array(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N" "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "1", "2", "3", "4", "5", "6", "7", "8", "9", 
        "0", "!", "#", "&", "@", "%", "*", "?", "^", "(", ")"], dtype = str) #Array that contains all of the passwords possible characters

        return np.random.choice(possible_password_characters, size = Generator.length()) #Returns random contents from "possible_password_characters"

Generator = generator()

def main():
    print (("".join(str(cell) for cell in Generator.create_password()))) #Prints the function "create_password" as one word

if __name__ == "__main__":
    main()