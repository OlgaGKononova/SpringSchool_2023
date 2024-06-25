def get_structures(raw_data, num_mols) -> list:
    """Generates list of most similar molecules

    Args:
        raw_data (_type_): _description_
        num_mols (_type_): _description_

    Returns:
        list: list of SMILES
    """
    
    smiles_data = [(d["molecule_structures"]["canonical_smiles"], d["similarity"]) for d in raw_data]
    sorted_smiles_data = sorted(smiles_data, key=lambda x: x[1], reverse=True)
    return [s for s, _ in sorted_smiles_data][:num_mols]