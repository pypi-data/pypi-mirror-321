import typer
import inquirer
import time
import os
import logging
from yaspin import yaspin
import pyfiglet
from db2az.utils import DB2AzureUtils

class DB2AzureCLI:
    """Main CLI tool for DB2Azure."""

    def __init__(self):
        self.app = typer.Typer()
        self.utils = DB2AzureUtils()
        self.app.command()(self.run_cli)

    def setup_logger(self, log_dir: str):
        """Set up logging to a specified directory."""
        log_file = os.path.join(log_dir, f"db2azure_{time.strftime('%Y%m%d_%H%M%S')}.log")
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        logging.info("Logger initialized")
        return log_file

    def print_banner(self):
        """Print the banner for the CLI tool."""
        print(pyfiglet.figlet_format("DB2Azure CLI"))

    def prompt_for_missing_inputs(self, db_type, source_file, destination_file, file_format):
        """Prompt user for missing inputs."""
        if not db_type:
            db_type = inquirer.prompt([
                inquirer.List(
                    'db_type',
                    message="Choose the database type",
                    choices=['MSSQL', 'PostgreSQL', 'MySQL'],
                ),
            ])['db_type']

        if not source_file:
            source_file = typer.prompt("Enter the source file path (contains connection string and query)")

        if not destination_file:
            destination_file = typer.prompt("Enter the destination file path (contains Azure configuration)")

        if not file_format:
            file_format = inquirer.prompt([
                inquirer.List(
                    'file_format',
                    message="Choose the file format",
                    choices=['CSV', 'JSON'],
                ),
            ])['file_format']

        return db_type, source_file, destination_file, file_format

    def run_cli(self,
                ms: bool = typer.Option(False, "-ms", help="Use MSSQL database"),
                my: bool = typer.Option(False, "-my", help="Use MySQL database"),
                pg: bool = typer.Option(False, "-pg", help="Use PostgreSQL database"),
                sf: str = typer.Option(None, "-sf", help="Source config file path (server config)"),
                df: str = typer.Option(None, "-df", help="Destination config file path (Azure config)"),
                csv: bool = typer.Option(False, "-csv", help="File format as CSV"),
                json_format: bool = typer.Option(False, "-json", help="File format as JSON"),
                log: str = typer.Option(None, "-log", help="Directory to save log files")):
        is_interactive = not any([ms, my, pg, sf, df, csv, json_format, log])

        if is_interactive:
            self.print_banner()

        db_type = "MSSQL" if ms else "MySQL" if my else "PostgreSQL" if pg else None
        file_format = "CSV" if csv else "JSON" if json_format else None

        db_type, source_file, destination_file, file_format = (
            self.prompt_for_missing_inputs(db_type, sf, df, file_format)
            if is_interactive else (db_type, sf, df, file_format)
        )

        log_file = None
        if log:
            if not os.path.exists(log):
                os.makedirs(log)
            log_file = self.setup_logger(log)
            logging.info("Starting DB2Azure CLI process")

        try:
            logging.info("Loading configurations")
            azure_config = self.utils.load_config(destination_file)
            source_config = self.utils.load_config(source_file)

            query = source_config.get('query')
            connection_params = source_config.get('connection_params')

            if log:
                logging.info(f"Loaded source config: {source_file}")
                logging.info(f"Loaded destination config: {destination_file}")
                logging.info(f"Database type: {db_type}")
                logging.info(f"File format: {file_format}")

            logging.info("Getting loader class")
            loader_class = self.utils.get_loader_class(db_type)

            if is_interactive:
                with yaspin(text="Uploading file to Azure", color="green") as spinner:
                    logging.info("Performing upload")
                    time.sleep(2)
                    status = self.utils.perform_upload(loader_class, query, connection_params, azure_config, file_format)
                    if status.get("status") == "success":
                        spinner.ok("✅")
                        self.utils.display_success(status)
                        if log:
                            logging.info("Upload successful")
                            logging.info(f"Status: {status}")
                    else:
                        spinner.fail("❌")
                        if log:
                            logging.error("Upload failed")
                            logging.error(f"Status: {status}")
            else:
                logging.info("Performing upload (non-interactive mode)")
                status = self.utils.perform_upload(loader_class, query, connection_params, azure_config, file_format)
                if status.get("status") == "success":
                    if log:
                        logging.info("Upload successful")
                        logging.info(f"Status: {status}")
                else:
                    if log:
                        logging.error("Upload failed")
                        logging.error(f"Status: {status}")
                    raise Exception("Upload failed. Check logs for more details.")

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            if log:
                logging.exception(error_message)
            if is_interactive:
                print(error_message)
            raise typer.Exit(code=1)

        if is_interactive and log:
            print(f"Log file saved to: {log_file}")

if __name__ == "__main__":
    cli = DB2AzureCLI()
    cli.app()