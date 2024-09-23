const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 8001;

// 启用 CORS
app.use(cors());

// 示例路由
app.get('/api/data', (req, res) => {
    res.json({ message: '你好 CORS!' });
});

// 启动服务器
app.listen(PORT, () => {
    console.log(`://localhost:${PORT}`);
});
