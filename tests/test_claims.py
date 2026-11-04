from src.claims import member_copay


def test_member_copay():
    assert member_copay(200.0, 0.2) == 40.0
