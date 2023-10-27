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
import axios from 'axios'
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
      activeTab:"all",
      posts: [
        {
          id: 1,
          title: "哈哈哈",
          username: "faqfaq",
          content: "This is the first card.",
          year: 2002,
          month: 9,
          day: 6
        },
        {
          id: 2,
          title: "Card 2",
          username: "faqfaq",
          content: "This is the second card.",
          year: 2002,
          month: 9,
          day: 6
        },
        {
          id: 3,
          title: "Card 3",
          username: "faqfaq",
          content: "This is the third card.",
          year: 2002,
          month: 9,
          day: 6
        },
        {
          id: 4,
          title: "Card 4",
          username: "faqfaq",
          content: "This is the fourth card.",
          year: 2002,
          month: 9,
          day: 6
        },
        {
          id: 5,
          title: "Card 5",
          username: "faqfaq",
          content: "This is the fifth card.",
          year: 2002,
          month: 9,
          day: 6
        },
      ],
      myposts: []
    }
  },
  mounted() {
    axios.get('/api/getuserpost').then(res => {
      this.myposts = res.data.list
    })
    /*     this.$http.post('/api/getposts').then(response => {
    
        }).catch(console.log("JI")) */
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

p {
  text-align: center;
}

.floating-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 9999;
}
</style>

