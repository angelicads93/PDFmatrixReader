import fitz  # PyMuPDF
import matplotlib.pylab as plt
import seaborn as sns
import pandas as pd


###--- Path were the Correlation Matrix is located:
filePath = './CorrelationMatrix_A.pdf'

###--- Extracts text from PDF image and stores it in a list:
stringList = fitz.open(filePath)[0].get_text().split()

###--- Transfer the global list to a nested List:
sublist_i = -1
labelsList, valuesList = [], []
for i in range(len(stringList)):
	tmp = stringList[i]
	if '+' not in tmp and '-' not in tmp and tmp!=stringList[i-1] and tmp==stringList[i+1]:
		sublist_i += 1
		labelsList.append(tmp)
		valuesList.append([])			
	elif '+' in tmp or '-' in tmp:
		valuesList[sublist_i].append(float(tmp))

###--- Invert order of each sublist:
for i in range(len(valuesList)):
	valuesList[i].reverse()


###--- Write labels in latex-format:
latexList = []
for i in range(len(labelsList)):
    if labelsList[i]=='AlsMz':
        latexList.append("$"+"\\alpha_S(M_Z^2)$")
    elif labelsList[i]=='mtop': 
        latexList.append("$m_t$")
    elif labelsList[i]=='mHl':
        latexList.append("$M_h$")
    elif labelsList[i]=='Mz':
        latexList.append("$M_Z$")
    elif labelsList[i]=='Mw_inp':
        latexList.append("$M_W$")
    elif labelsList[i]=='mup':
        latexList.append("$m_u$")
    elif labelsList[i]=='mdown':
        latexList.append("$m_d$")
    elif labelsList[i]=='mstrange':
        latexList.append("$m_s$")
    elif labelsList[i]=='mcharm':
        latexList.append("$m_c$")
    elif labelsList[i]=='mbottom':
        latexList.append("$m_b$")
    elif '_LNP' in labelsList[i]:
        tmp = labelsList[i].split('_LNP')[0].split('C')[1]
        if 'r' not in tmp:
            name = 'C_{'+tmp+'}' 
        else:
            tmp2 = tmp.split('r')[0].split('_') 
            name = 'C_{'+tmp2[0]+','+tmp2[1]+'}'
        latexList.append("$"+name+"$")


###--- Build dataframe and plot CM as heatmap:
df = pd.DataFrame(valuesList, index=latexList, columns=latexList)
fig = plt.figure()
ax = sns.heatmap(df, cmap="coolwarm")
ax.xaxis.tick_top()
ax.xaxis.set_label_position('top')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.show()


###--- Create histogram:
###--- (It excludes the diagonal elements expected to be fully correlated)
noDiagonal = []
for i in range(len(valuesList)):
    for j in range(len(valuesList)):
        if j!=i:
            noDiagonal.append(valuesList[i][j])
fig2 = plt.hist(noDiagonal, bins=50)
plt.xlabel('Correlation')
plt.show()

