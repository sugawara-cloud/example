# 社器保険料率
social_rate = 0.15

# 所得税率
tax_rate = 0.1


# 10円単位切り捨て
def trunc10(v):
    t = int(v / 10) * 10
    return t


if __name__ == "__main__":
