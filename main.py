import random
print("enter the option between rolling the dice or exiting the simulator")
print("\"y\".rolling the dice   /  \"n\".exiting the simulator")
value_by_user = input("what do you want to do \n")
while True:
    if value_by_user == "y":
        values = random.randint(1, 6)
        if values == 1 :
            print("[     ]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[     ]")

        elif values == 2 :
            print("[     ]")
            print("[     ]")
            print("[0   0]")
            print("[     ]")
            print("[     ]")

        elif values == 3 :
            print("[     ]")
            print("[     ]")
            print("[0 0 0]")
            print("[     ]")
            print("[     ]")

        elif values == 4 :
            print("[0   0]")
            print("[     ]")
            print("[     ]")
            print("[     ]")
            print("[0   0]")

        elif values == 5 :
            print("[0   0]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[0   0]")

        elif values == 6 :
            print("[0 0 0]")
            print("[     ]")
            print("[0 0 0]")
            print("[     ]")
            print("[0 0 0]")

        value_by_user = input("want to continue or not,say \"yes(y)\"/\"no(n)\"")
    else :
        print("we are exiting the simulator")
        break
