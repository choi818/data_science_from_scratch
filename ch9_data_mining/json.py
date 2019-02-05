import json

serialized = """
            {"title": "Data Science Book",
             "author": "Joel Grus",
             "publicationYear": 2014,
             "topics": ["data", "science", "data science"]}
             """

# JSON을 파이썬 dict로 파싱
deserialized = json.loads(serialized)
if "data science" in deserialized["topics"]:
    print(deserialized)
