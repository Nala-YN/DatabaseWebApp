<template>
  <div>
    <el-container style="height: 95vh">
      <el-menu default-active="2" mode="vertical" :collapse="isCollapse">
        <el-sub-menu index="1">
          <template #title>
            <el-icon>
              <Menu />
            </el-icon>
          </template>
          <el-menu-item-group>
            <el-menu-item index="1-1" @click='gotoMainPage'>
              <h3 class="h3" style="font-size: 18px">首页</h3>
            </el-menu-item>
            <el-menu-item index="1-2" @click='gotoMessage'>
              <h3 class="h3" style="font-size: 18px">我的消息</h3>
            </el-menu-item>
            <el-menu-item index="1-3" @click='gotoCart'>
              <h3 class="h3" style="font-size: 18px">购物车</h3>
            </el-menu-item>
            <el-menu-item index="1-4" @click='gotoBought'>
              <h3 class="h3" style="font-size: 18px">我已购买</h3>
            </el-menu-item>
            <el-menu-item index="1-5" @click='gotoBoughtHistory'>
              <h3 class="h3" style="font-size: 18px">历史购买记录</h3>
            </el-menu-item>
            <el-menu-item index="1-6" @click='gotoSoldHistory'>
              <h3 class="h3" style="font-size: 18px">我已出售</h3>
            </el-menu-item>
            <el-menu-item index="1-7" @click='gotoPost'>
              <h3 class="h3" style="font-size: 18px">查看求书贴</h3>
            </el-menu-item>
            <el-menu-item index="1-8" @click='gotoAddPost'>
              <h3 class="h3" style="font-size: 18px">添加帖子</h3>
            </el-menu-item>
          </el-menu-item-group>
        </el-sub-menu>
      </el-menu>
      <el-container>
        <el-header class="header">
          <div class="left">
            <div v-if="mainContent === 'mainPage'"><h3 class="h3">首页</h3></div>
            <div v-if="mainContent === 'message'"><h3 class="h3">我的消息</h3></div>
            <div v-if="mainContent === 'cart'"><h3 class="h3">购物车</h3></div>
            <div v-if="mainContent === 'bought'"><h3 class="h3">我已购买</h3></div>
            <div v-if="mainContent === 'boughtHistory'"><h3 class="h3">历史购买记录</h3></div>
            <div v-if="mainContent === 'addselling'"><h3 class="h3">添加出售</h3></div>
            <div v-if="mainContent === 'soldHistory'"><h3 class="h3">我已出售</h3></div>
            <div v-if="mainContent === 'post'"><h3 class="h3">求书帖</h3></div>
            <div v-if="mainContent === 'addpost'"><h3 class="h3">添加帖子</h3></div>
            <div v-if="mainContent === 'shopping'"><h3 class="h3">购买</h3></div>
            <div v-if="mainContent === 'detail'"><h3 class="h3">详细信息</h3></div>
            <div v-if="mainContent === 'userinfo'"><h3 class="h3">用户信息</h3></div>
          </div>
          <div class="right">
            <h3 class="h3" style="padding-right: 3vh;">你好，{{ username }}</h3>
            <!-- 把el-button放在el-dropdown的slot中 -->
            <el-dropdown trigger="click" placement="bottom-end" :hide-on-click=false @command="handleCommand">
              <el-button size="large" icon="UserFilled" :circle=true :plain=true></el-button>
              <!-- 添加一个el-dropdown-menu组件 -->
              <template #dropdown>
                <el-dropdown-menu>
                  <!-- 添加两个el-dropdown-item组件 -->
                  <el-dropdown-item command="user">个人信息</el-dropdown-item>
                  <el-dropdown-item command="logout">退出登录</el-dropdown-item>
                </el-dropdown-menu>
              </template>
            </el-dropdown>
          </div>
        </el-header>
        <el-main>
          <div v-if="mainContent === 'mainPage'"><mainPage @update-content="mainContent = $event"></mainPage></div>
          <div v-if="mainContent === 'cart'"><cart></cart></div>
          <div v-if="mainContent === 'bought'"><bought></bought></div>
          <div v-if="mainContent === 'message'"><message></message></div>
          <div v-if="mainContent === 'userinfo'"><userinfo></userinfo></div>
          <div v-if="mainContent === 'shopping'"><shopping></shopping></div>
          <div v-if="mainContent === 'addselling'"><addselling></addselling></div>
          <div v-if="mainContent === 'soldHistory'"><soldHistory></soldHistory></div>
          <div v-if="mainContent === 'boughtHistory'"><boughtHistory></boughtHistory></div>
          <div v-if="mainContent === 'detail'"><detail></detail></div>
          <div v-if="mainContent === 'post'"><post></post></div>
          <div v-if="mainContent === 'addpost'"><addpost></addpost></div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
<script>
import mainPage from '@/components/MainPage.vue'
import cart from '@/components/Cart.vue'
import bought from '@/components/Bought.vue'
import shopping from '@/components/Shopping.vue'
import detail from '@/components/Detail.vue'
import userinfo from '@/components/Userinfo.vue'
import boughtHistory from '@/components/BoughtHistory.vue'
import message from '@/components/Message.vue'
import router from '@/router'
import post from '@/components/Post.vue'
import addpost from '@/components/AddPost.vue'
import addselling from '@/components/AddSelling.vue'
import soldHistory from '@/components/SoldHistory'
export default {
  name: "MainView",
  data() {
    return {
      username: this.$store.getters.status.username,
      mainContent: 'message',
      isCollapse: true,
    };
  },
  methods: {
    gotoMainPage() {
      //this.$router.push('/home')
      this.mainContent = 'mainPage';
    },
    gotoCart() {
      //this.$router.push('/cart')
      this.mainContent = 'cart';
    },
    gotoMessage() {
      // this.$router.push('/bought')
      this.mainContent = 'message';
    },
    gotoBought() {
      this.mainContent = 'bought';
    },
    gotoBoughtHistory() {
      this.mainContent = 'boughtHistory';
    },
    gotoAddSelling() {
      this.mainContent = 'addselling';
    },
    gotoSoldHistory() {
      this.mainContent = 'soldHistory';
    },
    gotoPost() {
      this.mainContent = 'post';
    },
    gotoAddPost() {
      this.mainContent = 'addpost';
    },
    handleCommand(command) {
      // 根据不同的命令值执行不同的操作
      if (command === 'user') {
        // 显示用户信息
        this.mainContent = 'userinfo';
      } else if (command === 'logout') {
        // 退出登录
        localStorage.removeItem('loginData');
        this.$store.state.userInfo=null;
        router.push({
          path: '/login',
        })
      }
    }
  },
  components: { mainPage, cart, bought, shopping, detail, boughtHistory, userinfo, message,post,addpost,addselling,soldHistory}
}
</script>
<style scoped>
.main {
  background-color: var(--el-color-primary-light-3);
}

.header {
  border-bottom: solid #d6d6d6 0.5px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.right {
  display: flex;
  align-items: center;
}

.h3 {
  color: rgb(69, 69, 69);
  font-size: 22px;
}

.icon {
  padding-right: 10px;
  /* 可以根据需要调整 */
}
</style>