# CAIVA-APP
## description: 


## Requirements
- Pythons 3.9
#### Install Python using Anaconda
1) Dowonload and install anacond from link -> 
https://www.anaconda.com/download/success

2) create new environment using the following command:
```bash
$ conda create -n caiva-app python=3.8      
```
3) activate the environment using the following command:
```bash
conda activate caiva-app
```
4) pip install requirements file using the following command:
```bash
pip install -r requirements.txt
```
5) Setup the environment variables
```bash
cp .env.example .env
```
Set your environment variable in the `.env` file. `like GOOGLE_API_KEY` value
6) Run FastApi server

```bash
uvicorn main:app --reload
```
