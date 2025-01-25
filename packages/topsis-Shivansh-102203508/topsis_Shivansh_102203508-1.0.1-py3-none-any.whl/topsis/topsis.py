import pandas as pd
import sys

def parse_weights(df,weights,impacts):
    if len(impacts.split(',')) != df.shape[1]-1 or len(weights.split(',')) != df.shape[1]-1:
        raise ValueError("Number of impacts and weights must match the number of columns in the DataFrame.")

    w = [float(weight) for weight in weights.split(",")]
    imp = [1 if impact == '+' else 0 for impact in impacts.split(",")]
    
    return w,imp

def normalize_dec_mat(df,w):
    rsumsq=0
    for i,col in enumerate(df.columns[1:]):
        df[col]=df[col].astype(float)
        rsumsq=((df[col]**2).sum())**0.5
        df.loc[:df.shape[0] - 1, col] /= rsumsq/w[i]
    return df

def calculate_ideal_solutions(norm_df, impacts):
    vpos = [] 
    vneg = [] 

    for i, col in enumerate(norm_df.columns[1:]):
        if impacts[i] == 1: 
            vpos.append(norm_df[col].max())
            vneg.append(norm_df[col].min())
        else:
            vpos.append(norm_df[col].min())
            vneg.append(norm_df[col].max())
    return vpos, vneg

def calculate_topsis_scores(norm_df, vpos, vneg):
    spos = []
    sneg = []

    for i in range(len(norm_df)):
        spos.append(sum((norm_df.iloc[i, 1:] - vpos) ** 2) ** 0.5)
        sneg.append(sum((norm_df.iloc[i, 1:] - vneg) ** 2) ** 0.5)

    scores = [sneg[i] / (sneg[i] + spos[i]) for i in range(len(spos))]
    return scores

def topsis(df,weights,impacts):
    w,imp=parse_weights(df,weights,impacts)
    df=normalize_dec_mat(df,w)
    vpos,vneg=calculate_ideal_solutions(df,imp)
    scores = calculate_topsis_scores(df, vpos, vneg)
    df['Topsis Score'] = scores
    df['Rank'] = df['Topsis Score'].rank(ascending=False).astype(int)
    return df


def main():
    # Ensure correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    # Parse command-line arguments
    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    result_file = sys.argv[4]

    try:
        # Read input data
        df = pd.read_excel(input_file)

        # Perform TOPSIS analysis
        result = topsis(df, weights, impacts)

        # Save the result to the output file
        result.to_excel(result_file, index=False)
        print(f"Results saved to {result_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()