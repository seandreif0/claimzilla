from src.claims import member_copay


def test_member_copay():
    assert member_copay(200.0, 0.2) == 40.0


def test_member_copay_for_sample_members(sample_members):
    copays = [member_copay(100.0, m["copay_rate"]) for m in sample_members]
    assert copays == [10.0, 20.0, 30.0]
