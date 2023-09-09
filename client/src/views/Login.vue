<template>
  <!-- 整体背景 -->
  <div id="body" class="login-wrap">
    <div id="background"></div>
    <!--输入框-->
    <div class="form-wrapper">
      <div class="header">music manage</div>
      <div class="input-wrapper">
        <div class="border-wrapper">
          <input
            type="text"
            name="username"
            placeholder="username"
            class="border-item"
            autocomplete="off"
            v-model="username"
          />
        </div>
        <div class="border-wrapper">
          <input
            type="password"
            name="password"
            placeholder="password"
            class="border-item"
            autocomplete="off"
            v-model="password"
          />
        </div>
      </div>
      <div class="action">
        <button class="btn" type="submit" @click="submit">登录</button>
        <button class="btn" type="submit" @click="register">注册</button>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "LoginView",
  
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
  top: -20px;
  bottom: -20px;
  left: -20px;
  right: -20px;
  z-index: -1;
}
.form-wrapper {
  width: 300px;
  background-color: rgba(248, 136, 7, 0.8);
  color: #fff;
  border-radius: 20px;
  padding: 50px;
}

.form-wrapper .header {
  text-align: center;
  font-size: 35px;
  text-transform: uppercase;
  line-height: 100px;
}

.form-wrapper .input-wrapper input {
  background-color: rgb(255, 255, 255);
  border: 0;
  width: 100%;
  text-align: center;
  font-size: 15px;
  color: #fff;
  outline: none;
}

.form-wrapper .input-wrapper input::placeholder {
  text-transform: uppercase;
}

.form-wrapper .input-wrapper .border-wrapper {
  background-image: linear-gradient(to right, #e8198b, #0eb4dd);
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
  border: 2px solid #c0d65d;
  text-align: center;
  line-height: 50px;
  border-radius: 30px;
  cursor: pointer;
}

.form-wrapper .action .btn:hover {
    background-color: rgba(233, 189, 139, 0.8);
}

.form-wrapper .icon-wrapper {
  text-align: center;
  width: 60%;
  margin: 0 auto;
  margin-top: 20px;
  border-top: 1px dashed rgb(146, 146, 146);
  padding: 20px;
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
