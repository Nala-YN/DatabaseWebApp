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
              <el-menu-item index="1-1" @click='gotoHome'>
                <h3 class="h3" style="font-size: 18px">首页</h3>
              </el-menu-item>
              <el-menu-item index="1-2" @click='seeBought'>
                <h3 class="h3" style="font-size: 18px">我已购买</h3>
              </el-menu-item>
              <el-menu-item index="1-3" @click='gotoCart'>
                <h3 class="h3" style="font-size: 18px">购物车</h3>
              </el-menu-item>
              <el-menu-item index="1-4" @click='seeSelling'>
                <h3 class="h3" style="font-size: 18px">我已出售</h3>
              </el-menu-item>
            </el-menu-item-group>
          </el-sub-menu>
        </el-menu>
      <el-container>
        <el-header class="header">
          <div class="left">
            <div v-if="mainContent === 'mainPage'">
              <h3 class="h3">首页</h3>
            </div>
            <div v-if="mainContent === 'cart'">
              <h3 class="h3">购物车</h3>
            </div>
            <div v-if="mainContent === 'bought'">
              <h3 class="h3">我已购买</h3>
            </div>
            <div v-if="mainContent === 'userInfo'">
              <h3 class="h3">用户信息</h3>
            </div>
            <div v-if="mainContent === 'shopping'">
              <h3 class="h3">购买</h3>
            </div>
            <div v-if="mainContent === 'addselling'">
              <h3 class="h3">添加出售</h3>
            </div>
            <div v-if="mainContent === 'selling'">
              <h3 class="h3">我已出售</h3>
            </div>
            <div v-if="mainContent === 'userinfo'">
              <h3 class="h3">个人信息</h3>
            </div>
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
          <div v-if="mainContent === 'mainPage'">
            <mainPage @update-content="mainContent = $event"></mainPage>
          </div>
          <div v-if="mainContent === 'cart'">
            <cart></cart>
          </div>
          <div v-if="mainContent === 'bought'">
            <bought></bought>
          </div>
          <div v-if="mainContent === 'userInfo'">这是用户界面</div>
          <div v-if="mainContent === 'shopping'">
            <shopping></shopping>
          </div>
          <div v-if="mainContent === 'addselling'">
            <h3 class="h3">添加出售</h3>
          </div>
          <div v-if="mainContent === 'selling'">我已出售</div>
          <div v-if="mainContent === 'boughtHistory'">
            <boughtHistory></boughtHistory>
          </div>
          <div v-if="mainContent === 'detail'">
            <detail></detail>
          </div>
          <div v-if="mainContent === 'userinfo'">
            <userinfo></userinfo>
          </div>
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
import router from '@/router'
export default {
  name: "MainView",
  data() {
    return {
      username: this.$store.getters.status.username,
      mainContent: 'mainPage',
      isCollapse: true,
    };
  },
  methods: {
    gotoHome() {
      //this.$router.push('/home')
      this.mainContent = 'home';
    },
    gotoCart() {
      //this.$router.push('/cart')
      this.mainContent = 'cart';
    },
    seeBought() {
      // this.$router.push('/bought')
      this.mainContent = 'bought';
    },
    gotoUserPage() {
      this.mainContent = 'userInfo';
    },
    seeSelling() {
      this.mainContent = 'selling';
    },
    gotoShopping() {
      this.mainContent = 'shopping';
    },
    handleCommand(command) {
      // 根据不同的命令值执行不同的操作
      if (command === 'user') {
        // 显示用户信息
        this.mainContent='userinfo';
      } else if (command === 'logout') {
        // 退出登录
        localStorage.removeItem('loginData');
        this.$store.state.userInfo = {};
        router.push({
          path: '/login',
        })
      }
    }
  },
  components: { mainPage, cart, bought, shopping, detail, boughtHistory,userinfo }
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