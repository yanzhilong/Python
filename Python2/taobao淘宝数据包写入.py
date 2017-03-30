# -*- coding: utf-8 -*-
import csv
#  淘宝类目字典

cid_dict = {"低帮鞋": "50012906", "高帮": "50012907", "凉鞋": "50011745", "拖鞋": "50011746"}

property_dict = {
    # 高帮低帮鞋头款式
    "圆头": "30233", "尖头": "30232", "扁头": "6280721","方头": "30234",

    # 凉鞋鞋头款式
    "露趾": "3226297", "套趾": "139173", "夹趾": "139172", "包头": "46112",

    # 拖鞋款式
    "软木拖鞋": "9575796", "鸟巢拖鞋": "21640537", "人字拖": "134273", "一字拖": "3226299",
    "T型": "139170",

    # 低帮闭合方式、凉鞋高帮闭合方式
    "搭扣": "139183", "魔术贴": "3227269", "松紧带": "9887404", "套脚": "3267935", "系带": "28102", "套筒": "3226327",

    # 帮面材质
    "二层牛皮（除牛反绒）": "668430252", "二层牛皮（除牛反绒": "668430252", "棉布": "53908", "孔雀皮": "126870948",
    "涤沦": "21852311", "网布": "3702871", "灯芯绒": "28344", "鳄鱼皮": "44858", "牛仔布": "28343",
    "头层牛皮（除牛反绒）": "668328569", "头层猪皮": "26834269", "绸缎": "28354", "太空革": "18339161",
    "亮片布": "14461751", "毛线": "28685", "二层猪皮": "6474787", "多种材质拼接": "28855009",
    "磨砂皮": "9994999", "牛反绒": "668360480", "绒面": "3227901", "珍珠鱼皮": "6856831", "羊反绒（羊猄）": "668304701",
    "羊皮毛一体": "14461016", "羊皮（除羊反绒/羊猄）": "743634287", "羊驼皮": "107798468", "腹膜皮": "57871492",
    "藤草": "14461857", "蛇皮": "44857", "袋鼠皮": "28400", "超纤": "15099895", "马皮": "44855",
    "高丝光反绒皮": "235494498","鳗鱼皮": "19304060", "鸵鸟皮": "11029301", "鹿皮": "44854", "麂皮": "44673",
    "人造革": "28404", "布": "3804702", "塑胶": "20370",

    # 真皮材质工艺、鞋面内里材质
    "水染皮": "18344312", "摔纹皮": "18344313", "半粒面": "113700976", "疯马皮": "18344310",
    "擦色皮": "19440496", "印花皮": "14464884", "贴膜皮": "18344316", "裂纹皮": "18344317", "粒面皮": "18344309", "反绒皮": "18033040",
    "油蜡皮": "18344311", "纳帕纹": "18344314", "压花皮": "14464883", "漆皮": "28402", "树膏皮": "28394027",
    "植鞣": "99579637", "打蜡皮": "6042236", "修面皮": "18344315",

    # 内里材质
    "无内里": "119244974", "仿毛": "3670020", "兔毛": "21122", "头层牛皮": "3880992", "狐狸毛": "46278",
    "羊毛羊绒混纺": "59182921", "羊皮": "28398",
    "网纱": "9115784", "人造长毛绒": "14465078", "人造短毛绒": "14465077",

    # 鞋跟高
    "平跟(小于等于1cm)": "30228", "低跟(1-3cm)": "29069296", "中跟(3-5cm)": "24574746", "高跟(5cm及以上)": "3673609",

    # 跟底款式
    "跟底款式": "121296261", "松糕底": "44634045", "平跟": "30228", "内增高": "3994116", "厚底": "19550002",

    # 鞋底材质
    "纯羊毛": "3229201",
    "超纤皮": "15099895", "EVA": "3376399", "EVA发泡胶": "77117384", "MD": "27366", "PU": "3323086",
    "PVC": "29228", "TPR(牛筋）": "807070564", "tpu": "7097887", "橡胶发泡": "19308111", "烟胶": "127517938",
    "皮": "3353142", "聚氨酯": "18956417","麻": "3267653", "泡沫": "134280", "橡胶": "30161", "木": "3260684",
    "复合底": "3268018", "软木": "18859111",

    # 图案
    "纯色": "29454", "格子": "29453", "拼色": "3222561", "手绘": "29455",

    # 流行元素
    "素面": "3302333", "豹纹": "3255041", "奢华马毛": "91477857", "图腾": "123658", "翻边": "29950",
    "荧光": "6330860", "雕花": "3341344", "迷彩": "52813", "金属": "20369", "马衔扣": "29033539", "车缝线": "115775",
    "皮草装饰": "43735669", "镂空": "115771", "编制": "3347671", "铆钉": "115776", "绣花" :"29957",
    "亮片": "29959", "流苏": "115777", "皮革拼接": "3226301", "水钻": "28209",

    # 场合
    "沙滩": "103414", "宴会": "139179", "办公室": "122738", "约会": "3267767", "日常": "3224795",
    "居家": "4068154", "运动休闲": "3325552", "结婚": "3267768",

    # 风格
    "青春潮流": "48816930", "复古": "43747", "休闲": "29535", "简约": "109835873", "韩版": "28105", "朋克": "29931",
    "商务": "28908", "日系": "3411108", "英伦": "3291373", "欧美": "125200612", "运动": "1628", "民族风": "132483",

    # 季节
    "夏季": "29457", "冬季": "29458", "春秋": "29456",

    # 功能
    "矫正": "599790307", "增高": "112301", "轻质": "25380975", "防水": "3217611", "减震": "7200622", "保暖": "4194098",
    "耐磨": "4526599", "透气": "137928",

    # 鞋制作工艺
    "固特异": "3280045", "缝制鞋": "14545463", "胶粘鞋": "14545464", "硫化鞋": "3272885", "注压鞋": "14545465",

    # 适用对象
    "青年（18-40周岁）": "3267959", "中年（40-60周岁）": "3267960", "老年（60周岁以上）": "101181",
    "儿童（18周岁以下）": "27845"
}


# 宝贝属性的key
cateProps = {
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

# 销售属性的key
skuProps = {
    "1627207": "",  # 颜色
    "20549": "",  # 尺码
}
skuProps = {
    "29544": "",  # 49
    "29545": "",  # 50
    "28396": "",  # 47
    "28395": "",  # 46
    "28394": "",  # 45
    "28393": "",  # 44
    "28392": "",  # 43
    "28391": "",  # 42
    "28390": "",  # 41
    "28389": "",  # 40
    "672": "",  # 39
    "28388": "",  # 38
    "29542": "",  # 37
    "671": "",  # 36
    "670": "",  # 35
    "28341": "", #黑色
    "28321": "",  # 乳白色
    "28320": "",  # 白色
    "4266701": "",  # 米白色
    "28332": "",  # 浅灰色
    "3232478": "",  # 深灰
    "28334": "",  # 灰色
    "28330": "",  # 银色
    "28326": "",  # 红色
    "28331": "",  # 卡其色
    "28328": "",  # 金色
    "28324": "",  # 黄色
    "3707775": "",  # 宝蓝色
    "28340": "",  # 深蓝色
    "28338": "",  # 蓝色
    "129819": "",  # 咖啡色
    "30158": "",  # 浅棕色
    "6588790": "",  # 深棕色
    "132069": "",  # 褐色
    "3232480": "",  # 粉红色
    "4950473": "桔红色", #
    "28327": "",  # 酒红色
    "3232483": "",  # 军绿色
    "28335": "",  # 绿色
    "3455405": "",  # 青色
    "3232484": "",  # 天蓝色
    "5483105": "",  # 湖蓝色
    "3232479": "",  # 深紫色
    "5167321": "",  # 紫红色
    "28329": "",  # 紫色
    "-1001": "",  # 自定义颜色1 需要在自定义属性项中添加
    "-1002": "",  # 自定义颜色2 同上
}
# 销售属性的value


# 第一行英文标题
rows_eng = {
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

rows_eng_cn = {
    "title": "宝贝名称",
    "cid": "宝贝类目",
    "seller_cids": "店铺类目",
    "stuff_status": "新旧程度",
    "location_state": "省",
    "location_city": "城市",
    "item_type": "出售方式",
    "price": "宝贝价格",
    "auction_increment": "加价幅度",
    "num": "宝贝数量",
    "valid_thru": "有效期",
    "freight_payer": "运费承担",
    "post_fee": "平邮",
    "ems_fee": "EMS",
    "express_fee": "快递",
    "has_invoice": "发票",
    "has_warranty": "保修",
    "approve_status": "放入仓库",
    "has_showcase": "橱窗推荐",
    "list_time": "开始时间",
    "description": "宝贝描述",
    "cateProps": "宝贝属性",
    "postage_id": "邮费模版ID",
    "has_discount": "会员打折",
    "modified": "修改时间",
    "upload_fail_msg": "上传状态",
    "picture_status": "图片状态",
    "auction_point": "返点比例",
    "picture": "新图片",
    "video": "视频",
    "skuProps": "销售属性组合",
    "inputPids": "用户输入ID串",
    "inputValues": "用户输入名 - 值对",
    "outer_id": "商家编码",
    "propAlias": "销售属性别名",
    "auto_fill": "代充类型",
    "num_id": "数字ID",
    "local_cid": "本地ID",
    "navigation_type": "宝贝分类",
    "user_name": "用户名称",
    "syncStatus": "宝贝状态",
    "is_lighting_consigment": "闪电发货",
    "is_xinpin": "新品",
    "foodparame": "食品专项",
    "features": "尺码库",
    "buyareatype": "采购地",
    "global_stock_type": "库存类型",
    "global_stock_country": "国家地区",
    "sub_stock_type": "库存计数",
    "item_size": "物流体积",
    "item_weight": "物流重量",
    "sell_promise": "退换货承诺",
    "custom_design_flag": "定制工具",
    "wireless_desc": "无线详情",
    "barcode": "商品条形码",
    "sku_barcode": "sku 条形码",
    "newprepay": "7天退货",
    "subtitle": "宝贝卖点",
    "cpv_memo": "属性值备注",
    "input_custom_cpv": "自定义属性值",
    "qualification": "商品资质",
    "add_qualification": "增加商品资质",
    "o2o_bind_service": "关联线下服务",
}

rows_eng_value = {
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


rows_eng_list = [
    "title",
    "cid",
    "seller_cids",
    "stuff_status",
    "location_state",
    "location_city",
    "item_type",
    "price",
    "auction_increment",
    "num",
    "valid_thru",
    "freight_payer",
    "post_fee",
    "ems_fee",
    "express_fee",
    "has_invoice",
    "has_warranty",
    "approve_status",
    "has_showcase",
    "list_time",
    "description",
    "cateProps",
    "postage_id",
    "has_discount",
    "modified",
    "upload_fail_msg",
    "picture_status",
    "auction_point",
    "picture",
    "video",
    "skuProps",
    "inputPids",
    "inputValues",
    "outer_id",
    "propAlias",
    "auto_fill",
    "num_id",
    "local_cid",
    "navigation_type",
    "user_name",
    "syncStatus",
    "is_lighting_consigment",
    "is_xinpin",
    "foodparame",
    "features",
    "buyareatype",
    "global_stock_type",
    "global_stock_country",
    "sub_stock_type",
    "item_size",
    "item_weight",
    "sell_promise",
    "custom_design_flag",
    "wireless_desc",
    "barcode",
    "sku_barcode",
    "newprepay",
    "subtitle",
    "cpv_memo",
    "input_custom_cpv",
    "qualification",
    "add_qualification",
    "o2o_bind_service",
]

# 第二行中文标题
rows_cn = {
    "宝贝名称": "",
    "宝贝类目": "",
    "店铺类目": "",
    "新旧程度": "1",
    "省": "福建",
    "城市": "泉州",
    "出售方式": "1",  # 一口价
    "宝贝价格": "",
    "加价幅度": "0",
    "宝贝数量": "1000",
    "有效期": "7",
    "运费承担": "2",  # 使用模版
    "平邮": "",
    "EMS": "",
    "快递": "0",
    "发票": "0",
    "保修": "0",
    "放入仓库": "1",
    "橱窗推荐": "0",
    "开始时间": "",
    "宝贝描述": "",
    "宝贝属性": "",
    "邮费模版ID": "9213395490",  # 申通部分不包邮
    "会员打折": "0",
    "修改时间": "2017/3/29  16:08:05",
    "上传状态": "200",
    "图片状态": "1;1;1;1;-1;-1;-1;",  # 上了几个图就前面几个1
    "返点比例": "0",

    # (..本地的文件):1:0(这个是主图的顺序0,1,2,3,4):|[这里可选的指定一个在线的图片]'
    "新图片": "1b37f....8:1:0:|;2f6....8b0c17:1:1:|https://www..._074026.jpg;",
    "视频": "",

    # 红色,尺码49价格20数量19
    # 20:19::1627207:28326;20549:29544;
    # 绿色,尺码:49,价格:20,数量:19,SKU:20
    # 20:19:20:1627207:28335;20549:29544;
    # 绿色,尺码:50,价格:30,数量:30
    # 30:30::1627207:28335;20549:29545;
    "销售属性组合": "",
    "用户输入ID串": "13021751",
    "用户输入名 - 值对": "", # 商家编码
    "商家编码": "", # 商家编码
    "销售属性别名": "",
    "代充类型": "0",
    "数字ID": "0",
    "本地ID": "0",
    "宝贝分类": "1", # 未选
    "用户名称": "gfdonx", # 淘宝名称
    "宝贝状态": "6", # 本地库存宝贝(不确定)
    "闪电发货": "216",
    "新品": "241",
    "食品专项": "",
    "尺码库": "mysize_tp:-1;sizeGroupId:29148;sizeGroupName:欧码;sizeGroupType:men_shoes;tags:52290,50370",
    "采购地": "0",
    "库存类型": "-1",
    "国家地区": "",
    "库存计数": "2",
    "物流体积": "bulk:0.000000",
    "物流重量": "1",
    "退换货承诺": "0",
    "定制工具": "",
    "无线详情": "",
    "商品条形码": "",
    "sku 条形码": "",
    "7天退货": "1",
    "宝贝卖点": "",
    "属性值备注": "",
    "自定义属性值": "",
    "商品资质": "%7B%20%20%7D",
    "增加商品资质": "0",
    "关联线下服务": "",
}

def function():
    print("测试是否有空值")
    for key, value in property_dict.items():
        if key is None:
            print value
        if value is None:
            print key


def create_csv():
    with open("Taobao/shoes.csv", 'wb') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=rows_eng_list)
        writer.writeheader()
        writer.writerow(rows_eng_cn)

        # 关cn中的值写入到value中
        for key, value in rows_eng_cn.items():
            for key1,value1 in rows_cn.items():
                if value == key1:
                    rows_eng_value[key] = value1

        writer.writerow(rows_eng_value)



        # writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

def function_run():
    print("--------------------")
    function()
    print("--------------------")
    create_csv()
    print("--------------------")


if __name__ == "__main__":
    function_run()
