import argparse
import sys
from environment import Environment
from base_agent import BaseAgent
import numpy as np
import matplotlib.pyplot as plt

class MineSweeper():
    BasicAgent = "base_agent"
    CSPAgent = "csp_agent"

    def __init__(self,
                 ground_dimension = None,
                 mine_density = None,
                 agent_name = None,
                 visual = False,
                 end_game_on_mine_hit = True,
                 bonus_uncertain_p = 0.0):
        self.ground_dimension = ground_dimension
        self.mine_density = mine_density
        self.agent_name = agent_name
        self.visual = visual
        self.end_game_on_mine_hit = end_game_on_mine_hit
        self.bonus_uncertain_p = bonus_uncertain_p
        self.use_probability_agent = False

        if self.bonus_uncertain_p > 0:
            self.use_probability_agent = True

    def create_environment(self):

        # Create the maze
        self.env = Environment(n = self.ground_dimension,
                               mine_density = self.mine_density,
                               visual = self.visual,
                               end_game_on_mine_hit = self.end_game_on_mine_hit)
        self.env.generate_environment()

    def run(self):

        # Use the agent to find mines in our mine-sweeper environment
        if self.agent_name == self.BasicAgent:
            self.mine_sweeper_agent = BaseAgent(env = self.env)


        self.mine_sweeper_agent.play()

        self.env.render_env(100)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'create AI agents to play mine-sweeper')
    parser.add_argument("-n", "--ground_dimension", default = 10)
    parser.add_argument("-a", "--agent_name", default = "base_agent")
    parser.add_argument("-d", "--mine_density", default = 0.1)
    parser.add_argument('-v', "--visual", default = False)
    parser.add_argument('-e', "--end_game_on_mine_hit", default = False)
    parser.add_argument("-bp", "--bonus_uncertain_p", default = 0)
    args = parser.parse_args(sys.argv[1:])

    mine_sweeper = MineSweeper(ground_dimension = int(args.ground_dimension),
                               mine_density = float(args.mine_density),
                               agent_name = args.agent_name,
                               visual = args.visual,
                               end_game_on_mine_hit = args.end_game_on_mine_hit,
                               bonus_uncertain_p = float(args.bonus_uncertain_p))

    mine_sweeper.create_environment()
    mine_sweeper.run()


