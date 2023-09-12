<template>
  <div>
    <el-container style="height: 95vh">
      <el-aside width="68px" class="aside">
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
      </el-aside>
      <el-container>
        <el-header class="header">
          <div class="left">
            <div v-if="mainContent === 'home'"><h3 class="h3">首页</h3></div>
            <div v-if="mainContent === 'cart'"><h3 class="h3">购物车</h3></div>
            <div v-if="mainContent === 'bought'"><h3 class="h3">我已购买</h3></div>
            <div v-if="mainContent === 'userInfo'"><h3 class="h3">用户信息</h3></div>
            <div v-if="mainContent === 'shopping'"><h3 class="h3">购买</h3></div>
            <div v-if="mainContent === 'addselling'"><h3 class="h3">添加出售</h3></div>
            <div v-if="mainContent === 'selling'"><h3 class="h3">我已出售</h3></div>
          </div>
          <div class="right">
            <h3 class="h3">你好，</h3>
            <el-button size="large" icon="UserFilled" @click="gotoUserPage" circle=true plain=true>
            </el-button>
          </div>
        </el-header>
        <el-main>
          <div v-if="mainContent === 'home'">
            <mainPage @update-content="mainContent = $event"></mainPage>
          </div>
          <div v-if="mainContent === 'cart'">这是购物车的内容</div>
          <div v-if="mainContent === 'bought'">这是已购买的内容</div>
          <div v-if="mainContent === 'userInfo'">这是用户界面</div>
          <div v-if="mainContent === 'shopping'">这是购买界面</div>
          <div v-if="mainContent === 'addselling'"><h3 class="h3">添加出售</h3></div>
          <div v-if="mainContent === 'selling'">我已出售</div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
<script>
import mainPage from '@/components/mainPage.vue'
export default {
  name: "MainView",
  data() {
    return {
      mainContent: 'home',
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
    seeSelling(){
      this.mainContent='selling';
    }
  },
  components: { mainPage }
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
.right{
  display:flex;
  align-items: center;
}
.h3{
  color: rgb(69, 69, 69);
  font-size:22px;
}
.icon {
  padding-right: 10px;
  /* 可以根据需要调整 */
}</style>