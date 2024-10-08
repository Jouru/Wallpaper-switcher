import os, subprocess
from random import randint
from time import sleep
from sys import exit


class Config:
    def __init__(self):
        self.home = os.getenv("HOME")
        self.dir = f"{self.home}/.config/wallpaper"
        self.file = f"{self.dir}/wallpapers.conf"
        self.wallsdir = self.getconf()["path"]
        self.time = self.getconf()["time"]

    @property
    def dir(self):
        return self._dir

    @dir.setter
    def dir(self, dir):
        if not os.path.isdir(f"{self.home}/.config/wallpaper"):
            self.mk_dirs(f"{self.home}/.config/wallpaper")
        self._dir = f"{self.home}/.config/wallpaper"

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, file):
        self._file = f"{self.dir}/wallpapers.conf"
        if not os.path.isfile(f"{self.dir}/wallpapers.conf"):
            self.writeconf(f"{self.dir}/wallpapers.conf")

    @property
    def wallsdir(self):
        return self._wallsdir

    @wallsdir.setter
    def wallsdir(self, wallsdir):
        if not self.getconf()["path"]:
            self._wallsdir = f"{self.home}/Wallpapers"
        else:
            if not os.path.isdir(self.getconf()["path"]):
                self.mk_dirs(self.getconf()["path"])
            self._wallsdir = self.getconf()["path"]

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        if not self.getconf()["time"]:
            self._time = 3600
        else:
            self._time = self.getconf()["time"]

    # Check if running wayland or X11
    @staticmethod
    def check_backend():
        result = subprocess.run(
            "echo $XDG_SESSION_TYPE",
            shell=True,
            capture_output=True,
            text=True
        )
        backend = result.stdout.strip("b ''\n")
        return backend

    def getconf(self):
        with open(self.file, "r") as conf:
            lines = conf.readlines()
            data = {}
            for line in lines:
                key, value = line.strip().split("=")
                data[key] = value
        return data

    def writeconf(self, time=None, path=None):
        if not os.path.isfile(self.file):
            path = f"{self.home}/Wallpapers"
            time = 3600
            self.mk_dirs(path)

        else:
            if path is None:
                path = self.wallsdir

            if time is None:
                time = self.time

        with open(self.file, "w") as conf:
            params = [f"time={time}", f"path={path}"]
            conf.writelines("\n".join(params))

    def mk_dirs(self, path):
        if not os.path.isdir(path):
            os.mkdir(path)


class Walls:
    def get_wallpapers(path):
        pics = os.listdir(path)
        if len(pics) == 0:
            exit("Put some images in your wallpapers directory")
        return pics


class Way_Walls(Walls):
    @classmethod
    def random_walls(cls, time, path):
        os.system("swww init")
        while True:
            # Get the wallpapers list
            pics = super().get_wallpapers(path)
            # Set wallpaper
            i = randint(0, (len(pics) - 1))
            wallpaper = f"{path}/'{pics[i]}'"
            os.system(f"swww img '{wallpaper}' &")
            # Time until next wallpaper
            sleep(int(time))


class X_Walls(Walls):
    @classmethod
    def random_walls(cls, time, path):
        while True:
            # Get the wallpapers list
            pics = super().get_wallpapers(path)
            # Set wallpaper
            i = randint(0, (len(pics) - 1))
            wallpaper = f"{path}/{pics[i]}"
            os.system(f"feh --bg-fill '{wallpaper}'")
            # Time until new wallpaper
            sleep(int(time))


if __name__ == "__main__":
    pass
