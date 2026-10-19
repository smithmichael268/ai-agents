def make_variant(source, seed, index, replacement):
    variant = source.copy()
    variant["sample_sizes"] = source["sample_sizes"].copy()
    variant["seed"] = seed
    variant["sample_sizes"][index] = replacement
    return variant
