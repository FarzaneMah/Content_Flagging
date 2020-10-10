For creating an API using FastAPI: 
1. Run the model "LSTM_Flagging_Inappropriate_Contents.ipynb" and save the model as .keras (this is included in the code)
2. Create a virtual environment before installing the required packages and activate your invironment.
```
 conda create -n YourInvironmentName python=3.7
```
```
conda activate YourInvironmentName
```

3. Install the required packages using "requirements.txt"
```
pip install -r requirements.txt
```
4. Run "API_LSTM.py" in cmd:
```
uvicorn API_LSTM:app --reload
```
5. Open the browser at the link that is created. For more information regarding FastAPI visit https://fastapi.tiangolo.com/tutorial/first-steps/
6. You can choose the level of flag strictness and upload a .csv file to flag the inappropriate content in it.
