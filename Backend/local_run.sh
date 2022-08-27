#! /bin/sh
echo "================================================================================="
echo "Welcome to the automated setup system. This will setup the local virtual env."
echo "Then it will install all the required libraries and its dependencies."
echo "You can rerun this without any issues."
echo "================================================================================="

if [ -d ".backend_env" ];
then 
    echo "Virtual env exist.Enabling virtual environment"
else
    echo "No virtual env found. Please run setup.sh first"
    exit N
fi 

#Activate virtual env
. .backend_env/bin/activate
export ENV=development
python main.py
deactivate 