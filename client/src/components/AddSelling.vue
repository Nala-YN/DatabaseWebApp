<template>
  <div class="container">
    <h1>发布您的出售信息</h1>
    <el-form class="form" ref="form" :model="form" label-width="100px">
      <el-form-item label="书籍名称">
        <el-input v-model="name" placeholder="请输入书籍名称"></el-input>
      </el-form-item>
      <el-form-item label="书籍介绍">
        <el-input
          type="textarea"
          v-model="intro"
          placeholder="请输入书籍介绍"
          :autosize="{ minRows: 5, maxRows: 10 }"
        ></el-input>
      </el-form-item>
      <el-form-item label="书籍价格">
        <el-input-number v-model="price" :min="0" :step="1" controls-position="right"></el-input-number>
      </el-form-item>
      <el-form-item label="书籍图片">
        <el-upload
          list-type="picture-card"
          :on-remove="handleRemove"
          :on-exceed="handleExceed"
          :file-list="fileList"
          :http-request="uploadFile"
          :limit="1"
        >
          <i class="el-icon-plus"></i>
        </el-upload>
        <el-image style="width: 100px; height: 100px" :src="url" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('form')">发布</el-button>
        <el-button @click="resetForm('form')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from 'axios';
import { ElMessage } from 'element-plus'; 
export default {
  data() {
    return {
      name: "",
      intro: "",
      price: 0,
      dialogImageUrl: "",
      dialogVisible: false,
      base64:"",
      fileList:[],
      url:""
    };
  },
  methods: {
    submitForm() {
      // 这里是你的发布逻辑，可以发送请求到后端或者其他操作
      //console.log(this.fileList)
      axios.post('http://127.0.0.1:8000/api/upload',
      {
        image:this.base64
      }).then(response=>{
        console.log(response);
        this.url=response.data.image_data;
      }).catch(error=>{
        ElMessage({message:error,type:"error"})
      })
      this.resetForm();
    },
    resetForm() {
      this.name="";
      this.intro="";
      this.price="";
      this.fileList=[];
    },
    uploadFile(file) {
      console.log(file);
      // 这里是你的上传前的验证逻辑，可以检查文件类型和大小等
      const reader=new FileReader();
      reader.readAsDataURL(file.file);
      reader.onload=()=>{
        this.base64=reader.result;
      }
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handleExceed(){
      ElMessage({message:"只允许上传一张图片",type:"error"})
    }
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 80vh;
}

h1 {
  font-size: 24px;
}

.form {
  width: 75%;
}
</style>
