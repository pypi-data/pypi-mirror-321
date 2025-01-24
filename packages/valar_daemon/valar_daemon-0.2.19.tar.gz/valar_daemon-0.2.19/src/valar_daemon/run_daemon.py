"""
Run the Valar Daemon. For more information see https://pypi.com.

Options:
  - `--config_path`,  Path to the config file. Defaults to `./daemon.config`.
  - `--log_path`,     Path to the log directory (created if does not exist). Defaults to `./valar-daemon-log`
"""
from pathlib import Path
import argparse

# Ensure the 'src' directory is added to the sys.path for development
# import sys
# sys.path.insert(0, str(Path(*Path(__file__).parent.parts[:-1])))

from valar_daemon.Daemon import Daemon


if __name__ == '__main__':

    repo_link = 'https://pypi.com'
    parser = argparse.ArgumentParser(description=
        f"Run the Valar Daemon. For more information see {repo_link}."
    )
    parser.add_argument(
        '--config_path', type=str, required=False, 
        help='Path to the config file. Defaults to `./daemon.config`.',
        default=Path(Path.cwd(), 'daemon.config')
    )
    parser.add_argument(
        '--log_path', type=str, required=False, 
        help='Path to the log directory (created if does not exist). Defaults to `./valar-daemon-log`',
        default=Path(Path.cwd(), 'valar-daemon-log')
    )
    args = parser.parse_args()

    print(
        'Pointing to the following:\n'
        f'\t Config file at: {args.config_path}\n'
        f'\t Log directory at: {args.log_path}\n'
        'Expect no further stdout stream. Starting Valar Daemon.'
    )

    daemon = Daemon(
        args.log_path,
        args.config_path
    )

    daemon.run()
