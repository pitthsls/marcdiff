import click

import marcdiff.core

@click.command()
@click.argument('file1', type=click.Path())
@click.argument('file2', type=click.Path())
@click.argument('outfile', type=click.Path(), default="marcdiff_output.html")
def run(file1, file2, outfile):
    marcdiff.core.html_compare(file1, file2, outfile)
