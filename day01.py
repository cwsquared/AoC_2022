from input_prep import file_to_str_list
from results_out import solution


def part1(data):
    part = "01"
    calorie_loads = []
    calories = 0
    
    for line in data:
        if line == '':
            calorie_loads.append(calories)
            calories = 0
        else:
            calories += int(line)

    solution(day, part, max(calorie_loads))


def part2(data):
    part = "02"
    calorie_loads = []
    calories = 0
    
    for line in data:
        if line == '':
            calorie_loads.append(calories)
            calories = 0
        else:
            calories += int(line)
    
    sorted_loads = calorie_loads.sort(reverse=True)        
    top_three_total = calorie_loads[0] + calorie_loads[1] + calorie_loads[2]

    solution(day, part, top_three_total)


if __name__ == "__main__":
    day = "01"
    
    data = file_to_str_list("input01.txt")
    
    part1(data)
    part2(data)