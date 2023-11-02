<template>
  <div v-if="items.length === 0" style="display: flex;justify-content: center;align-items: center;">
    <h3 style=" color: rgb(126, 126, 126);font-size: 22px;">还没有历史购买的书籍哦</h3>
  </div>
  <el-container direction="vertical">
    <transition-group name="list" tag="div">
      <div v-for="(item) in items" :key="item.id" class="list-item">
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
              <h3>¥{{ item.prize.toFixed(2) }}</h3>
            </el-col>
            <el-col :span="3" class="centered-col">
              <h3>{{ item.sellerName }}</h3>
            </el-col>
            <el-col :span="4" class="centered-col">
              <h3>联系方式:<br>{{ item.phoneNum }}</h3>
            </el-col>
          </el-row>
        </el-card>
        <el-divider></el-divider>
      </div>
    </transition-group>
  </el-container>
</template>
  
<script>
import axios from 'axios';
import Mock from 'mockjs';
import { ElMessage } from "element-plus"
Mock.mock('/api/data', {
  'list|10-20': [{
    'id|+1': 1,
    'name': '@ctitle(10, 20)',
    'image': '@image(\'200x100\', \'#50B347\', \'Hello\')',
    'datetime': '@datetime()',
    'sellerName': '@cname()',
    'phoneNum': '@integer(11111111111,11111111112)',
    'prize': '@integer(10,20)',
    'intro': '@ctitle(4, 20)',
  }]
})
export default {
  name: "BoughtHistoryView",
  data() {
    return {
      items: [{ id: 1, name: "1111",prize:100.1000 }],
    }
  },
  mounted() {
    this.$http.post('/api/getboughtHistory', {
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