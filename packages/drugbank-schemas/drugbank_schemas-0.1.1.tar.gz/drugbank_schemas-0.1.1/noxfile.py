from contextlib import closing
from pathlib import Path

import nox
import requests


@nox.session
def generate_packages(session):
    session.install("requests", "xsdata-pydantic[cli,lxml,soap]")

    # Get the Drugbank schema
    base_path = Path("downloads/schemas")
    base_path.mkdir(exist_ok=True, parents=True)

    drugbank_schemas = {
        "v3.0": "http://go.drugbank.com/docs/drugbank_v3.0.xsd",
        "v4.1": "http://go.drugbank.com/docs/drugbank_v4.1.xsd",
        "v4.2": "http://go.drugbank.com/docs/drugbank_v4.2.xsd",
        "v4.3": "http://go.drugbank.com/docs/drugbank_v4.3.xsd",
        "v4.6": "http://go.drugbank.com/docs/drugbank_v4.6.xsd",
        "v5.0": "http://go.drugbank.com/docs/drugbank_v5.0.xsd",
        "latest": "http://go.drugbank.com/docs/drugbank.xsd"
    }

    for schema_version, schema_url in drugbank_schemas.items():
        try:
            # Download the schema file using requests
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }

            response = requests.get(schema_url, headers=headers, allow_redirects=True)
            response.raise_for_status()  # Raise HTTP errors if any

            schema_path = base_path.joinpath(f"drugbank_{schema_version}.xsd")
            with open(schema_path, "wb") as file:
                file.write(response.content)
            
            print(f"Downloaded drugbank_{schema_version}.xsd successfully.")

            # Generate Pydantic models
            session.run(
                "xsdata",
                "generate",
                str(schema_path),
                "--package",
                "src.drugbank_schemas.models",
            )
        except requests.exceptions.RequestException as e:
            print(f"Failed to download drugbank_{schema_version}.xsd: {e}")
        
        except Exception as e:
            print(f"An error occurred during xsdata generation: {e}")

    # Remove extraneous __init__ file
    init_file = Path("src/__init__.py")
    if init_file.exists():
        init_file.unlink()
