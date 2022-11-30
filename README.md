# Pytopia Dashboard

## How to Run
First, you need to install the dependencies. You can do this by running the following command:
```
pip install -r requirements.txt
```

Then, run the following command to start the export environment variables in main repo directory:
```
source .env
```

Run `export PYTHONPATH=${PWD}` to add the current directory to the python path.

Build django migrations by running the following command:
```
python src/manage.py makemigrations db
python src/manage.py migrate
```

Then, you can run the dashboard by running the following command:
```
streamlit run src/app.py
```
