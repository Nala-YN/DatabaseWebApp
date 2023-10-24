<template>
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
</template>

<script>
export default {
  name:"PostView",
  data() {
    return {
      posts: [
        {
          id: 1,
          title: "哈哈哈",
          username:"faqfaq",
          content: "This is the first card.",
          year:2002,
          month:9,
          day:6
        },
        {
          id: 2,
          title: "Card 2",
          username:"faqfaq",
          content: "This is the second card.",
          year:2002,
          month:9,
          day:6
        },
        {
          id: 3,
          title: "Card 3",
          username:"faqfaq",
          content: "This is the third card.",
          year:2002,
          month:9,
          day:6
        },
        {
          id: 4,
          title: "Card 4",
          username:"faqfaq",
          content: "This is the fourth card.",
          year:2002,
          month:9,
          day:6
        },
        {
          id: 5,
          title: "Card 5",
          username:"faqfaq",
          content: "This is the fifth card.",
          year:2002,
          month:9,
          day:6
        },
      ]
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-wrap: wrap;
}

.card {
  width: 62vh;
  margin: 10px;
}

h3 {
  font-size: 18px;
  text-align: center;
}

.image {
  width: 200px;
  height: 200px;
}

p {
  text-align: center;
}
</style>

