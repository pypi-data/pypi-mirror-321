# First cell in the notebook
"""
# Install the required packages
!pip install --upgrade python-dotenv aiq-platform-api
"""

# Second cell in the notebook
"""
# load your .env file to colab environment or set the environment variables manually (not recommended)
# import os
# 
# ATTACKIQ_PLATFORM_URL= os.environ["ATTACKIQ_PLATFORM_URL"] = "https://firedrill.attackiq.com"
# ATTACKIQ_API_TOKEN = os.environ["ATTACKIQ_API_TOKEN"] = "your_token_here"
"""
import itertools  # noqa: F401, E402
import os  # noqa: F401, E402
import sys  # noqa: F401, E402
import time  # noqa: F401, E402
from datetime import datetime, timedelta  # noqa: F401, E402
from typing import Optional, Dict, Any, List  # noqa: F401, E402

from dotenv import load_dotenv  # noqa: E402

load_dotenv()


def get_env_vars():
    platform_url = os.environ.get("ATTACKIQ_PLATFORM_URL")
    api_token = os.environ.get("ATTACKIQ_API_TOKEN")

    if not platform_url or not api_token:
        if "pytest" not in sys.modules:
            # Only exit if not running tests
            if not platform_url:
                print("Error: ATTACKIQ_PLATFORM_URL environment variable is not set.")
            if not api_token:
                print("Error: ATTACKIQ_API_TOKEN environment variable is not set.")
            sys.exit(1)

    return platform_url or "https://firedrill.attackiq.com", api_token or "test-token"


ATTACKIQ_PLATFORM_URL, ATTACKIQ_API_TOKEN = get_env_vars()
