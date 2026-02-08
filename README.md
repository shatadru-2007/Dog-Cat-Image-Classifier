Download the dataset from : https://www.kaggle.com/datasets/princelv84/dogsvscats and save it as dogs_vs_cats.zip
2 Prediction Images are provided in the repository, which migght be used.

METHOD-1 (Google Colab (Browser) based method, anyone can use, even on devices  without GPU):
1) Open the Dog_Cat_Classify.ipynb directly or by using the given link: https://colab.research.google.com/drive/1qyaddKqRMsD8OxUXD-dTdXx9xU38NJp2?usp=sharing
2) Connect to T4 GPU and use Python3
3) Upload dogs_vs_cats.zip in the notebook
4) Run all the code snippets one by one
5) Download the Dog_Cat_Classify.keras file
6) Open the Dog_Cat_Predict.ipynb file directly or by using the given link: https://colab.research.google.com/drive/13jYPYfArTKQIUn9AQwkV8oZbdYw87w4y?usp=sharing
7) Connect to T4 GPU and use Python3
8) Upload Dog_Cat_Classify.keras file in the notebook
9) Upload prediction images to the notebook and change the required path in the code
10) Run all the code snippets one by one

OR 

METHOD-2 (Terminal based method, use VS Code or Anaconda, USe this method only if there is GPU in the device):
1) Download Dog_Cat_Classify.py, Dog_Cat_Predict.py and dogs_vs_cats.zip in the same folder.
2) Create a virtual environment using Python 3.10.19 or any other suitable version.
3) In the virtual environment, install gthe packages like: tensorflow, matplotlib and numpy.
4) In the Dog_Cat_Classify.py file update the path for the dogs_vs_cats.zip.
5) Run the Dog_Cat_Classify.py file. A file named Dog_Cat_Classify.keras gets savedd in the same folder.
6) Enter the path of the Dog_Cat_Classify.keras file and the path of the iimage to be predicted in the correct places in the Dog_Cat_Predict.py file. We get the prediction
