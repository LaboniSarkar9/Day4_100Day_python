# list - store data
states_of_america = ["Delaware", "Pennsylvania", "New jersey", "Georgia", "Connection" ]
print(states_of_america[0])
print(states_of_america[1])
print(states_of_america[2])
print(states_of_america[3])
print(states_of_america[-1])
print(states_of_america[-2])

# replace
states_of_america[1] = "pencilvania"
print(states_of_america)

# append at the end
states_of_america.append("Angelaland")
print(states_of_america)

# extend : combine 2 lists
states_of_america.extend(["Angelaland","jack Bauer Land"])
print(states_of_america)