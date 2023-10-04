<template>
  <!-- 整体背景 -->
  <div id="body" class="login-wrap">
    <div id="background"></div>
    <!--输入框-->
    <div class="form-wrapper">
      <div class="header">书觅</div>
      <div class="input-wrapper">
        <div class="border-wrapper">
          <input type="text" name="username" placeholder="username" class="border-item" autocomplete="off"
            v-model="username" />
        </div>
        <div class="border-wrapper">
          <input type="password" name="password" placeholder="password" class="border-item" autocomplete="off"
            v-model="password" />
        </div>
      </div>
      <div class="action">
        <el-button class="btn" :plain="true" @click="goToLogin">登录</el-button>
        <el-button class="btn" :plain="true" @click="goToRegister">注册</el-button>
      </div>
      <br />
    </div>
  </div>
</template>

<script >
import axios from 'axios';
import { ElMessage } from 'element-plus';
// @ is an alias to /src
export default {
  name: "LoginView",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    goToLogin() {
      console.log("我要登陆了")
      axios.post('http://127.0.0.1:8000/login', {
        username: this.username,
        password: this.password,
      },)
      .then(response => {
        if(response.data.success===true){
          ElMessage({
          message:'登录成功',
          type: 'success'})
          this.$router.push({ name: 'main' });
        }
        else{
          ElMessage({
          message:'登录失败',
          type: 'warning'})
        }
      })
      .catch(error => {
        console.error(error);
      });
    },
    goToRegister() {
      // 使用编程式导航跳转到注册页面
      this.$router.push({ name: 'register' });
    }
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
  overflow: hidden;
  margin: 0;
}

#background {
  background: url("../assets/image/backgroundOfLogin.jpg");
  background-size: cover;
  position: absolute;
  top: -50px;
  bottom: -20px;
  left: -20px;
  right: -20px;
  z-index: -1;
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

.form-wrapper .input-wrapper input {
  background-color: rgb(255, 255, 255);
  border: 0;
  width: 100%;
  text-align: center;
  font-size: 15px;
  color: rgb(96, 93, 9);
  outline: none;
}

.form-wrapper .input-wrapper input::placeholder {
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
