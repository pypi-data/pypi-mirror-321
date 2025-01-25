# ruff: noqa: S603 = allow check_output with arbitrary cmdline

import json
from pathlib import Path
from shlex import split
from subprocess import check_output

from docsub import Environment, pass_env, click


IMG = 'makukha/multipython:unsafe'
BAKEFILE = 'tests/docker-bake.hcl'
TEMP_ID = 'reports'

PASSING = '✅'
NOINSTALL = '💥'
NOTFOUND = '🚫'
COLSP = ' '


@click.group()
def x(): ...


SUITE = {
    'tox3_v': ('tox3', '>=20'),
    'tox3_v27': ('tox3', '>=20,<20.27'),
    'tox3_v22': ('tox3', '>=20,<20.22'),
}


@x.command()
@pass_env
def generate(env: Environment) -> None:
    """
    Generate test reports.
    """
    temp_dir = env.get_temp_dir(TEMP_ID)
    # get source data
    bake = check_output(split(f'docker buildx bake -f {BAKEFILE} test --print'))
    (temp_dir / 'bake.json').write_bytes(bake)
    data = json.loads(bake)
    tags = check_output(
        split(f'docker run --rm {IMG} py ls --tag'),
        text=True,
    ).splitlines()
    # generate reports
    for suite in SUITE:
        write_report(temp_dir, data, tags, suite, skip=('py20',))


def write_report(
    base_dir: Path,
    data: dict,
    tags: list[str],
    suite: str,
    skip: tuple[str, ...],
) -> None:
    def host_tag_results(args: dict) -> tuple[str, list[str]]:
        marks = [
            *((t, 'P') for t in args['TARGET_TAGS_PASSING'].split()),
            *((t, 'I') for t in set(args['TARGET_TAGS_NOINSTALL'].split()) - set(skip)),
            *((t, 'F') for t in set(args['TARGET_TAGS_NOTFOUND'].split()) - set(skip)),
        ]
        marks.sort(key=lambda tm: tags.index(tm[0]))
        return (args['HOST_TAG'], ''.join(tm[1] for tm in marks))

    bake_group, venv_pin = SUITE[suite]
    targets = data['group'][bake_group]['targets']
    args = [data['target'][t]['args'] for t in targets]
    table = [host_tag_results(a) for a in args if a['VIRTUALENV_PIN'] == venv_pin]
    table.sort(key=lambda row: tags.index(row[0]))
    results = dict(target_tags=tags, host_tag_results=dict(table))
    with (base_dir / f'{suite}.json').open('wt') as f:
        json.dump(results, f, indent=2)


@x.command()
@click.argument('suite', type=str, required=True)
@pass_env
def pretty(env: Environment, suite: str) -> None:
    """
    Print report in compact terminal-based format.
    """
    ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVW'
    temp_dir = env.get_temp_dir(TEMP_ID)

    with (temp_dir / f'{suite}.json').open() as f:
        data = json.load(f)
    row_title = 'HOST'
    col_title = 'TARGETS'
    tags = data['target_tags']

    if len(tags) > len(ALPHA):
        raise RuntimeError('Too many tags')

    width = max(len(row_title), max(len(v) for v in tags))

    print(f'{row_title: >{width}}    {col_title}')
    print(f'{"—" * width}    {COLSP.join(ALPHA[: len(tags)])}')
    for i, tag in enumerate(tags):
        res = data['host_tag_results'].get(tag)
        marks = (
            [{'P': PASSING, 'I': NOINSTALL, 'F': NOTFOUND}[x] for x in res]
            if res
            else COLSP.join('.' * len(tags))
        )
        print(f'{tag: >{width}}  {ALPHA[i]} {"".join(marks)}')
