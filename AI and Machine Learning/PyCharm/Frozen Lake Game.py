import gym
import random

env = gym.make('FrozenLake-v0')

env.reset()

print(env.observation_space)
print(env.action_space)

score = 0

numbGames = 1000
numbSteps = 10

def PlayGame():
    global score
    for i in range(numbSteps):
        obs, rew, done, infp = env.step(random.randint(1,2))
        if done:
            score += rew
            break

for g in range (numbGames):
    env.reset()
    PlayGame()

print(score)