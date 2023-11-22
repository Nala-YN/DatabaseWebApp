<template>
  <el-tabs v-model="activeTab">
    <el-tab-pane label="所有帖子" name="all">
      <div class="container">
        <el-card v-for="item in posts" :key="item.id" class="card">
          <h3>{{ item.title }}</h3>
          <p>{{ item.content }}</p>
          <div style="display: flex;flex-direction: column;align-items: flex-end;">
            <div>BY {{ item.username }}</div>
            {{ item.year }}-{{ item.month }}-{{ item.day }}
          </div>
        </el-card>
      </div>
    </el-tab-pane>
    <el-tab-pane label="我发布的帖子" name="mine">
      <div class="container">
        <el-card v-for="(item, index) in myposts" :key="item.id" class="card">
          <h3>{{ item.title }}</h3>
          <p>{{ item.content }}</p>
          <div style="display: flex;flex-direction: column;align-items: flex-start;">
            {{ item.year }}-{{ item.month }}-{{ item.day }}
          </div>
          <div style="display: flex;flex-direction: column;align-items: flex-end;">
            <el-button type="danger" class="button" size="large" @click="deletePost(index)">撤回帖子</el-button>
          </div>
        </el-card>
      </div>
    </el-tab-pane>
  </el-tabs>
</template>


<script>
import Mock from 'mockjs';
import { ElMessage } from 'element-plus';
Mock.mock('/api/getuserpost', {
  'list|10-20': [{
    'content': '@ctitle(30, 100)',
    'title': '@ctitle(8,14)',
  }]
})
export default {
  name: "PostView",
  data() {
    return {
      activeTab: "all",
      posts: [],
      myposts: []
    }
  },
  methods: {
    deletePost(index) {
      this.$http.post("/api/deletepost",{
        post_id:this.myposts[index].id,
      }).then(response=>{
        if(response.data.success){
          ElMessage({message:"撤回成功",type:"success"})
          this.myposts.splice(index, 1)
        }
        else{
          ElMessage({message:"撤回失败",type:"error"})
        }
      }).catch(error=>{
        ElMessage({message:error,type:"error"})
      })
    },
  },
  mounted() {
    this.$http.post('/api/getuserpost', {
      user_id: this.$store.getters.status.userid,
    }).then(response => {
      this.myposts = response.data.userposts
    }).catch(error => {
      ElMessage({ message: error, type: "error" })
    })
    this.$http.post('/api/getallpost')
      .then(response=>{
        this.posts=response.data.posts
      }).
      catch(error=>{
        ElMessage({message:error,type:"error"})
      })
  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-wrap: wrap;
}

.card {
  width: 55vh;
  margin: 10px;
}

h3 {
  font-size: 18px;
  text-align: center;
}



.floating-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 9999;
}
</style>

