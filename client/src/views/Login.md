### goToLogin()
前端：向后端/login发送post请求，其中
username:String类型，表示账号
password:String类型，表示密码
后端：接收请求，搜索用户信息表，查找对应于username和password的行，向前端返回信息：
isSuccess:Boolean类型,True表示登录成功，False表示登录失败
