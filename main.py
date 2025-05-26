from data import MolecularCalculationTox21 as mct


def main():
    print("Obliczanie statystyk z SMILES lub 'q' aby zakończyć")
    while True:
        input_file = input("Podaj nazwę pliku tox1: ").strip()
        if input_file == 'q':
            print("Zakończenie działania programu")
            break
        data = mct.read_smiles_from_file(input_file)


if __name__ == "__main__":
    main()
