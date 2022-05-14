from os import system


class adbKit(object):
    def screenshots(self, pngpos):
        cmdl = []
        cmdl.append("adb shell screencap -p /sdcard/DCIM/Screenshots/" + pngpos)
        cmdl.append("adb pull -p /sdcard/DCIM/Screenshots/" + pngpos)
        cmdl.append("adb shell rm /sdcard/DCIM/Screenshots/" + pngpos)
        self.docmd(cmdl)

    def docmd(self, cmdl):
        for i in cmdl:
            system(i)

    def click(self, point):
        return system("adb shell input tap " + str(point[0]) + " " + str(point[1]))
