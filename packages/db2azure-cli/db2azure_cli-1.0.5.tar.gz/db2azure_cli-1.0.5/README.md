# DB2Azure CLI

`db2az` is a powerful command-line interface (CLI) designed to transfer data from on-premises SQL Server (MSSQL), PostgreSQL, and MySQL databases to Azure Blob Storage. This CLI supports both **interactive** and **non-interactive** modes, allowing for seamless and flexible data migration workflows.

## Features

- **Database Support**: MSSQL, PostgreSQL, and MySQL.
- **Azure Integration**: Uploads data to Azure Blob Storage in JSON or CSV formats.
- **Interactive Mode**: User-friendly prompts to guide through the configuration.
- **Non-Interactive Mode**: Direct execution with command-line options for automation.
- **Logging**: Detailed logs for troubleshooting and monitoring.
- **Error Handling**: Provides descriptive error messages for quick resolution.

## Installation

Ensure Python is installed on your system. Then run the following command in your terminal:

```bash
pip install db2azure db2azure-cli
```

## Usage

The CLI supports two modes:

### Interactive Mode

Run the `db2az` CLI without any command-line options to enter interactive mode. You will be prompted to:

1. Select the database type (MSSQL, PostgreSQL, or MySQL).
2. Provide the source configuration file path (with database connection and query).
3. Provide the destination configuration file path (with Azure Blob Storage settings).
4. Choose the file format (JSON or CSV).

### Non-Interactive Mode

In non-interactive mode, provide all necessary options via the command line:

```bash
> db2az [OPTIONS]
```

#### Options

| Option       | Description                                               |
|--------------|-----------------------------------------------------------|
| `-ms`       | Use MSSQL database                                        |
| `-my`       | Use MySQL database                                        |
| `-pg`       | Use PostgreSQL database                                   |
| `-sf`       | Source config file path (server config)                   |
| `-df`       | Destination config file path (Azure config)               |
| `-csv`      | File format as CSV                                        |
| `-json`     | File format as JSON                                       |
| `-log`      | Directory to save log files                               |

#### Example:

```bash
db2az -ms -sf source_config.json -df azure_config.json -csv -log logs/
```

## Configuration

### Source Configuration File

The source configuration file should include the database connection parameters and query, e.g.:

```json
{
  "connection_params": {
    "host": "localhost",
    "port": "5432",
    "dbname": "SampleDB",
    "user": "username",
    "password": "password"
  },
  "query": "SELECT * FROM public.users"
}
```

### Destination Configuration File

The destination configuration file should include Azure Blob Storage settings, e.g.:

```json
{
  "container_name": "my-container",
  "folder_path": "my-folder",
  "file_name": "data.json",
  "azure_blob_url": "https://<account_name>.blob.core.windows.net",
  "sas_token": "<your_sas_token>"
}
```

## Logging

If the `-log` option is specified, logs will be saved in the specified directory. Logs include information about the execution process, errors, and upload status.

## Error Handling

The CLI provides detailed error messages in case of failures. Example:

```json
{
  "status": "error",
  "message": "Connection failed: Invalid credentials"
}
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions! Feel free to open an issue or submit a pull request for improvements or bug fixes.

## Acknowledgements

- **pyodbc**: For SQL Server connections.
- **psycopg**: For PostgreSQL connections.
- **pymysql**: For MySQL connections.
- **azure-storage-blob**: For Azure Blob Storage integration.