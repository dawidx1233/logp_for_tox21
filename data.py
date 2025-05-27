from rdkit import Chem
import logging
import pandas as pd
from rdkit.Chem import Descriptors

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MolecularFormulaCalculator")


class MolecularCalculationTox21:
    @staticmethod
    def read_smiles_from_file(file_path: str) -> pd.DataFrame | None:
        try:
            df = pd.read_csv(file_path, usecols=[0], header=None, names=["SMILES"])
            logger.info(f"Dane wszytane pomyślnie, {len(df)} wierszy")
            return df
        except Exception as e:
            logger.error(f"Błąd wczytywania danych: {e}")
            return None

    @staticmethod
    def smiles_to_mol(df: pd.DataFrame) -> pd.DataFrame | None:
        try:
            df["mol"] = df["SMILES"].apply(Chem.MolFromSmiles)
            invalid_smiles = df[df["mol"].isnull()]
            if not invalid_smiles.empty:
                logger.error(f"Znaleziono nie prawidłowy SMILES dla: {len(invalid_smiles)} cząsteczek")
            logger.info("Poprawnie przeknwertowano SMILES na mol")
            return df
        except Exception as e:
            logger.error(f"Błąd konwersji SMILES: {e}")
            return None

    @staticmethod
    def mol_to_logp(df: pd.DataFrame) -> pd.DataFrame | None:
        try:
            df["logp"] = df["mol"].apply(lambda mol: Descriptors.MolLogP(mol) if mol is not None else None)
            logger.info("Poprawnee przekonwertowanie na logp")
            return df
        except Exception as e:
            logger.error(f"Błąd konwersji logp: {e}")
            return None

    @staticmethod
    def average_logp(df: pd.DataFrame) -> float | None:
        try:
            average_logp = df["logp"].mean()
            logger.info("Pomyślnie obliczono średnią")
            return average_logp
        except Exception as e:
            logger.error(f"Błąd podczas obliczania średniej: {e}")
            return None

    @staticmethod
    def min_logp(df: pd.DataFrame) -> float | None:
        try:
            min_logp = df["logp"].min()
            logger.info("Pomyślnie znaleziono minimalną wartość")
            return min_logp
        except Exception as e:
            logger.error(f"Błąd podczas szukania minimalnej wartości: {e}")
            return None

    @staticmethod
    def max_logp(df: pd.DataFrame) -> float | None:
        try:
            max_logp = df["logp"].max()
            logger.info("Pomyślnie znaleziono maksymalną wartość")
            return max_logp
        except Exception as e:
            logger.error(f"Błąd podczas szukania maksymalną wartości: {e}")
            return None
