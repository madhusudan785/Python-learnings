def check_longest_sentence():
    with open("practice.txt","r") as file:
        bigger=""
        for line in file:
            if len(line)>len(bigger):
                bigger=line
        return bigger
        

result =check_longest_sentence()
print(result)




with open("newFile.txt","w") as file:
    file.write("Hey There \nthis is a new file for practice")

with open("practice.txt","w")as file:
    file.write("Line 1: Madhu\nLine 2: Milan\nLine 3: Sahoo")

with open("practice.txt","r")as file:
    data=True
    count_line=0
    while data:
        data=file.readline()
        if(data==""):
            break
        else:
           count_line +=1

print(count_line)




with open("newFile.txt","r") as f:
    data=f.read()

new=data.replace("java","Python")
print(new)

with open("newFile.txt","w") as f:
    data=f.write(new)

with open("newFile.txt","r") as f:
    data=f.read()
    if data.find("file"):
        print("true")


def check_word():
    with open("newFile.txt","r") as f:
        word="file"
        data=True
        count_line=1
        while data:
            data=f.readline()
            if(word in data):
                print("found in line",count_line)
            count_line+=1

check_word()         




