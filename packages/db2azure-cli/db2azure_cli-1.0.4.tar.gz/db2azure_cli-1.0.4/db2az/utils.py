import json
from db2azure import MSSQLLoader, PostgreLoader, MySQLLoader
from tabulate import tabulate

def load_config(file_path):
    """Load JSON configuration from a file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def get_loader_class(db_type):
    """Return the appropriate loader class based on the database type."""
    db_loader_map = {
        'MSSQL': MSSQLLoader,
        'PostgreSQL': PostgreLoader,
        'MySQL': MySQLLoader
    }
    return db_loader_map.get(db_type)

def perform_upload(loader_class, query, connection_params, azure_config, file_format):
    """Perform the actual upload using the appropriate loader class (MSSQL, PostgreSQL, or MySQL)."""
    if file_format == "JSON":
        return loader_class.load_to_json(query, connection_params, azure_config)
    elif file_format == "CSV":
        return loader_class.load_to_csv(query, connection_params, azure_config)

def display_success(status):
    """Display the success message in tabular format."""
    success_data = [
        ["Status", status.get("status")],
        ["Container", status.get("container_name")],
        ["Folder Path", status.get("folder_path")],
        ["File Name", status.get("file_name")],
        ["Records Uploaded", status.get("rows_uploaded")]
    ]
    print(tabulate(success_data, tablefmt="fancy_grid"))