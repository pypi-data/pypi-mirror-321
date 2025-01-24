# Devin.cursorrules

Transform your $20 Cursor/Windsurf into a Devin-like experience in one minute! This repository contains configuration files and tools that enhance your Cursor or Windsurf IDE with advanced agentic AI capabilities similar to Devin, including:

- Process planning and self-evolution
- Extended tool usage (web browsing, search, LLM-powered analysis)
- Automated execution (for Windsurf in Docker containers)

[![Tests](https://github.com/yourusername/devin.cursorrules/actions/workflows/test.yml/badge.svg)](https://github.com/yourusername/devin.cursorrules/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/yourusername/devin.cursorrules/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/devin.cursorrules)
[![PyPI version](https://badge.fury.io/py/cursor-agent.svg)](https://badge.fury.io/py/cursor-agent)
[![Python versions](https://img.shields.io/pypi/pyversions/cursor-agent.svg)](https://pypi.org/project/cursor-agent/)

## Installation

You can install cursor-agent using pip:

```bash
# Install from PyPI
pip install cursor-agent

# Initialize in current directory
cursor-agent

# Or specify a target directory
cursor-agent /path/to/project
```

### Using Docker

You can also run cursor-agent using Docker:

```bash
# Using docker directly
docker run -v $(pwd):/workspace -e OPENAI_API_KEY=your_key cursor-agent /workspace

# Or using docker-compose
export TARGET_DIR=$(pwd)  # Directory to initialize
export OPENAI_API_KEY=your_key  # Your API keys
docker-compose up
```

Available environment variables:
- `TARGET_DIR`: Directory to initialize (default: current directory)
- `OPENAI_API_KEY`: OpenAI API key
- `ANTHROPIC_API_KEY`: Anthropic API key
- `DEEPSEEK_API_KEY`: DeepSeek API key
- `GOOGLE_API_KEY`: Google API key

### Staying Updated

To get the latest version:

```bash
# Check and update to latest version
python -m cursor_agent.update

# Force update even if current version is up to date
python -m cursor_agent.update --force
```

## Quick Start

The easiest way to add Cursor agent capabilities to your project is using the initialization script:

```bash
# Initialize in current directory
python init_cursor_agent.py

# Or specify a target directory
python init_cursor_agent.py /path/to/project

# Force overwrite existing files (creates backups)
python init_cursor_agent.py --force

# Skip virtual environment creation
python init_cursor_agent.py --skip-venv
```

The script will:
1. Copy necessary configuration files
2. Set up Python virtual environment
3. Install required dependencies
4. Configure environment variables

## Manual Setup

If you prefer manual setup, follow these steps:

1. Create Python virtual environment:
```bash
# Create a virtual environment in ./venv
python3 -m venv venv

# Activate the virtual environment
# On Unix/macOS:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
```

2. Configure environment variables:
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your API keys and configurations
```

3. Install dependencies:
```bash
# Install required packages
pip install -r requirements.txt

# Install Playwright's Chromium browser (required for web scraping)
python -m playwright install chromium
```

## Tools Included

- Web scraping with JavaScript support (using Playwright)
- Search engine integration (DuckDuckGo)
- LLM-powered text analysis
- Process planning and self-reflection capabilities

## Development

### Running Tests

The project uses pytest for testing. To run tests:

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests with coverage
pytest

# Run specific test file
pytest tests/test_init_cursor_agent.py

# Run tests excluding slow ones
pytest -m "not slow"

# Run only unit tests
pytest -m unit
```

### Continuous Integration

The project uses GitHub Actions for continuous integration, running tests on:
- Multiple Python versions (3.8, 3.9, 3.10, 3.11)
- Multiple operating systems (Ubuntu, Windows, macOS)

The CI pipeline:
1. Runs all tests
2. Generates coverage reports
3. Uploads coverage to Codecov
4. Fails if coverage drops below threshold

### Changelog

The project uses automated changelog generation based on conventional commits.

1. **Commit Message Format**:
   ```
   type(scope): description
   
   [optional body]
   [optional footer]
   ```
   
   Types:
   - `feat`: New feature
   - `fix`: Bug fix
   - `docs`: Documentation
   - `style`: Formatting
   - `refactor`: Code restructuring
   - `perf`: Performance improvement
   - `test`: Tests
   - `build`: Build system
   - `ci`: CI/CD
   - `chore`: Maintenance

2. **Generate Changelog**:
   ```bash
   # Preview changelog
   python tools/generate_changelog.py
   
   # Update CHANGELOG.md
   python tools/generate_changelog.py --update
   
   # Specify version
   python tools/generate_changelog.py --version v1.0.0
   ```

3. **Automated Generation**:
   - Changelog is automatically generated on new releases
   - Generated from commits since last tag
   - Categorized by commit type
   - Included in GitHub release notes

### Deployment

The project supports multiple deployment methods:

1. **PyPI Package**:
   ```bash
   # Install latest release
   pip install cursor-agent
   
   # Install specific version
   pip install cursor-agent==1.0.0
   ```

2. **Docker Container**:
   ```bash
   # Build locally
   docker build -t cursor-agent .
   
   # Run with volume mount
   docker run -v /path/to/project:/workspace cursor-agent
   ```

3. **Manual Setup**:
   ```bash
   git clone https://github.com/yourusername/devin.cursorrules.git
   cd devin.cursorrules
   python init_cursor_agent.py /path/to/project
   ```

### Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests locally (`pytest`)
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## Background

For detailed information about the motivation and technical details behind this project, check out the blog post: [Turning $20 into $500 - Transforming Cursor into Devin in One Hour](https://yage.ai/cursor-to-devin-en.html)

## License

MIT License
