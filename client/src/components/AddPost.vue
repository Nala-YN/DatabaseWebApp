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
import { ElMessage } from 'element-plus';

  export default {
    data() {
      return {
          title: "",
          content: "",
      };
    },
    methods: {
      submitForm() {
        this.$http.post('/api/uploadpost',{
          user_id:this.$store.getters.status.userid,
          title:this.title,
          content:this.content
        }).then(response=>{
          if(response.data.success){
            ElMessage({message:"发布成功",type:"success"})
          }
          else{
            ElMessage({message:"发布失败"+response.data.message,type:"error"})
          }
        }).catch(error=>{
          ElMessage({error,type:"error"})
        })
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
  
  