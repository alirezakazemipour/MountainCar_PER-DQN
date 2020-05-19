import gym
import control_flags as flag
from train import Agent
from play import Play

env_name = "MountainCar-v0"

env = gym.make(env_name)
num_states = env.observation_space.shape[0]
num_actions = env.action_space.n
num_features = 64

s_low_b = env.observation_space.low
s_high_b = env.observation_space.high


print("Number of states:{}".format(num_states))
print("Number of actions:{}".format(num_actions))


def test_env_working():
    test_env = gym.make(env_name)
    for _ in range(300):
        test_env.render()
        action = test_env.action_space.sample()
        test_env.step(action)
    test_env.close()


if __name__ == "__main__":

    if flag.CHECK_ENV_WORKS:
        test_env_working()
        print("Environment works.")
        exit(0)

    agent = Agent(env, num_actions, num_states, num_features)
    # agent.run()
    player = Play(env, agent)
    player.evaluate()


