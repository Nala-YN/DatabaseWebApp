<template>
    <el-container direction="vertical" v-loading="this.loading">
        <div v-if="items.length === 0 && loading === false" style="display: flex;justify-content: center;align-items: center;">
            <h3 style=" color: rgb(126, 126, 126);font-size: 22px;">您还没有发布的在售书籍哦</h3>
        </div>
            <div v-for="(item, index) in items" :key="item.id" class="list-item">
                <el-card class="card">
                    <el-row style="  display: flex;align-items: center;height: 160px;">
                        <el-col :span="5" class="centered-col" style="height:160px ;">
                            <el-image  :src="item.image" class="image"></el-image>
                        </el-col>
                        <el-col :span="5" class="centered-col">
                            <h3>{{ item.name }}</h3>
                        </el-col>
                        <el-col :span="10" class="centered-col">
                            {{ item.intro }}
                        </el-col>
                        <el-col :span="4" class="centered-col">
                            <h3>¥{{ toFixed2(item.price) }}</h3>
                        </el-col>
                    </el-row>
                </el-card>
                <div style="display: flex; justify-content: flex-end; margin-top: 20px;">
                    <el-button type="warning" class="button" size="large" @click="withdraw(index)">撤回在售书籍</el-button>
                </div>
                <el-divider></el-divider>
            </div>
    </el-container>
</template>
    
<script>
import { ElMessage } from "element-plus"
export default {
    name: "OnSaleView",

    data() {
        return {
            items: [],
            loading: true
        }
    },
    methods: {
        toFixed2(str) {
            let num = Number(str);
            return isNaN(num) ? str : num.toFixed(2);
        },
        withdraw(index) {
            this.$http.post("/api/withdrawOnsale", {
                item_id: this.items[index].id,
            }).then().catch(error => {
                ElMessage({ message: error, type: "error" })
            })
            this.show = false;
            ElMessage({ message: "撤回成功", type: "success" })
            this.items.splice(index, 1);
        }
    },
    mounted() {
        this.$http.post('/api/getOnsale', {
            user_id: this.$store.getters.status.userid,
        }).then(res => {
            this.items = res.data.items
        }).catch(error => {
            ElMessage({ message: error, type: "error" })
        })
        this.loading = false
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
    word-break: break-all;
}

.card {
    height: 200px;
    border-radius: 30px;
}

.image {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  width: auto;
}

.list-item {
    transition: all 0.5s ease;
}
.button {
    margin-left: 50px;
    margin-right: 20px;
}
</style> 