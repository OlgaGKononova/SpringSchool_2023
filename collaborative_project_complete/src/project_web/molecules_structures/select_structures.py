def select_structures_by_properties(mol_data, prop_ranges):
    """
    Select list of smiles that satisfies the properties
    """
    smiles_list = []
    for data in mol_data:
        ind = []
        for prop, values in prop_ranges.items():
            v_min, v_max = values
            if prop == "similarity":
                data_prop = data["similarity"]
            else:
                data_prop = data["molecule_properties"][prop]
                
            ind.append(int(v_min <= data_prop <= v_max))
            
        if all(i == 1 for i in ind):
            smiles_list.append(data["molecule_structures"]["canonical_smiles"])
    return smiles_list
