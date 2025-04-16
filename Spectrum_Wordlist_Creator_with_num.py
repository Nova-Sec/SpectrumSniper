#! /usr/bin/env python3
import time
import sys

write_block = []
start_time = time.time()

def run_time_calc():
    run_time = time.time() - start_time
    return run_time


def write_combined_words(adjectives_file, nouns_file, number_file, output_file):
    with open(adjectives_file, "r") as adj_file, \
         open(nouns_file, "r") as noun_file, \
         open(number_file, "r") as num_file, \
         open(output_file, "a") as out_file:
            
        adjectives = [adj.strip() for adj in adj_file.readlines()]
        nouns = [noun.strip() for noun in noun_file.readlines()]
        numbers = [num.strip() for num in num_file.readlines()]

        num_combinations = len(adjectives) * len(nouns) * len(numbers)
        current_combination = 0
        
        for adj in adjectives:
            for noun in nouns:
                for num in numbers:
                    #out_file.write(adj + noun + num + "\n")
                    write_block.append(adj + noun + num + "\n")
                    if len(write_block) >= 10000:
                        for i in write_block:
                            out_file.write(i)
                        write_block.clear()

                    current_combination += 1
                    run_per_sec = current_combination / run_time_calc()
                    run_per_sec = int(run_per_sec)
                    time_left = (num_combinations - current_combination) / run_per_sec
                    time_hours = (time_left / 60) / 60
                    time_hours = int(time_hours)
                    time_left = int(time_left)
                    progress_pct = int(current_combination / num_combinations * 100)
                    print(f"Processed {current_combination}/{num_combinations} combinations ({progress_pct}%) , {run_per_sec}/s , {time_hours}hours", end="\r")
                    sys.stdout.flush()
                    


if __name__ == "__main__":
    adjectives_file = "adjectives.txt"
    nouns_file = "nouns.txt"
    output_file = "output.txt"
    number_file = "numbers.txt"

    write_combined_words(adjectives_file, nouns_file, number_file, output_file)
    print("\nDone!") 