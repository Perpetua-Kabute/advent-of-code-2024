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
            return (is_decreasing or is_increasing ) and is_differing_at_margin
        if report[i] > report [i+1]:
            is_decreasing = True
            is_differing_at_margin = (1 <= (report[i] - report[i+1]) <= 3)
            if is_increasing or is_differing_at_margin == False: 
                return False
        else:
            is_increasing = True
            is_differing_at_margin = (1 <= (report[i+1] - report[i]) <= 3)
            if is_decreasing or is_differing_at_margin == False:
                return False
    # return (is_increasing and is_differing_at_margin and is_decreasing == False) or (is_decreasing and is_differing_at_margin and is_increasing == False)

def is_gradual_after_removing_number(report):
    report_copy = report[:]

    if is_increasing_or_decreasing_gradually(report):
        return True
    else:
        for i in range(len(report)):
            print(f"i = {i} removed = {report_copy[i]}")
            report_copy.pop(i)
            if is_increasing_or_decreasing_gradually(report_copy):
                return True
            else:
                print(f"Report was not gradual  at this point. i = {i} report = {report_copy}")
                report_copy = report[:]
                
        return False
    
            
def is_gradual_dampened(report):
    return is_increasing_or_decreasing_gradually(report) or is_gradual_after_removing_number(report)


def find_safe_reports(reports):
    """
    param reports: list of lists
    return: Int the number of safe reports"""
    
    safe_reports = 0
    for report in reports:
        if is_gradual_dampened(report) == True:
            safe_reports = safe_reports + 1
    return safe_reports

reports = fetch_and_parse_reports()
print(find_safe_reports(reports))