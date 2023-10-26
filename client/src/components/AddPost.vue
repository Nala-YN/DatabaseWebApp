<template>
    <div class="container">
      <h1>发布您的帖子</h1>
      <el-form class="form" ref="form" :model="form" label-width="80px">
        <el-form-item label="标题">
          <el-input v-model="title" placeholder="请输入标题"></el-input>
        </el-form-item>
        <el-form-item label="内容">
          <el-input
            type="textarea"
            v-model="content"
            placeholder="请输入内容"
            :autosize="{ minRows: 10, maxRows: 20 }"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('form')">发布</el-button>
          <el-button @click="resetForm('form')">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
          title: "",
          content: "",
      };
    },
    methods: {
      submitForm(formName) {
        // 这里是你的发布逻辑，可以发送请求到后端或者其他操作
        console.log(this.form);
      },
      resetForm(formName) {
        this.title="";
        this.content="";
      },
    },
  };
  </script>
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 100vh;
  }
  
  h1 {
    font-size: 24px;
  }
  
  .form {
    width: 75%;
  }
  </style>
  
  