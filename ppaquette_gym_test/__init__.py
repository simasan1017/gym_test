from gym.envs.registration import register
from gym.scoreboard.registration import add_task, add_group
from .package_info import USERNAME
from .acrobot import AcrobotEnv
from .cartpole import CartPoleEnv

# Env registration
# ==========================
register(
    id='{}/CartPole-v0'.format(USERNAME),
    entry_point='{}_gym_test:CartPoleEnv'.format(USERNAME),
    timestep_limit=200,
    reward_threshold=195.0,
)

register(
    id='{}/CartPole-v1'.format(USERNAME),
    entry_point='{}_gym_test:CartPoleEnv'.format(USERNAME),
    timestep_limit=500,
    reward_threshold=475.0,
)

register(
    id='LolAcrobot-v1',
    entry_point='{}_gym_test:AcrobotEnv'.format(USERNAME),
    timestep_limit=500,
)


# Scoreboard registration
# ==========================
add_task(
    id='{}/CartPole-v0'.format(USERNAME),
    group='classic_control',
    summary="Balance a pole on a cart (for a short time).",
    description="""\
A pole is attached by an un-actuated joint to a cart, which moves along a frictionless track.
The system is controlled by applying a force of +1 or -1 to the cart.
The pendulum starts upright, and the goal is to prevent it from falling over.
A reward of +1 is provided for every timestep that the pole remains upright.
The episode ends when the pole is more than 15 degrees from vertical, or the
cart moves more than 2.4 units from the center.
""",
    background="""\
This environment corresponds to the version of the cart-pole problem described by
Barto, Sutton, and Anderson [Barto83]_.
.. [Barto83] AG Barto, RS Sutton and CW Anderson, "Neuronlike Adaptive Elements That Can Solve Difficult Learning Control Problem", IEEE Transactions on Systems, Man, and Cybernetics, 1983.
""",
)

add_task(
    id='{}/CartPole-v1'.format(USERNAME),
    group='classic_control',
    summary="Balance a pole on a cart.",
    description="""\
A pole is attached by an un-actuated joint to a cart, which moves along a frictionless track.
The system is controlled by applying a force of +1 or -1 to the cart.
The pendulum starts upright, and the goal is to prevent it from falling over.
A reward of +1 is provided for every timestep that the pole remains upright.
The episode ends when the pole is more than 15 degrees from vertical, or the
cart moves more than 2.4 units from the center.
""",
    background="""\
This environment corresponds to the version of the cart-pole problem described by
Barto, Sutton, and Anderson [Barto83]_.
.. [Barto83] AG Barto, RS Sutton and CW Anderson, "Neuronlike Adaptive Elements That Can Solve Difficult Learning Control Problem", IEEE Transactions on Systems, Man, and Cybernetics, 1983.
""",
)

add_task(
    id='LolAcrobot-v1',
    group='classic_control',
    summary="Swing up a two-link robot.",
    description="""\
The acrobot system includes two joints and two links, where the joint between the two links is actuated.
Initially, the links are hanging downwards, and the goal is to swing the end of the lower link
up to a given height.
""",
    background="""\
The acrobot was first described by Sutton [Sutton96]_. We are using the version
from `RLPy <https://rlpy.readthedocs.org/en/latest/>`__ [Geramiford15]_, which uses Runge-Kutta integration for better accuracy.
.. [Sutton96] R Sutton, "Generalization in Reinforcement Learning: Successful Examples Using Sparse Coarse Coding", NIPS 1996.
.. [Geramiford15] A Geramifard, C Dann, RH Klein, W Dabney, J How, "RLPy: A Value-Function-Based Reinforcement Learning Framework for Education and Research." JMLR, 2015.
""",
)
