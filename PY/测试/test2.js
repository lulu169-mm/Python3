// TODO:输入三个整数,按从小到大的顺序输出
const list = [10222, 412, 666];
list.sort((A, B) => A - B)         //sort()方法用于对数组的元素进行排序
console.log(list)
console.log("----------------------------")

//TODO:函数方法写
// function sort_list(a,b,c){
//     var sort_list=[a,b,c]
//     sort_list.sort((A,B)=>A-B)
//     console.log(sort_list)
// }
// sort_list(11,9,8)

//TODO:水仙花数
//python的写法
// for i in range(100,1000):
//     a=i//100
//     b=(i//10)%10
//     c=i%10
//     if i==a**3+b**3+c**3:
//         print(i)

for (let i = 100; i < 1000; i++) {
    const a = Math.floor(i / 100);    //floor用于向下取整
    const b = Math.floor((i / 10) % 10);
    const c = i % 10;
    if (i === a ** 3 + b ** 3 + c ** 3) {
        console.log(i)
    }
}
console.log("----------------------------")

//TODO:程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位,向下取整
for (let m = 100; m < 1000; m++) {
    const a1 = m % 10;
    const a2 = Math.floor(m / 10 % 10);
    const a3 = Math.floor(m / 100 % 10);
    console.log("数字:" + m, "百位:" + a3, "十位:" + a2, "个位:" + a1)
}
console.log("----------------------------")

//TODO:输出100-200之间不能被3整除的数
for (let l = 100; l < 200; l++) {
    if (l % 3 !== 0) {
        console.log("l=" + l)
    }
}

console.log("----------------------------")

//TODO:一张纸的厚度为0.1mm,珠穆朗玛峰的高度为8848m,问将纸折叠多少次才能超过珠穆朗玛峰的高度
let paper = 0.1, height = 8848130;
let count = 0;
while (paper < height) {
    paper *= 2
    count++
}
console.log("折叠次数为:" + count)

console.log("----------------------------")

//TODO:用1元纸币兑换1分,2分,5分的硬币,要求兑换的总数为50枚,问可以有多少中组合,每种组合对应的硬币各是多少枚
let w, e, y;
count = 0;
for (w = 0; w <= 20; w++) {
    for (e = 0; e <= 50; e++) {
        for (y = 0; y <= 50; y++) {
            if (w + e + y === 50 && 5 * w + 2 * e + y === 100) {
                console.log("w=" + w, "e=" + e, "y=" + y)
                count++
            }
        }
    }
}
console.log("共有" + count + "种组合")

console.log("----------------------------")

//TODO:function
function sum(a, b) {
    sum = a + b
    console.log("两个数的和为:" + sum)
}

sum(395655, 26675757)


// 使用 Array.from() 生成包含数字 1 到 999 的数组
let list1 = Array.from({ length: 999 }, (_, index) => index + 1);
console.log(list1);
