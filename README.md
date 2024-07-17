Python code that reads a PDF file containing a predetermined correlation matrix and reformats it to be easily readable and usable in papers/presentations.
A histogram of the individual correlations is also displayed to provide an additional representation of how correlated the system is.

The dependencies needed are fitz, matplotlib, seaborn and pandas. 
To install them, you can run the following commands in the terminal:
  pip3 install PyMuPDF
  
  pip3 install matplotlib
  
  pip3 install seaborn
  
  pip3 install pandas

The name of the input pdf file can be changed in "filePath".

If using the terminal, execute the following command from the git-repo directory:
  python3 formatCorrelationMatrix.py



