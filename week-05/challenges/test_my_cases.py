"""综合题 A 的自选输入；与教师测试一样通过同名 fixture 接收实现。"""


def test_my_summarize_case(summarize_values):
    values = [4, -4, 4, 0, 4, -4]

    result = summarize_values(values)

    assert result == {
        "unique": [4, -4, 0],
        "counts": {4: 3, -4: 2, 0: 1},
        "repeated": {4, -4},
    }
    assert values == [4, -4, 4, 0, 4, -4]