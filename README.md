# Setup
1. Install python3 or all-in-one toolkit (e.g. anaconda)

2. (optional) create a virtual environment
    `> python3 -m venv ./venv`
    `> source ./venv/bin/activate`

3. install tabpy (and other) requirements
    `(venv)> pip install -r requirements`

4. Start local tabpy server 
    * Could also run on dedicated/remote server
    `(venv)> tabpy`

5. Connect Tableau to tabpy server
    * local host or remote server

6. Deploy function for normalize (tabpy must be running in another terminal)
    `(venv)> python normalize.py`

7. Provided mysql (`comments.sql`) file should be used to create a `comments` table

# Overview
* Operate as table calculations
* Can only pass aggregates (or ATTR) of fields
* Must return JSON-serializable object
* Select `SCRIPT_{BOOL,INT,REAL,STR}` based on return type

