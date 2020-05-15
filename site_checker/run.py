import os
import subprocess as s

import click

# import site_checker


@click.group()
def cli():
    pass


@click.command()
@click.option('--site', default="", help='The website you need to monitor')
def start(site):
    pid = os.getpid()
    f = open("pid.txt", "w+")
    f.write(str(pid))
    f.close()

    if len(site) == 0:
        site = input("Paste the URL you want to check for updates: ")

    from checker import check
    check(site)


@click.command()
def stop():
    f = open("pid.txt", "r")
    pid = f.read()
    f.close()
    s.Popen('taskkill /F /PID {0}'.format(pid), shell=True)


cli.add_command(start)
cli.add_command(stop)
