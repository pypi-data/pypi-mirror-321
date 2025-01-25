# Standard libraries
from os import environ
from pathlib import Path
from subprocess import run, CalledProcessError, DEVNULL, PIPE
from typing import Dict, List, Optional

# Components
from ..prints.colors import Colors

# Tools class
class Tools:

    # Members
    DESCRIPTION: str = ''
    NAME: str = ''

    # Run command
    @staticmethod
    def run_command(
        command: list[str],
        stdout: bool = True,
        stderr: bool = True,
        env: Optional[Dict[str, str]] = None,
    ) -> int:
        return run(
            command,
            stdout=None if stdout else DEVNULL,
            stderr=None if stderr else DEVNULL,
            text=True,
            check=False,
            env={
                **environ,
                **env
            } if env else None,
        ).returncode

    # Run with output
    @staticmethod
    def run_output(
        command: list[str],
        stderr: bool = True,
    ) -> str:
        try:
            result = run(
                command,
                text=True,
                check=True,
                stdout=PIPE,
                stderr=PIPE if stderr else DEVNULL,
            )
            return str(result.stdout.strip())
        except CalledProcessError as error:
            if stderr and error.stderr:
                return str(error.stderr.strip())
            return ''

    # Get .git directory
    @staticmethod
    def git_dir() -> str:
        return Tools.run_output(
            [
                'git',
                'rev-parse',
                '--git-dir',
            ],
            stderr=False,
        )

    # Fetch remote branch
    @staticmethod
    def git_fetch(remote: str, branch: str) -> bool:
        return Tools.run_command([
            'git',
            'fetch',
            remote,
            branch,
        ]) == 0

    # Get git hooks
    @staticmethod
    def git_hooks() -> List[str]:

        # Variables
        git_dir: str
        hooks: List[str] = []

        # Access .git
        git_dir = Tools.git_dir()
        if not git_dir:
            return []

        # Detect hooks
        hooks_dir = Path(git_dir) / 'hooks'
        for hooks_item in hooks_dir.iterdir():
            if hooks_item.is_file() and not hooks_item.name.endswith('.sample'):
                hooks.append(hooks_item.name)

        # Result
        return hooks

    # Select remote
    @staticmethod
    def select_remote() -> str:

        # Acquire remotes
        remotes = Tools.run_output([
            'git',
            'remote',
        ]).splitlines()
        if not remotes:
            return ''

        # Detect single remote
        if len(remotes) == 1:
            return remotes[0]

        # Selector header
        print(' ')
        print(f'{Colors.GREEN} === {Tools.NAME} - Remote selection ==='
              f'{Colors.RESET}')
        print(' ')

        # Selector items
        for idx, remote in enumerate(remotes, start=1):
            remote_url = Tools.run_output([
                'git',
                'config',
                '--get',
                f'remote.{remote}.url',
            ])
            print(
                f'{Colors.YELLOW} [{idx}] {Colors.BOLD}{remote} - {Colors.YELLOW_THIN}{remote_url}'
                f'{Colors.RESET}')

        # Selector input
        print(' ')
        try:
            choice = int(
                input(f'{Colors.YELLOW} {Tools.NAME}:'
                      f'{Colors.BOLD} Choose a remote'
                      f'{Colors.GREEN} [1-{len(remotes)}] {Colors.YELLOW}:'
                      f'{Colors.RESET} '))
            if 1 <= choice <= len(remotes):
                return remotes[choice - 1]
            raise ValueError

        # Selector interruption
        except KeyboardInterrupt:
            print(' ')
            return ''

        # Selector fallback
        except (IndexError, ValueError):
            return ''

    # Select branch
    @staticmethod
    def select_branch(remote: str) -> str:

        # Validate input
        if not remote:
            return ''

        # Acquire branches
        branches = sorted({
            line.split(f'{remote}/')[-1]
            for line in Tools.run_output([
                'git',
                'branch',
                '-ar',
            ]).splitlines() if remote in line and '->' not in line
        })
        if not branches:
            return ''

        # Selector header
        print(' ')
        print(f'{Colors.GREEN} === {Tools.NAME} - Branch selection ==='
              f'{Colors.RESET}')
        print(' ')

        # Selector items
        print(f'{Colors.YELLOW} [0] {Colors.BOLD}Manual branch input'
              f'{Colors.RESET}')
        print(' ')
        for idx, branch in enumerate(branches, start=1):
            print(
                f'{Colors.YELLOW} [{idx}] {Colors.BOLD}{branch} - {Colors.YELLOW_THIN}{remote}'
                f'{Colors.RESET}')

        # Selector input
        print(' ')
        try:
            choice = int(
                input(f'{Colors.YELLOW} {Tools.NAME}:'
                      f'{Colors.BOLD} Select branch'
                      f'{Colors.GREEN} [0-{len(branches)}] {Colors.RESET}: '))

            # Manual branch input
            if choice == 0:
                print(' ')
                branch = input('Enter branch name: ').strip()
                return branch if branch else ''

            # Branch selection
            if 1 <= choice <= len(branches):
                return branches[choice - 1]

            # Unknown selection
            raise ValueError

        # Selector interruption
        except KeyboardInterrupt:
            print(' ')
            return ''

        # Selector fallback
        except (IndexError, ValueError):
            return ''
