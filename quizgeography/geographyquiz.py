import json
import os
import time

class Question:
  def __init__(self, text, options, answer):
    self.text = text
    self.options = options
    self.answer = answer

  def is_correct(self, user_answer):
    return user_answer.lower().strip() == self.answer.lower().strip()

class QuizManager:
  def __init__(self, json_path):
    self.json_path = json_path
    self.questions = []
    self.score = 0
    self.load_questions()

  def load_questions(self):
    with open(self.json_path, 'r', encoding= 'utf-8') as file:
      data = json.load(file)
      for item in data:
        obj_question = Question(item["question"], item["options"], item["answer"])
        self.questions.append(obj_question)

  def start_game(self):
    print('------ GEOGRAPHY QUIZ ------')
    print("Let's have some fun playing a quiz about curious facts of world geography...")
    time.sleep(2)

  def run_quiz(self):
    for q in self.questions:
      print("\n" + "="*150)  
      print(q.text)
      print("="*150)

      for o in q.options:
        print(o)
      print("-" * 150)

      answer = input("Your answer is (A, B, C, or D): ").lower().strip()

      if q.is_correct(answer):
        print("\n ✨ Correct! Well done.")
        self.score +=1
        
        bars = "█" * self.score
        spaces = "░" * (len(self.questions) - self.score)
        print(f"Score: [{bars}{spaces}] ({self.score})\n")
      
      else:
        print(f"\n❌ Wrong! The correct answer was option ({q.answer.upper()}).")
        bars = "█" * self.score
        spaces = "░" * (len(self.questions) - self.score)
        print(f"Score: [{bars}{spaces}] ({self.score})\n")

  def show_results(self):
    print("\n" + "#"*50)
    print(f"🎉 QUIZ FINISHED! Your final score is: {self.score}/{len(self.questions)}")
    print("#"*50)

if __name__ == "__main__":
  current_dir = os.path.dirname(os.path.abspath(__file__))
  json_path = os.path.join(current_dir, 'questions.json')

  quiz_game = QuizManager(json_path)

  quiz_game.start_game()
  quiz_game.run_quiz()
  quiz_game.show_results()