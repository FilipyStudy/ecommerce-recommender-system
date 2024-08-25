from data_visuallization import data_visuallization as dtv
import socket


#TODO: Create a socket process to handle requests
#Init the script
while True:
    print("1 for Data Visualization \t 2 for training the machine learning")
    
    try:
        #Get a choice from the user
        choice = int(input('> '))
        if choice == 1:
            print("1 for the train data \t 2 for the test data")
            second_choice = int(input('> '))

            #Select what database shoud be used
            if second_choice == 1:
                dtv.show_pie_chart('train')
            elif second_choice == 2:
                dtv.show_pie_chart('test')
            else:
                print("Select a correct answer!")
        #TODO: will be used to run the ML script in the future
        elif choice == 2:
            print('In development!')

    #Raise an exception if an error occurs
    except Exception as e:
        print("Verify the number of your choice and try again")
        print(f"Error {e}")