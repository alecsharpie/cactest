from packtest.lib import try_me

from unittest.mock import patch

@patch('builtins.print')
def test_try_me(mock_print):
    # The actual test
    try_me()
    mock_print.assert_called_with('\x1b[31m      [___________]\n       |         |\n       |         |\n       |         |\n       |_________|\n       \x1b[0m')

    # Showing what is in mock
    import sys
    sys.stdout.write(str( mock_print.call_args ) + '\n')
    sys.stdout.write(str( mock_print.call_args_list ) + '\n')

# def test_length_cactus():
#    assert len() > 0

# def test_type_cactus():
#    assert type(try_me()) == str
