<template>
  <div v-loading="loading">
    <el-container>
    <el-aside width="50%">
      <el-image :src="book.image" alt="Book Image" style="width: 100%; height: auto;" ></el-image>
    </el-aside>
    <el-main>
      <div>
        <div>
          <h3 style="font-size:25px">{{ book.name }}</h3>
        </div>
        <el-divider></el-divider>
        <div class="rounded-box">
          <p style="font-weight: bold;color: rgb(103, 103, 103);">{{ book.intro }}</p>
        </div>
        <el-divider></el-divider>
        <div class="rounded-box">
          <h3 style="font-size:25px;color: rgb(0, 0, 0);">¥{{ toFixed2(book.price) }}</h3>
          <h3>卖家昵称:{{ seller.name }}</h3>
          <h3>卖家所在校区:{{ seller.campus }}</h3>
          <h3>卖家详细地址:{{ seller.address }}</h3>
          <h3>卖家联系电话:{{ seller.phonenum }}</h3>
        </div>
      </div>
    </el-main>
  </el-container>
  <el-divider></el-divider>
  <div style="display: flex;flex-direction: column;align-items: center;">
    <h3 style="font-size:20px;color: rgb(83, 83, 83);">评论</h3>
    <div id="app" style="flex-wrap: wrap;font-size: 10px;">
    <el-table
      :data="comments"
      style="width: 100%;font-size: 15px;"
      :row-class-name="tableRowClassName"
      stripe
    >
      <el-table-column prop="content" label="评论内容" width="1000px"></el-table-column>
      <el-table-column prop="name" label="评论者昵称" width="200px"></el-table-column>
      <el-table-column prop="date" label="评论日期" width="200px"></el-table-column>
    </el-table>
  </div>
  </div>
  </div>
</template>
  
<script>
import { ElMessage } from 'element-plus';
export default {
  name: "DetailView",
  props: {
    id: Number
  },
  data() {
    return {
      comments: [],
      book: {},
      seller: {
        name: "",
        address: "",
        campus:"",
        phoneNum:"",
      },
      loading:true
    }
  },
  methods:{
    toFixed2(str){
      let num = Number(str);
      return isNaN(num) ? str : num.toFixed(2);
    },
  },
  mounted() {
    this.$http.post("/api/getdetail",{
      book_id:this.id
    }).then(response=>{
      this.seller=response.data.seller
      this.book=response.data.book
      this.comments=response.data.comments
    }).catch(error=>{
      ElMessage({ message: error, type: "error" })
    })
    this.loading=false
  }
}
</script>
  
<style scoped>
.el-container {
  height: 100vh;
}

.el-aside {
  display: flex;
  align-items: center;
  justify-content: center;
}

.el-main {
  display: flex;
  flex-direction: column;
  padding-left: 100px;
}

.rounded-box {
  background-color: #f5f5f5;
  /* 灰色背景 */
  border-radius: 10px;
  margin-top: 25px;
  margin-bottom: 25px;
  /* 圆角 */
  padding: 20px;
  /* 内边距 */
}
</style>
  