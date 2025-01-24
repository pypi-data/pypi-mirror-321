import pytest
import asyncio
from unittest.mock import patch, MagicMock, AsyncMock
from cursor_agent.tools.web_scraper import validate_url, fetch_page, parse_html, process_urls

@pytest.fixture
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

class TestWebScraper:
    """Test web scraper functionality."""

    @pytest.mark.asyncio
    async def test_fetch_page(self):
        """Test page fetching."""
        mock_context = AsyncMock()
        mock_page = AsyncMock()
        
        mock_context.new_page.return_value = mock_page
        mock_page.content.return_value = "<html><body>Test content</body></html>"
        
        result = await fetch_page("https://example.com", mock_context)
        assert result == "<html><body>Test content</body></html>"
        mock_context.new_page.assert_called_once()
        mock_page.goto.assert_called_once_with("https://example.com")
        mock_page.wait_for_load_state.assert_called_once_with('networkidle')
        mock_page.content.assert_called_once()
        mock_page.close.assert_called_once()

    def test_parse_html(self):
        """Test HTML parsing."""
        html = "<html><body><p>Test content</p><script>alert('test');</script></body></html>"
        result = parse_html(html)
        assert "Test content" in result
        assert "alert" not in result

    @pytest.mark.asyncio
    async def test_process_urls(self):
        """Test URL processing."""
        urls = ["https://example.com", "https://test.com"]
        
        # Create mock objects
        mock_browser = AsyncMock()
        mock_context = AsyncMock()
        mock_playwright = MagicMock()
        mock_playwright.chromium.launch = AsyncMock(return_value=mock_browser)
        mock_browser.new_context = AsyncMock(return_value=mock_context)
        mock_context.new_page = AsyncMock()
        
        # Mock the playwright module
        with patch('playwright.async_api.async_playwright') as mock_playwright_class:
            mock_playwright_class.return_value.__aenter__.return_value = mock_playwright
            mock_playwright_class.return_value.__aexit__ = AsyncMock()
            
            # Mock the fetch_page function
            with patch('cursor_agent.tools.web_scraper.fetch_page') as mock_fetch:
                mock_fetch.side_effect = [
                    "<html><body>Content 1</body></html>",
                    "<html><body>Content 2</body></html>"
                ]
                
                results = await process_urls(urls=urls, max_concurrent=2)
                assert len(results) == 2
                assert "Content 1" in results[0]
                assert "Content 2" in results[1]
                
                await mock_browser.close()
                mock_browser.close.assert_awaited_once()

    def test_validate_url(self):
        """Test URL validation."""
        assert validate_url("https://example.com") is True
        assert validate_url("not_a_url") is False
