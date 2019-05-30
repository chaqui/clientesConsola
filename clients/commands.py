import click
from clients.services import ClientService
from clients.models import ClientModel

@click.group()
def clients():
  """Manages de clients lifecycle"""
  pass


@clients.command()
@click.option('-n', '--name', type=str, prompt=True, help= 'The Client Name')
@click.option('-c', '--company', type=str, prompt=True, help= 'The Client Company')
@click.option('-e', '--email', type=str, prompt=True, help= 'The Client email')
@click.option('-p', '--position', type=str, prompt=True, help= 'The Client position')
@click.pass_context
def create(ctx, name, company, email, position):
  """Create a new Client"""
  client = ClientModel(name, company, email, position)
  client_service = ClientService(ctx.obj['clients_table'])
  client_service.create_client(client)



@clients.command()
@click.pass_context
def list(ctx):
  """List all clients"""
  client_service = ClientService(ctx.obj["clients_table"])
  click.echo('ID  |  Name  | Company  |  Email  | Position')
  click.echo ('*'*100) 
  clients = client_service.list_clients()
  for client in clients:
    click.echo('{uid} | {name} | {company} | {email} | {position}'.format(
      uid=client['uid'],
      name=client['name'],
      company=client['company'],
      email = client['email'],
      position = client['position']))



@clients.command()
@click.pass_context
def update(ctx, client_uid):
  """updates a client"""
  pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
  """Deletes a client""" 
  pass

all = clients
