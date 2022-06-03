## Follow-Along Setup Guide for Reproducing Experiments

The code is required to run in a Linux setup, because of the use of Mujoco, which is only available on Linux. Therefore the first step is to install Ubuntu using [Rufus](https://rufus.ie/en/) and then to boot Ubuntu on e.g. a Windows computer using [this guide](https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/?fbclid=IwAR0wImYmF4EMh3DvoUI2stqLJ293N4p-tglvzx06UVyum-E3rWfJaQIlFNw). Unless the computer installed on is running an MPR partitioning system, in which [this guide](https://itsfoss.com/install-ubuntu-dual-boot-mode-windows/) should be followed instead. It is important during the install of the setup that "can use third-party software and graphics" is accepted, as the system will otherwise run very slowly.

After booting Ubuntu on our pc, we installed Anaconda using [this guide](https://linuxize.com/post/how-to-install-anaconda-on-ubuntu-20-04/). It is important that it is this version or 4.11.0, as well as downloading [the decision transformer code](https://github.com/kzl/decision-transformer). 
#Dette er en test

The next step is to download MuJoCo200 by going to [the website](https://roboti.us/download.html), as well as [the license key](https://roboti.us/file/mjkey.txt), which should be put inside the directory of ````.mujoco````. When downloaded we created a secret directory ````.mujoco```` (The secret files can be seen by pressing ````Ctrl+H````), and in this directory the downloaded MuJoCo200 was placed. The path should look like this 
````
/home/pcname/.mujoco/mujoco200/
````
It is important the the name is mujoco200 and should be renamed if it has another name. 


Then the environment is created by going to the directory, that looks approximately like this 

```
/home/pcname/decision-transformer-master/gym
```
, and running the file ````conda\_env.yml```` in command prompt by using the command: 
```
conda env create -f conda_env.yml
```


This will run for some time, and give you an error, called 
````
could not create wheel
````
This is the main error, and should be fixed by fixing 2-3 errors. 


From here input the following into the terminal:

````
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/pcname/.mujoco/mujoco200/bin
````




## CondaValueError: prefix already exist
This is a suberror, if you tried to create the environment, and you should therefore go to the directory envs, and delete the environment just created. 

After deletion, the environment should be able to be set up again.\\ 


## Wheels: GCC
To fix this error type the following in the terminal:
````
sudo apt install libosmesa6-dev libgl1-mesa-glx libglfw3
````
## D4RL and producing the dataset
When the errors are fixed above, the next step is then to download D4RL, from the [repository](https://github.com/rail-berkeley/d4rl). This is can be done in the following two ways:


````
git clone https://github.com/rail-berkeley/d4rl.git
````
go to the directory where d4rl is located
````
pip install -e .
````


Or the shorter version

````
pip install git+https://github.com/rail-berkeley/d4rl@master#egg=d4rl
````

When D4Rl is downloaded, go to that directory and open setup.py. In this file change the content to:
````
from distutils.core import setup
from platform import platform

from setuptools import find_packages

setup(
    name='d4rl',
    version='1.1',
    install_requires=['gym',
                      'numpy',
                      'mujoco_py',
                      'pybullet',
                      'h5py',
                      'termcolor',  # adept_envs dependency
                      'click',  # adept_envs dependency
                      'dm_control==0.0.364896371', 
                      'mjrl @ git+https://github.com/aravindr93/mjrl@master#egg=mjrl'],
    packages=find_packages(),
    package_data={'d4rl': ['locomotion/assets/*',
                          'hand_manipulation_suite/assets/*',
                          'hand_manipulation_suite/Adroit/*',
                          'hand_manipulation_suite/Adroit/gallery/*',
                          'hand_manipulation_suite/Adroit/resources/*',
                          'hand_manipulation_suite/Adroit/resources/meshes/*',
                          'hand_manipulation_suite/Adroit/resources/textures/*',
                          ]},
    include_package_data=True,
)
````


This changes the dm version to the one that is needed. 

By following the original guide, the next step is to download the dataset:

````
cd /decision-transformer-master/gym/data
python download_d4rl_datasets.py
````
## MuJoCo error: could not find path

To solve this issue run the following export commands in your environment. 
Initialize the environment \\


````
export MUJOCO_GL="glfw"
export MJLIB_PATH=$HOME/.mujoco/mujoco200/bin/libmujoco200.dylib
export MJKEY_PATH=$HOME/.mujoco/mujoco200/mjkey.txt
export LD_LIBRARY_PATH=$HOME/.mujoco/mujoco200/bin:$LD_LIBRARY_PATH
export MUJOCO_PY_MJPRO_PATH=$HOME/.mujoco/mujoco200/
export MUJOCO_PY_MJKEY_PATH=$HOME/.mujoco/mujoco200/mjkey.txt
````





