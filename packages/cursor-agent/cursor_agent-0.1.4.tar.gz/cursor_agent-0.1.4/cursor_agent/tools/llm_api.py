#!/usr/bin/env /workspace/tmp_windsurf/venv/bin/python3

import google.generativeai as genai
from openai import OpenAI
from anthropic import Anthropic
import argparse
import os
from dotenv import load_dotenv
from pathlib import Path
import sys

def load_environment():
    """Load environment variables from .env files in order of precedence"""
    # Order of precedence:
    # 1. System environment variables (highest priority)
    # 2. .env.local
    # 3. .env
    # 4. .env.example (lowest priority)
    
    env_files = ['.env.example', '.env', '.env.local']
    env_loaded = False
    
    # First, save any existing environment variables
    existing_vars = {}
    for key in ['OPENAI_API_KEY', 'ANTHROPIC_API_KEY', 'DEEPSEEK_API_KEY', 'GOOGLE_API_KEY']:
        if key in os.environ:
            existing_vars[key] = os.environ[key]
    
    for env_file in env_files:
        env_path = Path('.') / env_file
        if env_path.exists():
            # Load new variables but don't override existing ones
            load_dotenv(dotenv_path=env_path, override=False)
            env_loaded = True

            with open(env_path) as f:
                keys = [line.split('=')[0].strip() for line in f if '=' in line and not line.startswith('#')]
    
    # Restore any existing environment variables (highest priority)
    for key, value in existing_vars.items():
        os.environ[key] = value
    
    if not env_loaded:
        print("Warning: No .env files found. Using system environment variables only.", file=sys.stderr)

# Load environment variables at module import
load_environment()

def create_llm_client(provider="openai"):
    if provider == "openai":
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        return OpenAI(
            api_key=api_key
        )
    elif provider == "deepseek":
        api_key = os.getenv('DEEPSEEK_API_KEY')
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY not found in environment variables")
        return OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com/v1",
        )
    elif provider == "anthropic":
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        return Anthropic(
            api_key=api_key
        )
    elif provider == "gemini":
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        genai.configure(api_key=api_key)
        return genai
    elif provider == "local":
        return OpenAI(
            base_url="http://192.168.180.137:8006/v1",
            api_key="not-needed"
        )
    else:
        raise ValueError(f"Unsupported provider: {provider}")

def query_llm(prompt, client=None, model=None, provider="openai"):
    if client is None:
        client = create_llm_client(provider)
    
    try:
        # Set default model
        if model is None:
            if provider == "openai":
                model = "gpt-4o-mini"
            elif provider == "deepseek":
                model = "deepseek-chat"
            elif provider == "anthropic":
                model = "claude-3-sonnet-20240229"
            elif provider == "gemini":
                model = "gemini-pro"
            elif provider == "local":
                model = "Qwen/Qwen2.5-32B-Instruct-AWQ"
            
        if provider == "openai" or provider == "local" or provider == "deepseek":
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
            )
            return response.choices[0].message.content
        elif provider == "anthropic":
            response = client.messages.create(
                model=model,
                max_tokens=1000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text
        elif provider == "gemini":
            model = client.GenerativeModel(model)
            response = model.generate_content(prompt)
            return response.text
    except Exception as e:
        print(f"Error querying LLM: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Query various LLM providers with a prompt')
    parser.add_argument('--prompt', required=True, help='The prompt to send to the LLM')
    parser.add_argument('--provider', choices=['openai', 'anthropic', 'gemini', 'local', 'deepseek'],
                      default='openai', help='The LLM provider to use')
    parser.add_argument('--model', help='Optional specific model to use')
    args = parser.parse_args()
    
    try:
        # Environment variables are already loaded at module import
        # Create client
        client = create_llm_client(args.provider)
        if not client:
            print("Failed to create LLM client", file=sys.stderr)
            sys.exit(1)
            
        # Debug: Print which API key is actually being used
        if args.provider == "openai":
            key = os.getenv('OPENAI_API_KEY')
            
        # Query LLM
        response = query_llm(args.prompt, provider=args.provider, client=client, model=args.model)
        if response:
            print(response)
            sys.exit(0)
        else:
            print("Failed to get response from LLM", file=sys.stderr)
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\nQuery interrupted by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error querying LLM: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
