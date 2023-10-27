<template>
  <div class="container">
    <h1>发布您的出售信息</h1>
    <el-form class="form" ref="form" :model="form" label-width="100px">
      <el-form-item label="书籍名称">
        <el-input v-model="name" placeholder="请输入书籍名称"></el-input>
      </el-form-item>
      <el-form-item label="书籍介绍">
        <el-input type="textarea" v-model="intro" placeholder="请输入书籍介绍：如作者、出版社、新旧程度等"
          :autosize="{ minRows: 5, maxRows: 10 }"></el-input>
      </el-form-item>
      <el-form-item label="书籍价格">
        <el-input-number v-model="price" :min="0" :step="1" controls-position="right"></el-input-number>
      </el-form-item>
      <el-form-item label="书籍封面图片">
        <el-upload list-type="picture-card" :on-remove="handleRemove" :on-exceed="handleExceed" :file-list="fileList"
          :http-request="uploadFile" :before-upload="handleUpload" :limit="1">
          <i class="el-icon-plus"></i>
        </el-upload>
        <!-- <el-image style="width: 100px; height: 100px" :src="url" /> -->
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
      base64: "",
      fileList: [],
    };
  },
  methods: {
    submitForm() {
      // 这里是你的发布逻辑，可以发送请求到后端或者其他操作
      //console.log(this.fileList)
      this.$http.post('/api/uploadsell',
        {
          user_id:this.$store.getters.status.userid,
          book_name:this.name,
          book_intro:this.intro,
          book_price:this.price,
          book_image: this.base64
        }).then(response => {
          if(response.data.success){
            ElMessage({message:"发布成功",type:"success"})
          }
          else{
            ElMessage({message:"发布失败"+response.data.message,type:"error"})
          }
        }).catch(error => {
          ElMessage({ message: error, type: "error" })
        })
    },
    resetForm() {
      this.name = "";
      this.intro = "";
      this.price = "";
      this.fileList = [];
    },
    uploadFile(file) {
      console.log(file);
      // 这里是你的上传前的验证逻辑，可以检查文件类型和大小等
      const reader = new FileReader();
      reader.readAsDataURL(file.file);
      reader.onload = () => {
        this.base64 = reader.result;
      }
    },
    handleUpload(file) {
      const isLt10M = file.size / 1024 / 1024 < 10; // 判断文件是否小于2MB
      if (!isLt10M) {
        // 如果文件大于2MB
        ElMessage({ message: '上传图片大小不能超过 10MB', type: "error" }); // 弹出错误信息
        return false; // 停止上传
      }
      const isImage = file.type.startsWith("image/"); // 判断文件是否是图片类型
      if (!isImage) {
        // 如果文件不是图片类型
        ElMessage({ message: '只能上传图片格式', type: "error" });// 弹出错误信息
        return false; // 停止上传
      }
      return true;
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handleExceed() {
      ElMessage({ message: "只允许上传一张图片", type: "error" })
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
