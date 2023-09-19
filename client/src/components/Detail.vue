<template>
  <el-container>
    <el-aside width="50%">
      <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
        alt="Book Image" style="width: 100%; height: auto;">
    </el-aside>
    <el-main>
      <div>
        <div >
          <h3 style="font-size:25px">{{ book.title }}</h3>
        </div>
        <div class="rounded-box">
          <p>{{ book.description }}</p>
          <h3 style="font-size:25px;color: rgb(0, 0, 0);">￥{{ book.price }}</h3>
          <h3>评价:<el-rate v-model="solder.rate" disabled="true" /></h3>
          <h3>地址:{{ solder.address }}</h3>
        </div>
        <el-button type="primary" @click="buyBook">确认购买</el-button>
          <el-button type="success" @click="addToCart">加入购物车</el-button>
      </div>
    </el-main>
  </el-container>
</template>
  
<script>
export default {
  name: "DetailView",
  data() {
    return {
      book: {
        title: '计算机组成原理',
        description: '书的介绍红红火火恍恍惚惚或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或',
        price: '30',
        authorReview: 5
      },
      solder: {
        rate: 4,
        address: "学院路大运村",
      }
    }
  },
  methods: {
    buyBook() {
      // 购买书籍的逻辑
    },
    addToCart() {
      // 将书籍添加到购物车的逻辑
    }
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
  background-color: #fafafa;
  /* 灰色背景 */
  border-radius: 10px;
  margin-top:50px;
  margin-bottom: 50px;
  /* 圆角 */
  padding: 20px;
  /* 内边距 */
}</style>
  