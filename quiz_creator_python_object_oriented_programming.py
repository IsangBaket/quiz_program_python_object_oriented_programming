# For Assignment 9: Quiz Creator
# Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. 
# Write the collected data to a text file. Ask another question until the user chose to exit.

class QuizReader:
    print("-----WELCOME TO MY QUIZ CREATOR-----")

    def __init__(self):
        print("-----WELCOME TO MY QUIZ CREATOR-----")
        self.filename = self.file_name()

    def file_name(self):
        while True:     # asks for user file name
            txt_file = input("file name with '.txt': ")
            if txt_file.endswith('.txt'):   # ensures that user puts file extension
                return txt_file
            print("please add a '.txt' extension!")

    def quiz_creator(self, filename):
        while True:
            question = input("Enter Question(enter e to exit): ")   # asks user for question
            
            if question == 'e':   # ends program 
                break

            print("Input answers for A to D") 

            choices = []
            for items in ['A', 'B', 'C', 'D']:  # asks user for input for choices A to D
                answers = input(f"Choices {items}: ")
                choices.append(answers)

            correct_answer = input("letter of correct answer: ").upper()    # asks user for the correct answer

            with open(filename, "a") as file:   # saves input to external text file
                file.write(f"Question: {question}\n")
                file.write(f"A: {choices[0]}\n")
                file.write(f"B: {choices[1]}\n")
                file.write(f"C: {choices[2]}\n")
                file.write(f"D: {choices[3]}\n")
                file.write(f"Correct Answer: {correct_answer}\n")
                file.write('------\n\n')

