# # -*- coding: utf-8 -*-
# """
# Created on Fri Jan 10 19:57:33 2020

# @author: hp
# """
# import sys
# import os
# import pandas as pd
# import math
# import numpy as np

# class Topsis:
#     def __init__(self,filename):
#         if os.path.isdir(filename):
#             head_tail = os.path.split(filename)
#             data = pd.read_csv(head_tail[1])
#         if os.path.isfile(filename):
#             data = pd.read_csv(filename)
#         self.d = data.iloc[1:,1:].values
#         self.features = len(self.d[0])
#         self.samples = len(self.d)
#     def fun(self,a):
#         return a[1]
#     def fun2(self,a):
#         return a[0]
#     def evaluate(self,w = None,im = None):
#         d = self.d
#         features = self.features
#         samples = self.samples       
#         if w==None:
#            w=[1]*features
#         if im==None:
#          im=["+"]*features
#         ideal_best=[]
#         ideal_worst=[]
#         for i in range(0,features):
#             k = math.sqrt(sum(d[:,i]*d[:,i]))
#             maxx = 0
#             minn = 1 
#             for j in range(0,samples):
#                 d[j,i] = (d[j,i]/k)*w[i]
#                 if d[j,i]>maxx:
#                     maxx = d[j,i]
#                 if d[j,i]<minn:
#                     minn = d[j,i]
#             if im[i] == "+":
#                 ideal_best.append(maxx)
#                 ideal_worst.append(minn)
#             else:
#                 ideal_best.append(minn)
#                 ideal_worst.append(maxx)
#         p = []
#         for i in range(0,samples):
#             a = math.sqrt(sum((d[i]-ideal_worst)*(d[i]-ideal_worst)))
#             b = math.sqrt(sum((d[i]-ideal_best)*(d[i]-ideal_best)))
#             lst = []
#             lst.append(i)
#             lst.append(a/(a+b))
#             p.append(lst)
#         p.sort(key=self.fun)
#         rank = 1
#         for i in range(samples-1,-1,-1):
#             p[i].append(rank)
#             rank+=1
#         p.sort(key=self.fun2)
#         return p


# def findTopsis(filename,w,i):
#     ob = Topsis(filename)
#     res = ob.evaluate(w,i)
#     print(res)


# def main():
#     lst = sys.argv
#     length = len(lst)
#     if length > 4 or length< 4:
#         print("wrong Parameters")
#     else:
#         w = list(map(int,lst[2].split(',')))
#         i = lst[3].split(',')
#         ob = Topsis(lst[1])
#         res = ob.evaluate(w,i)
#         print (res)
        

# if __name__ == '__main__':
#      main()








# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:57:33 2020
@author: hp
"""

import sys
import os
import pandas as pd
import math
import numpy as np

class Topsis:
    def __init__(self, filename):
        # Check if file exists
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"Input file '{filename}' not found.")
        
        # Load data from file with encoding specified
        try:
            data = pd.read_csv(filename, encoding='latin1')  # Use 'latin1' or 'ISO-8859-1' depending on the file's encoding
        except UnicodeDecodeError:
            raise ValueError("Failed to decode file. Ensure it is in a compatible encoding (e.g., UTF-8 or Latin1).")

        # Validate number of columns
        if data.shape[1] < 3:
            raise ValueError("Input file must contain three or more columns.")

        # Validate numeric data from 2nd to last columns
        if not all(data.iloc[:, 1:].map(lambda x: isinstance(x, (int, float))).all()):
            raise ValueError("All columns except the first must contain numeric values.")

        self.data = data
        self.d = data.iloc[:, 1:].values  # Numeric values only
        self.features = self.d.shape[1]  # Number of features (columns)
        self.samples = self.d.shape[0]  # Number of samples (rows)

    def evaluate(self, weights, impacts):
        # Validate weights and impacts
        if len(weights) != self.features or len(impacts) != self.features:
            raise ValueError("Number of weights and impacts must match the number of criteria (columns).")
        
        if not all(impact in ['+', '-'] for impact in impacts):
            raise ValueError("Impacts must be '+' or '-'.")

        d = self.d
        weights = np.array(weights)

        # Step 1: Normalize the decision matrix
        for i in range(self.features):
            column = d[:, i]
            norm = math.sqrt(sum(column**2))
            d[:, i] = (column / norm) * weights[i]

        # Step 2: Determine the ideal best and ideal worst values
        ideal_best = []
        ideal_worst = []
        for i in range(self.features):
            if impacts[i] == '+':
                ideal_best.append(max(d[:, i]))
                ideal_worst.append(min(d[:, i]))
            else:
                ideal_best.append(min(d[:, i]))
                ideal_worst.append(max(d[:, i]))

        # Step 3: Calculate the separation measures and Topsis score
        scores = []
        for i in range(self.samples):
            positive_distance = math.sqrt(sum((d[i, :] - ideal_best)**2))
            negative_distance = math.sqrt(sum((d[i, :] - ideal_worst)**2))
            score = negative_distance / (positive_distance + negative_distance)
            scores.append(score)

        # Step 4: Rank the scores
        self.data['Topsis Score'] = scores
        self.data['Rank'] = self.data['Topsis Score'].rank(ascending=False, method='dense').astype(int)

        return self.data

def main():
    try:
        # Validate number of arguments
        if len(sys.argv) != 5:
            print("Usage: python <RollNumber>.py <InputDataFile> <Weights> <Impacts> <ResultFileName>")
            print("Example: python 102203551.py 102203551-data.csv \"1,1,1,2\" \"+,+,-,+\" 102203551-result.csv")
            return

        input_file = sys.argv[1]  # Input data file (e.g., 102203551-data.csv)
        weights = list(map(float, sys.argv[2].split(',')))  # Weights (e.g., "1,1,1,2")
        impacts = sys.argv[3].split(',')  # Impacts (e.g., "+,+,-,+")
        output_file = sys.argv[4]  # Output result file (e.g., 102203551-result.csv)

        # Run Topsis
        topsis = Topsis(input_file)
        result = topsis.evaluate(weights, impacts)

        # Save result to output file
        result.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
