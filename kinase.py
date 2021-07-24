
import pandas as pd
from rdkit import Chem
from rdkit.Chem.Draw import IPythonConsole

def smiles_tokenizer(smi):
    """ 
    Tokenize a SMILES string representation of a molecule
    Returns a list of tokens in SMILES vocabulary
    """
    import re
    pattern =  "(\[[^\]]+]|Br?|Cl?|N|O|S|P|F|I|b|c|n|o|s|p|\(|\)|\.|=|#|-|\+|\\\\|\/|:|~|@|\?|>|\*|\$|\%[0-9]{2}|[0-9])"
    regex = re.compile(pattern)
    tokens = [token for token in regex.findall(smi)]
    assert smi == ''.join(tokens)
    return tokens


def main():
    df = pd.read_csv('./kinase_JAK.csv')
    print(df.head())
    print(df.groupby(['measurement_type']).count())

def get_mol(smi):
    #IPythonConsole.molSize = (400, 300)
    #IPythonConsole.ipython_useSVG=True
    # Chem.MolFromSmiles returns a Chem.Mol object, which rdkit automatically visualizes in a jupyter notebook
    mol= Chem.MolFromSmiles(smi)
    return mol





