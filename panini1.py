plan = ['dance', 'dinner', 'movie', 'sleep', 'study']
print(plan[0])
print(plan[-1])
print(plan[0:3])
print(plan[::-1])
plan[1] = 'gaming'
print(plan[1])
plan.append('have fun')
plan.insert(0, 'be jolly')
print(plan)
plan.remove('sleep')
weekend = ['do dishes', 'walk around poznan']
plan.extend(weekend)
print(plan)