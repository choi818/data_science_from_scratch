#from __future__ import division
from collections import Counter

# global variables
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

friendships = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4),
                (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number_of_friends(user):
    return len(user["friends"])

total_connections = sum(number_of_friends(user) for user in users)

num_users = len(users)
avg_connections = total_connections / num_users

#print(avg_connections)

# sorting
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
print(sorted(num_friends_by_id, key=lambda x: x[1], reverse=True))

# recommending friends of friend
def friends_of_friend_ids_bad(user):
    return [foaf["id"] for friend in user["friends"] for foaf in friend["friends"]]

print(friends_of_friend_ids_bad(users[0]))

# delete duplication
def not_the_same(user, other_user):
    """만약 두 사용자의 id가 다르면 다른 사용자로 인식"""
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    """만약 other_user가 user["friends"]에 포함되지 않으면 친구가 아닌 것으로 간주
    즉, other_user를 not_the_same 함수를 사용해서
    user["friends"]에 포함된 사람과 다르다고 인식"""
    return all(not_the_same(friend, other_user) for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                    for friend in user["friends"]
                    for foaf in friend["friends"]
                    if not_the_same(user, foaf)
                    and not_friends(user, foaf))

print(friends_of_friend_ids(users[3]))
