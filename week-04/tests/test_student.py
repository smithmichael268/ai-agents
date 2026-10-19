def test_make_variant_keeps_results_independent(make_variant):
    source = {"seed": 13, "sample_sizes": [250, 750, 1250, 1750]}
    expected_source = {"seed": 13, "sample_sizes": [250, 750, 1250, 1750]}
    expected_result = {"seed": 2027, "sample_sizes": [250, 900, 1250, 1750]}

    first = make_variant(source, seed=2027, index=1, replacement=900)
    second = make_variant(source, seed=2027, index=1, replacement=900)

    assert first == expected_result
    assert second == expected_result
    assert source == expected_source

    assert first is not source
    assert second is not source
    assert first is not second
    assert first["sample_sizes"] is not source["sample_sizes"]
    assert second["sample_sizes"] is not source["sample_sizes"]
    assert first["sample_sizes"] is not second["sample_sizes"]

    first["seed"] = 2028
    first["sample_sizes"][1] = 901
    first["sample_sizes"].append(9999)

    assert second == expected_result
    assert source == expected_source
