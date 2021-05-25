import random
from json import loads

with open("./questions.json") as q:
    questions = loads(q.read())

question = (list(questions.values())[
            random.randrange(len(questions.values()))])
qanswers = list(question["a"].keys())
answers = random.sample(qanswers, k=len(qanswers))

print(" ")
print(f'Odpowiedz na pytanie: { question["q"] }')
print(f'a) {answers[0]}')
print(f'b) {answers[1]}')
print(f'c) {answers[2]}')
print(f'd) {answers[3]}')
userAnswer = str(input("Twoja odpowiedz: ")).lower()

ans = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3
}


if((question["a"])[answers[ans[userAnswer]]] == True):
    print(" ")
    print("Poprawna odpowiedź!!")
    print(" ")
else:
    print(" ")
    print("Niepoprawna odpowiedz :<")
    print(" ")
