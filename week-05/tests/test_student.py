"""可修改的小测试示例：另选输入，保留自己的预期与解释。

测试通过参数接收课程 fixture，--impl 才能切换候选实现。
不要直接 from operations import pop_last 绕过这个开关。
"""


def test_my_pop_example(pop_last):
    items = [7, 4]

    result = pop_last(items)

    assert result == 4
    assert items == [7]


def test_my_pop_last_empty(pop_last):
    items = []

    result = pop_last(items)

    assert result is None
    assert items == []


def test_my_positive_squares_case(positive_squares):
    values = [0, 3, 3, -1, 4]

    result = positive_squares(values)

    assert result == [9, 9, 16]
    assert values == [0, 3, 3, -1, 4]


def test_my_positive_square_map_case(positive_square_map):
    record = {"a": 2, "b": -5, "c": 0, "d": 3}

    result = positive_square_map(record)

    assert result == {"a": 4, "d": 9}
    assert record == {"a": 2, "b": -5, "c": 0, "d": 3}
