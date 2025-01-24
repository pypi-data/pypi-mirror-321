import click
import yaml
from .yaml_reader import yaml_reader
from .templates.django_template.Setup.DjangoProjectCreator import DjangoProjectCreator
from .templates.flask_template.Setup.create_project_structure import FlaskProjectCreator

@click.command()
@click.option("--project-name", help="Define the project name.")
@click.option("--framework", default="none", help="Project's framework (e.g., flask, django, etc.).")
@click.option("--port", type=int, default=5000, help="Project port number.")
@click.option("--image-version", default="latest", help="Version of the Docker image (e.g., latest, 16, 3.11).")
@click.option("--db-type", default="none", help="Database type (e.g., mysql, postgresql, etc.).")
@click.option("--db-version", default="latest", help="Database version (e.g., latest, 12, 14).")
@click.option("--db-name", help="Database name (e.g., my_db, etc.).")
@click.option("--db-user", help="Database user's username.")
@click.option("--db-password", help="Database user's password.")
@click.option("--db-port", type=int,  help="Database port number (default is 5432).")
@click.option("--config", type=click.Path(exists=True), help="Path to the config YAML file for configuration.")
def generate_project(project_name, framework, port, image_version, db_type, db_version, db_name, db_user, db_password,  db_port, config):
    """
    Generate a project based on the CLI options and/or a YAML configuration file.
    
    This function checks if a configuration file is provided; if so, it overrides
    the CLI options with values from the configuration file.
    Then, it proceeds to create the project using the specified framework and database settings.
    """
    try:
        # Read configuration from YAML file if provided, else use default empty dictionary
        yaml_config = yaml_reader.read(config) if config else {}

        # Override CLI options with YAML file values if available
        project_name = project_name or yaml_config.get("project_name", "my_project")
        framework = framework or yaml_config.get("framework", "")
        port = port or yaml_config.get("port", 5000)
        image_version = image_version or yaml_config.get("image_version", "latest")
        db_type = db_type or yaml_config.get("db_type", "none")
        db_version = db_version or yaml_config.get("db_version", "latest")
        db_name = db_name or yaml_config.get("db_name", "my_db")
        db_user = db_user or yaml_config.get("db_user", "admin")
        db_password = db_password or yaml_config.get("db_password", "admin")
        db_port = db_port or yaml_config.get("db_port", 5432)

        # Print configuration summary
        print(f"Starting the creation of project: {project_name}")
        print(f"Framework: {framework.capitalize()} | Port: {port} | Image Version: {image_version}")
        print(f"Database: {db_type.capitalize()} | Version: {db_version} | Name: {db_name}")

        # Create project based on selected framework
        if framework.lower() == "flask":
            print("Initializing Flask project setup...")
            creator = FlaskProjectCreator(project_name, port, image_version)
            creator.create_project()
            print(f"Flask project '{project_name}' created successfully.")
        elif framework.lower() == "django":
            print("Initializing Django project setup...")
            creator = DjangoProjectCreator(
                project_name, port, image_version, db_type, db_version, db_name, db_user, db_password, db_port
            )
            creator.create_project()
            print(f"Django project '{project_name}' created successfully.")
        else:
            print(f"Error: Framework '{framework}' is not supported. Please choose 'flask' or 'django'.")

    except Exception as err:
        print(f"Error: {err}")
        print("Project creation failed due to the error mentioned above.")
        raise

if __name__ == "__main__":
    main()
