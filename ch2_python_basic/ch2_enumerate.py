# not pythonic
for i in range(len(documents)):
    document = documents[i]
    do_something(i, document)

# also not pythonic
i = 0
for document in documents:
    do_something(i, document)
    i += 1

# most pythonic
for i, document in enumerate(documents):
    do_something(i, document)
