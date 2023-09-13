<template>
  <el-container direction="vertical">
    <transition-group name="list" tag="div">
      <div v-for="(item, index) in items" :key="item.id" class="list-item">
        <el-card class="card">
          <el-row style="  display: flex;
  align-items: center;height: 160px;">
            <el-col :span="5" class="centered-col">
              <el-image :src="item.image" class="image"></el-image>
            </el-col>
            <el-col :span="4" class="centered-col">
              <h3>{{ item.description }}</h3>
            </el-col>
            <el-col :span="2" class="centered-col">
              <h3>¥{{ item.prize }}</h3>
            </el-col>
            <el-col :span="4" class="centered-col">
              <h3>联系方式:<br>{{ item.number }}</h3>
            </el-col>
            <el-col :span="6" class="centered-col">
              <h3>备注:</h3>
              <div>{{ item.description }}</div>
            </el-col>
            <el-col :span="3" class="centered-col">
              <h3>{{ item.state }}</h3>
            </el-col>
          </el-row>
        </el-card>
          <div style="display: flex; justify-content: flex-end; margin-top: 20px;"> 
            <el-popconfirm confirm-button-text="确认" cancel-button-text="取消" title="确认收货？" @confirm="removeItem(index)">
    <template #reference>
      <el-button type="primary" round class="button" size="large" >确认收货</el-button>
    </template>
  </el-popconfirm>
            <el-button type="info" round class="button" size="large" @click="removeItem(index)">修改备注</el-button>
          </div>

            <el-divider></el-divider>
        </div>
    </transition-group>
  </el-container>
</template>
  
<script>
import axios from 'axios';
import Mock from 'mockjs';
Mock.mock('/api/data', {
  'list|10-20': [{
    'id|+1': 1,
    'title': '@ctitle(10, 20)',
    'image': '@image(\'200x100\', \'#50B347\', \'Hello\')',
    'datetime': '@datetime()',
    'author': '@cname()',
    'number': '@integer(11111111111,11111111112)',
    'prize': '@integer(10,20)',
    'description': '@ctitle(4, 20)',
    'state': '@integer(1,4)'
  }]
})
export default {
  name: "cartView",

  data() {
    return {
      items: [],
    }
  },
  methods: {
    removeItem(index) {
      this.items.splice(index, 1);
    }
  },
  mounted() {
    axios.get('/api/data').then(res => {
      this.items = res.data.list
    }).catch(console.log("JI"))
    console.log('get')
    console.log(this.items)
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