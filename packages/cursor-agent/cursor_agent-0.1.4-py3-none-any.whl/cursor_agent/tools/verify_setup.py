#!/usr/bin/env python3

import os
import sys
import logging
import subprocess
from typing import Dict, List, Tuple
import argparse
import importlib

# Required packages for the agent
REQUIRED_PACKAGES = [
    'playwright',
    'beautifulsoup4',
    'duckduckgo_search',
    'openai',
    'anthropic',
    'google-generativeai'
]

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger(__name__)

def check_python_version() -> Tuple[bool, str]:
    """Check if Python version is compatible."""
    import platform
    version = platform.python_version_tuple()
    if int(version[0]) < 3 or (int(version[0]) == 3 and int(version[1]) < 8):
        return False, f"Python 3.8+ required, found {platform.python_version()}"
    return True, f"Python version {platform.python_version()} OK"

def check_playwright() -> Tuple[bool, str]:
    """Check if Playwright and browsers are installed."""
    try:
        import playwright
        from playwright.sync_api import sync_playwright
        
        # Check if browser is installed
        with sync_playwright() as p:
            try:
                browser = p.chromium.launch()
                browser.close()
                return True, "Playwright and Chromium browser OK"
            except Exception as e:
                return False, f"Playwright browser error: {str(e)}"
    except ImportError:
        return False, "Playwright not installed"
    except Exception as e:
        return False, f"Playwright error: {str(e)}"

def check_api_keys() -> List[Tuple[str, bool, str]]:
    """Check if required API keys are set."""
    keys = [
        ('OPENAI_API_KEY', 'OpenAI'),
        ('ANTHROPIC_API_KEY', 'Anthropic'),
        ('DEEPSEEK_API_KEY', 'DeepSeek'),
        ('GOOGLE_API_KEY', 'Google')
    ]
    
    results = []
    for env_var, provider in keys:
        value = os.environ.get(env_var)
        if value:
            results.append((provider, True, f"{provider} API key found"))
        else:
            results.append((provider, False, f"{provider} API key not found"))
    return results

def check_dependencies() -> List[Tuple[str, bool, str]]:
    """Check if required Python packages are installed."""
    required_packages = [
        'duckduckgo_search',
        'html5lib',
        'playwright',
        'openai',
        'anthropic',
        'google-generativeai'
    ]
    
    results = []
    for package in required_packages:
        try:
            __import__(package)
            results.append((package, True, f"{package} OK"))
        except ImportError:
            results.append((package, False, f"{package} not installed"))
    return results

def verify_all() -> bool:
    """
    Verify all components of the setup.
    Returns True if all checks pass, False otherwise.
    """
    all_passed = True
    
    # Check Python version
    python_ok, python_msg = check_python_version()
    logger.info(python_msg)
    all_passed &= python_ok
    
    # Check Playwright
    playwright_ok, playwright_msg = check_playwright()
    logger.info(playwright_msg)
    all_passed &= playwright_ok
    
    # Check API keys
    logger.info("\nChecking API keys:")
    for provider, ok, msg in check_api_keys():
        logger.info(f"  {msg}")
        # Don't fail if some API keys are missing
    
    # Check dependencies
    logger.info("\nChecking dependencies:")
    for package, ok, msg in check_dependencies():
        logger.info(f"  {msg}")
        all_passed &= ok
    
    return all_passed

def verify_main():
    """Main function for the verify command."""
    parser = argparse.ArgumentParser(description='Verify Cursor Agent setup')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    args = parser.parse_args()

    try:
        # Run verification
        success = verify_all()
        if success:
            print("All dependencies verified successfully!")
            sys.exit(0)
        else:
            print("Verification failed", file=sys.stderr)
            sys.exit(1)

    except Exception as e:
        if args.verbose:
            logger.exception("Error during verification")
        else:
            logger.error(f"Error during verification: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    verify_main() 