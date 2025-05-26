from rdkit import Chem
import logging
import pandas as pd

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
        except Exception as e:
            logger.error(f"Błąd konwersji SMILES: {e}")
            return None
        invalid_smiles = df[df["mol"].isnull()]
        if  not invalid_smiles.empty():
            logger.error(f"Znaleziono nie prawidłowy SMILES dla: {len(invalid_smiles)} cząsteczek")
        logger.info("Poprawnie przeknwertowano SMILES na mol")
        return df


