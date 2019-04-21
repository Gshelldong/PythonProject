class Letter_Game():

    def a(self):
        for i in range(1, 6):
            for k in range(6 - i):
                print(" ", end="")
            for j in range(1, i + 1):
                if j == 1 or i == j:
                    print("*", end=" ")
                elif i == 4:
                    print("*", end=" ")
                else:
                    print("  ", end="")
            print()

    def b(self):
        for i in range(1, 4):  # 控制行
            for j in range(1, 4):  # 控制列
                if i == 1 or i == 4 or j == 1:
                    if j < 3:
                        print("*", end=" ")
                elif j == 3:
                    print("*", end="")
                else:
                    print(" ", end=" ")
            print()
        for i in range(1, 5):  # 控制列
            for j in range(1, 4):  # 控制行
                if i == 1 or i == 4 or j == 1:
                    if j < 3:
                        print("*", end=" ")
                elif j == 3:
                    print("*", end="")
                else:
                    print(" ", end=" ")
            print()

    def c(self):
        for i in range(1, 5):  # 控制行
            for j in range(1, 4):  # 控制列

                if i == 4 or i == 1:
                    if j == 1:
                        print(" ", end="")
                    else:
                        print("*", end=" ")
                elif j == 1:
                    if i == 2 or i == 3:
                        print("* ", end=" ")
            print()

    def d(self):
        for i in range(1, 5):  # 控制行
            for j in range(1, 4):  # 控制列

                if i == 4 or i == 1:
                    if j == 1:
                        print(" ", end="")
                    else:
                        print("*", end=" ")
                elif j == 1:
                    if i == 2 or i == 3:
                        print("* ", end=" ")
            print()

    def e(self):
        for i in range(1, 6):
            for j in range(1, 4):
                if i == 1 or i == 5 or i == 3 or j == 1:
                    print("*", end=" ")
            print()

    def g(self):
        for i in range(1, 5):  # 控制行
            for j in range(1, 5):  #
                if i == 1 or i == 4:
                    if j == 1:
                        print(" ", end="")
                    else:
                        print("*", end=" ")
                elif i == 2 and j == 1:
                    print("*", end=" ")
                elif i == 3:
                    if j == 2:
                        print(" ", end="")
                    else:
                        print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()