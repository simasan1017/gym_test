ppaquette/gym-envs
******
**User environments for OpenAI Gym.**

Installation
============

``gym_pull`` should be downloaded through pip with the command: ``pip install gym_pull``

To install the user environments, you need to import gym, and then gym_pull:

.. code:: python

	  import gym
	  import gym_pull
	  gym.pull('ppaquette/gym-envs/*')

Environments
======
A more detailed description of each environment is available in the README file inside each subfolder.

- **SuperMarioBros**: Contains the 32 levels of the original Super Mario Bros (with screen as input, or with 16x13 tiles), and a meta-level of all 32 levels
- **Doom**: Contains 9 Doom levels, and a meta-level of the 9 levels. Based on VizDoom.

Install Requirements
======

- **SuperMarioBros**:   ``apt-get install fceux``
- **Doom**: ``apt-get install python-numpy cmake zlib1g-dev libjpeg-dev libboost-all-dev gcc libsdl2-dev wget unzip``
