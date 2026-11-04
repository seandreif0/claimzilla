# Synthetic data: no PHI
import pytest


@pytest.fixture
def sample_members():
    return [
        {"member_id": "TEST-000001", "name": "Test Member One", "copay_rate": 0.1},
        {"member_id": "TEST-000002", "name": "Test Member Two", "copay_rate": 0.2},
        {"member_id": "TEST-000003", "name": "Test Member Three", "copay_rate": 0.3},
    ]
