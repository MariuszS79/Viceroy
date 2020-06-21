import random
from random import randrange

#Welcoming intro
print("It is 105 AD, 6th year under administration of Marcus Ulpius,known as Trajan.")
print("The Roman Empire is at it's territorial peak.")
print("\n")

#asking player if he/she wants to play the game
startQuestion=input("Would you like to become Viceroy of Roman colony in Western Roman Empire?\n").lower()
if startQuestion!="yes":
    print("See you next year.")
    quit()
    
else:
    name=input("Your name: ")
    age=int(input("Age: "))
    if age<18:
        print("You are too young!")
        quit()
    elif age>96:
        print("Unfortunately Marcus Ulpius thinks, you are too old and infirm.")
        quit()
    else:
        print("\n")
        print("You were nominated. Good luck.")
        
#intro if the player has been chosen to run the Colony
print("\nYour administrator Gallius sends you regular reports.")
print("The decisions are yours.")
print("\nYour term of office is 10 years.")
print("\n")

#game starting parameters
start_colony_size=(randrange(50,150))
start_acres=(randrange(1000,2000))
start_grain=(randrange(2500,3500))
died=0
year_of_rule=1
seed=0

colony_size=start_colony_size #population of the colony
grain=start_grain #grain the colony has
acres=start_acres #area of the colony
seeds=seed #area you want to seed
alive=True

population_list=[]
death_list=[]
grain_list=[]
acres_list=[]

#main game loop
while alive:
    #stats for the year/beginning of each loop
    rats_ate=[0,0,0,(randrange(0,1000))]
    eaten_by_rats=random.choice(rats_ate)
    immigrants=(randrange(0,30))
    cost_of_acre=(randrange(17,28))
    harvestlist=[1,2,2,3,3,3,4,4,4,4,5,5,5,6,6,7]
    harvest=random.choice(harvestlist)
    
    #lists for statistics of colony performance

    population_list.append(colony_size)
    death_list.append(died)
    grain_list.append(grain)
    acres_list.append(acres)
    
    #summary of ruling after 10 years
    year_of_rule_list=[11,21,31,41,51,61,71,81,91,101,111,121,131,141,151,161,171,181,191,201]
    if year_of_rule in year_of_rule_list:
        rule_points_ten_years=[]
        if population_list[-11]<=population_list[-1]:
            rule_points_ten_years.append(1)
        if sum(death_list[-11:-1])==0:
            rule_points_ten_years.append(1)
        if grain_list[-11]<=grain_list[-1]:
            rule_points_ten_years.append(1)
        if acres_list[-11]<=acres_list[-1]:
            rule_points_ten_years.append(1)
        summary_of_rule_points_ten_years=sum(rule_points_ten_years)
        
        died_in_10_years=sum(death_list[-10:-1])
        print("\nDuring your term of office" ,died_in_10_years, "people died because of you, ")
        percentage=round(((died_in_10_years)/(population_list[-10])*100),2)
        print("it is",percentage,"% of the colony you took under administration.")
        land_per_person_before=((acres_list[-10])//(population_list[-10]))
        land_per_person_now=((acres_list[-1])//(population_list[-1]))
        print("On the beginning each colonist had",land_per_person_before, "acres of land, now each colonist has",land_per_person_now," acres.")
        
        if summary_of_rule_points_ten_years>=3:
            print("During your administration the colony has improved a lot.")
            print("Colonists want you to be their Viceroy for another 10 years.")
            ten_year_question=input("Do you agree?\n").lower()
            if ten_year_question !="yes":
                print("Thank you for your service.")
                quit()
        
        if summary_of_rule_points_ten_years==2:
            print("You could do better but it wasn't so bad. Part of your colonists want you to be their Viceroy for another 10 years.")
            ten_year_question=input("Do you agree?\n").lower()
            if ten_year_question !="yes":
                print("Thank you for your service.")
                quit()
        
        if summary_of_rule_points_ten_years==1:
            print("You were cruel like Neron. Colonists who survived your rules hate your style of administration.")
            quit()
        
        if summary_of_rule_points_ten_years==0:
            print("For such poor performance you were taken off office and sent to prison.")
            quit()
        print("-------------------")
        print("-------------------")
    
    #results of the year
    print("In",year_of_rule,"year",died,"people died and",immigrants," has joined the colony.")
    colony_size=((colony_size+immigrants)-died)
    print("Colony has",colony_size,"people and",acres,"acres of land.")
    print("Harvest was",harvest,"bushels of grain from acre.")
    grain=(harvest*seeds)+grain
    print("Rats ate",eaten_by_rats,"bushels of grain.")
    grain=grain-eaten_by_rats
    if grain<0:
        grain=0
    print("In your granaries you have",grain,"bushels of grain.")
    print("Land costs this year",cost_of_acre,"bushels for acre.")
    
    #define if you want to buy more land
    buy=int(input("How many acres would you like to buy?: "))
    while grain<=0:
        grain=0
        break
    while grain<(buy*cost_of_acre):
        buy=0
        print("Think about it, you have only",grain,"bushels of grain.")
        while grain<=0:
            grain=0
            buy=0
        buy=int(input("How many acres would you like to buy?: "))
        if grain>(buy*cost_of_acre):
            continue
        continue
    grain=grain-(buy*cost_of_acre)
    acres=acres+buy
    
    #define if you want to sell land
    sell=int(input("How many acres would you like to sell?: "))
    
    while acres<sell:
        sell=0
        print("Think about it, you have only",acres,"acres of land.")
        sell=int(input("How many acres would you like to sell?: "))
        if sell<=acres:
              break
    grain=grain+(sell*cost_of_acre)
    acres=acres-sell
    
    #provide grain to feed people
    print("You will have in your grannaries",grain,"bushels of grain.")
    food_for_people=int(input("How many bushels will you provide for food?: "))
    while food_for_people>grain:
        print("Think about it, you have only",grain,"bushels of grain.")
        food_for_people=int(input("How many bushels will you provide for food?: "))
        continue
    grain=grain-food_for_people
    if grain<=0:
        grain=0
        
    #area you want to seed
    print("You will have in your grannaries",grain,"bushels of grain.")
    seeds=int(input("How many acres would you like to seed?: "))
    while seeds>acres:
        print("Think about it, you have only",acres,"acres of land.")
        seeds=int(input("How many acres would you like to seed: "))
        continue
    
    while (seeds*2)>grain:
        print("Think about it, you have only",grain,"bushels of grain.")
        seeds=int(input("How many acres would you like to seed?: "))
        continue
    grain=grain-(seeds*2)
    
    #calculates how much land people of colony can seed
    how_much_seed=(colony_size*20)        
    while how_much_seed<seeds:
        print("But you have only",colony_size,"people to work in the fields ,who can seed",how_much_seed,"acres.")
        seeds=int(input("How many acres would you like to seed?: "))
        continue
    
    #calculates howmuch foodpeopleofyour colony need
    food_required=colony_size*20
    if food_required>(food_for_people):
        died=((food_required)-(food_for_people))//20
    else:
        died=0
    
    print("-------------------")
    print("-------------------")
    
    #Summary of the year after you made your decisions
    year_of_rule=year_of_rule+1
    if died>(colony_size//2):
        print("",died,"People died of hunger.")
        print("Angry people of your colony burn house of your administrator\nand hang him on a tree.\nThen they plunder grannaries.")
        print("For such bad administration\nyou are taken off office and sent to prison.")
        quit()
    
    #disease
    disease=randrange(1,4)
    if disease==1:
        print("Deadly disease spread across your colony.")
        print("Half of your people died.")
        print("\n")
        colony_size=(colony_size//2)
    
    #age of player after the year
    age=age+1
    
    #performance after 10 years of rule or at death
    rule_points_death=[]
    if population_list[0]<=population_list[-1]:
        rule_points_death.append(1)
    if death_list[0]<=death_list[-1]:
        rule_points_death.append(1)
    if grain_list[0]<=grain_list[-1]:
        rule_points_death.append(1)
    if acres_list[0]<=acres_list[-1]:
        rule_points_death.append(1)
    summary_of_rule_points_death=sum(rule_points_death)
    
    #death of player
    if 18<=age<=24:
        age18to24=randrange(1,1908)
        if age18to24==1:
            print("In",year_of_rule,"year you die suddenly.")
            if summary_of_rule_points_death>3:
                print("Your colonists are mourning for you, build you monuments and remember about you for generations.")
            elif summary_of_rule_points_death==2:    
                print("Your colonists are mourning for you.")
            elif summary_of_rule_points_death==1:
                print("Your colonists feel relieved.")
            elif summary_of_rule_points_death==0:
                print("Your colonist are thanking their gods, vandalise your grave and throw your corpse into river.")
            alive=False
            quit()
    if 25<=age<=34:
        age25to34=randrange(1,1215)
        if age25to34==1:
            print("In",year_of_rule,"year you die suddenly.")
            if summary_of_rule_points_death>3:
                print("Your colonists are mourning for you, build you monuments and remember about you for generations.")
            elif summary_of_rule_points_death==2:    
                print("Your colonists are mourning for you.")
            elif summary_of_rule_points_death==1:
                print("Your colonists feel relieved.")
            elif summary_of_rule_points_death==0:
                print("Your colonist are thanking their gods, vandalise your grave and throw your corpse into river.")
            alive=False
            quit()
    if 35<=age<=44:
        age35to44=randrange(1,663)
        if age35to44==1:
            print("In",year_of_rule,"year you die suddenly.")
            if summary_of_rule_points_death>3:
                print("Your colonists are mourning for you, build you monuments and remember about you for generations.")
            elif summary_of_rule_points_death==2:    
                print("Your colonists are mourning for you.")
            elif summary_of_rule_points_death==1:
                print("Your colonists feel relieved.")
            elif summary_of_rule_points_death==0:
                print("Your colonist are thanking their gods, vandalise your grave and throw your corpse into river.")
            alive=False
            quit()
    if 45<=age<=54:
        age45to54=randrange(1,279)
        if age45to54==1:
            print("In",year_of_rule,"year you die suddenly.")
            if summary_of_rule_points_death>3:
                print("Your colonists are mourning for you, build you monuments and remember about you for generations.")
            elif summary_of_rule_points_death==2:    
                print("Your colonists are mourning for you.")
            elif summary_of_rule_points_death==1:
                print("Your colonists feel relieved.")
            elif summary_of_rule_points_death==0:
                print("Your colonist are thanking their gods, vandalise your grave and throw your corpse into river.")
            alive=False
            quit()
    if 55<=age<=64:
        age55to64=randrange(1,112)
        if age55to64==1:
            print("In",year_of_rule,"year you die suddenly.")
            if summary_of_rule_points_death>3:
                print("Your colonists are mourning for you, build you monuments and remember about you for generations.")
            elif summary_of_rule_points_death==2:    
                print("Your colonists are mourning for you.")
            elif summary_of_rule_points_death==1:
                print("Your colonists feel relieved.")
            elif summary_of_rule_points_death==0:
                print("Your colonist are thanking their gods, vandalise your grave and throw your corpse into river.")
            alive=False
            quit()
    if 65<=age<=74:
        age65to74=randrange(1,42)
        if age65to74==1:
            print("In",year_of_rule,"year you die suddenly.")
            if summary_of_rule_points_death>3:
                print("Your colonists are mourning for you, build you monuments and remember about you for generations.")
            elif summary_of_rule_points_death==2:    
                print("Your colonists are mourning for you.")
            elif summary_of_rule_points_death==1:
                print("Your colonists feel relieved.")
            elif summary_of_rule_points_death==0:
                print("Your colonist are thanking their gods, vandalise your grave and throw your corpse into river.")
            alive=False
            quit()
    if 75<=age<=84:
        age75to84=randrange(1,15)
        if age75to84==1:
            print("In",year_of_rule,"year you die suddenly.")
            if summary_of_rule_points_death>3:
                print("Your colonists are mourning for you, build you monuments and remember about you for generations.")
            elif summary_of_rule_points_death==2:    
                print("Your colonists are mourning for you.")
            elif summary_of_rule_points_death==1:
                print("Your colonists feel relieved.")
            elif summary_of_rule_points_death==0:
                print("Your colonist are thanking their gods, vandalise your grave and throw your corpse into river.")
            alive=False
            quit()
    if age>85:
        age85up=randrange(1,6)
        if age85up==1:
            print("In",year_of_rule,"year you die suddenly.")
            if summary_of_rule_points_death>3:
                print("Your colonists are mourning for you, build you monuments and remember about you for generations.")
            elif summary_of_rule_points_death==2:    
                print("Your colonists are mourning for you.")
            elif summary_of_rule_points_death==1:
                print("Your colonists feel relieved.")
            elif summary_of_rule_points_death==0:
                print("Your colonist are thanking their gods, vandalise your grave and throw your corpse into river.")
            alive=False
            quit()
    
    
    
        print("-------------------")
        print("-------------------")
        
    
    
    continue