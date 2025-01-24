import numpy as np
from pufferlib.ocean import Connect4, Rware
envs = Rware(num_envs = 10)
observations, _ = envs.reset()
observations = observations.copy()
N = 1000
same_obs = True
for step in range(N):
    actions = np.array([envs.single_action_space.sample()  for _ in range(envs.num_agents)])
    next_obs, rewards, terminals, truncateds, infos = envs.step(actions)
    if not np.array_equal(observations, next_obs):
        same_obs = False
        print(f"Observation changed at step {step + 1}.")
        break
    observations = next_obs
if same_obs:
    print(f"All {N} steps returned identical observations.")
envs.close()
