def fetch_and_parse_reports():
    reports: list[int] = []
    with open("input.txt", "r") as f:
        for line in f:
            line.replace("\n","")
            report = list(line.split(" "))
            reports.append(list(map(int, report)))

    # print(reports)
    print(len(reports))
    return reports

def is_increasing_or_decreasing_gradually(report):
    """
    param report: list of int - the list of numbers
    return: Boolean if the list is increasing or decreasing return true
    """
    is_increasing = False
    is_differing_at_margin = False
    is_decreasing = False
    for i in range(len(report)):
        if i == len(report) - 1:
            break 
        if report[i] > report [i+1]:
            is_decreasing = True
            is_differing_at_margin = (1 <= (report[i] - report[i+1]) <= 3)
            if is_increasing or is_differing_at_margin == False: 
                break
        else:
            is_increasing = True
            is_differing_at_margin = (1 <= (report[i+1] - report[i]) <= 3)
            if is_decreasing or is_differing_at_margin == False:
                break

        # if is_differing_at_margin == False:
        #         break
    
    return (is_increasing and is_differing_at_margin and is_decreasing == False) or (is_decreasing and is_differing_at_margin and is_increasing == False)


def is_increasing_or_decreasing_gradually_dampened(report, has_removed_element):
    """
    param report: list of int - the list of numbers
    return: Boolean if the list is increasing or decreasing return true
    """
    is_increasing = False
    is_differing_at_margin = False
    is_decreasing = False
    for i in range(len(report)):
        if i == len(report) - 1:
            break 
        if report[i] > report [i+1]:
            is_decreasing = True
            is_differing_at_margin = (1 <= (report[i] - report[i+1]) <= 3)
            if is_increasing or is_differing_at_margin == False: 
                if(has_removed_element):
                    return False
                else:
                    if i == 1 and report[i+1] < report[i+2]:
                        report.remove(report[0])
                    else:
                        report.remove(report[i + 1])
                    print(report)
                    return is_increasing_or_decreasing_gradually_dampened(report, True)
                          
        elif report[i] < report [i+1] :
            is_increasing = True
            is_differing_at_margin = (1 <= (report[i+1] - report[i]) <= 3)
            if is_decreasing or is_differing_at_margin == False:
                if(has_removed_element):
                    return False
                else:
                    report.remove(report[i + 1])
                    print(report)
                    return is_increasing_or_decreasing_gradually_dampened(report, True)  
        else:
            if(has_removed_element):
                return False
            else:
                report.remove(report[i])
                print(report)
                return is_increasing_or_decreasing_gradually_dampened(report, True)

        
                    

    return (is_increasing and is_differing_at_margin and is_decreasing == False) or (is_decreasing and is_differing_at_margin and is_increasing == False)

# def do_second_iteration(report,element_to_remove, has_removed_element):
#     if(has_removed_element == False):
#         is_increasing_or_decreasing_gradually_dampened([report.remove(element_to_remove)])


def find_safe_reports(reports):
    """
    param reports: list of lists
    return: Int the number of safe reports"""
    
    safe_reports = 0
    for report in reports:
        if is_increasing_or_decreasing_gradually_dampened(report, False) == True:
            safe_reports = safe_reports + 1
    return safe_reports

reports = fetch_and_parse_reports()
print(find_safe_reports(reports))
# is_increasing_or_decreasing_gradually([8,6,4,4,1])