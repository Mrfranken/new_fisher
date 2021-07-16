# -*- coding: utf-8 -*-
import platform
import requests
from requests.exceptions import ConnectionError
import json
import http.client

content = {"create_time": "2021-06-02 08:53:27", "isbn": "9787108070371", "title": "什么是社会学",
           "book_info": {"作者": "赵鼎新", "出版社": "生活·读书·新知三联书店", "出版年": "2021-5", "页数": "160", "定价": "39.00元", "装帧": "平装",
                         "丛书": "乐道文库", "ISBN": "9787108070371"}, "abstract": "赵鼎新 / 生活·读书·新知三联书店 / 2021-5 / 39.00元",
           "book_intro": "结构／机制叙事和事件／时间序列叙事是人类在描述和分析社会现象时所采用的两类最为基本的叙事形式。如果说历史学是一门以事件／时间序列叙事为基础的学科，社会学则是一门以结构／机制叙事为基础的学科，历史学和社会学也就构成了社会科学中的两个最为核心的基础学科，或者说它们是其它专题性的应用社会科学学科，比如法学、商学、管理学、传播学、社会工作、宗教学（在一定意义上甚至应该包括经济学和政治学）等学科的母学科。",
           "author_intro": "赵鼎新，芝加哥大学 Max Palevsky 讲席教授，浙江大学教授。研究领域包括历史社会学、社会运动和社会学方法。曾著有中文专著《社会与政治运动讲义》《东周战争和儒法国家的形成》《民主的限制》《合法性的政治》《国家、战争与历史发展：前现代中西模式的比较》以及英文专著两部，分别获得美国社会学学会2001年度亚洲研究最佳书籍奖、美国社会学学会2016年度政治社会学研究最佳书籍奖。",
           "catalog": "总论什么是社会学\n\n第一章结构和机制\n什么是社会结构？\n惯习和权力\n社会不是系统，社会结构不见得有功能\n宏观社会结构、变量和机制\n中层理论和社会机制\n什么是社会机制\n机制和定理/法则\n普适机制和特殊机制\n特殊机制到普遍机制的抽象\n特殊机制的重要性\n涌现机制\n还原论的得失\n正反馈机制与负反馈机制\n社会学中的三个“交互演化”\n符号互动\n社会关系网络\n制度和新制度主义\n生态\n证明常识的意义\n\n第二章机制解释的问题\n机制和宏观结构\n结构／机制和行动者\n归纳还是演绎\n机制解释所面临的“过度决定”和“重要性多变”难题\n\n第三章机制解释弱点的弥补\n准实验方法\n排除其他可能解释\n把机制置于事件顺序和历史情景之中\n反事实推理\n加大被解释问题的信息量\n\n结语\n参考文献\n",
           "original_texts": [], "labels": ["社会学", "赵鼎新", "社会学理论", "研究方法", "入门", "社会科学", "社会史", "知识社会学"],
           "cover_url": "https://img1.doubanio.com/view/subject/m/public/s33885357.jpg",
           "url": "https://book.douban.com/subject/35445945/",
           "rating": {"count": 32, "rating_info": "", "star_count": 4.5, "value": 8.9}, "comments": [
        {"user_name": "伯樵·阿苏勒", "user_page": "https://www.douban.com/people/yuanzhigao_0/",
         "user_pic": "https://img2.doubanio.com/icon/u1756440-11.jpg", "vote": "9", "rate": "40", "time": "2021-05-09",
         "content": "一次“元方法论”的降维打击，有些靶子甚至没提都能想得出来这个是谁、那个是谁  #辣个男人来方法论扶贫了#……不过第三章提到明代灭亡以及改开后的财富分配问题，感觉功力又一下从“神坛”掉到地上，跟《儒法中国》差不多的毛病～感觉顺带还给过一/两年出版的Gould的《起义者的认同》打了个大型广告~~哦对了，最后还举贤不避妻......很甜"},
        {"user_name": "小螺号滴滴滴吹", "user_page": "https://www.douban.com/people/183761869/",
         "user_pic": "https://img9.doubanio.com/icon/u183761869-4.jpg", "vote": "7", "rate": "50", "time": "2021-04-29",
         "content": "老赵有好几把刷子"}, {"user_name": "Mr. Someone", "user_page": "https://www.douban.com/people/65245284/",
                                  "user_pic": "https://img9.doubanio.com/icon/u65245284-6.jpg", "vote": "5",
                                  "rate": "30", "time": "2021-05-20",
                                  "content": "就是已发表的几篇中文论文，一家之言~但科学哲学观实在是太朴素了，如此入门定会让人误入歧途而不自知"},
        {"user_name": "CarlGauss", "user_page": "https://www.douban.com/people/65399328/",
         "user_pic": "https://img2.doubanio.com/icon/u65399328-2.jpg", "vote": "3", "rate": "30", "time": "2021-06-01",
         "content": "老赵对机制相关的文献是完全不熟悉(然而Philosophy of Science期刊好像就是芝加哥办的)，他这些年的很多文章其实都很misleading。"},
        {"user_name": "韧勉", "user_page": "https://www.douban.com/people/anchoretic/",
         "user_pic": "https://img9.doubanio.com/icon/u2860322-115.jpg", "vote": "3", "rate": "50", "time": "2021-05-20",
         "content": "本书是为赵鼎新多年研究后，已对社会学概念有了体系化的全新认知，故而可以从最鞭辟入里的角度全盘输出对社会学的理解干货，形成了这么一本纯理论机制建构的社会学入门读物。本书讨论了作为社会学基础的三个最为核心的问题：其一，社会结构和社会机制，以及围绕着社会结构和社会机制的多重复杂性而衍生出的各种理论问题。其二，结构／机制解释在经验层面和方法层面上面临着的多种难以完全解决的困境。其三，针对结构／机制解释在经验层面上的弱点社会学家发展出来的五种解决方案，即准实验方法、排除其他可能解释方法、置机制于事件顺序和历史情景之中方法、反事推理方法以及加大被解释问题信息量方法。虽然仍存在一定的制约，但是最后一种方法为老赵最为推崇。"},
        {"user_name": "獭上尉", "user_page": "https://www.douban.com/people/51446771/",
         "user_pic": "https://img2.doubanio.com/icon/u51446771-1.jpg", "vote": "1", "rate": "50", "time": "2021-05-21",
         "content": "赵鼎新对他近几年关于结构/机制叙事相关成果的一个系统总结。\n行文流畅到能在医院排号的时候读下去…"},
        {"user_name": "江海一蓑翁", "user_page": "https://www.douban.com/people/batongyang/",
         "user_pic": "https://img2.doubanio.com/icon/u1928576-2.jpg", "vote": "0", "rate": "40", "time": "2021-05-26",
         "content": "罗志田老师主编的“乐道文库”推出的一部最新作品，由理工科出身的知名社会学学者赵鼎新老师执笔。在不算长的篇幅里，作者放弃了面面俱到地对社会学学科进行科普式介绍，而是聚焦于社会学的结构/机制分析视角，详细分析这一分析视角的固有研究方法、对其视角与方法局限性和不足的反思，以及就此给出的改进建议。作者的理工科出身背景，让其讲述逻辑严谨、层次分明，在理论色彩极强的同时，尽可能地做到了清晰可读。其讲述过程中，一以贯之的问题意识与反思意识，直接助力读者培养起社会学的思维方式，并对该学科进行清醒认识与反思。堪称一部高阶意义上的学科科普作品，值得推荐。"},
        {"user_name": "孟青山", "user_page": "https://www.douban.com/people/gwt196455/",
         "user_pic": "https://img9.doubanio.com/icon/u50182232-4.jpg", "vote": "0", "rate": "50", "time": "2021-05-26",
         "content": "读着忘记了时间"}, {"user_name": "Roger", "user_page": "https://www.douban.com/people/181854959/",
                                 "user_pic": "https://img1.doubanio.com/icon/u181854959-8.jpg", "vote": "0",
                                 "rate": "40", "time": "2021-05-19",
                                 "content": "作为事件/时间叙事的历史学和作为结构/机制叙事的社会学，浓缩版可参看作者《什么是历史社会学？》一文。（虽然赵汀阳、赵鼎新等人被老师批没有get历史性的真谛。"},
        {"user_name": "s", "user_page": "https://www.douban.com/people/187278916/",
         "user_pic": "https://img2.doubanio.com/icon/u187278916-1.jpg", "vote": "0", "rate": "50", "time": "2021-05-23",
         "content": "up to now…阅读用时最短的一本书了，坐等未来方法论的相关著作😍"}], "source": "redis"}


class HttpHelper(object):

    @staticmethod
    def get(url=None, isbn=None, return_json=True):

        proxies = {"http": "http://10.158.100.9:8080", "https": "https://10.158.100.9:8080"}
        data = {
            'isbn': isbn,
            'key': '6Ffb9ZNmRVvi7YowQ2eRARLfB'

        }
        resp = requests.get('https://binstd.apistd.com/isbn/query', params=data, proxies=proxies)
        # if response.status_code != 200:
        #     return {} if return_json else ''
        # return response.json() if return_json else response.text
        # outcome = None
        # with open(r'C:\D\myworkspace\mygitpro\new_fisher\9787108070371.txt', 'r', encoding='utf8') as f:
        #     outcome = f.readlines()[0]
        # return json.loads(outcome)
        with open(r'C:\D\myworkspace\mygitpro\new_fisher\{}.txt'.format(isbn), 'w', encoding='utf8') as f:
            f.write(str(resp.json()))
        # return json.loads(outcome)

        # return content


if __name__ == '__main__':
    url = 'https://book.feelyou.top/isbn/9787201094014'  # 'http://t.yushu.im/v2/web/isbn/9787501524044'
    isbn_list = [
        '9787108012586',
        '9787546206134',
        '9787108012555',
        '9787108012548',
        '9787108012692'
    ]
    for isbn in isbn_list:
        outcome = HttpHelper.get(isbn=isbn)
    # html = requests.get(url)
    # html1 = html.json()
    print(outcome)
    print('-----')
