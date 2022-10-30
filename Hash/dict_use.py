

# Dictionary


a = dict(one=1, two=2, three=(3,2))

"""
    python dictionary key는 중복 불가능하다. 
    값은 중복될 수 있지만, 키가 중복되면 마지막 값으로 덮어 씌워진다. 
    
"""
print("length : {}".format(len(a)))

"""
    dict => key - value 
    하나의 key에 하나의 value만 가진다.
    

"""

participant = ['one', 'two', 'one', 'three']


completion = ['one', 'two', 'three']

# p_dict = dict(zip(participant, [[0] for _ in range(len(participant))]))
p_dict = dict()

# completion for문 -> 참가 여부 정함.
for player in participant:
    if player in p_dict:
        p_dict[player].append(0)
    else:
        p_dict[player] = [0]

for player in completion:
    if player in p_dict:
        p_dict[player].pop(0)

