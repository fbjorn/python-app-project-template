from invoke import task, run


BLACK_CMD = "black ."


@task
def unittest(ctx):
    """Run tests."""
    ctx.run(f"pytest -v -s tests")


@task
def check(ctx):
    """Run linters and code checks."""
    run("flake8")
    run("mypy .")
    run(f"{BLACK_CMD} --check")


@task(pre=[unittest, check])
def test(ctx):
    """Run linters and unit tests."""
    pass
