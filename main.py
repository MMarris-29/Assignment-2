"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semCost = annual_cost / SEMESTERS_PER_YEAR # 2
    return semCost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    monthCost = annual_cost / MONTHS_PER_YEAR
    return monthCost


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    dayCost = annual_cost / (CLASS_DAYS_PER_SEMESTER * SEMESTERS_PER_YEAR)
    return dayCost


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    perCredit = annual_cost / (float(credits) * 2) # not sure if i need the float but im doing it just in case
    return perCredit


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    #perClass = annual_cost / (CS1430_MEETINGS_PER_SEMESTER * SEMESTERS_PER_YEAR)
    #perClass = (annual_cost / (CLASS_DAYS_PER_SEMESTER * SEMESTERS_PER_YEAR)) / CS1430_MEETINGS_PER_SEMESTER
    perClass = ((annual_cost / credits) * CS1430_CREDITS) / (CS1430_MEETINGS_PER_SEMESTER * SEMESTERS_PER_YEAR) # ?????????????????
    return perClass

def trips_per_cs1430(annual_cost, trips):
    perTrip = (cost_per_class(annual_cost, credits)) // trips # does this work????
    if perTrip <= 400:
        worthIt = False
    else:
        worthIt = True
    return worthIt

# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    totalCost = float(input("What is your total cost of college this year? (please enter only numbers)  $"))
    # Then ask for the credits this semester.
    totalCredits = int(input("What is your total credits this year? (please enter only numbers)  "))

    while 1==1:
        # Show your menu here.
        sem_cost = 0.00
        month_cost = 0.00
        day_cost = 0.00
        per_credit_cost = 0.00
        how_many_trips = 0

        print("1 - Per semester")
        print("2 - Per month")
        print("3 - Per class day")      
        print("4 - Per credit")
        print("5 - Per CS 1430 class")
        print("6 - Is It Worth It?") # custom one i have to make
        print("Q - Quit")

        # Menu:
        choice = input("Choose an option: ")

        if choice == "1": # or "one" or "One":
            sem_cost = cost_per_semester(totalCost)
            print(f"One semester at Platteville costs ${sem_cost:.2f}!") #something is missing or broken here -- nvm it's the words

        elif choice == "2": # or "two" or "Two":
            month_cost = cost_per_month(totalCost)
            print(f"One month at Platteville costs ${month_cost:.2f}!")
        elif choice == "3": # or "three" or "Three":
            day_cost = cost_per_day(totalCost)
            print(f"One day at Platteville costs ${day_cost:.2f}!")
        elif choice == "4": # or "four" or "Four":
            per_credit_cost = cost_per_credit(totalCost, totalCredits)
            print(f"One credit at Platteville costs ${per_credit_cost:.2f}!")
        elif choice == "5": # or "five" or "Five":
            per_class_cost = cost_per_class(totalCost, totalCredits)
            print(f"Each individual CS1430 class day costs ${per_class_cost:.2f}!")
        elif choice == "6": # or "six" or "Six":
            yesOrNo = input("Would you want to go to Disney world? Answer with Yes or No: ")
            while True:
                if yesOrNo == "Yes" or yesOrNo == "yes":
                    how_many_trips = int(input("How many times would you go to Disney World? "))
                    if how_many_trips <= 2:
                        print(f"{how_many_trips}? You're thinking too small, so for now I'd say your money is in safe hands.")
                        print("College is worth it.")
                        break
                    else:
                        worth_it = trips_per_cs1430(totalCost, how_many_trips)
                        if worth_it == True:
                            print("Disney is too expensive. Especially when you could be at CS1430 instead.")
                            print("College is worth it.")
                            break
                        else:
                            print(f"You could go to Disney {how_many_trips} times for under $400 each!? Yeah, you're wasting your money.")
                            print("College is NOT worth it.")
                            break
                    break
                elif yesOrNo == "No" or yesOrNo == "no":
                    print("Really? Well, in that case, I'd say your money is in safe hands.")
                    print("College is worth it.")
                    break
                else:
                    print("That's not a Yes or No response, pal. Back to the menu with you.")
                    break
        elif (choice == "Q") or (choice == "q"): # fixed it
            break # quits loop
        else:
            print("Sorry. That isn't an option. Please select a number, or type Q to quit.")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
