from gym.envs.registration import register

register(
    id='roar-v0',
    entry_point='ROAR_Gym.envs:ROAREnv',
)