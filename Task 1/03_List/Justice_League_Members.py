#1.Calculate the number of members in the Justice League.

justice_league = ["Superman", "Batman", "WonderWoman", "Flash", "Aquaman", "Green Lantern"]
print("The Number of Member is",len(justice_league))

#Output=The Number of Member is 6

#2.Batman recruited Batgirl and Nightwing as new members.
#Add them to your list.

justice_league = ["Superman", "Batman", "WonderWoman", "Flash", "Aquaman", "Green Lantern"]
new_member="Nightwing","Batgirl"
justice_league.extend(new_member)

print(justice_league)

#Output=['Superman', 'Batman', 'WonderWoman', 'Flash', 'Aquaman', 'Green Lantern', 'Nightwing', 'Batgirl']


#3.Wonder Woman is now the leader of the Justice League.
#Move her to the beginning of the list.


justice_league = ["Superman", "Batman", "WonderWoman", "Flash", "Aquaman", "Green Lantern"]
justice_league[justice_league.index("WonderWoman")], justice_league[0] = justice_league[0], justice_league[justice_league.index("WonderWoman")]
print(justice_league)


#Output=['WonderWoman', 'Batman', 'Superman', 'Flash', 'Aquaman', 'Green Lantern']


#4.Aquaman and Flash are having conflicts, and you need to
#separate them. Choose either "Green Lantern" or "Superman"
#and move them in between Aquaman and Flash.

justice_league = ['WonderWoman', 'Batman', 'Superman', 'Flash', 'Aquaman', 'Green Lantern']
Flash=(justice_league.index("Flash"))
Aquaman=(justice_league.index("Aquaman"))
if Flash<Aquaman:
    justice_league[justice_league.index('Flash')],justice_league[justice_league.index('Superman')]=justice_league[justice_league.index('Superman')],justice_league[justice_league.index('Flash')]
print(justice_league)


#Output=['WonderWoman', 'Batman', 'Flash', 'Superman', 'Aquaman', 'Green Lantern']


#5.The Justice League faced a crisis, and Superman decided to
#assemble a new team. Replace the existing list with the following
#new members: "Cyborg", "Shazam", "Hawkgirl", "Martian
#Manhunter", "Green Arrow".

justice_league = ['Superman', 'Batman', 'WonderWoman', 'Flash', 'Aquaman', 'Green Lantern', 'Nightwing', 'Batgirl']
New_Team = ['Cyborg', "Shazam", 'Hawkgirl', 'Martian Manhunter', 'Green Arrow']

justice_league.clear()
justice_league.extend(New_Team)
print(justice_league)

#Output=['Cyborg', 'Shazam', 'Hawkgirl', 'Martian Manhunter', 'Green Arrow']


#6.Sort the Justice League alphabetically. The hero at the 0th
#index will become the new leader.

print(sorted(justice_league))
print("Leader is=", justice_league[0])

#Output=['Cyborg', 'Green Arrow', 'Hawkgirl', 'Martian Manhunter', 'Shazam']
#Output=Leader is Cyborg