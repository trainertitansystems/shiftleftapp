import pytest

@pytest.mark.skip(reason="Smoke tests run post-deploy")
def test_smoke_placeholder():
    assert True

