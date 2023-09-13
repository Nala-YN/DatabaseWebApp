<template>
  <div class="register-form">
    <el-form
      :model="registerForm"
      :rules="rules"
      ref="registerForm"
      label-width="80px"
    >
      <el-form-item label="用户名" prop="username">
        <el-input v-model="registerForm.username"></el-input>
      </el-form-item>

      <el-form-item label="密码" prop="password">
        <el-input type="password" v-model="registerForm.password"></el-input>
      </el-form-item>

      <el-form-item label="确认密码" prop="confirmPassword">
        <el-input type="password" v-model="registerForm.confirmPassword"></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm">注册</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'RegisterView',
  data() {
    return {
      registerForm: {
        username: '',
        password: '',
        confirmPassword: '',
      },
      rules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, message: '密码长度不能少于6个字符', trigger: 'blur' },
        ],
        confirmPassword: [
          { required: true, message: '请再次输入密码', trigger: 'blur' },
          {
            validator: (rule, value, callback) => {
              if (value === this.registerForm.password) {
                callback();
              } else {
                callback(new Error('两次输入的密码不一致'));
              }
            },
            trigger: 'blur',
          },
        ],
      },
    };
  },
  methods: {
    submitForm() {
      this.$refs.registerForm.validate(valid => {
        if (valid) {
          // 执行注册逻辑，例如向后端发送注册请求
          // 在注册成功后，可以进行页面跳转或其他操作
          // 示例：向控制台打印注册信息
          console.log('注册信息:', this.registerForm);
          this.$router.push({ name: 'Main' });
        }
      });
    },
  },
};
</script>

<style scoped>
.register-form {
  max-width: 400px;
  margin: 0 auto;
}
</style>
