import re

def get_content():
    ordering_rules = []
    update_pages = []
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            rule = re.match("\d+\|\d+", line)
            if rule != None:
                first, second = line.split('|')
                ordering_rules.append((first, second))
            else:
                if line != '':
                    row = list(line.split(','))
                    update_pages.append(row)
    return ordering_rules, update_pages


def arrange_order_rules_per_key(order_rules):
    order_rules_dictionary = {}
    for pair in order_rules:
        if order_rules_dictionary.__contains__(pair[0]):
            order_rules_dictionary[pair[0]].add(pair[1])
        else:
            order_rules_dictionary.update({pair[0]: {pair[1]}})
        if order_rules_dictionary.__contains__(pair[1]) == False:
            order_rules_dictionary.update({pair[1]: set()})
    return order_rules_dictionary
def is_page_in_right_order(order_rules_dictionary,update_row):
    updates_set =  set()
    is_ordered_correcty = True
    for page in update_row:
        print(order_rules_dictionary[page])
        if order_rules_dictionary[page] - updates_set != order_rules_dictionary[page]:
            is_ordered_correcty = False
            break
        else:
            updates_set.add(page)
    return is_ordered_correcty
def find_right_ordered_updates(order_rules_dictionary, update_pages):
    ordered_pages = []
    unordered_pages =[]
    for row in update_pages:
        if is_page_in_right_order(order_rules_dictionary, row):
            ordered_pages.append(row)
        else:
            unordered_pages.append(row)
    return ordered_pages, unordered_pages

def order_page_correctly( order_rules_dictionary, unordered_page):
    updates_set =  set()
    unordered_page_copy = unordered_page[:]
    correcty_ordered = False
    while not correcty_ordered: 
        for i in range(len(unordered_page_copy)):
            if order_rules_dictionary[unordered_page_copy[i]] - updates_set != order_rules_dictionary[unordered_page_copy[i]]:
                correcty_ordered = True
                if i == 0:
                    break
                page_temp = unordered_page_copy[i - 1]
                unordered_page_copy[i - 1] = unordered_page_copy[i]
                unordered_page_copy[i] = page_temp
                updates_set = set()
                print(unordered_page_copy)
                correcty_ordered = False
                break
            else:
                updates_set.add(unordered_page_copy[i])
                correcty_ordered = True
            
        print(correcty_ordered)
    return unordered_page_copy

def find_corrected_pages(order_rules_dictionary,unordered_pages):
    ordered_pages = []
    for row in unordered_pages:
        ordered_pages.append(order_page_correctly(order_rules_dictionary,row))
    return ordered_pages

def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])
    
def find_sum_of_middle_nums(ordered_pages):
    sum_of_middle_number = 0
    for row in ordered_pages:
        sum_of_middle_number += int(findMiddle(row))
    return sum_of_middle_number

if __name__ == "__main__":
    ordering_rules, update_pages = get_content()
   
    arranged_rules = arrange_order_rules_per_key(ordering_rules)
    ordered_pages, unordered_pages = find_right_ordered_updates(arranged_rules, update_pages)
    ordered_pages = find_corrected_pages(arranged_rules, unordered_pages)
    print(find_sum_of_middle_nums(ordered_pages))

    