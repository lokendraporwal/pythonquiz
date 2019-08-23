import json
with open("quiz.json",'r') as f:
    dict=json.load(f)
result = 0
for j in dict['quiz']:
    print(j)
n=input("Enter Any one of the above : ")
result=0
for i in dict['quiz'][n]:
    que=dict['quiz'][n][i]['question']
    option=dict['quiz'][n][i]['options']
    print(que)
    index=1
    for k in option:
        print(index,k)
        index=index+1
    ans=int(input("Enter Index of above Option to answer : "))
    if(option[ans-1]==dict['quiz'][n][i]['answer']):
        result=result+1
print("Your Result is : ", result)
