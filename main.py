import json
n=int(input("Enter 1 for sports \n Enter 2 for Maths : "))
with open("quiz.json",'r') as f:
    dict=json.load(f)
if n==1:
    result = 0;
    for j in dict['quiz']['sport']:
            i = 1
            que = dict['quiz']['sport'][j]['question']
            options = dict['quiz']['sport'][j]['options']
            print(que)
            for k in options:
                print(i, k)
                i = i + 1
            ans = int(input("Your Answer(1/2/3/4) : "))
            if (options[ans - 1] == dict['quiz']['sport'][j]['answer']):
                result = result + 1
    print("Your result is : ", result)
if(n==2):
    result = 0;
    for j in dict['quiz']['maths']:
            i = 1
            que = dict['quiz']['maths'][j]['question']
            options = dict['quiz']['maths'][j]['options']
            print(que)
            for k in options:
                print(i, k)
                i = i + 1
            ans = int(input("Your Answer(1/2/3/4) : "))
            if (options[ans - 1] == dict['quiz']['maths'][j]['answer']):
                result = result + 1
    print("Your result is : ", result)
