import pytest

@pytest.mark.usefixtures('setup','tear_down')
class Base:
    pass