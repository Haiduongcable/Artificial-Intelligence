# Artificial-Intelligence
Pull code before you push and commit code, please!

'''Environment'''
Ubuntu 20.04 
Conda version : 4.8.3
Conda-build version : 3.18.11
Python version: 3.8.5

'''Install package'''
pip install -r requirement.txt

'''Edit config yaml'''
cd src
open config.yaml and change "path_save_data" with your directory Save data


'''Download data'''
cd src
python download_data.py

'''Run'''
cd src
python main.py
