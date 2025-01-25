import click
import requests
import os
from pathlib import Path


@click.command()
def cli():
    """Main entry point for the CLI."""
    click.echo("Welcome to Techtonique CLI!")

# # Help
# python3 cli/cli.py --help
# python3 cli/cli.py forecasting --help
# python3 cli/cli.py forecasting univariate --help
# python3 cli/cli.py ml --help
# python3 cli/cli.py ml classification --help
# python3 cli/cli.py reserving --help
# python3 cli/cli.py survival --help
# # Univariate forecasting
# python3 cli/cli.py forecasting univariate /Users/t/Documents/datasets/time_series/univariate/a10.csv --base_model RidgeCV --h 3
# # Multivariate forecasting
# python3 cli/cli.py forecasting multivariate /Users/t/Documents/datasets/time_series/multivariate/ice_cream_vs_heater.csv --lags 25 --h 10
# # Classification
# python3 cli/cli.py ml classification /Users/t/Documents/datasets/tabular/classification/iris_dataset2.csv --base_model RandomForestRegressor
# # Regression
# python3 cli/cli.py ml regression /Users/t/Documents/datasets/tabular/regression/mtcars2.csv --base_model ElasticNet
# # Chain Ladder
# python3 cli/cli.py reserving chainladder /Users/t/Documents/datasets/tabular/triangle/abc.csv
# # Mack Chain Ladder
# python3 cli/cli.py reserving mack /Users/t/Documents/datasets/tabular/triangle/abc.csv
# # Survival Analysis
# python3 cli/cli.py survival /Users/t/Documents/datasets/tabular/survival/kidney.csv --model coxph
class TechtoniqueCLI:
    def __init__(self, token=None):
        self.base_url = "https://www.techtonique.net"
        self.token = input(
            "Enter your API token (or press Enter to use the environment variable): "
        ) or os.getenv("TECHTONIQUE_API_TOKEN")
        if not self.token:
            raise ValueError(
                "API token must be provided or set in TECHTONIQUE_API_TOKEN environment variable"
            )

    def _make_request(self, endpoint, file_path, params):
        headers = {"Authorization": f"Bearer {self.token}"}
        try:
            with open(file_path, "rb") as f:
                files = {"file": (file_path.name, f, "text/csv")}
                response = requests.post(
                    f"{self.base_url}/{endpoint}",
                    headers=headers,
                    files=files,
                    params=params,
                )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            click.echo(f"Error making request: {e}")
            return None


def init_cli(ctx):
    """Initialize CLI if not in help mode"""
    if ctx.obj is None:
        ctx.ensure_object(dict)

    if "--help" not in ctx.args and "-h" not in ctx.args:
        token = ctx.obj.get("token")
        if "cli" not in ctx.obj:
            try:
                ctx.obj["cli"] = TechtoniqueCLI(token)
            except ValueError as e:
                click.echo(str(e), err=True)
                ctx.exit(1)


@click.group()
@click.option("--token", envvar="TECHTONIQUE_API_TOKEN", help="API token", required=False)
@click.pass_context
def cli(ctx, token):
    """Techtonique API CLI tool"""
    ctx.ensure_object(dict)
    ctx.obj["token"] = token


@cli.group()
@click.pass_context
def forecasting(ctx):
    """Forecasting commands"""
    pass


@forecasting.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--base_model", default="RidgeCV", help="Base model to use")
@click.option("--n-hidden-features", default=5, help="Number of hidden features")
@click.option("--lags", default=25, help="Number of lags")
@click.option("--type-pi", default="kde", help="Type of prediction interval")
@click.option("--replications", default=4, help="Number of replications")
@click.option("--h", default=3, help="Forecast horizon")
@click.pass_context
def univariate(ctx, file, base_model, n_hidden_features, lags, type_pi, replications, h):
    """Univariate forecasting

    Parameters:
        file: str
            Path to the CSV file
        base_model: str
            Base model to use
        n_hidden_features: int
            Number of hidden features
        lags: int
            Number of lags
        type_pi: str
            Type of prediction interval
        replications: int
            Number of replications
        h: int
            Forecast horizon

    Returns:
        dict: Result of the forecasting

    Example:

        ```python

        techtonique forecasting univariate /Users/t/Documents/datasets/time_series/univariate/a10.csv --base_model RidgeCV --h 3
        
        ```
    """
    init_cli(ctx)
    params = {
        "base_model": base_model,
        "n_hidden_features": n_hidden_features,
        "lags": lags,
        "type_pi": type_pi,
        "replications": replications,
        "h": h,
    }
    result = ctx.obj["cli"]._make_request("forecasting", Path(file), params)
    click.echo(result)


@forecasting.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--base_model", default="RidgeCV", help="Base model to use")
@click.option("--n-hidden-features", default=5, help="Number of hidden features")
@click.option("--lags", default=25, help="Number of lags")
@click.option("--h", default=3, help="Forecast horizon")
@click.pass_context
def multivariate(ctx, file, base_model, n_hidden_features, lags, h):
    """Multivariate forecasting

    Parameters:
        file: str
            Path to the CSV file
        base_model: str
            Base model to use
        n_hidden_features: int
            Number of hidden features
        lags: int
            Number of lags
        h: int
            Forecast horizon

    Returns:
        dict: Result of the forecasting

    Example:

        ```python

        techtonique forecasting multivariate /Users/t/Documents/datasets/time_series/multivariate/ice_cream_vs_heater.csv --lags 25 --h 10

        ```
    """
    init_cli(ctx)
    params = {
        "base_model": base_model,
        "n_hidden_features": n_hidden_features,
        "lags": lags,
        "h": h,
    }
    result = ctx.obj["cli"]._make_request("forecasting", Path(file), params)
    click.echo(result)


@cli.group()
def ml():
    """Machine Learning commands"""
    pass


@ml.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--base_model", default="RandomForestRegressor", help="Base model to use")
@click.option("--n-hidden-features", default=5, help="Number of hidden features")
@click.pass_context
def classification(ctx, file, base_model, n_hidden_features):
    """Classification tasks

    Parameters:
        file: str
            Path to the CSV file
        base_model: str
            Base model to use
        n_hidden_features: int
            Number of hidden features

    Returns:
        dict: Result of the classification

    Example:

        ```python

        techtonique ml classification /Users/t/Documents/datasets/tabular/classification/iris_dataset2.csv --base_model RandomForestRegressor

        ```
    """
    init_cli(ctx)
    params = {"base_model": base_model, "n_hidden_features": n_hidden_features}
    result = ctx.obj["cli"]._make_request("mlclassification", Path(file), params)
    click.echo(result)


@ml.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--base_model", default="ElasticNet", help="Base model to use")
@click.option("--n-hidden-features", default=5, help="Number of hidden features")
@click.pass_context
def regression(ctx, file, base_model, n_hidden_features):
    """Regression tasks

    Parameters:
        file: str
            Path to the CSV file
        base_model: str
            Base model to use
        n_hidden_features: int
            Number of hidden features

    Returns:
        dict: Result of the regression

    Example:

        ```python

        techtonique ml regression /Users/t/Documents/datasets/tabular/regression/mtcars2.csv --base_model ElasticNet

        ```
    """
    init_cli(ctx)
    params = {"base_model": base_model, "n_hidden_features": n_hidden_features}
    result = ctx.obj["cli"]._make_request("mlregression", Path(file), params)
    click.echo(result)


@cli.group()
def reserving():
    """Reserving commands"""
    pass


@reserving.command()
@click.argument("file", type=click.Path(exists=True))
@click.pass_context
def chainladder(ctx, file):
    """Chain Ladder method

    Parameters:
        file: str
            Path to the CSV file

    Returns:
        dict: Result of the chain ladder

    Example:

        ```python

        techtonique reserving chainladder /Users/t/Documents/datasets/tabular/triangle/abc.csv

        ```
    """
    init_cli(ctx)
    params = {"method": "chainladder"}
    result = ctx.obj["cli"]._make_request("reserving", Path(file), params)
    click.echo(result)


@reserving.command()
@click.argument("file", type=click.Path(exists=True))
@click.pass_context
def mack(ctx, file):
    """Mack Chain Ladder method

    Parameters:
        file: str
            Path to the CSV file

    Returns:
        dict: Result of the mack chain ladder

    Example:

        ```python

        techtonique reserving mack /Users/t/Documents/datasets/tabular/triangle/abc.csv

        ```
    """
    init_cli(ctx)
    params = {"method": "mack"}
    result = ctx.obj["cli"]._make_request("reserving", Path(file), params)
    click.echo(result)


@cli.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--model", default="coxph", help="Survival model to use")
@click.pass_context
def survival(ctx, file, model):
    """Survival Analysis

    Parameters:
        file: str
            Path to the CSV file
        model: str
            Survival model to use

    Returns:
        dict: Result of the survival analysis

    Example:

        ```python
        
            techtonique survival /Users/t/Documents/datasets/tabular/survival/kidney.csv --model coxph

        ```
    """
    init_cli(ctx)
    params = {"model": model}
    result = ctx.obj["cli"]._make_request("survivalregression", Path(file), params)
    click.echo(result)


if __name__ == "__main__":
    cli()
