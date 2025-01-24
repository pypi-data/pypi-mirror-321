import os
import shutil
import tempfile
import pytest
from pathlib import Path
from init_cursor_agent import CursorAgentInitializer

@pytest.fixture
def test_env():
    """Create a test environment with temporary directory."""
    test_dir = tempfile.mkdtemp()
    source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    initializer = CursorAgentInitializer(test_dir, source_dir)
    
    yield test_dir, source_dir, initializer
    
    # Cleanup after test
    shutil.rmtree(test_dir)

def test_create_directory(test_env):
    _, _, initializer = test_env
    test_path = os.path.join(initializer.target_dir, "test_dir")
    initializer.create_directory_if_not_exists(test_path)
    assert os.path.exists(test_path)
    assert os.path.isdir(test_path)

def test_backup_file(test_env):
    _, _, initializer = test_env
    # Create a test file
    test_file = os.path.join(initializer.target_dir, "test.txt")
    with open(test_file, "w") as f:
        f.write("test content")

    initializer.backup_existing_file(test_file)
    backup_files = [f for f in os.listdir(initializer.target_dir) 
                   if f.startswith("test.txt.") and f.endswith(".bak")]
    assert len(backup_files) == 1

def test_copy_file_if_not_exists(test_env):
    _, _, initializer = test_env
    # Create source file
    src_file = os.path.join(initializer.target_dir, "src.txt")
    with open(src_file, "w") as f:
        f.write("test content")

    # Test normal copy
    dst_file = os.path.join(initializer.target_dir, "dst.txt")
    initializer.copy_file_if_not_exists(src_file, dst_file)
    assert os.path.exists(dst_file)

    # Test force copy
    with open(src_file, "w") as f:
        f.write("new content")
    initializer.copy_file_if_not_exists(src_file, dst_file, force=True)
    with open(dst_file, "r") as f:
        assert f.read() == "new content"

def test_check_dependencies(test_env):
    _, _, initializer = test_env
    missing_deps = initializer.check_dependencies()
    assert isinstance(missing_deps, list)

def test_init_cursor_agent_basic(test_env):
    """Test basic initialization without virtual environment."""
    _, _, initializer = test_env
    initializer.init_cursor_agent(skip_venv=True)
    
    # Check if essential directories exist
    assert os.path.exists(os.path.join(initializer.target_dir, "tools"))
    
    # Check if essential files exist
    essential_files = [
        ".cursorrules",
        ".env.example",
        "requirements.txt",
        "tools/llm_api.py",
        "tools/search_engine.py",
        "tools/web_scraper.py",
    ]
    for file in essential_files:
        assert os.path.exists(os.path.join(initializer.target_dir, file)), \
            f"File {file} should exist"

def test_init_cursor_agent_with_force(test_env):
    """Test initialization with force flag."""
    _, _, initializer = test_env
    # First normal initialization
    initializer.init_cursor_agent(skip_venv=True)
    
    # Modify a file
    test_file = os.path.join(initializer.target_dir, ".cursorrules")
    with open(test_file, "w") as f:
        f.write("modified content")
    
    # Force initialization
    initializer.init_cursor_agent(force=True, skip_venv=True)
    
    # Check if backup was created
    backup_files = [f for f in os.listdir(initializer.target_dir) 
                   if f.startswith(".cursorrules.") and f.endswith(".bak")]
    assert len(backup_files) == 1

def test_platform_specific_paths(test_env):
    """Test platform-specific path handling."""
    _, _, initializer = test_env
    python_exec = initializer.get_python_executable()
    pip_exec = initializer.get_pip_executable()
    
    if initializer.platform == "windows":
        assert python_exec.endswith(".exe")
        assert pip_exec.endswith(".exe")
        assert "Scripts" in python_exec
        assert "Scripts" in pip_exec
    else:
        assert not python_exec.endswith(".exe")
        assert not pip_exec.endswith(".exe")
        assert "bin" in python_exec
        assert "bin" in pip_exec 