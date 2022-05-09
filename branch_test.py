# 社器保険料率
social_rate = 0.15

# 所得税率
tax_rate = 0.1


# 10円単位四捨五入
def round10(v):
    r = int(v / 10 + 0.5) * 10
    return r


# 10円単位切り捨て
def trunc10(v):
    t = int(v / 10) * 10
    return t


# 管理職
def calc_manager(base, post):
    salary = base + post
    social = round10(salary * social_rate)
    tax = (salary - social) * tax_rate
    bank = salary - social - tax
    return int(bank)


if __name__ == "__main__":
    bank_terao = calc_manager(350000, 80000)
    bank_waka = calc_manager(375000, 40000)

    print(f'寺尾哲雄さんの振込額={bank_terao}')
    print(f'若林仁継さんの振込額={bank_waka}')