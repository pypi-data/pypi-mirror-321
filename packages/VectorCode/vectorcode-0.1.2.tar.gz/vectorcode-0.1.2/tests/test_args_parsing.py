import os
from pathlib import Path
import tempfile
from vectorcode import cli_utils


"""
write unittests that works for pytest.
when comparing files and directories, use os.path.samefile 
and take orders into account.
when you complete a test method, add the following comment string: "# completed"
"""


class TestArgs:
    def test_expand_envs_in_dict(self):
        d = {"a": "$HOME", "b": "${USER}", "c": "${PATH}"}
        cli_utils.expand_envs_in_dict(d)
        assert d["a"] == os.environ["HOME"]
        assert d["b"] == os.environ["USER"]
        assert d["c"] == os.environ["PATH"]

    def test_expand_path(self):
        assert cli_utils.expand_path("$HOME") == os.environ["HOME"]
        assert (
            cli_utils.expand_path("${HOME}/.config/vectorcode/config.json")
            == f"{os.environ['HOME']}/.config/vectorcode/config.json"
        )

    def test_find_project_config_dir(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            os.chdir(tmpdir)
            config_dir = cli_utils.find_project_config_dir()
            assert config_dir is None

    def test_expand_globs(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            os.chdir(tmpdir)
            files = ["file1.txt", "file2.txt"]
            for file in files:
                open(file, "w").close()

            globs = [Path("*.txt")]
            expanded_files = cli_utils.expand_globs(globs)
            assert len(expanded_files) == 2
            assert all([os.path.isfile(file) for file in expanded_files])
            assert sorted(files) == sorted(expanded_files)
