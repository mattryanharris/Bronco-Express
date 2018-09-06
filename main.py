import click

@click.command()
@click.option('--route', prompt="What route", help="Defines which bus route student is taking.")

def test(route):
    """Bronco Express is a CLI tracker for the CPP bus system.  This program helps student find the arrival times for the Bronco Express shuttle.  Users will apply two flags to info the program which route and stop are at."""
    

if __name__ == '__main__':
    test()
