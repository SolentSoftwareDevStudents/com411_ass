# A while loop used to ensure that correct selection has been made in case of invalid selection

has_selected = False
user_input = 0

while not has_selected:

    if variant is None or variant == 0:
        user_input = int(input("[1] Process Data\n[2] Visualise Data\n[3] Export Data\n[4] Exit"))
        if 1 <= user_input <= 4:
            has_selected = True
            return
        else:
            print("Please make appropriate selection")

    elif variant == 1:
        user_input = int(input("""[1] Record by Serial Number\n[2] Records by Observation Date
           [3] Group Records by Country/Region\n[4] Summarise Records"""))
        if 1 <= user_input <= 4:
            has_selected = True
            return
        else:
            print("Please make appropriate selection")

    elif variant == 2:
        user_input = int(input("[1] Country/Region Pie Chart\n[2] Observations Chart\n[3] Animated Summary"))
        if 1 <= user_input <= 3:
            has_selected = True
            return
        else:
            print("Please make appropriate selection")

    elif variant == 3:
        user_input = int(input("[1] All Data\n[2] Data for Specific Country/Region"))
        if 1 <= user_input <= 2:
            has_selected = True
            return
    else:
        print("Please make appropriate selection")

else:
    user_input