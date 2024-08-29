a = int(input('ENTER NUMBER OF PLAYER :'))
if a < 8:
    name = []
    name1 = []
    name2 = []
    name3 = []
    name4 = []
    name5 = []
    name6 = []
    i = 0

    if i < a:  # ----------------------------player 1
        a1 = str(input('PLAYER NAME :'))
        name.append(a1)
        p1 = name[0]
        p1 = []
        i = i + 1
        if i < a:  # -------------------player 2
            a2 = str(input('PLAYER NAME :'))
            name1.append(a2)
            p2 = name1[0]
            p2 = []
            i = i + 1
            if i < a:  # ------------------player 3
                a3 = str(input('PLAYER NAME :'))
                name2.append(a3)
                p3 = name2[0]
                p3 = []
                i = i + 1
                if i < a:  # ------------------player 4
                    a4 = str(input('PLAYER NAME :'))
                    name3.append(a4)
                    p4 = name3[0]
                    p4 = []
                    i = i + 1
                    if i < a:  # ------------------player 5
                        a5 = str(input('PLAYER NAME :'))
                        name4.append(a5)
                        p5 = name4[0]
                        p5 = []
                        i = i + 1
                        if i < a:  # ------------------player 6
                            a6 = str(input('PLAYER NAME :'))
                            name5.append(a6)
                            p6 = name5[0]
                            p6 = []
                            i = i + 1
                            if i < a:  # ------------------player 7
                                a7 = str(input('PLAYER NAME :'))
                                name6.append(a7)
                                p7 = name6[0]
                                p7 = []
                                i = i + 1
    for j in range(1, 8, 1):
        print(f'-------ROUND{j}--------')
        k = 0
        if k < a:  # --------------------------result 1
            r1 = int(input(name[0]))
            p1.append(r1)
            k = k + 1
            t1 = sum(p1)
            print(a1, '=', t1)
            if k < a:  # ----------------------result 2
                r2 = int(input(name1[0]))
                p2.append(r2)
                k = k + 1
                t2 = sum(p2)
                print(a2, '=', t2)
                if k < a:  # --------------------result 3
                    r3 = int(input(name2[0]))
                    p3.append(r3)
                    k = k + 1
                    t3 = sum(p3)
                    print(a3, '=', t3)
                    if k < a:  # ----------------------result 4
                        r4 = int(input(name3[0]))
                        p4.append(r4)
                        k = k + 1
                        t4 = sum(p4)
                        print(a4, '=', t4)
                        if k < a:  # ----------------------result 5
                            r5 = int(input(name4[0]))
                            p5.append(r5)
                            k = k + 1
                            t5 = sum(p5)
                            print(a5, '=', t5)
                            if k < a:  # ----------------------result 6
                                r6 = int(input(name5[0]))
                                p6.append(r6)
                                k = k + 1
                                t6 = sum(p6)
                                print(a6, '=', t6)
                                if k < a:  # ----------------------result 7
                                    r7 = int(input(name6[0]))
                                    p7.append(r7)
                                    k = k + 1
                                    t7 = sum(p7)
                                    print(a7, '=', t7)





else:
    print('MAX 7 PLAYERS ONLY ALLOWED IN THIS GAME')

















