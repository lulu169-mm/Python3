const express = require('express');
const app = express();

app.get('/api/data', (req, res) => {
  const callback = req.query.callback; // 获取回调函数名称
  const data = { message: '这是jsonp实现的跨域' };
  res.type('application/javascript'); // 设置响应类型
  res.send(`${callback}(${JSON.stringify(data)})`); // 返回JSONP格式
});

app.listen(3000, () => {
  console.log('请访问:http://localhost:3000/api/data?callback=handleData');
});
