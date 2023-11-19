import argparse

from logic import run_simulation
from utils import parse_file


def game_of_life(state_file_path: str, generations: int):
    matrix = parse_file(state_file_path)
    run_simulation(matrix, generations) 


def parse_args():
    # `state_file_path`
    #   Path to a file containing the initial state for the simulation. You may choose the format of the file.
    # `generations``
    #   The number of generations to run the simulation.
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument('--state_file_path', type=str, default='./initial_state.txt', help='Path to a file containing the initial state for the simulation.')
    parser.add_argument('--generations', type=int, default=1000, help='The number of generations to run the simulation.')
    return parser.parse_args()


def main():
    args = parse_args()
    game_of_life(args.state_file_path, args.generations)


if __name__ == "__main__":
    main()
