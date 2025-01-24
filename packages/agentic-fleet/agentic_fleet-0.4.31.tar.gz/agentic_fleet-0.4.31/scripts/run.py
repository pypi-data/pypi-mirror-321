#!/usr/bin/env python3
import os
import sys
import click
import subprocess
from dotenv import load_dotenv
from pathlib import Path

@click.group()
def cli():
    """AgenticFleet CLI"""
    pass

@cli.command()
def start():
    """Start AgenticFleet with OAuth enabled"""
    run_app(no_oauth=False)

@cli.command()
def no_oauth():
    """Start AgenticFleet without OAuth"""
    run_app(no_oauth=True)

def run_app(no_oauth: bool):
    # Load .env from project root
    env_path = Path(__file__).parent.parent / '.env'
    load_dotenv(env_path)

    app_path = os.path.join(os.path.dirname(__file__), "..", "src", "app", "app.py")

    cmd = ["chainlit", "run", app_path, "--port", "8001"]

    if no_oauth:
        # Only disable OAuth-specific variables
        oauth_vars = [
            "OAUTH_GITHUB_CLIENT_ID",
            "OAUTH_GITHUB_CLIENT_SECRET",
            "OAUTH_PROMPT",
            "OAUTH_GITHUB_PROMPT",
            "OAUTH_USER_PROMPT"
        ]
        for var in oauth_vars:
            if var in os.environ:
                del os.environ[var]
        os.environ["DISABLE_OAUTH"] = "1"

    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    cli()
