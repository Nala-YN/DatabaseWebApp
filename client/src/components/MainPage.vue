<template>
    <div class="button-container">
        <el-button class="el-button" round @click="gotoShopping">
            <div><el-icon size="60px"><ShoppingCart /></el-icon>
            <br>
            <h3 style="font-size: 20px ;">我要购买</h3>
            </div>
        </el-button>
        <el-button class="el-button" round @click="gotoSelling">
            <div><el-icon size="60px"><Coin /></el-icon>
            <br>
            <h3 style="font-size: 20px ;">我要出售</h3>
            </div>
        </el-button>
    </div>
</template>
<script>
export default {
    name: "mainPage",
    methods: {
  updateContent: function(newValue) {
    this.$emit('update-content', newValue);
  },
  gotoSelling(){
    this.updateContent("addselling");
  },
  gotoShopping(){
    this.updateContent("shopping");
  },
}
}
</script>
<style scoped>
.el-button {
    box-shadow: var(--el-box-shadow);
    width: 40vh;
    height: 40vh;
}

.button-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80vh;
    /* 确保容器占满其父元素 */
}
</style>
