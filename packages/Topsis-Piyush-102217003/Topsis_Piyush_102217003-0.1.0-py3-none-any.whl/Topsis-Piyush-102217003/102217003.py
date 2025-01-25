import numpy as np;
import pandas as pd;
import sys;

def get_values():
    values=sys.argv[1:];
    if(len(values) <4):
        raise Exception('The number of arguments is incorrect');
    return values;

def check_numeric(df):
    cols_to_check = df.columns[1:]  # Get the last two columns
    for col in cols_to_check:
        if not pd.api.types.is_numeric_dtype(df[col]):
            return False
    return True

def getData(fileName):
    data = pd.read_csv(fileName,index_col=None);
    if(data.shape[1] < 3):
        raise Exception('The data file must have at least 3 columns');
    elif(check_numeric(data) == False):
        raise Exception('The data file must have numeric columns');
    else:
        return data;

def apply_topsis(data,weights,impacts,outputfile):
    data1=data.copy();
    for i in range(len(data1.columns)):
        data1.iloc[:, i] = data.iloc[:, i] / np.sqrt(np.sum(data.iloc[:, i]**2));

    weighted_matrix = data1.copy();
    for i in range(len(data.columns)):
        weighted_matrix.iloc[:, i] = data1.iloc[:, i] * weights[i];

    ideal_solution = []
    negative_ideal_solution = []
    for i in range(len(data.columns)):
        if impacts[i] == '+':
            ideal_solution.append(weighted_matrix.iloc[:, i].max())
            negative_ideal_solution.append(weighted_matrix.iloc[:, i].min())
        else:
            ideal_solution.append(weighted_matrix.iloc[:, i].min())
            negative_ideal_solution.append(weighted_matrix.iloc[:, i].max())
    
    separation_from_ideal = np.sqrt(((weighted_matrix - ideal_solution) ** 2).sum(axis=1))
    separation_from_negative_ideal = np.sqrt(((weighted_matrix - negative_ideal_solution) ** 2).sum(axis=1))
    closeness = separation_from_negative_ideal / (separation_from_ideal + separation_from_negative_ideal)
    ranked_alternatives = pd.DataFrame({
        'Alternative': data.index,
        'Closeness': closeness
    }).sort_values(by='Closeness', ascending=False)
    # remove indexes from the dataframe
    ranked_alternatives= ranked_alternatives.reset_index(drop=True)
    data['Rankings']=ranked_alternatives.iloc[:,0];
    data['Topsis_score']=ranked_alternatives.iloc[:,1];
    data.to_csv('c:/Users/piyus/projects/pythonlibraryfortopsis/'+outputfile,index=False);
    return "generated file";


values=get_values();
inputdatafile=values[0];
try:
    data=getData('c:/Users/piyus/projects/pythonlibraryfortopsis/'+values[0]);  
except FileNotFoundError:
    print("Error: The file was not found. Please check the file path.")


weights=values[1]
impacts=values[2]
if ',' not in weights:
    raise ValueError("Weights must be comma-separated.")
if ',' not in impacts:
    raise ValueError("Impact must be comma-separated.")

weights = list(map(int, weights.split(',')))
impacts = list(map(str.lower, impacts.split(',')))

if not all(val in ['+', '-'] for val in impacts):
    raise ValueError("Impact must only contain '+' and '-' values.")

if len(weights) != len(impacts) or len(weights) != len(data.columns)-1:
    raise ValueError("The lengths of weights, impact, and the number of columns must be equal.")

outputfile=values[3];

apply_topsis(data.drop(data.columns[0],axis=1),weights,impacts,outputfile);