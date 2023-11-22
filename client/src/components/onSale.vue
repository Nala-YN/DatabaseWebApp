<template>
    <div v-if="items.length === 0" style="display: flex;justify-content: center;align-items: center;">
      <h3 style=" color: rgb(126, 126, 126);font-size: 22px;">您还没有发布在售书籍哦</h3>
    </div>
    <el-container direction="vertical">
      <transition-group name="list" tag="div">
        <div v-for="(item, index) in items" :key="item.id" class="list-item">
          <el-card class="card">
            <el-row style="  display: flex;align-items: center;height: 160px;">
              <el-col :span="4" class="centered-col">
                <el-image :src="item.image" class="image"></el-image>
              </el-col>
              <el-col :span="4" class="centered-col">
                <h3>{{ item.name }}</h3>
              </el-col>
              <el-col :span="5" class="centered-col">
                <h3>{{ item.intro }}</h3>
              </el-col>
              <el-col :span="3" class="centered-col">
                <h3>¥{{ toFixed2(item.price) }}</h3>
              </el-col>
            </el-row>
          </el-card>
          <div style="display: flex; justify-content: flex-end; margin-top: 20px;">
            <el-button type="warning" class="button" size="large" @click="show=true">撤回在售书籍</el-button>
            <el-dialog v-model="show" title="确认撤回吗" width="30%">
              <div style="display:flex;justify-content: end;padding-top: 10px;">
                <el-button type="primary" class="button" size=“large” @click="withdraw(index)">确认</el-button>
              </div>
            </el-dialog>
          </div>
          <el-divider></el-divider>
        </div>
      </transition-group>
    </el-container>
  </template>
    
  <script>
  import { ElMessage } from "element-plus"
  export default {
    name: "OnSaleView",
  
    data() {
      return {
        show: false,
        items: [],
      }
    },
    methods: {
      toFixed2(str) {
              let num = Number(str);
              return isNaN(num) ? str : num.toFixed(2);
          },
      withdraw(index) {
        this.$http.post("/api/withdrawOnsale", {
          item_id: this.items[index].id,
        }).then().catch(error => {
          ElMessage({ message: error, type: "error" })
        })
        this.show=false;
        ElMessage({ message: "撤回成功", type: "success" })
      }
    },
    mounted() {
      this.$http.post('/api/getOnsale', {
        user_id: this.$store.getters.status.userid,
      }).then(res => {
        this.items = res.data.items
      }).catch(error => {
        ElMessage({ message: error, type: "error" })
      })
    }
  }
  </script>
    
  <style scoped>
  .text.item {
    margin-bottom: 20px;
  }
  
  .centered-col {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .card {
    height: 200px;
    border-radius: 30px;
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