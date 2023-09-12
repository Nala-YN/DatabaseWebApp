<template>
    <div v-for="(item, index) in items" :key="index">
      <el-card>
        <div class="text item">
          {{ item.text }}
        </div>
        <el-image :src="item.image"></el-image>
      </el-card>
      <el-divider></el-divider>
    </div>
</template>
<script>

</script>
<style scoped>

</style>