import click


@click.command()
@click.argument('name')
@click.option('--greeting', '-g', default='Hello', help='optional alternate greeting')
def main(name, greeting):
    click.echo("{}, {}".format(greeting, name))


if __name__ == "__main__":
    main()
