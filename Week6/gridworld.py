import gym
from gym import spaces

import numpy as np
import random
from copy import deepcopy


class gridworld_custom(gym.Env):

    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    def __init__(self, *args, **kwargs):
        super(gridworld_custom, self).__init__()

        self.current_step = 0

        self.reward_range = (-10, 100)

        self.action_space = spaces.Discrete(2)

        self.observation_space = spaces.Box(low=np.array(
            [0, 0]), high=np.array([4, 4]), dtype=np.int64)

        self.target_coord = (4, 4)
        self.death_coord = [(3, 1), (4, 2)]

    def Reward_Function(self, obs):

        if (obs[0] == self.target_coord[0] and obs[1] == self.target_coord[1]):
            return 20
        elif (obs[0] == self.death_coord[0][0] and obs[1] == self.death_coord[0][1]) or \
                (obs[0] == self.death_coord[1][0] and obs[1] == self.death_coord[1][1]):
            return -10
        else:
            return -1

        return 0

    def reset(self):
        self.current_step = 0

        self.prev_obs = [random.randint(0, 4), random.randint(0, 4)]

        if (self.prev_obs[0] == self.target_coord[0] and self.prev_obs[1] == self.target_coord[1]):

            return self.reset()

        return self.prev_obs

    def step(self, action):

        action = int(action)

        self.current_step += 1

        obs = deepcopy(self.prev_obs)

        if(action == 0):
            if(self.prev_obs[0] < 4):
                obs[0] = obs[0] + 1
            else:
                obs[0] = obs[0]

        if(action == 1):
            if(self.prev_obs[0] > 0):
                obs[0] = obs[0] - 1
            else:
                obs[0] = obs[0]

        if(action == 2):
            if(self.prev_obs[1] < 4):
                obs[1] = obs[1] + 1
            else:
                obs[1] = obs[1]

        if(action == 3):
            if(self.prev_obs[1] > 0):
                obs[1] = obs[1] - 1
            else:
                obs[1] = obs[1]

        reward = self.Reward_Function(obs)

        if (obs[0] == self.target_coord[0] and obs[1] == self.target_coord[1]) or (self.current_step >= 250):
            done = True
        else:
            done = False

        self.prev_obs = obs

        return obs, reward, done, {}

    def render(self, mode='human', close=False):

        for i in range(0, 5):
            for j in range(0, 5):
                if i == self.prev_obs[0] and j == self.prev_obs[1]:
                    print("*", end=" ")
                elif i == self.target_coord[0] and j == self.target_coord[1]:
                    print("w", end=" ")
                elif (i == self.death_coord[0][0] and j == self.death_coord[0][1]) or \
                     (i == self.death_coord[1][0] and j == self.death_coord[1][1]):
                    print("D", end=" ")
                else:
                    print("_", end=" ")
            print()

        print()
        print()
