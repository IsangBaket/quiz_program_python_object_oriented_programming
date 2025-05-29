import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class QuizReader:
    def __init__(self):
        self.filename = self.file_name()
        self.questions = self.convert_quiz(self.filename)


    def file_name(self):    # added needed functions first
        while True:
            try:     # asks for user file name to read
                txt_file = input("file name with '.txt': ")
                if txt_file.endswith('.txt'):   # ensures that user puts file extension
                    break
                with open(txt_file):
                    pass
            except FileNotFoundError:
                print("File not found")
        return txt_file

    def convert_quiz(self, txt_file):
        with open(txt_file, "r") as file:
            content = file.read()

        raw_questions = content.strip().split('------\n\n')
        quiz_data = []

        for item in raw_questions:
            lines = item.strip().split('\n')
            if len(lines) >= 6:
                question_data = {
                    'question': lines[0][9:],  # remove "Question: "
                    'A': lines[1][3:],         # remove "A: "
                    'B': lines[2][3:],
                    'C': lines[3][3:],
                    'D': lines[4][3:],
                    'answer': lines[5][-1].upper()  # get last character (letter of correct answer)
                }
                quiz_data.append(question_data)
        return quiz_data

    def quiz(self):
        score_tracker = 0
        total_questions = 0
        while True:
            current_question = random.choice(self.questions)     # randomly chooses question until user exits program
            # score tracker
            print("\nSCORE:")
            print(score_tracker)

            print("\n" + current_question['question'])
            print("A.", current_question['A'])
            print("B.", current_question['B'])
            print("C.", current_question['C'])
            print("D.", current_question['D'])

            user_answer = input("Your answer (A/B/C/D or E to exit): ").upper()

            if user_answer == 'E':      # breaks program when user wants to quit
                print("Thank you for playing!")
                break
            elif user_answer == current_question['answer']:
                print(Fore.GREEN + "Correct!")
                score_tracker += 1      # adds score
                total_questions += 1
            else:
                print(Fore.RED + "Wrong!")
                print(f"The correct answer is {current_question['answer']}.")
                total_questions += 1
        
        print(Back.LIGHTCYAN_EX +  Style.BRIGHT + f"\n🥳🥳🥳Congratulations! You got a score of {score_tracker} out of {total_questions}")

    def main():
        print(Style.BRIGHT + "----------START QUIZ----------")
        txt_file = file_name()
        quiz_data = convert_quiz(txt_file)
        quiz(quiz_data)

    if __name__ == "__main__":
        main()