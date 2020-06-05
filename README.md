# **DeepPath**
This project attempts to use ML to generate a path for a vehicle to navigate
 obstacles.

---
In the world of autonomous vehicles, obstacle navigation is one of the most
challenging aspects. After the obstacle is detected in relation to the vehicle,
a path needs to be generated in order to navigate that situation. Most systems
rely on pre-generated paths that are fitted around the obstacle(s) it is facing,
using a very algorithmic approach, and this can work very well in ideal scenarios.

However, this approach requires many complicated paths to be pre-generated to match
real world scenarios. This opens up these systems up to edge cases. The goal of this
project is to build a system that uses a Deep Net to build these paths using information
from it's environment as input. The hope is this kind of system should be able to
generalize in different and new environments verses the strict algorithmic approach.

---
# **Project Structure**
## Sim Environment:

In order to build and train the Deep Net, a basic 2D simulation of a car type object
along with obstacles will be created to allow for training of the NN.
