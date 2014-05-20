import unittest
import os

from jdpylib import file
from jdpylib import errors

class TestFileHelpers(unittest.TestCase):

    def setUp(self):
        # Create a test file
        self.sample_file_name = 'sample_file.txt'
        self.sample_file_contents = "sample_file.txt\nthis is line 2"
        # Additional filename to use for testing write functions
        self.new_file_name = 'sample_file2.txt'
        with open(self.sample_file_name, 'w') as f:
            f.write(self.sample_file_contents)

    def tearDown(self):
        os.remove(self.sample_file_name)
        # Delete newly written file, if exists
        if os.path.lexists(self.new_file_name):
            os.remove(self.new_file_name)

    def test_read_nonexistent_path_raises_InvalidPath_error(self):
        with self.assertRaises(errors.InvalidPath):
            file.read('/foo/bar/NonExistentFile.txt')


    def test_read_returns_file_contents(self):
        contents = file.read(self.sample_file_name)
        self.assertEqual(contents, self.sample_file_contents,
            "Failed to read file contents - expected '{}', got '{}'".format(
                self.sample_file_contents, contents))

    def test_file_write_fails_if_file_exists_no_overwrite_flag(self):
        with self.assertRaises(errors.FileExistsNoOverwrite):
            file.write(self.sample_file_name, "test contents")

    def test_file_write_succeeds_if_file_exists_and_overwrite_is_true(self):
        new_content = "New Content!"
        file.write(self.sample_file_name, new_content, overwrite=True)
        with open(self.sample_file_name, 'r') as f:
            output = f.read()
        self.assertEqual(output, new_content,
            "Write failed - Expected to read '{}', got '{}'".format(
                new_content, output))
