# coding=gbk
import time

'''
ҳ������
'''
PAGES_AND_PAGE_CODE = (
    'http://xuzhou.ganji.com/zhiyepeixun/o2/',  # �ڶ�ҳ
    'http://xuzhou.ganji.com/zhiyepeixun/o3/',  # ����ҳ
    1,  # �ӵ�1ҳ��ʼ�ռ�
    30,  # ����2ҳ����
)


'''
xpath��������
'''
URL_REG = '//*/a[@class="list-info-title"]/@href'  # ��ȡÿҳ�е�url����url�򿪺������˾��Ϣ

INFO_REG = {
    'title': '//*/div[@class="title"]/h1/text()',  # ��ȡ������Ϣ
    'phone': '//*/span[@class="basic-tell-no fc-org"]/text()',  # ��ȡ�绰����
    'person': '//*/div[@class="basic-tell-col clearfix"]/span[@class="fl"]/text()',  # ��ȡ��ַ
}


'''
��������
'''
ENCODING = 'utf-8'


'''
�����ļ�����
'''
USE_LOCAL_URLS = False  # ʹ�ñ��ػ����url
URL_FILENAME = time.strftime('%Y-%m-%d') + 'urls.txt'  # ����url�ļ�����


'''
�ɼ���Ϣ�ļ�����
'''
APPEND = False  # �ɼ�������Ϣ��׷�ӵ���ʽ����
SAVE_FILENAME = 'info'  # �ɼ�������Ϣ���浽 info.csv �ļ���
FILE_HEADER = ['����', '�绰', '��ϵ��']  # �ļ�ͷ
FILE_HEADER_NAME = ['title', 'phone', 'person']  # ����˳��


