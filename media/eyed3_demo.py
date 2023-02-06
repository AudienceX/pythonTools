import eyed3
import os
import sys


def read(fp):
    f = eyed3.load(fp)
    print("标题=[" + f.tag.title + ']')
    print("曲艺人=[" + f.tag.artist + ']')
    print("专辑主导艺人=[" + f.tag.album + ']')


def write(fp, title):
    f = eyed3.load(fp)
    f.tag.title = title
    f.tag.save()


if __name__ == '__main__':
    dirname, filename = os.path.split(sys.argv[0])

    fp = os.path.join(dirname, '黄龄 - 骑士.mp3')
    read(fp)
    print("------------------------------")
    write(fp, "士骑")
    read(fp)
    print("------------------------------")
    write(fp, "骑士")


