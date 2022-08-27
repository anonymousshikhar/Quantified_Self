#! /bin/sh
echo "================================================================================="
echo "Welcome to the automated setup system. This will setup the local virtual env."
echo "Then it will install all the required libraries and its dependencies."
echo "You can rerun this without any issues."
echo "================================================================================="
if [ -d "$.backend_env" ];
then 
    echo ".backend_env folder exists. Installing using pip"
else
    echo "creating .backend_env and install using pip"
    python3 -m venv .backend_env
fi
# Activate virtual environment
. .backend_env/bin/activate

#Upgrade the pip 
pip install --upgrade pip
pip install -r reqiurements.txt

#Work done. Deactivating the virtual environment.
deactivate