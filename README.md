   # Site Checker

Command Line Tool to monitor a website to check if website is up and to see if there is any update.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development.

### Prerequisites

What things you need to install the software and how to install them

```
Python
pip
```

Once you install pip, install virtual env
```
pip install virtualenv
```

### Installing

A step by step series of examples that tell you how to get a development env running

You first need to activate the environment.

Windows
```
venv\scripts\activate
```
Mac OS / Linux

```
source venv/bin/activate
```

Next you need to install the project. Since it's a command tool  it can directly be installed using pip.

It will automatically install all the modules requires.
Run one of the two commands.
```
pip install --editable . 
pip install site_checker
```

## Running the script
The script consists of two functions 
* **start** - To start running the script
* **stop** - To stop the script, need to be run from another terminal.

To start running the script
```python
# To pass the website name later
checker start

# To pass the website name alog with run command
checker start --site {name of website}
```
To stop the script, open another terminal and do the following
```python
# Activate the environment
# Windows
venv\scripts\activate
# Mac OS / Linux
source venv/bin/activate

# To stop the script
checker stop
```

## Authors

* **Shivam Garg** - *student* - DTU (Final year CS undergrad)
 

