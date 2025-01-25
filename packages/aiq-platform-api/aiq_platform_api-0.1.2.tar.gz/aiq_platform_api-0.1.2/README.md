# AttackIQ Platform API Utilities

⚠️ **BETA / WORK IN PROGRESS** ⚠️

This package provides utility functions for interacting with the AttackIQ Platform API.

## Status

This project is currently in beta and under active development. Features and APIs may change without notice. Feedback and contributions are welcome!

## Installation

```bash
pip install aiq-platform-api
```

## Examples

To get started quickly with the example code:

1. Copy the example files to your project:
```bash
cp examples/basic_usage.py your-project/
cp examples/.env.example your-project/.env
```

2. Configure your credentials:
```bash
# Edit .env file with your AttackIQ Platform credentials
vim .env
```

3. Install required packages:
```bash
pip install aiq-platform-api python-dotenv
```

4. Run the example:
```bash
python basic_usage.py
```

## Basic Usage

```python
from aiq_platform_api import assessment_use_cases

assessment_use_cases.get_assessment_use_cases()
```

## Contributing

We welcome feedback and contributions! Please feel free to:
- Open issues for bugs or feature requests
- Submit pull requests
- Provide feedback on the API design

## License

MIT License - See LICENSE file for details