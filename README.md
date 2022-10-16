# mlop_flask
Create a flask application for ML Ops
#   Dependencies
#   PyCaret
    to instal pycaret 
    Install
    PyCaret is tested and supported on the following 64-bit systems:
        Python 3.6 – 3.8
        Python 3.9 for Ubuntu only
        Ubuntu 16.04 or later
    #   Windows 7 or later
    Install PyCaret with Python's pip package manager.
        pip install pycaret
    To install the full version (see dependencies below):
        pip install pycaret[full]
    If you want to try our nightly build (unstable) you can install pycaret-nightly from pip.
        pip install pycaret-nightly
    Environment
    In order to avoid potential conflicts with other packages, it is strongly recommended to use a virtual environment, e.g. python3 virtualenv (see python3 virtualenv documentation) or conda environments. Using an isolated environment makes it possible to install a specific version of pycaret and its dependencies independently of any previously installed Python packages. 
    # create a conda environment
    conda create --name yourenvname python=3.8

    # activate conda environment
    conda activate yourenvname

    # install pycaret
    pip install pycaret

    # create notebook kernel
    python -m ipykernel install --user --name yourenvname --display-name "display-name"
    PyCaret is not yet compatible with sklearn>=0.23.2.

    #   For MAC OS

    MAC users will have to install LightGBM separately using Homebrew, or it can be built using CMake and Apple Clang (or gcc). See the instructions below:

    Install CMake (3.16 or higher):

        >> brew install cmake
        Install OpenMP
        >> brew install libomp
        Run the following commands in terminal:

        git clone --recursive https://github.com/microsoft/LightGBM ; cd LightGBM
        mkdir build ; cd build
        cmake ..
        make -j4
    
#   Flask
    Prerequisite
    Python 2.6 or higher is usually required for installation of Flask. Although Flask and its dependencies work well with Python 3 (Python 3.3 onwards), many Flask extensions do not support it properly. Hence, it is recommended that Flask should be installed on Python 2.7.

    Install virtualenv for development environment
    virtualenv is a virtual Python environment builder. It helps a user to create multiple Python environments side-by-side. Thereby, it can avoid compatibility issues between the different versions of the libraries.

    The following command installs virtualenv

    pip install virtualenv
    This command needs administrator privileges. Add sudo before pip on Linux/Mac OS. If you are on Windows, log in as Administrator. On Ubuntu virtualenv may be installed using its package manager.

    Sudo apt-get install virtualenv
    Once installed, new virtual environment is created in a folder.

    mkdir newproj
    cd newproj
    virtualenv venv
    To activate corresponding environment, on Linux/OS X, use the following −

    venv/bin/activate
    On Windows, following can be used

    venv\scripts\activate
    We are now ready to install Flask in this environment.

    pip install Flask
    The above command can be run directly, without virtual environment for system-wide installation.
#   Docker
    install the docker extension in vs studio code and install the docker desktop application on the local machine.
    connect to your docker hub account and create a repository.
    then; 
        docker build -t follysage/pycaret:latest . # to build the the docker image
        docker run -d -p 5000:5000 follysage/pycaret  # to run the container
    