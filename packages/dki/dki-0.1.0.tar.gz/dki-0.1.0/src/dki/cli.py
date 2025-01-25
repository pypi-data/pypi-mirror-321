import click

from dki import libs


@click.group()
def cli():
  pass


@cli.command()
@click.option("--template", help="Template of the deployment")
@click.option("--name", help="Name of the image")
def build(template, name):
  """build image"""
  libs.build_image(template, name)


@cli.command()
def init():
  """init deployments"""
  if libs.has_deployments():
    click.echo("deployments already initialized")
  else:
    libs.download_deployment()


@cli.command()
@click.option("--branch", help="Branch of the deployment", default="main")
def update(branch):
  """update local deployments"""
  if libs.has_deployments():
    libs.pull_deployment(branch)
  else:
    if click.confirm("Do you want to download deployments?"):
      libs.download_deployment()
    click.echo("Error: deployments not found")
