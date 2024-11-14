shopping = [
    ('iphone 16 promax', 8999),
    ('mac pro', 12999),
    ('ipad pro', 7999),
    ('ipad air', 5999),
    ('casio', 1999),
    ('xiaomi', 2999),
    ('huawei', 3999),
    ('vivo', 1999),
    ('oppo', 1999),
    ('oneplus', 3999),
    ('realme', 1999),
    ('redmi', 1999),
    ('samsung', 3999),
    ('huawei', 3999),
    ('极乐号', 20000),
    ('东方红', 19800),
    ('神舟号', 19800),
    ('嫦娥五号', 19800),
    ('嫦娥六号', 19800),
    ('嫦娥七号', 19800),
    ('长江1-7号全家桶', 999999),
    ('长寿泡面', 300),
]
print("---------------欢迎来到天地人民超市--------------------")
# 获取在天地人民银行的余额
money = int(input('请输入您在天地人民银行的余额：'))
shoping_list = []  # 购物车

while True:
    # 打印商品列表
    print("\n商品列表：")
    for index, (product, price) in enumerate(shopping):
        print(f"{index + 1}. {product}--{price}元")

    # 获取用户选择的商品编号
    choice = input('请输入您要购买的商品编号 (退出请按 q)：')

    # 判断是否退出
    if choice.lower() == 'q':
        if shoping_list:
            print("\n您已成功购买以下商品：")
            print("---------------------------------------")
            for shop in shoping_list:
                print(f"{shop[0]} -- {shop[1]}元")
            print("---------------------------------------")
        else:
            print("您未购买任何商品。")
        print(f"您已退出购物！当前在天地人民银行的余额为 {money} 元")
        break

    # 判断商品编号是否有效
    if choice.isdigit():
        choice = int(choice) - 1
        if 0 <= choice < len(shopping):
            product_name, product_price = shopping[choice]

            # 判断在天地人民银行的余额情况
            if money >= product_price:
                money -= product_price
                # 将商品添加到购物车
                shoping_list.append((product_name, product_price))
                print(f"\n您已成功购买 {product_name}，当前在天地人民银行的余额为 {money} 元")

                # 询问是否继续购物
                if input('是否继续购物 (y/n)？').lower() == 'n':
                    print("\n您已成功购买以下商品：")
                    print("---------------------------------------")
                    for shop in shoping_list:
                        print(f"{shop[0]} -- {shop[1]}元")
                    print(f"购物结束，您在天地人民银行的余额为 {money} 元")
                    print("---------------------------------------")
                    break
            else:
                print(f"对不起，您在天地人民银行的余额不足以购买 {product_name}，当前在天地人民银行的余额为 {money} 元")
                if input('是否继续购物 (y/n)？').lower() == 'n':
                    print("\n您已成功购买以下商品：")
                    print("---------------------------------------")
                    for shop in shoping_list:
                        print(f"{shop[0]} -- {shop[1]}元")
                    print(f"购物结束，您在天地人民银行的余额为 {money} 元")
                    print("---------------------------------------")
                    break
        else:
            print("商品编号不存在！")
            if input('是否继续购物 (y/n)？').lower() == 'n':
                print("\n您已成功购买以下商品：")
                print("---------------------------------------")
                for shop in shoping_list:
                    print(f"{shop[0]} -- {shop[1]}元")
                print(f"购物结束，您在天地人民银行的余额为 {money} 元")
                print("---------------------------------------")
                break
    else:
        print("请输入有效的商品编号！")
        if input('是否继续购物 (y/n)？').lower() == 'n':
            print("\n您已成功购买以下商品：")
            print("---------------------------------------")
            for shop in shoping_list:
                print(f"{shop[0]} -- {shop[1]}元")
            print(f"购物结束，您在天地人民银行的余额为 {money} 元")
            print("---------------------------------------")
            break


