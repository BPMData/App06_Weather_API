import pandas as pd
import ast

def finder(input):
    dict = pd.read_csv("datafiles/dictionary.csv")
    input = input.casefold()
    output = dict.loc[dict["word"] == input]["definition"].squeeze()
    output = ast.literal_eval(f'"{output}"')
    return {"definition": output, "word": input}
    # print(result_dictionary)

treeoutput = finder("tree")

print(type(treeoutput))
