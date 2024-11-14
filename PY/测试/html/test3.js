//TODO:输出当前时间
const time = Date();
console.log(time)

//TODO:自定义对象，并输出
const obj = {
    name: '张三',
    age: 18
};
console.log(obj)

class object {
}

const person = new object();
person.name = '张三'
person.age = 18
console.log(person)

//TODO:Math函数
console.log(Math.random())  //0-1之间的随机数,包括0不包括1
console.log(Math.max(1, 2, 3, 4, 5))
console.log(Math.min(1, 2, 3, 4, 5))
console.log(Math.abs(-1))       //取绝对值
console.log(Math.pow(2, 3))   //2的3次方
console.log(Math.sqrt(4))       //4的平方根
console.log(Math.random() * 101)    //0-100之间的随机数
console.log(Math.round(12.94))  //四舍五入 13
console.log(Math.trunc(12.94))  //去除小数部分 12 ,相当于向下取整 Math.floor(12.94)

// TODO:完成一个猜数字游戏,随机产生1-100的整数,然后由用户在文本框
//  输入猜到的数据,将用户输入的数据和程序产生的做一个比较
// while (true){
//     let num_user = prompt("请输入你猜的数字(0-100):");
//     num_user = Number(num_user)
//     const num_computer = Math.trunc(Math.random() * 100)+1;
//     if (num_user < 0 || num_user > 100) {
//         alert("您输入的数字不合法!")
//     } else if (num_user > num_computer) {
//         alert("您猜的数字有点大了,请重新试试！")
//     } else if (num_user < num_computer) {
//         alert("您猜的数字太小了,请再试试!")
//     } else {
//         alert("恭喜您猜对了!")
//         break;
//     }}


//TODO:生成1-100的数组
// let arr = [];
// for (let i = 1; i <= 100; i++) {
//     arr.push(i);
// }
// // 随机抽取数组中的一个数
// let randomIndex = Math.floor(Math.random() * arr.length); // 生成随机索引
// let randomElement = arr[randomIndex]; // 获取随机元素
// // console.log("随机抽取的数字是:", randomElement);
// while (true) {
//     let num_user = prompt("请输入你猜的数字(1-100):");
//     num_user = Number(num_user)
//     if (num_user < 1 || num_user > 100) {
//         alert("您输入的数字不合法!")
//     } else if (num_user > randomElement) {
//         alert("您猜的数字有点大了,请重新试试！")
//     } else if (num_user < randomElement) {
//         alert("您猜的数字太小了,请再试试!")
//     } else {
//         alert("恭喜您猜对了!")
//         break;
//     }
// }

//TODO:使用process.stdout.write不换行输出字符串
const str = "hello world";
for (let i = 0; i < str.length; i++) {
    process.stdout.write(str[i]); // 直接输出每个字符，不会自动换行
}
console.log(); // 输出空行，使程序结束

//TODO:使用拼接""不换行输出字符串
const str1 = "hello world";
let str2 = ""
for (let i = 0; i < str1.length; i++) {
    str2 += str1[i]; // 使用+=操作符拼接字符串
}
console.log(str2); // 输出拼接后的字符串

//TODO:string的常用方法
const str3 = "Hello World";
console.log(str3.length) //字符串的长度
console.log(str3.toUpperCase()) //将字符串转换为大写,HELLO WORLD
console.log(str3.toLowerCase()) //将字符串转换为小写,hello world
console.log(str3.indexOf("o")) //返回指定字符串在原字符串中第一次出现的位置，4
console.log(str3.lastIndexOf("o")) //返回指定字符串在原字符串中最后一次出现的位置，7
console.log(str3.substring(6, 12)) //返回从指定位置开始到指定位置结束的子字符串,World
console.log(str3.split(" ")) //指定分隔符分割字符串,["Hello","World"]
console.log(str3.trim())  //去除两端的空格(用于用户输入)
console.log(str3.match(/World/)) //匹配字符串,返回一个数组,["World"]

//TODO:给定一个字符串,查找当中m出现的位置,统计每一个字母大小写出现的次数,字符出现的次数,其它字符
const string = "uiehfeuwhuWWFGHMMCMMHOOMMMXNIqqqqQQQQSODHM2389742378978934789234没舍得买cmwemq你好3499345*&^%^$$%^&*(())__)$%$";
// 统计字母大小写出现的次数的对象
let letterCounts = {};
// 统计字符出现的次数
let otherCharCount = 0;
// 统计m出现的位置
let positionsOfM = [];
for (let i = 0; i < string.length; i++) {
    let char = string[i].toLowerCase(); // 转换为小写以统一计数
    if (char >= 'a' && char <= 'z') {
        if (char === 'm') {
            positionsOfM.push(i); // 记录m出现的位置
        }
        if (!letterCounts[char]) {
            letterCounts[char] = 0;
        }
        letterCounts[char]++; // 统计字母出现的次数
    } else {
        otherCharCount++; // 统计非字母字符的个数
    }
}
// 输出字母出现的次数
for (let letter in letterCounts) {
    console.log(`${letter}出现的次数: ${letterCounts[letter]}`);
}
// 输出字符出现的次数
console.log(`其他字符出现的次数: ${otherCharCount}`);
// 输出m出现的位置
console.log(`m出现的位置: ${positionsOfM}`);

//TODO:使用match匹配指定字符出现次数
let str11 = "abcabcabcabcabcabcbabccabc";
let count_11 = str11.match(/abc/g).length;  // /g表示全局匹配
console.log(count_11);

//TODO:indexOf匹配
let text = "abcabcabcabcabcabcbabccabc", check = "abc", num = 0;
let idx = text.indexOf(check);
while (idx !== -1) {
    num++;
    idx = text.indexOf(check, idx + 1);
}
console.log(num);

//TODO:数组的常用方法
let arr = [1, 2, 3, 4, 5];
console.log(arr.toString().split(","))  // toString()方法将数组转换为字符串，然后使用split()方法将字符串转换为数组
console.log(arr.length); // 输出数组的长度，5
arr.push(6) // 在数组末尾添加元素
console.log(arr); // 输出 [1, 2, 3, 4, 5, 6]
arr.pop() // 删除数组末尾的元素
console.log(arr); // 输出 [1, 2, 3, 4, 5]
console.log(arr.join("-")); // 输出 "1-2-3-4-5"
console.log(arr.reverse()) // 输出 [5, 4, 3, 2, 1] 反转
console.log(arr.join("分 ")); // 输出 "5分4分3分2分1", 注意:只会在元素之间添加

//TODO:传入Hello World 返回 "dlroW olleH"
function reverseString(str) {
    return str.split("").reverse().join("");
}

console.log(reverseString("Hello World"));

let str33 = "Hello World";
split_str33 = str33.split("") //使用split()方法将字符串分割成数组
// console.log(split_str33)
reverse_str33 = split_str33.reverse()  //使用reverse()方法将数组反转
// console.log(reverse_str33)
join_str33 = reverse_str33.join("")    //使用join()方法将数组连接成字符串
console.log(join_str33)

//TODO:验证字符串:长度4-16,只包含数字,英文字符,下划线三种符号,首字符不能是数字
// function checkString() {
//     var string44 = prompt("请输入字符串")
//     if (string44.length < 4 || string44.length > 16) {
//         alert("字符串长度必须在4到16之间!")
//     }
//     if (!/^[a-zA-Z0-9_]+$/.test(string44)) {
//         alert("字符串只能包含数字,英文字符和下划线!")
//     }
//     if (/^[0-9]/.test(string44)) {
//         alert("字符串首字符不能是数字!")
//     }
//     if (string44.length >= 4 && string44.length <= 16 && /^[a-zA-Z0-9_]+$/.test(string44) && !/^[0-9]/.test(string44)) {
//         alert("字符串验证通过!")
//     }
// }
// checkString()






























