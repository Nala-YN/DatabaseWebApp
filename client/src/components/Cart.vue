<template>
  <el-container direction="vertical">
    <transition-group name="list" tag="div">
      <div v-for="(item, index) in items" :key="item.id" class="list-item">
        <el-card>
          <div class="card">
            <el-image :src="item.image" class="image"></el-image>
            <div>{{ item.description }}</div>
            <div>{{ item.prize }}</div>
            <el-button type="primary" round class="button" size="large" @click="removeItem(index)">确认购买</el-button>
            <el-button type="danger" round class="button" size="large" @click="removeItem(index)">取消购买</el-button>
          </div>
        </el-card>
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
    'prize':'@integer(30,30)',
    'description': '@ctitle(30, 100)'
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
}</style> 
