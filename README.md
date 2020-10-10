# cDETOX
cDETOX is based on a consulting project with Ongo Science for flagging inappropriate comments on their platforms as part of my Insight Data Science fellowship. 

Labelled data from multiple platforms were merged in three classes: zero tolerance (hate, etc.), offensive, and fine. The labelled data is not provided in this repository per the nature of consulting project. 

For running the model 
1. Create a virtual environment before installing the required packages and activate your invironment.
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
4. Run the "cDETOX_LSTM.ipynb" jupyter notebook (I would suggest using Colab or AWS services if you have a large dataset).
5. After running the notebook, the model will be saved as .keras or .h5 and it can be used to create an API (refer to readme file in API folder for more information)

p.s. Not all information is included given the nature of consulting project, but I will be happy to help if there are questions.
