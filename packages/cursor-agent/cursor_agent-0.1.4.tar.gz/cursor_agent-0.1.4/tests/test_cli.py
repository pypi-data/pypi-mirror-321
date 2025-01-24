import os
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from cursor_agent.main import CursorAgentInitializer, main as agent_main
from cursor_agent.tools.llm_api import main as llm_main
from cursor_agent.tools.web_scraper import main as scrape_main
from cursor_agent.tools.search_engine import main as search_main
from cursor_agent.tools.update_cursor_agent import main as update_main
from cursor_agent.tools.verify_setup import verify_main
from cursor_agent.tools.generate_changelog import changelog_main
import sys

@pytest.fixture
def temp_dir(tmp_path):
    """Provide a temporary directory for testing."""
    return tmp_path

class TestCursorAgent:
    def test_init_new_directory(self, temp_dir):
        """Test initializing cursor-agent in a new directory."""
        with patch('sys.argv', ['cursor-agent', str(temp_dir)]):
            result = agent_main()
            assert result == 0
            assert (temp_dir / '.cursorrules').exists()
            assert (temp_dir / '.env.example').exists()
            assert (temp_dir / 'requirements.txt').exists()
            assert (temp_dir / 'venv').exists()

    def test_init_force_overwrite(self, temp_dir):
        """Test force overwriting existing files."""
        # Create existing files
        (temp_dir / '.cursorrules').write_text('old content')
        
        with patch('sys.argv', ['cursor-agent', str(temp_dir), '--force']):
            result = agent_main()
            assert result == 0
            assert (temp_dir / '.cursorrules').exists()
            assert (temp_dir / '.cursorrules.bak').exists()

    def test_init_skip_venv(self, temp_dir):
        """Test initialization without virtual environment."""
        with patch('sys.argv', ['cursor-agent', str(temp_dir), '--skip-venv']):
            result = agent_main()
            assert result == 0
            assert not (temp_dir / 'venv').exists()

class TestLLMCLI:
    @patch('cursor_agent.tools.llm_api.query_llm')
    @patch('cursor_agent.tools.llm_api.create_llm_client')
    def test_llm_basic_query(self, mock_create_client, mock_query, mock_response):
        """Test basic LLM query."""
        mock_query.return_value = mock_response['choices'][0]['message']['content']
        mock_client = MagicMock()
        mock_create_client.return_value = mock_client
        with patch('sys.argv', ['cursor-llm', '--prompt', 'Hello']):
            with pytest.raises(SystemExit) as exc_info:
                llm_main()
            assert exc_info.value.code == 0
            mock_query.assert_called_once_with('Hello', provider='openai', client=mock_client, model=None)

    @patch('cursor_agent.tools.llm_api.query_llm')
    @patch('cursor_agent.tools.llm_api.create_llm_client')
    def test_llm_provider_selection(self, mock_create_client, mock_query, mock_response):
        """Test LLM provider selection."""
        mock_query.return_value = mock_response['choices'][0]['message']['content']
        mock_client = MagicMock()
        mock_create_client.return_value = mock_client
        with patch('sys.argv', ['cursor-llm', '--prompt', 'Hello', '--provider', 'anthropic']):
            with pytest.raises(SystemExit) as exc_info:
                llm_main()
            assert exc_info.value.code == 0
            mock_query.assert_called_once_with('Hello', provider='anthropic', client=mock_client, model=None)

class TestWebScraperCLI:
    @patch('cursor_agent.tools.web_scraper.process_urls')
    def test_scrape_single_url(self, mock_scrape, mock_scrape_result):
        """Test scraping a single URL."""
        mock_scrape.return_value = [mock_scrape_result['https://example.com']]
        with patch('sys.argv', ['cursor-scrape', 'https://example.com']):
            with pytest.raises(SystemExit) as exc_info:
                scrape_main()
            assert exc_info.value.code == 0
            mock_scrape.assert_called_once_with(urls=['https://example.com'], max_concurrent=3)

    @patch('cursor_agent.tools.web_scraper.process_urls')
    def test_scrape_multiple_urls(self, mock_scrape, mock_scrape_result):
        """Test scraping multiple URLs."""
        mock_scrape.return_value = list(mock_scrape_result.values())
        urls = list(mock_scrape_result.keys())
        with patch('sys.argv', ['cursor-scrape'] + urls):
            with pytest.raises(SystemExit) as exc_info:
                scrape_main()
            assert exc_info.value.code == 0
            mock_scrape.assert_called_once_with(urls=urls, max_concurrent=3)

class TestSearchEngineCLI:
    @patch('cursor_agent.tools.search_engine.search')
    def test_basic_search(self, mock_search, mock_search_result):
        """Test basic search functionality."""
        mock_search.return_value = mock_search_result
        with patch('sys.argv', ['cursor-search', 'test query']):
            with pytest.raises(SystemExit) as exc_info:
                search_main()
            assert exc_info.value.code == 0
            mock_search.assert_called_once_with(query='test query', max_results=10)

    @patch('cursor_agent.tools.search_engine.search')
    def test_search_with_max_results(self, mock_search, mock_search_result):
        """Test search with max results parameter."""
        mock_search.return_value = mock_search_result
        with patch('sys.argv', ['cursor-search', '--max-results', '5', 'test query']):
            with pytest.raises(SystemExit) as exc_info:
                search_main()
            assert exc_info.value.code == 0
            mock_search.assert_called_once_with(query='test query', max_results=5)

class TestUpdateCLI:
    @patch('cursor_agent.tools.update_cursor_agent.update_cursor_agent')
    def test_basic_update(self, mock_update):
        """Test basic update functionality."""
        mock_update.return_value = True
        with patch('sys.argv', ['cursor-update']):
            with pytest.raises(SystemExit) as exc_info:
                update_main()
            assert exc_info.value.code == 0
            mock_update.assert_called_once_with(force=False)

    @patch('cursor_agent.tools.update_cursor_agent.update_cursor_agent')
    def test_force_update(self, mock_update):
        """Test force update functionality."""
        mock_update.return_value = True
        with patch('sys.argv', ['cursor-update', '--force']):
            with pytest.raises(SystemExit) as exc_info:
                update_main()
            assert exc_info.value.code == 0
            mock_update.assert_called_once_with(force=True)

class TestVerifyCLI:
    """Test verify CLI functionality."""

    @patch('cursor_agent.tools.verify_setup.verify_all')
    @patch('cursor_agent.tools.verify_setup.logger')
    @patch('cursor_agent.tools.verify_setup.argparse.ArgumentParser')
    def test_basic_verify(self, mock_parser_class, mock_logger, mock_verify):
        """Test basic verify functionality."""
        # Setup mock verify
        mock_verify.return_value = True
        
        # Setup mock parser
        mock_parser = MagicMock()
        mock_parser.parse_args.return_value = MagicMock(verbose=False)
        mock_parser_class.return_value = mock_parser
        
        # Save and restore sys.argv
        old_argv = sys.argv
        sys.argv = ['cursor-verify']
        try:
            with pytest.raises(SystemExit) as exc_info:
                verify_main()
            assert exc_info.value.code == 0
            mock_verify.assert_called_once()
            # We don't need to check logger.info since it's called inside verify_all
            # which we've mocked
        finally:
            sys.argv = old_argv

    @patch('cursor_agent.tools.verify_setup.verify_all')
    @patch('cursor_agent.tools.verify_setup.logger')
    @patch('cursor_agent.tools.verify_setup.argparse.ArgumentParser')
    def test_verify_failure(self, mock_parser_class, mock_logger, mock_verify):
        """Test verify failure case."""
        # Setup mock verify
        mock_verify.return_value = False
        
        # Setup mock parser
        mock_parser = MagicMock()
        mock_parser.parse_args.return_value = MagicMock(verbose=False)
        mock_parser_class.return_value = mock_parser
        
        # Save and restore sys.argv
        old_argv = sys.argv
        sys.argv = ['cursor-verify']
        try:
            with pytest.raises(SystemExit) as exc_info:
                verify_main()
            assert exc_info.value.code == 1
            mock_verify.assert_called_once()
            # We don't need to check logger.info since it's called inside verify_all
            # which we've mocked
        finally:
            sys.argv = old_argv

class TestChangelogCLI:
    @patch('cursor_agent.tools.generate_changelog.generate_changelog')
    def test_basic_changelog(self, mock_generate):
        """Test basic changelog generation."""
        mock_generate.return_value = "Test changelog"
        with patch('sys.argv', ['cursor-changelog']):
            with pytest.raises(SystemExit) as exc_info:
                changelog_main()
            assert exc_info.value.code == 0
            mock_generate.assert_called_once()

    @patch('cursor_agent.tools.generate_changelog.generate_changelog')
    def test_changelog_update(self, mock_generate):
        """Test changelog update functionality."""
        mock_generate.return_value = "Test changelog"
        with patch('sys.argv', ['cursor-changelog', '--update']):
            with pytest.raises(SystemExit) as exc_info:
                changelog_main()
            assert exc_info.value.code == 0
            mock_generate.assert_called_once() 