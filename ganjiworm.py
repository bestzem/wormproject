# coding=gbk
from worm import Worm
import os

class GanJiWorm(Worm):
    def process_url(self, url):
        if url.endswith('/'):
            url = 'http://xuzhou.ganji.com' + url
        return url

    def write_to_stdout(self, row):
        pass

    def setup(self):
        os.system('cls')
        print '********************************************************************************'
        print '    ��ӭʹ�øϼ�����ҳ����(www.ganji.com/huangye ���ߣ�Allen �汾��V1.1)         \n'
        print '********************************************************************************'


def main():
    worm = GanJiWorm()
    worm.run()


if __name__ == '__main__':
    main()