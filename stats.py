def get_num_words(input):
    num = 0
    counting = input.split()
    
    for x in counting:
        num += 1
    return num
def characterCounter(input):
    lowered = input.lower()
    count = {}
    for x in lowered:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    
    return count
def sort_on(dict):
    return dict["count"]
def prettifyDict(putin):
    listOfChar = []
    for x in putin:
        if x.isalpha():
            listOfChar.append({"char":x, "count":putin[x]})

    listOfChar.sort(reverse=True, key=sort_on)
    

    return listOfChar
