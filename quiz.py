import json
with open("quetion.json",'r') as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question['question_text'])
    for index,alternatives in enumerate(question['alternatives']):
        print(f"{index+1}. {alternatives}")
    user_answer = int(input("Enter your answer: "))
    question["user_answer"] = user_answer

score = 0
for index, question in enumerate(data):
    if question["user_answer"] == question["correct_answer"]:
        score = score + 1
        result = "Correct answer"
    else:
        result = "Wrong answer"

    message = f"{index + 1}.{result} - your answer is : {question['user_answer']}, correct answer is : {question['correct_answer']}"
    print(message)
print(score,"/",len(data))