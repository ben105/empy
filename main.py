from empy.config import Config
from empy.empy import Empy
from src.computation import do_work


def main():
    Config.initialize()
    do_work(Empy())


if __name__ == '__main__':
    main()
