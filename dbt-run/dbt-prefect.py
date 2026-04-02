"""Prefect flow: dbt seed then dbt run for the `test` dbt project."""

from pathlib import Path

from dotenv import load_dotenv
from prefect import flow, task
import subprocess

REPO_ROOT = Path(__file__).resolve().parent.parent
DBT_DIR = REPO_ROOT / "test"


def _dbt_cmd(*args: str) -> list[str]:
    return [
        "dbt",
        *args,
        "--project-dir",
        str(DBT_DIR),
        "--profiles-dir",
        str(DBT_DIR),
    ]


@task
def run_dbt_seed() -> None:
    subprocess.run(_dbt_cmd("seed"), cwd=REPO_ROOT, check=True)


@task
def run_dbt_run() -> None:
    subprocess.run(_dbt_cmd("run"), cwd=REPO_ROOT, check=True)


@flow(name="dbt-prefect")
def dbt_pipeline() -> None:
    load_dotenv(DBT_DIR / ".env")
    run_dbt_seed()
    run_dbt_run()


if __name__ == "__main__":
    dbt_pipeline()
