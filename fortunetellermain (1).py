a = str(input('where do u live rn? '))
b = int(input('on a scale of 1-10, how good are you feeling today? '))
c = str(input('do you think you are a lucky person?'))
if (a == "New York") or (a == "new york") or (a == "ny") or (a == "NY") or (a == "New york"):
    print ("so u live in new york. how's the air? in other news: ")
if (b > 5):
    print ("i'm predicting you're gonna have a shit week")
elif (b == 5):
     print ("mediocre days ahead.")
else: 
    print ("next few days about to be great for you.")
if (c == "no") or (c == "No") or (c == "NO"):
    print ("man i feel sorry for you. bad feng shui")
elif (c == "yes") or (c == "ye" ) or (c == "Yes") or ( c == "Ye") or (c == "Ye"):
    print ("also you're not gonna be lucky for long i'm praying on your downfall")