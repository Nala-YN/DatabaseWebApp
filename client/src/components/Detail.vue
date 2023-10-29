<template>
  <el-container>
    <el-aside width="50%">
      <el-image :src="book.image" alt="Book Image" style="width: 100%; height: auto;"></el-image>
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
          <h3 style="font-size:25px;color: rgb(0, 0, 0);">¥{{ book.price.toFixed(2) }}</h3>
          <h3>卖家昵称:{{ seller.name }}</h3>
          <h3>卖家所在校区:{{ seller.campus }}</h3>
          <h3>卖家详细地址:{{ seller.address }}</h3>
          <h3>卖家联系电话:{{ seller.phoneNum }}</h3>
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
      comments: [
        {
          content: "这个网站很棒，我很喜欢,非常有用的信息，谢谢分享,非常有用的信息，谢谢分享，非常有用的信息，谢谢分享，非常有用的信息，谢谢分享",
          name: "小明",
          date: "2023-10-28",
        },
        {
          content: "非常有用的信息，谢谢分享",
          name: "小红",
          date: "2023-10-27",
        },
        {
          content: "我觉得这个网站有点乱，不太好用",
          name: "小李",
          date: "2023-10-26",
        },
        {
          content: "这个网站的设计很美观，很符合我的审美",
          name: "小花",
          date: "2023-10-25",
        },
      ],
      book: {
        id: 1,
        name: 'Vue.js实战',
        intro: '本书从Vue.js的基础知识开始，逐步介绍了Vue.js的核心概念和高级特性，如组件、过渡、路由、状态管理等，最后通过一个完整的电商项目实战，让读者掌握Vue.js的开发流程和方法。',
        image: 'https://img3m0.ddimg.cn/16/19/27978910-1_l_3.jpg',
        price: 69.00
      },
      seller: {
        name: "faqfaq",
        address: "学院路大运村",
        campus:"校区",
        phoneNum:"1355555",
      }
    }
  },
  mounted() {
    console.log(this.id);
    this.$http.post("/api/getdetail",{
      book_id:this.book.id
    }).then(response=>{
      this.seller=response.data.seller
      this.book=response.data.book
      this.comments=response.data.comments
    }).catch(error=>{
      ElMessage({ message: error, type: "error" })
    })
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
  