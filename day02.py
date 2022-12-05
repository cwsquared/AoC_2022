from input_prep import file_to_str_list
from results_out import solution


def part1(data):
    part = "1"
    total_score = 0
    score_dict = {
        'A X': 4,  # Rock Rock
        'A Y': 8,  # Rock Paper
        'A Z': 3,  # Rock Scissors
        'B X': 1,  # Paper Rock
        'B Y': 5,  # Paper Paper
        'B Z': 9,  # Paper Scissors
        'C X': 7,  # Scissors Rock
        'C Y': 2,  # Scissors Paper
        'C Z': 6   # Scissors Scissors
    }
    
    for line in data:
        total_score += score_dict.get(line)

    solution(day, part, total_score)


def part2(data):
    part = "2"
    total_score = 0
    score_dict = {
        'A X': 3,  # Rock Scissors     Lose
        'A Y': 4,  # Rock Rock         Draw
        'A Z': 8,  # Rock Paper        Win
        'B X': 1,  # Paper Rock
        'B Y': 5,  # Paper Paper
        'B Z': 9,  # Paper Scissors
        'C X': 2,  # Scissors Paper
        'C Y': 6,  # Scissors Scissors
        'C Z': 7   # Scissors Scissors
    }
    
    for line in data:
        total_score += score_dict.get(line)

    solution(day, part, total_score)


if __name__ == "__main__":
    day = "2"
    
    data = file_to_str_list("input02.txt")
    
    part1(data)
    part2(data)