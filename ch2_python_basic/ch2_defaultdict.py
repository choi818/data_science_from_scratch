from collections import defaultdict

dd_list = defaultdict(list) # list() creates empty list
dd_list[2].append(1)        # dd_list implies {2: [1]}

dd_dict = defaultdict(dict)         # dict() creates empty dict
dd_dict["Joel"]["City"] = "Seattle" # {"Joel": {"City": "Seattle"}}

dd_pair = defaultdict(lambda: [0,0])
dd_pair[2][1] = 1   # dd_pair implies {2: [0,1]}
