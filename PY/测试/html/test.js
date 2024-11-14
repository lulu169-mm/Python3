//TODO:1. 给定一个变量num,判断这个数字是否为整数,负数,还是0
//TODO:2. 给定两个变量a,b判断并输出较大的那个值
//TODO:3. 给定一个变量num,判断它是奇数还是偶数,并输出结果
//TODO:4. 给定两个变量a和b,计算他们的和,差,积,商,并输出结果,并且判断a和b的和与商是否相等

function choose(choice) {
    switch (choice) {
// TODO:1. 给定一个变量num1,判断这个数字是否为整数,负数,还是0
        case 1:
            let num1 = prompt("请输入一个数字:");
            num1 = Number(num1)  //转换成数字类型
            if (isNaN(num1)) {
                alert("输入的数字非法!")  //不允许为数字以外的其他数字
            } else if (num1 > 0) {
                alert("这是一个正数!")
            } else if (num1 < 0) {
                alert("这是一个负数!")
            } else {
                alert("这是一个蛋!")
            }
            break;
// TODO:2. 给定两个变量a,b判断并输出较大的那个值
        case 2:
            let a = prompt("请输入第一个数字:");
            let b = prompt("请输入第二个数字:");
            a = Number(a)
            b = Number(b)

            if (isNaN(a) || isNaN(b)) {
                alert("输入的数字不是有效的数字!")
            } else {
                const max = Math.max(a, b);
                alert("较大的数字是:" + max)
            }
            break;

// TODO:3. 给定一个变量num2,判断它是奇数还是偶数,并输出结果
        case 3:
            let num2 = prompt("请输入一个数字:");
            num2 = Number(num2)

            if (isNaN(num2)) {
                alert("输入的数字非法!") //不允许为数字以外的其他数字
            } else if (num2 % 2 === 0){
                alert(num2+"这是一个偶数!")
            }else {
                alert(num2+"这是一个奇数!")
            }
            break;

// TODO:4. 给定两个变量num3和num4,计算他们的和,差,积,商,并输出结果,并且判断a和b的和与商是否相等
        case 4:
            let num3 = prompt("请输入第一个数字:");
            let num4 = prompt("请输入第二个数字:");
            num3 = Number(num3)
            num4 = Number(num4)
            if (isNaN(num3) || isNaN(num4)) {
                alert("输入的数字非法!")
            }else {
                const sum = num3 + num4;
                const reduce = num3 - num4;
                const cheng = num3 * num4;
                const div = num3 / num4;
                alert("和:" + sum + "\n差:" + reduce + "\n积:" + cheng + "\n商:" + div)
                if (sum === div) {
                    alert("这两个数的和与商相等!")
                } else {
                    alert("这两个数的和与商不相等!")
                }
            }
            break;
            default:
                    alert("选择无效!")
    }
}

// TODO : 永真循环,可退出
while (true) {
    let choice = prompt("请输入数字选择功能：\n1. 判断数字的正负零\n2. 输出较大的数\n3. 判断数字的奇偶性\n4. 计算两数的和、差、积、商\n\n输入其他任何字符无效。");
    choice = Number(choice);
    if (isNaN(choice) || choice < 1 || choice > 4) {
        alert("请输入有效的数字选择!")  //不允许为数字以外的其他数字
    } else {
        choose(choice);
    }
    const go_on = confirm("是否继续?点击确定继续,点击取消退出");
    if (go_on === false) {
        break;  //用户选择取消退出循环
    }
}