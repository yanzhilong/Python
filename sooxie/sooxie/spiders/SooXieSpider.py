# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import FormRequest
from sooxie.items import SooxieItem
from enum import Enum
import csv
import chardet
import taobao_csv_writer as taobao

page = 1;
count = 0;
baseurl = "https://sooxie.com/?r=all&Page="  # 爬虫首页

# 定义属性枚举
Property = {"鞋头款式": {"圆头": "","露趾": "","套趾": "","尖头": "","扁头": "","夹趾": "","包头": "","方头": ""},
            "闭合方式": {"搭扣":"","拉链":"","粘搭":"","魔术贴":"","不系带":"","松紧带":"","套筒":"","其他":"","套脚":"","系带":""},
            "鞋底材质": {"千层底":"","复合底":"","塑胶":"","泡沫":"","PU":"","橡胶发泡":"","tpu":"","橡胶":"","牛筋":"","皮":"","软木":""},
            "鞋面材质": {"布":"","磨砂皮":"","牛反绒":"","二层牛皮（除牛反绒":"","绒面":"","棉布":"","真皮二层皮":"","真皮头层皮":"","PU":"","超纤皮":"",
                     "网布": "", "其他": "", "灯芯绒": "", "鳄鱼皮": "", "人造革": "", "塑胶": "", "腹膜皮": "", "牛仔布": "", "头层牛皮（除牛反绒）": "", "绸缎": "",
                     "太空革": "", "藤草": "", "超纤": "", "亮片布": "", "毛线": "", "二层牛皮（除牛反绒）": "", "牛反绒（磨砂皮）": "牛皮", "": "", "": "", "": "",},
            "鞋面内里材质": {"无内里":"","网纱":"","布":"","PU":"","棉":"","羊毛":"","超纤皮":"","皮":"","猪皮":"","人造长毛绒":"","人造短毛绒":""},
            "制作工艺": {"注压鞋":"","缝制鞋":"","硫化鞋":"","胶粘鞋":""},
            "鞋跟": {"内增高":"","厚底":"","平跟":"","坡跟":""},
            "图案": {"手绘":"","拼色":"","纯色":"","格子":""},
            "流行元素": {"素面":"","豹纹":"","奢华马毛":"","图腾":"","翻边":"","荧光":"","雕花":"","迷彩":"","金属":"","马衔扣":"","车缝线":"","皮草装饰":"","镂空":"","编制":"","铆钉":"","绣花":"","亮片":"","流苏":"","皮革拼接":"","":"",},
            "风格": {"青春潮流":"","复古":"","休闲":"","简约":"","韩版":"","朋克":"","商务":"","日系":"","英伦":"","欧美":"","运动":"","民族风":""},
            "场合": {"沙滩":"","宴会":"","办公室":"","约会":"","日常":"","居家":"","运动休闲":""},
            "季节": {"夏季":"","冬季":"","春秋":"","":"","":"","":"","":"","":"","":"","":"",},
            "款式": {"切尔西靴":"","棉靴/毛靴":"","休闲高帮皮鞋":"","休闲皮鞋":"","鸟巢拖鞋":"","一字拖":"","老北京布鞋":"","德比鞋（正装皮鞋）":"","户外休闲鞋":"","运动休闲鞋":"",
                   "沙滩鞋": "", "商务休闲鞋": "", "罗马鞋": "", "板鞋": "", "乐福鞋": "", "其他": "", "豆豆鞋": "", "网面鞋": "", "鸟巢鞋": "", "布鞋": "",
                   "镂空皮鞋": "", "包头": "", "洞洞鞋": "", "松糕鞋": "", "勃肯凉鞋": "", "高帮工装鞋": "", "马丁靴": "", "夹趾": "", "雪地靴": "", "勃肯拖鞋": "",
                   "布洛克高帮鞋": "", "高帮板鞋": "", "T型": "", "工装鞋": "", "布洛克鞋": "", "套趾": "", "皮靴": "", "人字拖": ""},


            "鞋帮高度": {"高帮":"","低帮":"","":"","":"","":"","":"","":"","":"","":"","":"",},
            "功能": {"矫正":"","增高":"","轻质":"","防水":"","减震":"","保暖":"","耐磨":"","透气":"","":"","":"",},
            "内里材质": {"网纱":"","无内里":"","布":"","皮":"","":"","":"","":"","":"","":"","":"",},
            "帮面内里材质": {"网纱":"","PU":"","布":"","棉":"","人造长毛绒":"","人造短毛绒":"","":"","":"","":"","":"",},
            "帮面材质": {"磨砂皮":"","绸缎":"","牛反绒":"","太空革":"","塑胶":"","腹膜皮":"","超纤":"","PU":"","毛线":"","猪皮":"","袋鼠皮":"","牛仔布":"",
                     "网布": "", "二层牛皮（除牛反绒）": "", "鳄鱼皮": "", "绒面": "", "藤草": "", "棉布": "","亮片布":"","牛皮":"","灯芯绒":"","":"","":"","":"",},
            "适用季节": {"夏季":"","冬季":"","春秋":"","皮":"","":"","":"","":"","":"","":"","":"",},
            "适用对象": {"青年":"","儿童":"","中老年":""},
            "材质工艺": {"软面皮":"","水染皮":"","摔纹皮":"","磨砂皮":"","半粒面":"","疯马皮":"","擦色皮":"","印花皮":"","贴膜皮":"","裂纹皮":"","粒面皮":"","反绒皮":"",
                     "油蜡皮":"","修面皮":"","树膏皮":"","纳帕纹":"","压花皮":"","漆皮":"","打蜡皮":"","":"","":"","":"",},
            }
#  淘宝属性
TProperty = {
"宝贝类目": {"低帮鞋": "50012906", "高帮": "50012907", "凉鞋": "50011745", "拖鞋": "50011746"},
""
"高帮低帮鞋头款式": {"圆头": "30233", "尖头": "30232", "扁头": "6280721","方头": "30234"},
"凉鞋鞋头款式": {"露趾": "3226297", "套趾": "139173", "夹趾": "139172", "包头": "46112"},
"拖鞋款式": {"软木拖鞋": "9575796", "鸟巢拖鞋": "21640537", "人字拖": "134273", "一字拖": "3226299","套趾": "139173","T型": "139170","夹趾": "139172", "包头": "46112"},
"低帮闭合方式": {"搭扣": "139183", "魔术贴": "3227269", "松紧带": "9887404", "套脚": "3267935", "系带": "28102"},
"凉鞋高帮闭合方式": {"搭扣": "139183", "魔术贴": "3227269", "松紧带": "9887404", "套筒": "3226327", "系带": "28102"},
"低帮鞋面材质": {"搭扣":"","拉链":"","粘搭":"","魔术贴":"","不系带":"","松紧带":"","套筒":"","其他":"","套脚":"","系带":""},

"鞋面材质": {"二层牛皮（除牛反绒）":"668430252","二层牛皮（除牛反绒":"668430252","棉布":"53908","真皮二层皮":"","PU":"", "孔雀皮":"126870948","涤沦":"21852311",
                "网布": "3702871", "灯芯绒": "28344", "鳄鱼皮": "44858", "牛仔布": "28343", "头层牛皮（除牛反绒）": "668328569", "头层猪皮": "26834269", "绸缎": "28354",
                "太空革": "18339161", "藤草": "", "超纤": "", "亮片布": "14461751", "毛线": "28685", "二层猪皮": "6474787", "多种材质拼接": "28855009",
                "磨砂皮": "9994999", "牛反绒": "668360480","绒面": "3227901", "珍珠鱼皮":"6856831","羊反绒（羊猄）":"668304701","羊皮毛一体":"14461016",
                "羊皮（除羊反绒/羊猄）": "743634287", "羊驼皮": "107798468", "腹膜皮": "57871492", "藤草": "14461857", "蛇皮": "44857",
                "袋鼠皮": "28400", "超纤": "15099895", "马皮": "44855", "高丝光反绒皮": "235494498",
                "鳗鱼皮": "19304060", "鸵鸟皮": "11029301", "鹿皮": "44854", "麂皮": "44673", "人造革": "28404", "布": "3804702",
                "塑胶": "20370"},


"帮面材质": {"二层牛皮（除牛反绒）":"668430252","二层牛皮（除牛反绒":"668430252","棉布":"53908","真皮二层皮":"","PU":"", "孔雀皮":"126870948","涤沦":"21852311",
                "网布": "3702871", "灯芯绒": "28344", "鳄鱼皮": "44858", "牛仔布": "28343", "头层牛皮（除牛反绒）": "668328569", "头层猪皮": "26834269", "绸缎": "28354",
                "太空革": "18339161", "藤草": "", "超纤": "", "亮片布": "14461751", "毛线": "28685", "二层猪皮": "6474787",  "多种材质拼接": "28855009",
                "磨砂皮": "9994999", "牛反绒": "668360480","绒面": "3227901", "珍珠鱼皮":"6856831","羊反绒（羊猄）":"668304701","羊皮毛一体":"14461016",
                "羊皮（除羊反绒/羊猄）": "743634287", "羊驼皮": "107798468", "腹膜皮": "57871492", "藤草": "14461857", "蛇皮": "44857",
                "袋鼠皮": "28400", "超纤": "15099895", "马皮": "44855", "高丝光反绒皮": "235494498",
                "鳗鱼皮": "19304060", "鸵鸟皮": "11029301", "鹿皮": "44854", "麂皮": "44673", "人造革": "28404", "布": "3804702",
                "塑胶": "20370"},

"真皮材质工艺": {"软面皮":"","水染皮":"18344312","摔纹皮":"18344313","磨砂皮":"9994999","半粒面":"113700976","疯马皮":"18344310","擦色皮":"19440496","印花皮":"14464884","贴膜皮":"18344316","裂纹皮":"18344317","粒面皮":"18344309","反绒皮":"18033040",
                     "油蜡皮":"18344311","纳帕纹":"18344314","压花皮":"14464883","漆皮":"28402","树膏皮":"28394027","植鞣":"99579637","打蜡皮":"6042236","修面皮":"18344315"},

"鞋面内里材质": {"软面皮":"","水染皮":"18344312","摔纹皮":"18344313","磨砂皮":"9994999","半粒面":"113700976","疯马皮":"18344310","擦色皮":"19440496","印花皮":"14464884","贴膜皮":"18344316","裂纹皮":"18344317","粒面皮":"18344309","反绒皮":"18033040",
                     "油蜡皮":"18344311","纳帕纹":"18344314","压花皮":"14464883","漆皮":"28402","树膏皮":"28394027","植鞣":"99579637","打蜡皮":"6042236","修面皮":"18344315"},




"内里材质": {"无内里":"119244974","二层猪皮": "6474787", "仿毛":"3670020","兔毛":"21122","头层牛皮":"3880992","狐狸毛":"46278","羊毛羊绒混纺":"59182921","头层猪皮": "26834269","布": "3804702","涤沦":"21852311",
         "羊皮":"28398","超纤":"15099895", "网纱":"9115784","棉":"105255","棉":"105255","人造长毛绒":"14465078","人造短毛绒":"14465077",},

"鞋跟高": {"平跟(小于等于1cm)":"30228","低跟(1-3cm)": "29069296", "中跟(3-5cm)":"24574746","高跟(5cm及以上)":"3673609"},


"跟底款式": {"跟底款式":"121296261","松糕底": "44634045", "平跟":"30228","内增高":"3994116","厚底":"19550002"},



"鞋底材质": {"二层猪皮": "6474787","人造长毛绒":"14465078","人造短毛绒":"14465077","头层牛皮":"3880992","头层猪皮": "26834269","布": "3804702","纯羊毛":"3229201","羊毛羊绒混纺":"59182921","羊皮":"28398","羊皮毛一体":"14461016","超纤皮":"15099895",
         "EVA": "3376399", "EVA发泡胶": "77117384", "MD": "27366", "PU": "3323086", "PVC": "29228", "TPR(牛筋）": "807070564", "tpu": "7097887", "橡胶发泡": "19308111", "烟胶": "127517938", "皮": "3353142", "聚氨酯": "18956417",
        "麻": "3267653", "泡沫": "134280", "橡胶": "30161", "木": "3260684", "塑胶": "20370", "复合底": "3268018", "软木": "18859111", },


"图案": {"纯色":"29454","格子": "29453", "拼色":"3222561","手绘":"29455",},

"流行元素": {"素面":"3302333","豹纹":"3255041","奢华马毛":"91477857","图腾":"123658","翻边":"29950","荧光":"6330860","雕花":"3341344","迷彩":"52813","金属":"20369","马衔扣":"29033539","车缝线":"115775",
         "皮草装饰":"43735669","镂空":"115771","编制":"3347671","铆钉":"115776","绣花":"29957","亮片":"29959","流苏":"115777","皮革拼接":"3226301","水钻":"28209",},


"场合": {"沙滩":"103414","宴会":"139179","办公室":"122738","约会":"3267767","日常":"3224795","居家":"4068154","运动休闲":"3325552","结婚":"3267768",},

"风格": {"青春潮流":"48816930","复古":"43747","休闲":"29535","简约":"109835873","韩版":"28105","朋克":"29931","商务":"28908","日系":"3411108","英伦":"3291373","欧美":"125200612","运动":"1628","民族风":"132483"},

"季节": {"夏季":"29457","冬季":"29458","春秋":"29456","":"","":"","":"","":"","":"","":"","":"",},

"功能": {"矫正": "599790307", "增高": "112301", "轻质": "25380975", "防水": "3217611", "减震": "7200622", "保暖": "4194098", "耐磨": "4526599", "透气": "137928", "": "", "": "", },

"鞋制作工艺": { "固特异": "3280045", "缝制鞋": "14545463", "胶粘鞋": "14545464","硫化鞋": "3272885","注压鞋": "14545465"},

"适用对象": { "青年（18-40周岁）": "3267959", "中年（40-60周岁）": "3267960", "老年（60周岁以上）": "101181","儿童（18周岁以下）": "27845"},


}

class csvrow:
    def __init__(self):
        self.csvrows_eng = {
            "title": "",
            "cid": "",
            "seller_cids": "",
            "stuff_status": "",
            "location_state": "",
            "location_city": "",
            "item_type": "",
            "price": "",
            "auction_increment": "",
            "num": "",
            "valid_thru": "",
            "freight_payer": "",
            "post_fee": "",
            "ems_fee": "",
            "express_fee": "",
            "has_invoice": "",
            "has_warranty": "",
            "approve_status": "",
            "has_showcase": "",
            "list_time": "",
            "description": "",
            "cateProps": "",
            "postage_id": "",
            "has_discount": "",
            "modified": "",
            "upload_fail_msg": "",
            "picture_status": "",
            "auction_point": "",
            "picture": "",
            "video": "",
            "skuProps": "",
            "inputPids": "",
            "inputValues": "",
            "outer_id": "",
            "propAlias": "",
            "auto_fill": "",
            "num_id": "",
            "local_cid": "",
            "navigation_type": "",
            "user_name": "",
            "syncStatus": "",
            "is_lighting_consigment": "",
            "is_xinpin": "",
            "foodparame": "",
            "features": "",
            "buyareatype": "",
            "global_stock_type": "",
            "global_stock_country": "",
            "sub_stock_type": "",
            "item_size": "",
            "item_weight": "",
            "sell_promise": "",
            "custom_design_flag": "",
            "wireless_desc": "",
            "barcode": "",
            "sku_barcode": "",
            "newprepay": "",
            "subtitle": "",
            "cpv_memo": "",
            "input_custom_cpv": "",
            "qualification": "",
            "add_qualification": "",
            "o2o_bind_service": "",
        }


        # self.


        # 宝贝属性
        self.cateProps = {
            "20000": "29534",  # 品牌:other/其他
            "122276315": "",  # 款式
            "122216563": "",  # 鞋底材质
            "20608": "",  # 风格
            "124128491": "",  # 鞋面材质
            "122216629": "",  # 真皮材质工艺
            "122216345": "",  # 适用季节
            "122216632": "",  # 鞋制作工艺
            "20603": "",  # 图案
            "34272": "",  # 流行元素
            "122216561": "",  # 鞋跟、跟底款式
            "122216515": "",  # 场合
            "20019": "",  # 功能
            "122216608": "",  # 适合对象
            "122216351": "",  # 鞋头款式
            "20490": "",  # 闭合方式
            "1626698": "",  # 鞋跟高
            "122216587": "",  # 鞋面内里材料
            "139520082": "",  # 帮面内里材质
        }

        self.csvrows_cn = {
            "宝贝名称": "",
            "宝贝类目": "",
            "店铺类目": "",
            "新旧程度": "",
            "省": "",
            "城市": "",
            "出售方式": "",
            "宝贝价格": "",
            "加价幅度": "",
            "宝贝数量": "",
            "有效期": "",
            "运费承担": "",
            "平邮": "",
            "EMS": "",
            "快递": "",
            "发票": "",
            "保修": "",
            "放入仓库": "",
            "橱窗推荐": "",
            "开始时间": "",
            "宝贝描述": "",
            "宝贝属性": "",
            "邮费模版ID": "",
            "会员打折": "",
            "修改时间": "",
            "上传状态": "",
            "图片状态": "",
            "返点比例": "",
            "新图片": "",
            "视频": "",
            "销售属性组合": "",
            "用户输入ID串": "",
            "用户输入名 - 值对": "",
            "商家编码": "",
            "销售属性别名": "",
            "代充类型": "",
            "数字ID": "",
            "本地ID": "",
            "宝贝分类": "",
            "用户名称": "",
            "宝贝状态": "",
            "闪电发货": "",
            "新品": "",
            "食品专项": "",
            "尺码库": "",
            "采购地": "",
            "库存类型": "",
            "国家地区": "",
            "库存计数": "",
            "物流体积": "",
            "物流重量": "",
            "退换货承诺": "",
            "定制工具": "",
            "无线详情": "",
            "商品条形码": "",
            "sku 条形码": "",
            "7天退货": "",
            "宝贝卖点": "",
            "属性值备注": "",
            "自定义属性值": "",
            "商品资质": "",
            "增加商品资质": "",
            "关联线下服务": "",
        }




def create_csv():
    """ 创建一个csv文件，并写入标题行 """
    csv_file =open("Taobao/shoes.csv", "w", encoding="utf8", newline="")
    try:
        write = csv.writer(csv_file)
        write.writerow((u"version 1.00"))






    finally:
            csv_file.closed()

def writerow():
    '''写一行数据到csv文件中'''
    csv_file = open("Taobao/shoes.csv", "w", encoding="utf8", newline="")
    try:
        write = csv.writer(csv_file)
        write.writerow((u"version 1.00"))
    finally:
            csv_file.closed()





progertyglo = {}




class SooXieSpider(scrapy.Spider):
    name = "sooxie_all"


    # 定义入口网址
    start_urls = [baseurl + str(page), ]

    def parse(self, response):
        global count
        global page
        global baseurl
        shoe = taobao.SooXie()
        print(u"处理当前页面" + str(page))
        # 得到所有的鞋子当前页的主页面数据
        shoeuls = response.css("ul.pro");
        for ul in shoeuls:
            shoe.market = ul.css("a.scico::text").extract_first()
            # print(u"市场:" + shoe.market)
            price_num = ul.css("li.rz div.left strong::text").extract_first()
            # 判断幸福街市场及价格
            if shoe.market is not None and shoe.market == u"幸福街市场" and 10 < float(price_num) < 50:
                # 得到链接并请求这个页面
                details_link = ul.css("li.img a::attr(href)").extract_first()
                if details_link is not None:
                    # count += 1
                    # print (u"处理第" + str(count) + u"个商品")
                    # 发起一个请求并由详情页面处理
                    yield scrapy.Request(details_link, callback=self.show_details, meta={"shoe": shoe})
        # 得到下一页的链接并打开
        page += 1;
        yield scrapy.Request(baseurl + str(page), callback=self.parse)


    # 搜鞋的详情页面
    def show_details(self, response):
        global count
        count += 1
        print (u"处理第" + str(count) + u"个商品")

        shoe = response.meta["shoe"]
        shoe.url = response.url
        shoe.title = response.css("div.xgr_3_h h2.xgr_3p::text").extract_first()
        shoe.shoeno = response.css("div.xgr_3_h div.xgr_3p strong::text").extract_first()
        shoe.price = response.css("div.xgr_3_h div.xgr_3p em::text").extract_first()
        shoe.sizes = response.css("div.xgr_3_h div.xgr_3p")[3].css("li::attr(datavalue)").extract()
        popularityandupdate = response.css("div.xgr_3_h div.xgr_3p")[2].css("strong")
        shoe.popularity = popularityandupdate[0].css("strong::text").extract_first()
        if len(popularityandupdate) > 1:
            shoe.update = popularityandupdate[1].css("strong font::text").extract_first()
        shoe.colors = response.css("div.xgr_3_h div.xgr_3p")[4].css("li::attr(datavalue)").extract()
        shoe.images = response.css("div.xgr_5 img.scrollLoading::attr(data-url)").extract()

        # key = response.url  # 这段是你要匹配的文本
        # p1 = "\\d+"  # 这是我们写的正则表达式规则，你现在可以不理解啥意思
        # pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
        # matcher1 = re.search(pattern1, key)  # 在源文本中搜索符合正则表达式的部分
        shoeid = self.get_shoe_id(response.url)
        # 请求头数据
        healurl = response.urljoin("/handler/getSXHandler.ashx")
        # 继续请求主要属性参数
        return [FormRequest(url=healurl,
                            formdata={'p': "xd", 'id': shoeid},
                            callback=self.getHead,
                            meta={"shoe": shoe, "shoeid": shoeid}), ]

    def getHead(self, response):
        shoe = response.meta["shoe"]
        shoeid = response.meta["shoeid"]
        shoe.property = response.css("ul.attributes-list li::text").extract()
        if shoe.property is None or len(shoe.property) == 0:
            return
        # 请求头数据
        healurl = response.urljoin("/handler/loadImgHandler.ashx")
        # 继续请求主要属性参数
        return [FormRequest(url=healurl,
                            formdata={'p': "xd", 'id': shoeid},
                            callback=self.getImages,
                            meta={"shoe": shoe}), ]
    def get_shoe_id(self,url):
        p1 = "\\d+"  # 这是我们写的正则表达式规则，你现在可以不理解啥意思
        pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
        matcher1 = re.search(pattern1, url)  # 在源文本中搜索符合正则表达式的部分
        pageid = matcher1.group(0)  # 打印出来
        return pageid

    def getImages(self, response):
        shoe = response.meta["shoe"]
        shoe.mainimg = response.css("img::attr(bimg)").extract()
        return self.last_action(shoe)


    def last_action(self,shoe):
        # shoe = response.meta["shoe"]
        # print (u"解析完成")
        # print(type(shoe.property))
        # print(type(shoe.property[0]))


        si = SooxieItem()
        si["url"] = shoe.url
        si["title"] = shoe.title
        si["mainimg"] = shoe.mainimg
        si["shoeno"] = shoe.shoeno
        si["price"] = shoe.price
        si["sizes"] = shoe.sizes
        # 获得尺码


        for size in shoe.sizes:
            print (u"尺码:" + size)

        si["popularity"] = shoe.popularity
        si["update"] = shoe.update
        si["colors"] = shoe.colors

        for color in shoe.colors:
            print (u"颜色:" + color)

        si["images"] = shoe.images
        # si["property"] = self.addproperty(shoe.property)

        # 获得属性的字典
        property_dict = self.getproperty(shoe.property)
        si["property"] = property_dict
        # si["property"] = shoe.property

        # for item in self.getproperty(shoe.property):
        #     for key, value in item.items():
        #         print("key:" + key + " value:" + value)


        si["market"] = shoe.market

        taobao.add_row(shoe)
        # self.showproper()
        yield si


    # 去除两多余的空行及空格
    def cutnewline(self, source):
        p1 = "[^\\r\\n(\\s+)]\.*[^\\r\\n(\\s+)]+"  # 这是我们写的正则表达式规则，你现在可以不理解啥意思
        pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
        matcher1 = re.search(pattern1, source)  # 在源文本中搜索符合正则表达式的部分
        title = matcher1.group(0)  # 打印出来
        return title

    def addproperty(self, propertys):
        global progertyglo
        for properitem in propertys:
            # print type(properitem)
            # chardit1 = chardet.detect(properitem)
            # print chardit1['encoding']
            items = properitem.split(": ")
            if items is not None and len(items) == 2:
                # chardit1 = chardet.detect(items[0])
                # print chardit1['encoding']
                key1 = items[0]
                # print type(key1)
                # print (key1)
                if key1 not in progertyglo:
                    # print ("key1:" + key1)
                    progertyglo[key1] = set()
                key2 = u""+items[1]
                # print("key2:" + key2)
                progertyglo[key1].add(key2)
        return progertyglo

    def getproperty(self, propertys):
        progertys = []

        for properitem in propertys:
            # print type(properitem)
            # chardit1 = chardet.detect(properitem)
            # print chardit1['encoding']
            items = properitem.split(": ")
            if items is not None and len(items) == 2:
                key = items[0]
                # key = unicode(items[0], "utf-8")
                value = items[1]
                proitem = {key: value}
                progertys.append(proitem)
                # print (chardet.detect(propertys[0]))
                # print (chardet.detect(properitem))
                # print(key + "  " + value)
        return progertys

    def showproper(self):
        global count
        global page
        global progertyglo
        print(u"处理当前页面:" + str(page))
        print(u"当前商品:" + str(count))
        for key, elem in progertyglo.items():
            # print key + u": ".join(elem)
            pros = u""
            for pro in elem:
                pros += pro + ","
            print key + u"," + pros