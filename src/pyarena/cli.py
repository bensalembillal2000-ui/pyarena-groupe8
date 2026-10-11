import sys

from pyarena import __version__


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--version":
        print(f"PyArena version {__version__}")
    else:
        print(
            "PyArena : Moteur opérationnel. Utilisez '--version' pour vérifier la version."
        )
