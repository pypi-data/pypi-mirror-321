import pufferlib
import pufferlib.vector
from pufferlib.environments import atari
env_creator = atari.env_creator('breakout')

# Make 4 copies of Breakout on the current process (Serial is the default)
vecenv = pufferlib.vector.make(env_creator, num_envs=4)
