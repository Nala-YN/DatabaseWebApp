### goToLogin()
前端：向后端/login发送post请求，其中
username:String类型，表示账号
password:String类型，表示密码
后端：接收请求，搜索用户信息表，查找对应于username和password的行，向前端返回信息：
isSuccess:Boolean类型,True表示登录成功，False表示登录失败
userId:int类型，标识用户的唯一id
### register()

前端：向后端/api/register发送post请求，
下面类型都是字符串
username: 用户名，必填
password: 用户登录密码，必填
email: 用户邮箱，必填
phoneNum: 10位只含数字的字符串
campus: 校区，目前没有设置可选列表，单纯让用户输入
address: 具体地址

后端：接受请求，搜索用户信息表，先检查邮箱是否注册过，
若已注册过，则在response.message返回错误描述，
若没注册过，尝试注册，设置response.success为登录是否成功，
再检查用户昵称是否已存在，
若已存在，则返回“用户昵称已存在”
若成功，**为新注册用户分配唯一的userid**,
若失败，返回错误信息