"""
功能
1. 输入买入价，计算卖出价为多少时才能保本
2. 输入买入价和卖出价，计算利润
"""

COMMISION_RATE = 1.3/10000  # 佣金，双向收取
STAMP_TAX = 1/1000  # 印花税，卖出收取
TRANSFER_FEE = 0.2/10000  # 过户费，双向收取
COMMISION_THRESHOLD = 5/COMMISION_RATE  # 佣金变化门槛  # 万 1.3 为 38461.5385

def stock(buying_price,nums,selling_price=None):
    print('-'*10+'计算开始'+'-'*10)
    print('股票买入价：{}，买入数量：{}'.format(buying_price,nums))
    buying_total = buying_price * nums
    print(f'买入总价: {buying_total}')
    buying_commision = max(buying_total * COMMISION_RATE,5)
    print(f"买入佣金：{buying_commision:.3f}")
    buying_trancfer = TRANSFER_FEE * buying_total
    print(f"买入过户费：{buying_trancfer:.3f}")
    buying_cost = buying_total + buying_commision + buying_trancfer
    print(f"实际买入成本：{buying_cost}")
    print(f"平均单股成本：{buying_cost/nums:.3f}")

    if selling_price:
        print('-'*20)
        selling_total = selling_price * nums
        print(f'卖出总价: {selling_total}')
        selling_commision = max(selling_total * COMMISION_RATE,5)
        print(f"卖出佣金：{selling_commision:.3f}")
        selling_stamp_tax = STAMP_TAX * selling_total
        print(f"卖出印花税：{selling_stamp_tax:.3f}")
        selling_trancfer = TRANSFER_FEE * selling_total
        print(f"卖出过户费：{selling_trancfer:.3f}")
        selling_actual = selling_total - selling_commision - selling_stamp_tax - selling_trancfer
        print(f"实际卖出收益：{selling_actual:.3f}，单股价格：{selling_actual/nums:.3f}")
        print(f"实际卖出利润：{selling_actual - buying_cost:.3f}")
    else:
        print('-'*20)
        selling_actual = buying_cost
        # 先按 5 块计算佣金
        selling_total = (selling_actual+5) / (1-STAMP_TAX-TRANSFER_FEE)

        if selling_total > COMMISION_THRESHOLD:
            # 佣金按百分比
            selling_total = selling_actual / (1-COMMISION_RATE-STAMP_TAX-TRANSFER_FEE)
            print(f'卖出价格(保底)：{selling_total:.3f}')
            print(f"卖出单价(保底)：{selling_total/nums:.3f}")

        print(f'卖出价格(保底)：{selling_total:.3f}')
        print(f"卖出单价(保底)：{selling_total/nums:.3f}")

    print('-'*10+'计算结束'+'-'*10+'\n\n')

if __name__ == "__main__":
    # stock(buying_price=2.93 ,nums=5000)
    # stock(buying_price=2.93 ,selling_price=2.9351,nums=5000)

    # stock(3.07,nums=3000)
    # stock(3.02,nums=700)
    # stock(2.97,nums=1000)
    # stock(2.93,nums=1000)

    stock(2.93,selling_price=2.94, nums=5000)