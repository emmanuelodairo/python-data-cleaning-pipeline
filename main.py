import pandas as pd


def clean_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)

    df = df.drop_duplicates()

    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["score"] = pd.to_numeric(df["score"], errors="coerce")

    df["age"] = df["age"].fillna(df["age"].median())
    df["score"] = df["score"].fillna(df["score"].median())

    df = df[(df["score"] >= 0) & (df["score"] <= 100)]

    return df


def main() -> None:
    cleaned_df = clean_data("sample_data.csv")
    cleaned_df.to_excel("cleaned_output.xlsx", index=False)
    print("Data cleaned and exported to cleaned_output.xlsx")


if __name__ == "__main__":
    main()
