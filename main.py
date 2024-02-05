from typing import Optional, List
import sys

def extract_player_name(line: str) -> Optional[str]:
    keywords = ['MVP++', 'MVP+', 'VIP+', 'VIP', 'YOUTUBER']
    return next((parts[1].split()[0] for keyword in keywords if len(parts := line.split(keyword)) > 1), None)

def main():
    path = 'players/' + (sys.argv[1] if len(sys.argv) > 1 else 'players.txt')
    with open(path, 'r', errors='ignore') as file:
        player_names = set([name for line in file if (name := extract_player_name(line))])
    print(f'\n{len(player_names)} players:\n')
    for name in player_names:
        print(name, end=' ')
    print('\n')

if __name__ == "__main__":
    main()