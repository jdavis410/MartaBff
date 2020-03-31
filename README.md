# BFF for Marta Mobile App

Language: Python, Flask

## Deployment:
Required:
  - gcloud cli
  - access to MartaTech Google Cloud Project

To deploy run:
  - $: gcloud app deploy -v VERSION_NUMBER
  - VERSION_NUMBER in format [0-9]\*-[0-9]\*
## Testing:
- pip
- python3
- python venv

1. Set up python virtual environment
2. Run $: pip3 install -r requirements.txt
3. Run $: python3 main.py
    - This will start a virtual server hosted on localhost:8080
