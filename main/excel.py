import xlrd
from multiprocessing import Pool
import sys

PATH = sys.path[1]

#常用列表
WC_LIST = ['1_德国', '2_巴西', '3_葡萄牙', '4_阿根廷', '5_比利时', '6_西班牙', '7_波兰', '8_瑞士', '9_法国', '11_秘鲁', '12_丹麦', '13_哥伦比亚', '15_克罗地亚', '16_英格兰', '17_墨西哥', '18_瑞典', '20_冰岛', '22_乌拉圭', '23_突尼斯', '24_塞内加尔', '27_哥斯达黎加', '30_埃及', '34_伊朗', '36_澳大利亚', '37_塞尔维亚', '39_摩洛哥', '51_尼日利亚', '53_巴拿马', '56_日本', '59_韩国', '62_俄罗斯', '65_沙特阿拉伯']
ASA = ['34_伊朗', '36_澳大利亚', '56_日本', '59_韩国', '65_沙特阿拉伯', '70_中国', '75_巴勒斯坦', '76_叙利亚', '77_乌兹别克', '78_阿联酋', '82_伊拉克', '85_黎巴嫩', '101_阿曼', '102_印度', '103_卡塔尔', '112_越南', '113_约旦', '114_土库曼斯坦', '116_吉尔吉斯斯坦', '119_朝鲜', '122_巴林', '123_菲律宾', '126_塔吉克斯坦', '129_泰国', '134_中国台北', '138_也门', '140_缅甸联邦', '144_中国香港', '148_阿富汗', '150_马尔代夫', '162_印度尼西亚', '165_尼泊尔', '172_柬埔寨', '173_新加坡', '174_科威特', '177_马来西亚', '183_老挝', '186_中国澳门', '188_不丹', '189_蒙古', '190_文莱', '191_东帝汶', '192_关岛', '197_孟加拉国', '200_斯里兰卡', '201_巴基斯坦']
EUP = ['1_德国', '3_葡萄牙', '5_比利时', '6_西班牙', '7_波兰', '8_瑞士', '9_法国', '12_丹麦', '14_意大利', '15_克罗地亚', '16_英格兰', '18_瑞典', '19_威尔士', '20_冰岛', '21_荷兰', '26_北爱尔兰', '28_斯洛伐克', '29_奥地利', '32_爱尔兰', '33_苏格兰', '35_乌克兰', '37_塞尔维亚', '38_波黑', '40_罗马尼亚', '41_土耳其', '42_保加利亚', '46_黑山', '47_希腊', '48_捷克', '54_匈牙利', '58_挪威', '60_阿尔巴尼亚', '62_俄罗斯', '64_斯洛文尼亚', '69_芬兰', '74_马其顿', '86_卢森堡', '88_爱沙尼亚', '91_阿美尼亚', '92_塞浦路斯', '94_白俄罗斯', '97_法罗群岛', '99_以色列', '104_格鲁吉亚', '118_阿塞拜疆', '131_拉脱维亚', '135_哈萨克斯坦', '136_安道尔', '147_立陶宛', '167_摩尔多瓦', '178_科索沃', '182_列支敦士登', '185_马耳他', '204_圣马力诺']
AFC = ['23_突尼斯', '24_塞内加尔', '30_埃及', '39_摩洛哥', '43_刚果民主共和国', '44_布基纳法索', '45_喀麦隆', '50_加纳', '51_尼日利亚', '57_阿尔及利亚', '61_科特迪瓦', '63_佛得角', '66_几内亚', '71_马里', '72_赞比亚', '73_乌干达', '79_南非', '81_贝宁', '83_几内亚比绍', '89_利比亚', '93_加蓬', '96_刚果', '98_塞拉利昂', '100_毛里塔尼亚', '105_肯尼亚', '106_尼日尔', '107_津巴布韦', '108_莫桑比克', '109_马达加斯加', '111_纳米比亚', '117_卢旺达', '121_中非共和国', '124_苏丹', '125_马拉维', '127_多哥', '130_科摩罗', '132_斯威士兰', '133_利比里亚', '137_埃塞俄比亚', '141_赤道几内亚', '142_安哥拉', '143_布隆迪', '145_莱索托', '146_坦桑尼亚', '149_博茨瓦纳', '153_南苏丹', '157_毛里求斯', '163_冈比亚', '170_乍得', '179_圣多美与普林西比', '187_吉布提', '193_塞舌尔', '208_厄立特里亚', '209_索马里']
SA = ['2_巴西', '4_阿根廷', '10_智利', '11_秘鲁', '13_哥伦比亚', '22_乌拉圭', '31_巴拉圭', '49_玻利维亚', '52_委内瑞拉', '68_厄瓜多尔']
OFC = ['120_新西兰', '151_所罗门群岛', '152_塔希提群岛', '154_新喀里多尼亚', '156_瓦努阿图', '158_巴布亚新几内亚', '168_斐济', '194_美属萨摩亚', '195_库克', '196_萨摩亚', '210_汤加']
NA = ['17_墨西哥', '25_美国', '27_哥斯达黎加', '53_巴拿马', '55_牙买加', '67_洪都拉斯', '80_特立尼达和多巴哥', '84_库拉索', '87_海地', '90_萨尔瓦多', '95_加拿大', '110_圣基茨和尼维斯', '115_尼加拉瓜', '128_危地马拉', '139_安提瓜和巴布达', '155_巴巴多斯', '159_格瑞那达', '160_苏利南共和国', '161_多米尼加共和国', '164_圭亚那', '166_波多黎各', '169_多米尼克', '171_伯利兹', '175_圣文森特及格瑞那丁', '176_圣路西亚', '180_阿鲁巴', '181_古巴', '184_百慕大群岛', '198_美属维津群岛', '199_蒙塞拉特岛', '202_特克斯和凯科斯群岛', '203_开曼群岛', '205_英属维津群岛', '206_安圭拉', '207_巴哈马']


def query(name):
    bookname = '../data/football_rank.xls'
    book = xlrd.open_workbook(bookname)
    namelist = book.sheet_names()
    dict = {}
    for i in namelist:
        c = i.split('_')
        dict[c[1]] = c[0]
    print(dict[name])
    return (dict[name])

class Excel(object):
    def __init__(self,name,game_type,time,rank):
        #常量
                         #保存结果文件名
        self.name = name #查询范围 列表形式
        self.start_time = time[0]
        self.end_time = time[1]

        #变量
        if  game_type:  #比赛类型
            self.game_type = game_type
        else:
            self.game_type = False
        if rank:
            if '*' in rank:
                if rank[0] == '*':
                    self.func = self.rank_1
                    self.rank = rank[1]
                elif rank[1] == '*':
                    self.func = self.rank_2
                    self.rank = rank[0]
            else:
                self.func = self.rank_3
                self.rank = rank
        else:
            self.func = self.rank_0


    def rank_0(self,c_home,c_away,win,lose,rank_home,rank_away):
        self.total_game += 1
        self.total_score_away += c_away
        self.total_score_home += c_home
        self.win_game += win
        self.lose_game += lose

    def rank_1(self,c_home,c_away,win,lose,rank_home,rank_away):
        if rank_home - rank_away >= self.rank:
            self.total_game += 1
            self.total_score_away += c_away
            self.total_score_home += c_home
            self.win_game += win
            self.lose_game += lose

    def rank_2(self,c_home,c_away,win,lose,rank_home,rank_away):
        if rank_home - rank_away <= -self.rank:
            self.total_game += 1
            self.total_score_away += c_away
            self.total_score_home += c_home
            self.win_game += win
            self.lose_game += lose

    def rank_3(self,c_home,c_away,win,lose,rank_home,rank_away):
        if rank_away >= self.rank[0] and rank_away <= self.rank[1]:
            self.total_game += 1
            self.total_score_away += c_away
            self.total_score_home += c_home
            self.win_game += win
            self.lose_game += lose

    def rank_go(self,name):
        bookname = PATH + '\\data\\football_rank.xls'
        book = xlrd.open_workbook(bookname)
        table = book.sheet_by_name(name)
        #print(name)
        game_type = table.col_values(8)
        home_team = table.col_values(9)
        away_team = table.col_values(11)
        team_score = table.col_values(5)
        time = table.col_values(2)
        win_rate = table.col_values(19)
        #需要参数
        self.total_score_home = 0
        self.total_score_away = 0
        self.total_game = 0
        self.lose_game = 0  #胜负平
        self.win_game = 0
        #需要条件
        #@1 确定比赛类型
        count = []
        if self.game_type:
            for k in range(len(game_type)):
                if game_type[k] in self.game_type:
                    count.append(k)
        else:
            count = [i for i in range(1,len(game_type))]

        for i in count:

            if  int(time[i][0:4])>= self.start_time and int(time[i][0:4]) <= self.end_time and '-' in team_score[i]:
                c = team_score[i].split('-')
                c_home = int(c[0])
                c_away = int(c[1])
                rank_home = int(home_team[i].split('_')[0])
                rank_away = int(away_team[i].split('_')[0])
                if name != home_team[i]:
                    tmp_1 =  c_home
                    c_home = c_away
                    c_away = tmp_1
                    tmp_2 = rank_away
                    rank_away = rank_home
                    rank_home = tmp_2

                if win_rate[i] == '负':
                    lose = 1
                else: lose = 0
                if win_rate[i] == '胜':
                    win = 1
                else: win = 0

                self.func(c_home,c_away,win,lose,rank_home,rank_away)
        #print(self.total_score_home,self.total_score_away,self.total_game)
        print(name)
        return(name,self.total_score_home,self.total_score_away,self.total_game,self.win_game,self.lose_game)


    def mulprocess(self,num):
        name = self.name
        p = Pool(num)
        go_rank = p.map(self.rank_go,name)
        p.close()
        return(go_rank)




if __name__ == '__main__':
    #name,filename,game_type,time
    p = Excel(name=WC_LIST, game_type=False, time=[2010, 2018], rank=[1, 10])
    p.mulprocess(8)
