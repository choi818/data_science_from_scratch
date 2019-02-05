empty_dict = {}
empty_dict2 = dict()
grades = {"Joel": 80, "Tim": 95}        # example of dictionary

joels_grade = grades["Joel"]            # result: 80

try:
    kates_grade = grades["Kate"]
except KeyError:
    print('no grade for Kate')

# in
joel_has_grade = "Joel" in grades       # True
kate_has_grade = "Kate" in grades       # False

# get method
joels_grade = grades.get("Joel", 0)     # result: 80
kates_grade = grades.get("Kate", 0)     # result: 0
no_ones_grade = grades.get("No One")    # None

# new align
grades["Tim"] = 99          # replace
grades["Kate"] = 100        # append
num_students = len(grades)  #result: 3

# all keys
tweet = {
    "user": "joelgrus",
    "text": "Data Science is Awesome",
    "retweet_count": 100,
    "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

"user" in tweet_keys        # True, but slow
"user" in tweet             # more pythonic
"joelgrus" in tweet_values  # True