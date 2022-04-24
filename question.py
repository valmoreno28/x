class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "¿Cuál es tu género?\n(a) Cisgénero \n(b) género no binario \n(c) Intersexual \n(d) Gay   \n(e) Lesbiana \n(f) Transgénero \n(g) Femenino \n(h) Masculino \n(i) Transexual",
     "Cual fue tu sexo asignado al nacer?\n(a) Hombre\n(b) Mujer",
     "¿Haz practicado alguna vez sexo sin métodos anticonceptivos físicos como el condón?\n(a) No\n(b) Si",
     "¿Haz practicado sexo sin condón?\n(a) No\n(b) Si", 
     "¿Haz presentado alguno de estos sintomas?\n(a) Llagas \n(b) Hinchazón \n(c) Verrugas \n(d) Inflamación \n(e) Enrojecimiento o irritación dentro o fuera de los genitales"
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "c"),
     Question(question_prompts[3], "d"),
     Question(question_prompts[4], "e"),
     Question(question_prompts[5], "f"),
     Question(question_prompts[6], "g"),
     Question(question_prompts[7], "h"),
     Question(question_prompts[8], "i"),
     Question(question_prompts[9], "j"),

     
     
     
     
     
     
     
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)
