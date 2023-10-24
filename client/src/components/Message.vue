<template>
    <el-container style="height: 100vh;">
        <el-header style="border-bottom: 1px solid lightgray;">
            <el-tabs v-model="activeTab">
                <el-tab-pane label="查看买家消息" name="buyer">
                    <transition-group name="list" tag="div">
                        <div v-for="(item, index) in  buyerMessages " :key="item.id" class="list-item">
                            <el-card>
                                <el-row :gutter="10">
                                    <el-col :span="22">
                                        <el-descriptions :column="1" border=true>
                                    <el-descriptions-item label="卖家姓名">{{ item.sellerName }}</el-descriptions-item>
                                    <el-descriptions-item label="电话号码">{{ item.phoneNum }}</el-descriptions-item>
                                    <el-descriptions-item label="内容">{{ item.content }}</el-descriptions-item>
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
                    <transition-group name="list" tag="div">
                        <div v-for="( item, index ) in  sellerMessages " :key="item.id" class="list-item">
                            <el-card>
                                <el-row :gutter="10">
                                    <el-col :span="22">
                                        <el-descriptions :column="1" border=true>
                                    <el-descriptions-item label="买家姓名">{{ item.sellerName }}</el-descriptions-item>
                                    <el-descriptions-item label="电话号码">{{ item.phoneNum }}</el-descriptions-item>
                                    <el-descriptions-item label="内容">{{ item.content }}</el-descriptions-item>
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
        </el-header>
        <el-header style="display:flex;align-items: center;justify-content: center; padding-top: 20px;">
            <el-button type="danger" @click="clearAllMessages">清除所有消息</el-button> </el-header>
    </el-container>
</template>
  
<script>
import Mock from 'mockjs';
import axios from 'axios';
Mock.mock('/api/getBuyerMessages', {
    'list|10-20': [{
        'content': '@ctitle(30, 100)',
        'phoneNum': '@ctitle(8,14)',
        'sellerName': '@ctitle(2,9)',
    }]
})
Mock.mock('/api/getSellerMessages', {
    'list|10-20': [{
        'content': '@ctitle(30, 100)',
        'phoneNum': '@ctitle(8,14)',
        'sellerName': '@ctitle(2,9)',
    }]
})
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
            this.buyerMessages.splice(index, 1);
        },
        removeSellerMessage(index) {
            this.sellerMessages.splice(index, 1);
        },
        clearAllMessages() {
            this.buyerMessages = [];
            this.sellerMessages = [];
        }
    },
    mounted() {
        axios.get('/api/getBuyerMessages').then(res => {
            this.buyerMessages = res.data.list
        }).catch(console.log("JI"))
        axios.get('/api/getSellerMessages').then(res => {
            this.sellerMessages = res.data.list
        }).catch(console.log("JI"))
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
}</style>