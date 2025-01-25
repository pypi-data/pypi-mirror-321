import pandas as pd
import numpy as np

def read_csv(file_path):
    return pd.read_csv(file_path)

def normalize_matrix(df):
    return df / np.sqrt((df ** 2).sum(axis=0))

def apply_weights(df, weights):
    return df * weights

def calculate_ideal_solution(df, impacts):
    ideal = []
    negative_ideal = []
    
    for i, impact in enumerate(impacts):
        if impact == '+': 
            ideal.append(df.iloc[:, i].max())
            negative_ideal.append(df.iloc[:, i].min())
        elif impact == '-': 
            ideal.append(df.iloc[:, i].min())
            negative_ideal.append(df.iloc[:, i].max())
    
    return np.array(ideal), np.array(negative_ideal)

def calculate_distance(df, ideal, negative_ideal):
    ideal_distance = np.sqrt(((df - ideal) ** 2).sum(axis=1))
    negative_ideal_distance = np.sqrt(((df - negative_ideal) ** 2).sum(axis=1))
    return ideal_distance, negative_ideal_distance

def topsis(df, weights, impacts):
    normalized_df = normalize_matrix(df.iloc[:, 1:])
    weighted_df = apply_weights(normalized_df, weights)
    ideal, negative_ideal = calculate_ideal_solution(weighted_df, impacts)
    ideal_distance, negative_ideal_distance = calculate_distance(weighted_df, ideal, negative_ideal)
    score = negative_ideal_distance / (ideal_distance + negative_ideal_distance)
    df['TOPSIS_Score'] = score
    df['Rank'] = score.rank(ascending=False) 
    return df

def main(input_file, weights, impacts):
    df = read_csv(input_file)
    result_df = topsis(df, weights, impacts)
    print(result_df)

weights = np.array([0.25, 0.25, 0.25,0.25])  
impacts = ['-', '+', '+','+']  
main(r'C:\Users\Arya Lal\Downloads\topsistest1.csv', weights, impacts)
