<template>
  <div v-if="isDetail === true" style="position: relative;">
    <el-button @click="closeDetail()" icon="Close" circle size="large" type="danger"
      style="position: absolute; top: 0; right: 0;"></el-button>
    <detail :id="detailId">
    </detail>
  </div>
  <div v-show="isDetail === false" style="height: 100vh;" v-loading="loading">
    <div v-if="this.books.length === 0 && this.loading === false"
      style="display: flex;justify-content: center;align-items: center;">
      <h3 style=" color: rgb(126, 126, 126);padding-bottom: 65vh;font-size: 22px;">购物车里还没有书籍哦</h3>
    </div>
    <el-container direction="vertical">
      <transition-group name="list" tag="div">
        <div v-for="(book, index) in books" :key="book.name" class="list-item">
          <el-card @click="gotoDetail(index)" style="cursor: pointer;" class="elcard">
              <el-row>
                <el-col :span="4" class="centered-col" style="height:120px ;">
                  <el-image :fit='cover' :src="book.image" class="image"></el-image>
                </el-col>
                <el-col :span="4" class="centered-col">
                  {{ book.name }}
                </el-col>
                <el-col :span="7" class="centered-col">
                  {{ book.intro }}
                </el-col>
                <el-col :span="3" class="centered-col">
                  ¥{{ toFixed2(book.price) }}
                </el-col>
                <el-col :span="3" class="centered-col">
                  <el-button type="primary" class="button" size="large" @click.stop="buyBook(index)">确认购买</el-button>
                </el-col>
                <el-col :span="3" class="centered-col">
                  <el-button type="success" class="button" size="large" @click.stop="rmFromCart(index)">移出购物车</el-button>
                </el-col>
              </el-row>
          </el-card>
          <el-divider></el-divider>
        </div>
      </transition-group>
    </el-container>
    <el-header>
      <div style="display: flex;justify-content:space-between;">
        <h3>已选书籍总价¥{{ sumPrice }}</h3>
        <div>
          <el-button type="warning" class="button" size="large" @click="buyAll()">结算</el-button>
        </div>
      </div>
    </el-header>
  </div>
</template>

<script>
import { ElHeader } from 'element-plus';
import { ElMessage } from 'element-plus';
import detail from './Detail.vue'
export default {
  name: 'CartView',
  data() {
    return {
      isDetail: false,
      detailId: 1,
      books: [],
      loading: true,
    };
  },
  computed: {
    sumPrice() {
      var sum = 0.0;
      this.books.forEach(element => {
        sum = sum + parseFloat(element.price)
      });
      return sum.toFixed(2);
    }
  },
  methods: {
    toFixed2(str) {
      let num = Number(str);
      return isNaN(num) ? str : num.toFixed(2);
    },
    buyAll() {
      this.loading = true
      if (this.books.length === 0) {
        ElMessage({ message: "您的购物车里还没有书籍", type: "error" })
        this.loading = false
        return
      }
      this.$http.post('/api/buyAll', {
        user_id: this.$store.getters.status.userid,
      }).then(response => {
        if (response.data.success === false) {
          ElMessage({ message: "购买失败，余额不足请充值", type: "error" })
        }
        else {
          ElMessage({ message: "购买成功，请您与售书者联系", type: "success" })
          this.books = []
        }
        this.loading = false
      }
      ).catch(error => {
        ElMessage({ message: error, type: "error" })
        this.loading = false
        return;
      })
    },
    closeDetail() {
      this.isDetail = false;
    },
    buyBook(index) {
      this.$http.post('/api/buybook', {
        user_id: this.$store.getters.status.userid,
        item_id: this.books[index].id,
      }).then(response => {
        if (response.data.success === false) {
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
    rmFromCart(index) {
      this.$http.post('/api/rmFromCart', {
        user_id: this.$store.getters.status.userid,
        item_id: this.books[index].id
      }).then().catch(error => {
        ElMessage({ message: error, type: "error" })
      })
    },
    gotoDetail(index) {
      this.isDetail = true;
      this.detailId = this.books[index].id;
    }
  },
  mounted() {
    this.$http.post("/api/getcart", {
      user_id: this.$store.getters.status.userid,
    }).then(response => {
      this.books = response.data.books
    }).catch(error => {
      ElMessage({ message: error, type: "error" })
    })
    setTimeout(() => {
      this.loading = false
    }, 1000)
  },
  components: { detail }
}
</script>

<style scoped>


.image {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  width: auto;
}

.list-item {
  transition: all 0.5s ease;
}
.button {
  margin-left: 50px;
  margin-right: 20px;
}

.centered-col {
  display: flex;
  justify-content: center;
  align-items: center;
  word-break: break-all;
}

.elcard:hover {
  border: 2px solid rgb(144, 205, 255);
}</style>
