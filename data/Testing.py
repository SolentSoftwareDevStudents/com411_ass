from tui import *


while True:

    main_variant = menu()

    if main_variant == 1:
        progress("data processing process", 0)
        processing_menu = menu(1)
        if processing_menu == 1:
            progress("record retrieval process", 0)
            # process.py function
            progress("record retrieval process", 100)
        elif processing_menu == 2:
            progress("records retrieval process", 0)
            # progress.py function
            # display_records()
            progress("records retrieval process", 100)
        elif processing_menu == 3:
            progress("grouping process", 0)
            # process.py function here
            # display_records()
            progress("grouping process", 100)
        elif processing_menu == 4:
            progress("summary process", 0)
            # process.py function
            # display_records()
            progress("summary process", 100)
        progress("data processing process", 100)

    elif main_variant == 2:
        progress("data visualisation operation", 0)
        visualisation_menu = menu(2)
        if visualisation_menu == 1:
            progress("pie chart creation process", 0)
            # visual.py function
        progress("pie chart creation process", 100)
        if visualisation_menu == 2:
            progress("observations chart creation process", 0)
            # visual.py function
        progress("observations chart creation process", 100)
        if visualisation_menu == 3:
            progress("animation creation process", 0)
            # visual.py function
            progress("animation creation process", 100)
        progress("data visualisation operation", 0)

    elif main_variant == 3:
        export_menu = menu(3)
        if export_menu == 1:
            progress("export all process", 0)
            # OOP
            progress("export all process", 100)
        elif export_menu == 2:
            progress("specific data export process", 0)
            # OOP
            progress("specific data export process", 100)

    elif main_variant == 4:
        break


    else:
        error("Invalid selection!!!")
        print()