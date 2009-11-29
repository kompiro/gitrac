from gitrac import command
from nose.tools import ok_
class TestListCommand:
    def test_execute(self):
        c = command.ListCommand();
        c.execute();
        ok_(True,"list");
