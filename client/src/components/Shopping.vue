<template>
  <div v-if="isDetail===true" style="position: relative;">
    <el-button @click="closeDetail()" icon="Close" circle size="large" type="danger" style="position: absolute; top: 0; right: 0;"></el-button>
    <detail :id="detailId">
    </detail>
  </div>
  <div v-show="isDetail === false">
    <el-container direction="vertical">
      <el-header style="height:10vh;display: flex;justify-content: center;padding-top: 10px;">
        <div style="height:10vh ;width: 100vh;">
          <el-input v-model="input" placeholder="请输入书名" style="font-size: 20px;padding-right: 20px;" />
        </div>
        <el-button type="primary" icon="Search" circle size='large' @click="search()"></el-button>
      </el-header>
      <transition-group name="list" tag="div">
        <div v-for="(book, index) in books" :key="book.name" class="list-item">
          <el-card @click="gotoDetail(index)" style="cursor: pointer;" class="elcard">
            <div class="card">
              <el-image :src="book.image" class="image"></el-image>
              <el-row>
                <el-col :span="2">
                  {{ book.name }}
                </el-col>
                <el-col :span="1">
                </el-col>
                <el-col :span="16">
                  {{ book.intro }}
                </el-col>
                <el-col :span="1">
                </el-col>
                <el-col :span="2">
                  ¥{{ toFixed2(book.price) }}
                </el-col>
              </el-row>
              <el-button type="success" round class="button" size="large" @click.stop="addToCart(index)">加入购物车</el-button>
              <el-button type="primary" round class="button" size="large" @click.stop="buyBook(index)">确认购买</el-button>
            </div>
          </el-card>
          <el-divider></el-divider>
        </div>
      </transition-group>
    </el-container>
  </div>
</template>

<script>
import { ElHeader } from 'element-plus';
import { ElMessage } from 'element-plus';
import detail from './Detail.vue'
export default {
  name: 'ShoppingView',
  data() {
    return {
      isDetail: false,
      detailId: 1,
      books: [
        {
          id: 1,
          name: 'Vue.js实战',
          intro: '本书从Vue.js的基础知识开始，逐步介绍了Vue.js的核心概念和高级特性，如组件、过渡、路由、状态管理等，最后通过一个完整的电商项目实战，让读者掌握Vue.js的开发流程和方法。',
          image: 'https://img3m0.ddimg.cn/16/19/27978910-1_l_3.jpg',
          price: 69.00
        },
        { id:2,
          name: 'JavaScript高级程序设计（第4版）',
          intro: '本书是JavaScript领域的经典著作，全面讲解了JavaScript语言的核心概念和实践技巧。本书不仅涵盖了ECMAScript 2019（ES10）的最新内容，还介绍了如何在现代Web浏览器中使用JavaScript开发客户端应用程序。',
          image: 'https://img3m0.ddimg.cn/72/6/28402910-1_l_3.jpg',
          price: 99.00
        },
        {
          id:3,
          name: 'CSS揭秘',
          intro: '本书深入浅出地介绍了CSS的各种新特性和技巧，如渐变、遮罩、滤镜、字体、动画等，让读者能够轻松实现各种炫酷的效果。本书适合所有对CSS感兴趣的读者，无论是初学者还是高手。',
          image: 'https://img3m0.ddimg.cn/8/21/25203310-1_l_3.jpg',
          price: 79.00
        }
      ],
      input: "",
    };
  },
  methods: {
    toFixed2(str){
      let num = Number(str);
      return isNaN(num) ? str : num.toFixed(2);
    },
    search(){
      this.$http.post("/api/searchbooks",{
        user_id: this.$store.getters.status.userid,
        content:this.input
      }).then(response=>{
        this.books=response.data.books
      }).catch(error=>{
        ElMessage({ message: error, type: "error" })
      })
    },
    closeDetail(){
      this.isDetail=false;
    },
    buyBook(index) {
      this.$http.post('/api/buybook', {
        user_id: this.$store.getters.status.userid,
        item_id: this.books[index].id,
      }).then(response=>{
        if(response.data.success===false){
          ElMessage({ message: "购买失败，余额不足请充值", type: "error" })
        }
      }
      ).catch(error => {
        ElMessage({ message: error, type: "error" })
        return;
      })
      ElMessage({ message: "购买成功，请您与售书者联系", type: "success" })
      this.books.splice(index, 1)
    },
    addToCart(index) {
      this.$http.post('/api/addtocart', {
        user_id: this.$store.getters.status.userid,
        item_id: this.books[index].id
      }).then(response => {
        if (response.data.success) {
          ElMessage({ message: "添加成功", type: "success" })
        }
        else {
          ElMessage({ message: "添加失败，购物车中已有该书籍", type: "error" })
        }
      }).catch(error => {
        ElMessage({ message: error, type: "error" })
      })
    },
    gotoDetail(index) {
      this.isDetail=true;
      this.detailId =this.books[index].id;
    }
  },
  mounted(){
    this.$http.post("/api/getbooks",{
      user_id: this.$store.getters.status.userid,
    }).then(response=>{
      this.books=response.data.books
    }).catch(error=>{
      ElMessage({ message: error, type: "error" })
    })
  },
  components: { ElHeader, detail }
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

.elcard:hover {
  border: 2px solid rgb(144, 205, 255);
}
</style>
