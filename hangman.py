def hangman():
    question=input("お題を入力してください：")
    list1=[]
    for i in question:
        list1.append(i)

    list2=[]
    while len(list2)<len(list1):
        list2.append("_")

    hangman=["1",
             "2----   ",
             "3|    0 ",
             "4|   /|~",
             "5|   / ~",
             "6|      ",
             "7|      ",
             "8|      "]
    wrong=0
    while wrong < len(hangman)-1 :
        print(list2)
        answer=input("お題に含まれる単語を1つ入力してください：")
        
        if answer in list1:
            a=list1.index(answer)
            list1[a]="$"
            list2[a]=answer
        else:
            wrong+=1

        n=wrong +1
        for i in range(0,n):
            print(hangman[i])

        if "_" not in list2:
            print("あなたの勝ちです！")
            break

    if "_" in list2:
        print("あなたの負けです...")
