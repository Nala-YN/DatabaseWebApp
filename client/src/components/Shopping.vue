<template>
  <div v-if="isDetail===true" style="position: relative;">
    <el-button @click="closeDetail()" icon="Close" circle size="large" type="danger" style="position: absolute; top: 0; right: 0;"></el-button>
    <detail :id="detailId">
    </detail>
  </div>
  <div v-show="isDetail === false">
    <el-container direction="vertical" v-loading="loading">
      <el-header style="height:10vh;display: flex;justify-content: center;padding-top: 10px;">
        <div style="height:10vh ;width: 100vh;">
          <el-input v-model="input" placeholder="请输入书名" style="font-size: 20px;padding-right: 20px;" />
        </div>
        <el-button type="primary" icon="Search" circle size='large' @click="search()"></el-button>
      </el-header>
      <transition-group name="list" tag="div">
        <div v-for="(book, index) in books" :key="book.name" class="list-item">
          <el-card @click="gotoDetail(index)" style="cursor: pointer;" class="elcard">
            <el-row >
            <el-col :span="4" class="centered-col" style="height:120px ;">
                <el-image :fit='scale-down' :src="book.image" class="image" ></el-image>
            </el-col>
            <el-col :span="4" class="centered-col">
              <h3>{{ book.name }}</h3>
            </el-col>
            <el-col :span="7" class="centered-col" >
              {{ book.intro }}
            </el-col>
            <el-col :span="3" class="centered-col">
              <h3>¥{{ toFixed2(book.price) }}</h3>
            </el-col>
            <el-col :span="3" class="centered-col">
              <el-button type="success" round class="button" size="large" @click.stop="addToCart(index)">加入购物车</el-button>
            </el-col>
            <el-col :span="3" class="centered-col">
              <el-button type="primary" round class="button" size="large" @click.stop="buyBook(index)">确认购买</el-button>
            </el-col>
          </el-row>
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
      books: [],
      input: "",
      loading:true,
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
    this.loading=false
  },
  components: { ElHeader, detail }
}
</script>

<style scoped>
.text.item {
  margin-bottom: 20px;
}

.card {
  height: 100px;
  border-radius: 100px;
}

.image {
  display: flex; align-items: center; justify-content: center;
  height: 100%;
  width: auto;
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
.centered-col {
  display: flex;
  justify-content: center;
  align-items: center;
  word-break: break-all;
}
.button {
  margin-left: 50px;
  margin-right: 20px;
}

.elcard:hover {
  border: 2px solid rgb(144, 205, 255);
}
</style>
