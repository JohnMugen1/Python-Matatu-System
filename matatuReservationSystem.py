#take user details
def details():
    user_details = {}
    global name
    global location
    name = input("What is your name?:")
    location = input("Where are you now?:")
    user_details.update({name:location})
    return user_details

#Guide the user on available services
def guideUser():
    customer = details()
    for name in customer.keys():
        print("\nWelcome!",name,".Explore our Services...")
    print(" " * 4 ," 1.Book a trip\n"," " * 4,"2.Check for available trips")
    return int(input("How can we assist you?:"))

#checking the trip status
def trip_details():
    trip_det = [[True for i in range(2)] for j in range(2)]
    trip_det[0][1] = False
    total_trip = 0
    for i in range(2):
        for j in range(2):
            if trip_det[i][j] == True:
                total_trip += 1
    return total_trip   

#making payment by the customer
def trip_payment():
    print("\nPayment of =/2500 via m-pesa?\n1.Yes\n2.No")
    return int(input())

#rating the travelSafe services
def rateUs():
    rating = int(input("\n\nRate our services in range 1-10?:\n\n"))
    if rating >= 0 and rating <= 10:
        if rating > 5:
            print("\n***Thank you! for trusting us.We are Family***")
        else:
            print("\n***Thank you! for your feedback.***")
    else:
            print("\n***Rating gone wrong!!!***")
            rateUs()

#processing payment 
def payConfirmation():
    payment = trip_payment()
    if payment == 1:
        print("\nCongratulations!",name,"*****")
        print("\nSuccessfully registered for a trip!\nThank you! for choosing us.")
        rateUs()
    elif payment == 2:
        print("\nSuccessfully canceled the registration process.Thank you!")
    else:
        payConfirmation()

#when user finds there are trips and decides to continue to book
def explore():
    number_of_trips = trip_details()
    if number_of_trips > 0:
         option = int(input("\nBook a trip for me?\n1.Yes\n2.No\n::"))
         if option == 1:
            print("\nWelcome back! ",name,"\nPayment process...")
            payConfirmation()
         elif option == 2:
            print("Thank you! for being part of us.")
         else:
            print("An Error! occured.Kindly try again later!")
    

#the main function
def operation():
    user_option = guideUser()
    if location == "EMBU" or location == "Embu" or location == "embu":
        number_of_trips = trip_details()
        if user_option == 1:
          if number_of_trips > 0:
             payConfirmation()
          else:
             print("No trips at the moment\nStay connected with us!")
        elif user_option == 2:
           print("\nTotal Remaining number of trips = ",number_of_trips)
           explore()
        else:
           operation()  
    else:
        print("Sorry!",name,"We only serve Embu residence.\nSoon we are reaching other Areas.")

#handling invokation with exceptions
try:
    operation()
except (ValueError,TypeError,AttributeError,ZeroDivisionError):
    print("An Error! occured,kindly re-check and try again later!!")


            




