
def fetch_and_parse_data():
    list1 = []
    list2 = []
    """
    input is a long ass file with 2 columns. 
    I want to get the lines
    then for each line split the two where there is a space
    """
    with open("input.txt", "r") as f:
        """
        read the content with f.read()
        read each line by looping """
        # if i was writing to a file this is how I would do it
        # f.write("This is a new file")
        # print("replaced",file=f)
        for line in f:
            col1, col2 = line.split("   ")
            list1.append(int(col1))
            list2.append(int(col2))
    return list1, list2


def find_distance(list1, list2):
    """
    param list1: list of Int - the first list of location ids
    param list2: list of Int - the second list of location ids
    return: Int - the total distance between the lists

    find the total distance by pairing the smallest numbers in the 2 list and finding the difference between them. the sign does not matter. 
    """
    list1.sort()
    list2.sort()
    distance = 0
    for i in range(len(list1)):
        distance = distance + abs(list1[i] - list2[i])
    return distance
def find_similarity_score(list1, list2):
    """
    param list1: list of ints - the left list
    param list2: list of ints - the rigit list
    return Int- the total similarity score
    similarity score - how often each number from the lest list appears in the right list
    to get the total similarity score add up each number from the left list after multiplying it by the number of times it appears on the right list

    """
    similarity_score = 0
    for number in list1:
        similarity_score += (number * list2.count(number))
    return similarity_score

if __name__ == "__main__":
    list1, list2 = fetch_and_parse_data()
    print(find_similarity_score(list1, list2))