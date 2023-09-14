<template>
  <el-container direction="vertical">
    <transition-group name="list" tag="div">
      <div v-for="(book, index) in books" :key="book.name" class="list-item">
        <el-card>
          <div class="card">
            <el-image :src="book.image" class="image"></el-image>
            <div>{{ book.name }}</div>
            <el-input
              v-model="book.intro"
              type="textarea"
              :rows="2"
              placeholder="请输入内容"
              readonly
              style="width: 300px;"
            >
            </el-input>
            <div>{{ book.price }}</div>
            <el-button type="warning" round class="button" size="large" @click="addToCart(index)">加入购物车</el-button>
            <el-button type="danger" round class="button" size="large" @click="buyBook(index)">确认购买</el-button>
          </div>
        </el-card>
        <el-divider></el-divider>
      </div>
    </transition-group>
  </el-container>
</template>

<script>
export default {
  name: 'ShoppingView',
  data() {
    return {
      books: [
        {
          name: 'Vue.js实战',
          intro: '本书从Vue.js的基础知识开始，逐步介绍了Vue.js的核心概念和高级特性，如组件、过渡、路由、状态管理等，最后通过一个完整的电商项目实战，让读者掌握Vue.js的开发流程和方法。',
          image: 'https://img3m0.ddimg.cn/16/19/27978910-1_l_3.jpg',
          price: '69.00'
        },
        {
          name: 'JavaScript高级程序设计（第4版）',
          intro: '本书是JavaScript领域的经典著作，全面讲解了JavaScript语言的核心概念和实践技巧。本书不仅涵盖了ECMAScript 2019（ES10）的最新内容，还介绍了如何在现代Web浏览器中使用JavaScript开发客户端应用程序。',
          image: 'https://img3m0.ddimg.cn/72/6/28402910-1_l_3.jpg',
          price: '99.00'
        },
        {
          name: 'CSS揭秘',
          intro: '本书深入浅出地介绍了CSS的各种新特性和技巧，如渐变、遮罩、滤镜、字体、动画等，让读者能够轻松实现各种炫酷的效果。本书适合所有对CSS感兴趣的读者，无论是初学者还是高手。',
          image: 'https://img3m0.ddimg.cn/8/21/25203310-1_l_3.jpg',
          price: '79.00'
        }
      ]
    }
  },
  methods: {
    buyBook(index) {
      // TODO: 实现购买书籍的逻辑
      alert('你已成功购买《' + this.books[index].name + '》');
    },
    addToCart(index) {
      // TODO: 实现加入购物车的逻辑
      alert('你已成功将《' + this.books[index].name + '》加入购物车');
    }
  }
}
</script>

<style scoped>
.text.item {
  margin-bottom: 20px;
}

.card {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100px;
  border-radius: 100px;
}

.image {
  margin-left: 20px;
  /* 距离左边的距离 */
  margin-right: 50px;
}
.list-item {
  transition: all 0.5s ease;
}

.list-leave-active {
  position: absolute;
}

.list-leave-to {
  transform: translateX(100%);
  opacity: 0;
}
.button {
  margin-left: 50px;
  margin-right: 20px;
}
</style>
