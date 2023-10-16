<template>
    <!-- 整体背景 -->
    <div id="body">
      <!-- <div id="background"></div> -->
      <!--输入框-->
      <div class="form-wrapper">
        <div class="header">创建新账户</div>
        <div v-if="step === 1" class="input-wrapper">
          <div class="border-wrapper">
            <input type="text" name="username" placeholder="username" class="border-item" autocomplete="off"
              v-model="username" />
          </div>
          <div class="border-wrapper">
            <input type="email" name="email" placeholder="email" class="border-item" autocomplete="off"
              v-model="email" />
          </div>
          <div class="border-wrapper">
            <input type="password" name="password" placeholder="password" class="border-item" autocomplete="off"
              v-model="password" />
          </div>
          <div class="border-wrapper">
            <input type="password" name="confirm" placeholder="confirm" class="border-item" autocomplete="off"
              v-model="confirmPassword" />
          </div>
        </div>
        <div v-else class="input-wrapper">
          <div class="border-wrapper">
            <input type="text" name="phone" placeholder="phone" class="border-item" autocomplete="off"
              pattern="[0-9]{10}" v-model="phoneNum" />
          </div>
          <div class="border-wrapper">
            <input type="text" name="campus" placeholder="campus" class="border-item" autocomplete="off"
              v-model="campus" />
          </div>
          <div class="border-wrapper">
            <input type="text" name="address" placeholder="address" class="border-item" autocomplete="off"
              v-model="address" />
          </div>
        </div>
  
        <div v-if="step === 1" class="action">
          <el-button class="btn" :plain="true" @click="$router.push('/login')">登录</el-button>
          <el-button class="btn" :plain="true" @click="nextPage">下一步</el-button>
        </div>
        <div v-else class="action">
          <el-button class="btn" :plain="true" @click="step = 1">上一步</el-button>
          <el-button class="btn" :plain="true" @click="submitForm">注册</el-button>
        </div>
        <br />
      </div>
    </div>
    
  </template>
  
  <script>
  import axios from 'axios';
  import { ElMessage } from 'element-plus';
  
  export default {
    name: 'RegisterView',

    data() {
      return {
        // userid: 1,
        username: '',
        password: '',
        phoneNum: '',
        email: '',
        campus: '',
        address: '',
        confirmPassword: '',
        
        step: 1,
      };
    },
    methods: {
      nextPage() {
        let emailReg = /^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$/;
        let passwordReg  = /^(?=.*[A-Za-z])(?=.*\d).{6,}$/;
        if (this.username.length === 0 || this.password.length === 0 || this.email.length === 0 || this.confirmPassword.length === 0) {
          ElMessage({message: "输入不可为空", type: 'warning'});
        } else if (!emailReg.test(this.email)) {
          // 如果不符合，显示错误信息
          // alert('请输入正确的邮箱地址');
          ElMessage({message: "请输入正确的邮箱地址", type: 'warning'});
        } else if (!passwordReg.test(this.password)) {
          ElMessage({message: "密码长度需大于等于6, 且数字和字母都要包含", type: 'warning'});
        } else if (this.password !== this.confirmPassword) {
          ElMessage({message: "二次密码输入不一致", type: 'warning'});
        } else {
          this.step = 2;
        }
      },
      submitForm() {
        let phoneReg = /^(?=.{10}\d)$/;
        if (this.phoneNum.length !== 0 && !phoneReg.test(this.phoneNum)) {
          ElMessage({message: "请输入合法的电话号码", type: 'warning'});
        }

        const registerForm = {
          // userid: toString(this.userid++),
          username: this.username,
          password: this.password,
          email: this.email,
          phoneNum: this.phoneNum,
          campus: this.campus,
          address: this.address
        };
  
        // 发送注册请求到后端
        // 假设使用axios库发送请求
        axios
          .post('/api/register', registerForm)
          .then((response) => {
            if (response.data.success) {
              // 注册成功，执行登录逻辑，例如重定向到登录页面
              alert('注册成功！');
              this.$router.push('/login');
            } else {
              // 注册失败，处理失败情况，例如显示错误信息
              // 已知错误类型：邮箱账户已存在
              alert('注册失败：' + response.data.message);
            }
          })
          .catch((error) => {
            // 处理网络请求失败等情况
            console.error('注册失败：', error);
            alert('注册失败，请稍后重试');
          });
  
      },
    },
  };
  </script>
  
  <style scoped>
  #body {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    height: 100vh;
    overflow: auto;
    margin: 0;

    background: url("../assets/image/backgroundOfLogin.jpg");
    background-size: cover;
    position: center top;
    background-attachment: fixed;
  }
  
  .form-wrapper {
    width: 300px;
    background-color: rgba(128, 128, 128, 0.8);
    color: #fff;
    border-radius: 20px;
    padding: 50px;
  }
  
  .form-wrapper .header {
    text-align: center;
    font-size: 40px;
    margin-bottom: 30px;
    text-transform: uppercase;
    line-height: 100px;
  }
  
  .form-wrapper .input-wrapper input,
  .form-wrapper .input-wrapper el-input {
    background-color: rgb(255, 255, 255);
    border: 0;
    width: 100%;
    text-align: center;
    font-size: 15px;
    color: rgb(96, 93, 9);
    outline: none;
  }
  
  .form-wrapper .input-wrapper input::placeholder,
  .form-wrapper .input-wrapper el-input::placeholder {
    text-transform: uppercase;
  }
  
  .form-wrapper .input-wrapper .border-wrapper {
    background-image: linear-gradient(to right, #000000, #000000);
    width: 100%;
    height: 50px;
    margin-bottom: 20px;
    border-radius: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .form-wrapper .input-wrapper .border-wrapper .border-item {
    height: calc(100% - 4px);
    width: calc(100% - 4px);
    border-radius: 30px;
  }
  
  .form-wrapper .action {
    display: flex;
    justify-content: center;
  }
  
  .form-wrapper .action .btn {
    width: 60%;
    text-transform: uppercase;
    border: 2px solid #3d3d3d;
    text-align: center;
    line-height: 50px;
    border-radius: 30px;
    cursor: pointer;
  }
  
  .form-wrapper .action .btn:hover {
    background-color: rgba(79, 79, 79, 0.8);
    color: #000000;
  }
  
  .form-wrapper .icon-wrapper {
    text-align: center;
    width: 60%;
    margin: 0 auto;
    margin-top: 20px;
    border-top: 1px dashed rgb(146, 146, 146);
    padding: 20px;
  }
  
  .el-message {
    max-width: 300px;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  
  .form-wrapper .icon-wrapper i {
    font-size: 20px;
    color: rgb(187, 187, 187);
    cursor: pointer;
    border: 1px solid #fff;
    padding: 5px;
    border-radius: 20px;
  }
  
  .form-wrapper .icon-wrapper i:hover {
    background-color: #0e92b3;
  }
  
  </style>
  