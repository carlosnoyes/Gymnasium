import gymnasium as gym


# Classic Control Example
def example_1():
    env = gym.make("CartPole-v1", render_mode="human")

    observation, info = env.reset(seed=42)
    for _ in range(1000):
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()
    env.close()


# Box2D Example
def example_2():
    env = gym.make("LunarLander-v2", render_mode="human")

    observation, info = env.reset(seed=42)
    for _ in range(1000):
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()
    env.close()


# Toy Text Example
def example_3():
    env = gym.make("Taxi-v3", render_mode="human")

    observation, info = env.reset(seed=42)
    for _ in range(1000):
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()
    env.close()


# MuJoCo Example
def example_4():
    env = gym.make("Ant-v5", render_mode="human")

    observation, info = env.reset(seed=42)
    for _ in range(1000):
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()
    env.close()


if __name__ == "__main__":
    for env in gym.envs.registry:
        print(env)

    example_num = 1
    if example_num == 1:
        example_1()
    elif example_num == 2:
        example_2()
    elif example_num == 3:
        example_3()
    elif example_num == 4:
        example_4()
    else:
        print("Invalid example number")
