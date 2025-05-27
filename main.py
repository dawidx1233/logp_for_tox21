from data import MolecularCalculationTox21 as mct
import os

def main():
    print("Obliczanie statystyk z SMILES lub 'q' aby zakończyć")
    while True:
        input_file = input("Podaj nazwę pliku tox1: ").strip()
        if not os.path.isfile(input_file):
            print(f"Plik '{input_file}' nie istnieje.")
            continue
        if input_file == 'q':
            print("Zakończenie działania programu")
            break
        data = mct.read_smiles_from_file(input_file)
        if data is None:
            continue
        df_mol = mct.smiles_to_mol(data)
        if df_mol is None:
            continue
        df_logp = mct.mol_to_logp(df_mol)
        if df_logp is None:
            continue
        logp_average = mct.average_logp(df_logp)
        logp_min = mct.min_logp(df_logp)
        logp_max = mct.max_logp(df_logp)
        print(f"Dane dla pliku: {input_file}\nŚrednia: {logp_average}\nMin: {logp_min}\nMax: {logp_max}")



if __name__ == "__main__":
    main()
