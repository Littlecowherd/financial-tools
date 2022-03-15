"""
功能
1. 输入买入价，计算卖出价为多少时才能保本
2. 输入买入价和卖出价，计算利润
"""

COMMISION_RATE = 1.3 / 10000  # 佣金，双向收取
STAMP_TAX = 1 / 1000  # 印花税，卖出收取
TRANSFER_FEE = 0.2 / 10000  # 过户费，双向收取
COMMISION_THRESHOLD = 5 / COMMISION_RATE  # 佣金变化门槛  # 万 1.3 为 38461.5385

SZ_COMMISION_RATE = 0.4 / 10000  # 深市可转债佣金
SH_COMMISION_RATE = 1 / 10000  # 沪市可转债佣金，起步 1 元
SH_COMMISION_THRESHOLD = 1 / SZ_COMMISION_RATE  # 佣金变化门槛，万 1 为 10000


def stock(buying_price, nums, selling_price=None):
    print("-" * 10 + "计算开始" + "-" * 10)
    print("股票买入价：{}，买入数量：{}".format(buying_price, nums))
    buying_total = buying_price * nums
    print(f"买入总价: {buying_total}")
    buying_commision = max(buying_total * COMMISION_RATE, 5)
    print(f"买入佣金：{buying_commision:.3f}")
    buying_trancfer = TRANSFER_FEE * buying_total
    print(f"买入过户费：{buying_trancfer:.3f}")
    buying_cost = buying_total + buying_commision + buying_trancfer
    print(f"实际买入成本：{buying_cost}")
    print(f"平均单股成本：{buying_cost/nums:.3f}")

    if selling_price:
        print("-" * 20)
        print(f"股票卖出价：{selling_price}，卖出数量：{nums}")
        selling_total = selling_price * nums
        print(f"卖出总价: {selling_total}")
        selling_commision = max(selling_total * COMMISION_RATE, 5)
        print(f"卖出佣金：{selling_commision:.3f}")
        selling_stamp_tax = STAMP_TAX * selling_total
        print(f"卖出印花税：{selling_stamp_tax:.3f}")
        selling_trancfer = TRANSFER_FEE * selling_total
        print(f"卖出过户费：{selling_trancfer:.3f}")
        selling_actual = (
            selling_total - selling_commision - selling_stamp_tax - selling_trancfer
        )
        print(f"实际卖出收益：{selling_actual:.3f}，单股价格：{selling_actual/nums:.3f}")
        print(f"实际卖出利润：{selling_actual - buying_cost:.3f}")
    else:
        print("-" * 20)
        selling_actual = buying_cost
        # 先按 5 块计算佣金
        selling_total = (selling_actual + 5) / (1 - STAMP_TAX - TRANSFER_FEE)

        if selling_total > COMMISION_THRESHOLD:
            # 佣金按百分比
            selling_total = selling_actual / (
                1 - COMMISION_RATE - STAMP_TAX - TRANSFER_FEE
            )
        print(f"卖出价格(保底)：{selling_total:.3f}")
        print(f"卖出单价(保底)：{selling_total/nums:.3f}")

    print("-" * 10 + "计算结束" + "-" * 10 + "\n\n")


def convertible_bond(
    buying_price=100, nums=10, selling_price=None, is_sz=True, by_sign=False
):
    print("-" * 10 + "计算开始" + "-" * 10)
    print(f"可转债买入价：{buying_price}，买入数量：{nums}")
    buying_total = buying_price * nums
    print(f"买入总价: {buying_total}")
    if by_sign:  # 打新没有佣金
        buying_commision = 0
    else:
        if not is_sz:  # 上海，最低 1 元
            buying_commision = max(1, buying_total * SH_COMMISION_RATE)
        else:
            buying_commision = buying_total * SZ_COMMISION_RATE
    print(f"买入佣金：{buying_commision:.3f}")
    buying_cost = buying_total + buying_commision
    print(f"实际买入成本：{buying_cost}")
    print(f"平均单张成本：{buying_cost/nums:.3f}")

    if selling_price:
        print("-" * 20)
        print(f"可转债卖出价：{selling_price}，卖出数量：{nums}")
        selling_total = selling_price * nums
        print(f"卖出总价: {selling_total}")
        if not is_sz:  # 上海，最低 1 元
            selling_commision = max(1, selling_total * SH_COMMISION_RATE)
        else:
            selling_commision = selling_total * SZ_COMMISION_RATE
        print(f"卖出佣金：{selling_commision:.3f}")
        selling_actual = selling_total - selling_commision
        print(f"实际卖出收益：{selling_actual:.3f}，单张价格：{selling_actual/nums:.3f}")
        print(f"实际卖出利润：{selling_actual - buying_cost:.3f}")
    else:
        print("-" * 20)
        selling_actual = buying_cost
        if is_sz:
            selling_total = selling_actual / (1 - SZ_COMMISION_RATE)
        else:
            selling_total = selling_actual + 1
            if selling_total > SH_COMMISION_THRESHOLD:
                selling_total = selling_actual / (1 - SH_COMMISION_RATE)
        print(f"卖出价格(保底)：{selling_total:.3f}")
        print(f"卖出单价(保底)：{selling_total/nums:.3f}")


if __name__ == "__main__":
    # stock(buying_price=2.93 ,nums=5000)
    # stock(buying_price=2.93 ,selling_price=2.9351,nums=5000)

    # stock(3.07,nums=3000)
    # stock(3.02,nums=700)
    # stock(2.97,nums=1000)
    # stock(2.93,nums=1000)

    # stock(2.93, nums=5000,selling_price=2.94)
    convertible_bond(buying_price=122, selling_price=123, nums=100, is_sz=False)
