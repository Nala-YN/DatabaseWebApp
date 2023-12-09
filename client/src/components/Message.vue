<template>
    <el-container style="height: 100vh;">
        <el-header style="border-bottom: 1px solid lightgray; height: 100vh;">
            <el-tabs v-model="activeTab" >
                <el-tab-pane label="查看买家消息" name="buyer">
                    <div v-if="this.buyerMessages.length === 0"
                        style="display:flex;align-items: center;justify-content: center;">
                        <h3 style=" color: rgb(126, 126, 126);font-size: 22px;">还没有收到消息哦</h3>
                    </div>
                    <transition-group name="list" tag="div">
                        <div v-for="(item, index) in  buyerMessages " :key="item.id" class="list-item">
                            <el-card>
                                <el-row :gutter="10">
                                    <el-col :span="22">
                                        <el-descriptions :column="3" border=true size="large">
                                            <el-descriptions-item label="买家昵称">{{ item.buyerName }}</el-descriptions-item>
                                            <el-descriptions-item label="电话号码">{{ item.phoneNum }}</el-descriptions-item>
                                            <el-descriptions-item label="发送时间">{{ item.year }}-{{ item.month }}-{{ item.day
                                            }}</el-descriptions-item>
                                            <el-descriptions-item label="消息内容">{{ item.content }}</el-descriptions-item>
                                        </el-descriptions>
                                    </el-col>
                                    <el-col :span="2" style="display: flex; align-items: center;">
                                        <el-button type="danger" round class=“button” size=“large” style="align-items:end"
                                            @click="removeBuyerMessage(index)">删除消息</el-button>
                                    </el-col>
                                </el-row>
                            </el-card>
                            <el-divider></el-divider>
                        </div>
                    </transition-group>
                </el-tab-pane>
                <el-tab-pane label="查看卖家消息" name="seller">
                    <div v-if="this.sellerMessages.length === 0"
                        style="display:flex;align-items: center;justify-content: center;">
                        <h3 style=" color: rgb(126, 126, 126);font-size: 22px;">还没有收到消息哦</h3>
                    </div>
                    <transition-group name="list" tag="div">
                        <div v-for="( item, index ) in  sellerMessages " :key="item.id" class="list-item">
                            <el-card>
                                <el-row :gutter="10">
                                    <el-col :span="22">
                                        <el-descriptions :column="3" border=true size="large">
                                            <el-descriptions-item label="卖家昵称">{{ item.sellerName }}</el-descriptions-item>
                                            <el-descriptions-item label="电话号码">{{ item.phoneNum }}</el-descriptions-item>
                                            <el-descriptions-item label="发送时间">{{ item.year }}-{{ item.month }}-{{ item.day
                                            }}</el-descriptions-item>
                                            <el-descriptions-item label="消息内容">{{ item.content }}</el-descriptions-item>
                                        </el-descriptions>
                                    </el-col>
                                    <el-col :span="2" style="display: flex; align-items: center;">
                                        <el-button type="danger" round class=“button” size=“large” style="align-items:end"
                                            @click="removeSellerMessage(index)">删除消息</el-button>
                                    </el-col>
                                </el-row>
                            </el-card>
                            <el-divider></el-divider>
                        </div>
                    </transition-group>
                </el-tab-pane>
            </el-tabs>
            <el-header style="display:flex;align-items: center;justify-content: center; padding-top: 20px;">
            <el-button type="danger" @click="clearAllMessages">清除所有消息</el-button> </el-header>
        </el-header>
    </el-container>
</template>
  
<script>
import { ElMessage } from 'element-plus'
export default {
    name: "MsgView",
    data() {
        return {
            activeTab: 'buyer',
            buyerMessages: [],
            sellerMessages: []
        }
    },
    methods: {
        removeBuyerMessage(index) {
            this.$http.post("/api/rmMsg",{
                msg_id:this.buyerMessages[index].msg_id
            }).catch(error=>{
                ElMessage({ message: error, type: "error" })
            })
            this.buyerMessages.splice(index, 1);
        },
        removeSellerMessage(index) {
            this.$http.post("/api/rmMsg",{
                msg_id:this.sellerMessages[index].msg_id
            }).catch(error=>{
                ElMessage({ message: error, type: "error" })
            })
            this.sellerMessages.splice(index, 1);
        },
        clearAllMessages() {
            if(this.buyerMessages.length===0&&this.sellerMessages.length===0){
                ElMessage({ message: "没有可以删除的消息", type: "error" })
            }
            this.$http.post("/api/rmUserMsg",{
                user_id: this.$store.getters.status.userid,
            }).catch(error=>{
                ElMessage({ message: error, type: "error" })
            })
            this.buyerMessages = [];
            this.sellerMessages = [];
        }
    },
    mounted() {
        this.$http.post('/api/getMsgs', {
            user_id: this.$store.getters.status.userid
        }).then(response => {
            this.buyerMessages = response.data.buyerMsgs;
            this.sellerMessages = response.data.sellerMsgs;
        }).catch(error => {
            ElMessage({ message: error, type: "error" })
        })
    }
};
</script>
  
<style scoped>
.text.item {
    margin-bottom: 20px;
}

.el-header {
    height: auto;
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
}
</style>