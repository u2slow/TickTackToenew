import time

frontField = [[" "," "," "],[" "," "," "],[" "," "," "]]
backField = [[0,0,0],[0,0,0],[0,0,0]]
fieldAbc = ["A", "B", "C"]
winner = False
def ShowField():
    print(" ",fieldAbc)
    counter1 = 0 
    
    for i in frontField:
        print(counter1,i)
        counter1 = counter1+1
def TurnPlayer():
    inputX = input("Wo soll das X hin?")
    Move(inputX,"X")
def End():
    print("Das Spiel ist zu Ende.")
def WinnorUnentschieden ():
    winner = Winncheck(11)
    if winner:
        ShowField()
        print("Der Spieler X hat gewonnen")
        End()
        return False
    else :
        winner = Winncheck(7)
        if winner:
            ShowField()
            print("Du hast nicht gerade gegen einen Bot verloren oder?")
            End()
            return False
        elif Unentschieden():
            ShowField()
            print("Das spiel ist Unentschieden ausgegenagen")
            End()
            return False
    return True     
def GameX():
    TurnBot()
    ShowField()
    if WinnorUnentschieden():
        TurnPlayer()
    if WinnorUnentschieden():
        GameX()
def Move(input, Player):
    x = 0
    y = int(input[1])
    backPlayer = 11
    if Player== "O":
        backPlayer = 7
    if backPlayer == 11:
        if input[0] == "A":
            x= 0
        if input[0] == "B":
            x = 1
        if input[0] == "C":
            x = 2
    else:
        x = int(input[0])
    if backField[y][x] == 0:
        frontField[y][x] = Player
        backField[y][x] = backPlayer
    else :
        print("Das Feld ist bereits Belegt!")
        if Player == "X":
            TurnPlayer()
        else:
            TurnBot()
            print("Das Feld ist bereits Belegt!")
def Winncheck (PlayerInt):
    for i in backField:
        counterhorizontal = 0
        for n in i:
            counterhorizontal += n
            if counterhorizontal == PlayerInt*3:
                return True
    for n in range(3):
        countervertical = 0
        for i in backField:
            countervertical += i[n]
            if countervertical == PlayerInt*3:
                return True
    nfor = 0
    nback = 2
    counterfor = 0
    counterback = 0
    for i in backField:
        counterfor += i[nfor]
        counterback += i[nback]
        if counterfor == PlayerInt*3 or counterback == PlayerInt*3:
            return True
        nfor +=1
        nback += -1
def TurnBot():
    if BotWinCheck():
        if BotloseCheck():
            if backField[2][2] == 0:
                Move("22","O")
            elif backField[2][0] == 0 and backField[2][1] == 0:
                Move("02","O")
            elif backField[0][2] == 0 and backField[0][1] == 0:
                Move("20", "O")
            elif backField[0][0] == 0:
                Move ("00","O")
def Horizontallcheck (PlayerInt):
    ycounter = 0
    for i in backField:
        counter = 0
        for n in i:
            counter += n
            if counter == PlayerInt*2:
                kcounter = 0
                for k in i:
                    if k == 0:
                        output = str(kcounter),str(ycounter)
                        if PlayerInt == 11:
                            Move(output,"O")
                        else:
                            Move(output,"O")
                        return True
                        break
                    kcounter += 1
        ycounter += 1
    return False
def Verticalcheck(PlayerInt):
    for i in range(3):
        counter = 0
        for n in backField:
            counter += n[i]
            if counter == PlayerInt*2:
                kcounter = 0
                for k in backField:
                    
                    if k[i]== 0:
                        output = str(i)+ str(kcounter)
                        if PlayerInt == 11:
                            Move(output,"O")
                        else:
                            Move(output,"O")
                        return True
                        break
                    kcounter += 1
    return False   
def DiagonalCheck(PlayerInt):
    nfor = 0
    nback = 2
    counterfor = 0
    counterback = 0
    for i in backField:
        counterfor += i[nfor]
        counterback += i[nback]
        if counterfor == PlayerInt*2:
            print("TEst")
            kfor = 0
            kcounter = 0
            for k in backField:
                if k[kfor] == 0:
                    output = str(kfor)+str(kcounter)
                    if PlayerInt == 11:
                        Move(output,"O")
                    else:
                        Move(output,"O")
                    return True
                    break
                kcounter += 1
                kfor += 1
        if counterback == PlayerInt*2:
            kback = 2
            kcounterback = 0
            for k in backField:
                if k[kback] == 0:
                    output = str(kback)+str(kcounterback)
                    if PlayerInt == 11:
                        Move(output,"O")
                    else:
                        Move(output,"O")
                    return True
                    break
                kcounterback += 1
                kback += -1
        nfor += 1
        nback += -1
    return False
def BotloseCheck():
    if Horizontallcheck(11)== False:
        if Verticalcheck(11) == False:
            if DiagonalCheck(11) == False: return True
def Unentschieden():
    pat = False
    for i in backField:
        for n in range(2):
            print(n)
            if i[n] == 0: return False
            else: pat = True
    return pat
def BotWinCheck():
    if Horizontallcheck(7)== False:
        if Verticalcheck(7) == False:
            if DiagonalCheck(7) == False:
                return True
GameX()
time.sleep(5)