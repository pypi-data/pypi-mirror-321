import pytest
from unittest.mock import patch, MagicMock
from cursor_agent.tools.search_engine import search

class TestSearchEngine:
    """Test search engine functionality."""

    @patch('cursor_agent.tools.search_engine.logger')
    @patch('cursor_agent.tools.search_engine.DDGS')
    def test_successful_search(self, mock_ddgs, mock_logger):
        """Test successful search."""
        # Mock search results
        mock_results = [
            {
                'link': 'http://example.com',
                'title': 'Example Title',
                'body': 'Example Snippet'
            },
            {
                'link': 'http://example2.com',
                'title': 'Example Title 2',
                'body': 'Example Body 2'
            }
        ]

        # Setup mock
        mock_ddgs_instance = MagicMock()
        mock_ddgs_instance.text.return_value = mock_results
        mock_ddgs.return_value = mock_ddgs_instance

        # Run search
        results = search("test query", max_results=2)

        # Verify results
        assert len(results) == 2
        assert results[0]['link'] == 'http://example.com'
        assert results[0]['title'] == 'Example Title'
        assert results[0]['snippet'] == 'Example Snippet'

    @patch('cursor_agent.tools.search_engine.logger')
    @patch('cursor_agent.tools.search_engine.DDGS')
    def test_no_results(self, mock_ddgs, mock_logger):
        """Test empty search results."""
        # Mock empty results
        mock_ddgs_instance = MagicMock()
        mock_ddgs_instance.text.return_value = []
        mock_ddgs.return_value = mock_ddgs_instance

        # Run search
        results = search("test query")

        # Verify empty results
        assert len(results) == 0

    @patch('cursor_agent.tools.search_engine.logger')
    @patch('cursor_agent.tools.search_engine.DDGS')
    def test_search_error(self, mock_ddgs, mock_logger):
        """Test search error handling."""
        # Mock search error
        mock_ddgs_instance = MagicMock()
        mock_ddgs_instance.text.side_effect = Exception("Test error")
        mock_ddgs.return_value = mock_ddgs_instance

        # Run search and check for empty results on error
        results = search("test query")
        assert len(results) == 0
        mock_logger.error.assert_called_once()

    @patch('cursor_agent.tools.search_engine.logger')
    @patch('cursor_agent.tools.search_engine.DDGS')
    def test_result_field_fallbacks(self, mock_ddgs, mock_logger):
        """Test result field fallbacks."""
        # Mock results with missing fields
        mock_results = [
            {
                'link': 'http://example.com',
                'title': '',  # Missing title
                'body': 'Example Body'
            },
            {
                'link': 'http://example2.com',
                'body': 'Example Body 2'  # Missing title
            }
        ]

        # Setup mock
        mock_ddgs_instance = MagicMock()
        mock_ddgs_instance.text.return_value = mock_results
        mock_ddgs.return_value = mock_ddgs_instance

        # Run search
        results = search("test query")

        # Verify fallbacks
        assert len(results) == 2
        assert results[0]['title'] == ''  # Empty title preserved
        assert results[0]['snippet'] == 'Example Body'
        assert results[1]['title'] == ''  # Missing title defaults to empty string
        assert results[1]['snippet'] == 'Example Body 2'
