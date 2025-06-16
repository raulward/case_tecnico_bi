import pandas as pd
from pathlib import Path
from ftfy import fix_text
import chardet
import numpy as np

BASE_DIR = Path(__file__).parent.parent / "data"
CSV_PATH = BASE_DIR / "base_vendas_corrigida_v2.csv"

MOJIBAKE_SIGNS = set("ÃÂƒ√�")

def detect_encoding(path: Path, num_bytes: int = 2000) -> str:
    with open(path, "rb") as f:
        raw = f.read(num_bytes)
    encoding = chardet.detect(raw)["encoding"]
    if encoding == "MacRoman":
        encoding = "cp1252"
    print(f"Best encoding: {encoding}")
    return encoding

def maybe_fix(s: str) -> str:
    if not isinstance(s, str):
        return s
    if any(ch in s for ch in MOJIBAKE_SIGNS):
        return fix_text(s)
    return s

def load_and_fix_csv(path: Path, sep: str = ";") -> pd.DataFrame:
    encoding = detect_encoding(path)
    df = pd.read_csv(path, encoding=encoding, sep=sep)
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].map(maybe_fix)
    df["VALOR_TOTAL"] = df["VALOR_UNITARIO"] * df["QUANTIDADE"]

    return df



if __name__ == "__main__":
    df = load_and_fix_csv(CSV_PATH)
    
    # print(df.info())
    # print(df.head(5))
    # df.to_csv(Path(BASE_DIR / "base_vendas_clean.csv"), index=False)

    sorted_vals = np.sort(df["PRODUTO_ID"].unique())
    print(sorted_vals)
