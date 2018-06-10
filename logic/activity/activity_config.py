# -*- coding: utf-8 -*-
# 活动配置 适用于450级以上


activity_config = {
    # 对战
    "KFRank": {
        "enable": True,  # 开启
        "task": {  # 任务 战胜比自己等级高的玩家3次, 胜利25场, 累计获得100积分, 连胜5场
            "enable": True,  # 刷新任务
            "list": [  # 可刷新任务列表
                # "以弱胜强",
                # "胜者为王",
                "突飞猛进",
                # "连胜传奇",
            ],
        },
        "limit_token": 10,  # 每日限制军令<=N
        "ack_formation": "不变阵",  # 攻击阵型 不变阵, 鱼鳞阵, 长蛇阵, 锋矢阵, 偃月阵, 锥形阵, 八卦阵, 七星阵, 雁行阵
        "def_formation": "鱼鳞阵",  # 防御阵型 不变阵, 鱼鳞阵, 长蛇阵, 锋矢阵, 偃月阵, 锥形阵, 八卦阵, 七星阵, 雁行阵
        "def_enable": True,  # 开启积分下降
        "def_score": 800,  # 积分>=N，使用防御阵型
    },
    # 大宴群雄
    "BGEvent": {
        "enable": True,  # 开启
        "limit_cost": 10,  # 花费金币<=N
    },
}