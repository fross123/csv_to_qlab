"""
Tests for CLI interface
"""
import pytest
import json
import sys
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from io import StringIO


class TestCLIArgumentParsing:
    """Test command-line argument parsing"""

    def test_basic_arguments(self):
        """Test parsing basic required arguments"""
        from cli import main
        import io

        test_args = ['cli.py', 'test.csv', '127.0.0.1', '5']

        with patch('sys.argv', test_args), \
             patch('cli.Path.exists', return_value=True), \
             patch('cli.Path.is_file', return_value=True), \
             patch('builtins.open', return_value=io.BytesIO(b'Number,Type,Name\n1,audio,Test\n')), \
             patch('cli.send_csv') as mock_send:
            exit_code = main()
            assert mock_send.called

    def test_qlab_version_validation(self):
        """Test that only QLab versions 4 and 5 are accepted"""
        from cli import main

        # Test invalid version
        test_args = ['cli.py', 'test.csv', '127.0.0.1', '3']

        with patch('sys.argv', test_args), \
             patch('sys.stderr', new_callable=StringIO):
            with pytest.raises(SystemExit):
                main()

    def test_passcode_argument(self):
        """Test passcode argument is passed correctly"""
        from cli import main
        import io

        test_args = ['cli.py', 'test.csv', '127.0.0.1', '5', '--passcode', 'secret']

        with patch('sys.argv', test_args), \
             patch('cli.Path.exists', return_value=True), \
             patch('cli.Path.is_file', return_value=True), \
             patch('builtins.open', return_value=io.BytesIO(b'Number,Type,Name\n1,audio,Test\n')), \
             patch('cli.send_csv') as mock_send:
            main()
            # Check that send_csv was called with the passcode
            call_args = mock_send.call_args
            assert call_args[1]['passcode'] == 'secret'

    def test_verbose_flag(self):
        """Test verbose flag"""
        from cli import main
        import io

        test_args = ['cli.py', 'test.csv', '127.0.0.1', '5', '--verbose']

        with patch('sys.argv', test_args), \
             patch('cli.Path.exists', return_value=True), \
             patch('cli.Path.is_file', return_value=True), \
             patch('builtins.open', return_value=io.BytesIO(b'Number,Type,Name\n1,audio,Test\n')), \
             patch('cli.send_csv'), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            assert 'Sending CSV file' in output or 'test.csv' in output

    def test_json_flag(self):
        """Test JSON output flag"""
        from cli import main

        test_args = ['cli.py', 'test.csv', '127.0.0.1', '5', '--json']

        with patch('sys.argv', test_args), \
             patch('cli.Path.exists', return_value=True), \
             patch('cli.Path.is_file', return_value=True), \
             patch('cli.send_csv'), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            # Output should be valid JSON
            data = json.loads(output)
            assert 'success' in data
            assert 'errors' in data


class TestFileHandling:
    """Test file input handling"""

    def test_file_not_found(self):
        """Test error when CSV file doesn't exist"""
        from cli import main

        test_args = ['cli.py', 'nonexistent.csv', '127.0.0.1', '5']

        with patch('sys.argv', test_args), \
             patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            exit_code = main()
            assert exit_code == 1
            assert 'not found' in mock_stderr.getvalue().lower()

    def test_path_is_directory(self):
        """Test error when path is a directory not a file"""
        from cli import main

        test_args = ['cli.py', '/tmp', '127.0.0.1', '5']

        with patch('sys.argv', test_args), \
             patch('cli.Path.exists', return_value=True), \
             patch('cli.Path.is_file', return_value=False), \
             patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            exit_code = main()
            assert exit_code == 1
            assert 'not a file' in mock_stderr.getvalue().lower()

    def test_file_storage_adapter(self):
        """Test FileStorageAdapter works correctly"""
        from cli import FileStorageAdapter

        # Create a temporary CSV file
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write('Number,Type,Name\n1,audio,Test\n')
            temp_path = f.name

        try:
            adapter = FileStorageAdapter(temp_path)
            assert hasattr(adapter, 'stream')
            content = adapter.stream.read()
            assert b'Number,Type,Name' in content
        finally:
            Path(temp_path).unlink()


class TestOutputFormatting:
    """Test output formatting"""

    def test_human_readable_format_success(self):
        """Test human-readable format for successful operations"""
        from cli import format_human_readable
        from error_success_handler import ErrorHandler

        handler = ErrorHandler()
        handler.count_success('ok', 'Cue created')
        handler.count_success('ok', 'Cue created')

        output = format_human_readable(handler)
        assert 'Successfully processed 2 cue(s)' in output
        assert '✓' in output

    def test_human_readable_format_errors(self):
        """Test human-readable format for errors"""
        from cli import format_human_readable
        from error_success_handler import ErrorHandler

        handler = ErrorHandler()
        handler.handle_errors('error', 'Something went wrong')

        output = format_human_readable(handler)
        assert 'error' in output.lower()
        assert 'Something went wrong' in output
        assert '✗' in output

    def test_json_format(self):
        """Test JSON output format"""
        from cli import format_json
        from error_success_handler import ErrorHandler

        handler = ErrorHandler()
        handler.count_success('ok', 'Success')
        handler.handle_errors('error', 'Error message')

        output = format_json(handler)
        data = json.loads(output)

        assert 'success' in data
        assert 'errors' in data
        assert 'has_errors' in data
        assert len(data['success']) == 1
        assert len(data['errors']) == 1
        assert data['has_errors'] is True


class TestExitCodes:
    """Test exit codes"""

    def test_exit_code_success(self):
        """Test exit code 0 on success"""
        from cli import main
        import io

        test_args = ['cli.py', 'test.csv', '127.0.0.1', '5']

        with patch('sys.argv', test_args), \
             patch('cli.Path.exists', return_value=True), \
             patch('cli.Path.is_file', return_value=True), \
             patch('builtins.open', return_value=io.BytesIO(b'Number,Type,Name\n1,audio,Test\n')), \
             patch('cli.send_csv'):
            exit_code = main()
            assert exit_code == 0

    def test_exit_code_with_errors(self):
        """Test exit code 1 when there are errors"""
        from cli import main

        test_args = ['cli.py', 'test.csv', '127.0.0.1', '5']

        def mock_send_csv_with_errors(ip, document, qlab_version, passcode, error_handler):
            error_handler.handle_errors('error', 'Test error')

        with patch('sys.argv', test_args), \
             patch('cli.Path.exists', return_value=True), \
             patch('cli.Path.is_file', return_value=True), \
             patch('cli.send_csv', side_effect=mock_send_csv_with_errors):
            exit_code = main()
            assert exit_code == 1

    def test_exit_code_file_not_found(self):
        """Test exit code 1 when file not found"""
        from cli import main

        test_args = ['cli.py', 'nonexistent.csv', '127.0.0.1', '5']

        with patch('sys.argv', test_args):
            exit_code = main()
            assert exit_code == 1


class TestErrorHandlerIntegration:
    """Test error handler integration"""

    def test_error_handler_passed_to_send_csv(self):
        """Test that error handler is passed to send_csv"""
        from cli import main
        import io

        test_args = ['cli.py', 'test.csv', '127.0.0.1', '5']

        with patch('sys.argv', test_args), \
             patch('cli.Path.exists', return_value=True), \
             patch('cli.Path.is_file', return_value=True), \
             patch('builtins.open', return_value=io.BytesIO(b'Number,Type,Name\n1,audio,Test\n')), \
             patch('cli.send_csv') as mock_send:
            main()

            call_args = mock_send.call_args
            assert 'error_handler' in call_args[1]
            assert call_args[1]['error_handler'] is not None

    def test_quiet_mode_suppresses_print(self):
        """Test that quiet mode suppresses print statements"""
        from cli import main

        test_args = ['cli.py', 'test.csv', '127.0.0.1', '5', '--quiet']

        def mock_send_csv_with_error(ip, document, qlab_version, passcode, error_handler):
            # This would normally print, but should be suppressed in quiet mode
            error_handler.handle_errors('error', 'Test error')

        with patch('sys.argv', test_args), \
             patch('cli.Path.exists', return_value=True), \
             patch('cli.Path.is_file', return_value=True), \
             patch('cli.send_csv', side_effect=mock_send_csv_with_error), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            # In quiet mode, should not print error details to stdout
            assert 'There was an error' not in output


class TestIntegrationWithRealFiles:
    """Integration tests with real CSV files"""

    def test_with_simple_csv(self):
        """Test with actual simple.csv example file"""
        from cli import main

        example_file = Path(__file__).parent.parent / 'static' / 'example_file' / 'simple.csv'

        if not example_file.exists():
            pytest.skip("Example CSV file not found")

        test_args = ['cli.py', str(example_file), '127.0.0.1', '5']

        with patch('sys.argv', test_args), \
             patch('cli.send_csv') as mock_send:
            exit_code = main()
            assert mock_send.called
            # Verify CSV was properly loaded
            call_args = mock_send.call_args
            assert call_args[1]['document'] is not None


class TestExceptionHandling:
    """Test exception handling"""

    def test_general_exception_handling(self):
        """Test that general exceptions are caught and reported"""
        from cli import main

        test_args = ['cli.py', 'test.csv', '127.0.0.1', '5']

        with patch('sys.argv', test_args), \
             patch('cli.Path.exists', return_value=True), \
             patch('cli.Path.is_file', return_value=True), \
             patch('cli.send_csv', side_effect=Exception('Test error')), \
             patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            exit_code = main()
            assert exit_code == 1
            assert 'error' in mock_stderr.getvalue().lower()

    def test_exception_with_json_output(self):
        """Test exception handling with JSON output"""
        from cli import main

        test_args = ['cli.py', 'test.csv', '127.0.0.1', '5', '--json']

        with patch('sys.argv', test_args), \
             patch('cli.Path.exists', return_value=True), \
             patch('cli.Path.is_file', return_value=True), \
             patch('cli.send_csv', side_effect=Exception('Test error')), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            exit_code = main()
            assert exit_code == 1
            output = mock_stdout.getvalue()
            data = json.loads(output)
            assert 'error' in data
