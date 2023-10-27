// index.js
import axios from 'axios';

// 创建自定义的axios实例
const service = axios.create({
  // 设置后端地址的前缀
  baseURL: 'http://127.0.0.1:8000/',
  // 设置其他全局选项，例如超时时间，请求头等
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// 导出自定义的axios实例
export default service;
