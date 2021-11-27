question_list = [
    "How many continents are there?",              # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?" ,   # teesra question
    "what is the largest state by area in india"]



options_list = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"],
    ["Rajasthan","Gujarat","Madhya pradesh","Uttar pradesh"]]

print("WELCOME TO KBC")
print("Let's start the GAME")
print("Here is Your FIRST QUESTION on your Computer Screen")
answer_list=[["3 Seven", "4 Eight"],["3 Bhopal","4 Delhi"],["1 Software Engineering","2 Counseling"],["1 Rajasthan","2 Gujarat"]]
solution_list=[3,4,1,1]
i=0
s=0
count=0
while i<len(question_list):
    print(question_list[i])
    k=i
    j=0
    while j<len(options_list[k]):
        n=options_list[k][j]
        print(j+1,n)
        j=j+1
    life_line=input("do you want 50:50 lifeline\ny/n:")
    if life_line=='y':
        if count==0:
            print(answer_list[i])
            answer=int(input("now again select your option:"))
        
            if answer==solution_list[i]:
                s+=10000
                print("your answer is correct")
                print("congratulations you won Rs.",s)
                
            else:
                print("sorry,you lost the game")
                break
            count+=1    
        else:
            print("the chance of taking life line is only once")
            final_answer=int(input("select your option:"))
            if final_answer==solution_list[i]:
                print("congrats your answer is right") 
                s+=10000
                print("you won the amount of Rs.",s)
            else:
                print("you have no chance")
                break
        
    else:
        pass
        final_answer=int(input("select your option:"))
        if final_answer==solution_list[i]:
            print("your answer is correct")
            s+=10000
            print("congratulations you won Rs.",s)
        else:
            print("sorry,you lost the game")
            break
    i=i+1
print("Thank you for playing with us")
print("Here is the amount you won of Rs.",s)       
