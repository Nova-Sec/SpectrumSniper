#!/bin/python3
def write_combined_words(adjectives_file, nouns_file, output_file):
    with open(adjectives_file, "r") as adj_file, \
         open(nouns_file, "r") as noun_file, \
         open(output_file, "w") as out_file:
            
        adjectives = [adj.strip() for adj in adj_file.readlines()]
        nouns = [noun.strip() for noun in noun_file.readlines()]

        num_combinations = len(adjectives) * len(nouns)
        current_combination = 0

        for adj in adjectives:
            for noun in nouns:
                out_file.write(adj + noun + "\n")

                current_combination += 1
                progress_pct = int(current_combination / num_combinations * 100)
                print(f"Processed {current_combination}/{num_combinations} combinations ({progress_pct}%)", end="\r")


if __name__ == "__main__":
    adjectives_file = "adjectives.txt"
    nouns_file = "nouns.txt"
    output_file = "output.txt"

    write_combined_words(adjectives_file, nouns_file, output_file)
    print("\nDone!") 