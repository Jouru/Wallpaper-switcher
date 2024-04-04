# Imports
import argparse
from wallpaper_switcher import Config as Cf
from wallpaper_switcher import Way_Walls
from wallpaper_switcher import X_Walls


def main():
    # Define the commands for cli
    parser = argparse.ArgumentParser(description="Wallpaper setter")
    subparsers = parser.add_subparsers(dest="command")
    settings = subparsers.add_parser("set", help="Set the configurations")
    settings.add_argument("--time", help="Define time in minutes", type=int)
    settings.add_argument("--path", help="Define wallpapers path")
    parser.add_argument(
        "--show", help="Show the current config data", action="store_true"
    )
    args = parser.parse_args()

    cf = Cf()

    if args.command == "set":
        if args.time is not None:
            time = args.time * 60
            print(time)
        else:
            time = args.time
        path = args.path
        cf.writeconf(time, path)

    elif args.show:
        print(f"Time: {int(cf.time)/60} Minutes\nWallpapers directory: {cf.wallsdir}")

    else:
        if Cf.check_backend() == "wayland":
            Way_Walls.random_walls(cf.time, cf.wallsdir)
        else:
            X_Walls.random_walls(cf.time, cf.wallsdir)


if __name__ == "__main__":
    main()
