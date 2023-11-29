<template>
  <el-container direction="vertical" v-loading="loading">
    <div v-if="items.length === 0 && this.loading === false"
      style="display: flex;justify-content: center;align-items: center;">
      <h3 style=" color: rgb(126, 126, 126);font-size: 22px;">还没有已购买的书籍哦</h3>
    </div>
    <transition-group name="list" tag="div">
      <div v-for="(item, index) in items" :key="item.id" class="list-item">
        <el-card class="card">
          <el-row style="  display: flex;align-items: center;height: 160px;">
            <el-col :span="4" class="centered-col" style="height: 160px;">
              <el-image :src="item.image" class="image"></el-image>
            </el-col>
            <el-col :span="4" class="centered-col">
              <h3>{{ item.name }}</h3>
            </el-col>
            <el-col :span="1" class="centered-col">
            </el-col>
            <el-col :span="7" class="centered-col">
              {{ item.intro }}
            </el-col>
            <el-col :span="2" class="centered-col">
              <h3>¥{{ toFixed2(item.price) }}</h3>
            </el-col>
            <el-col :span="3" class="centered-col">
              <h3>{{ item.sellerName }}</h3>
            </el-col>
            <el-col :span="3" class="centered-col">
              <h3>联系方式:<br>{{ item.phoneNum }}</h3>
            </el-col>
          </el-row>
        </el-card>
        <div style="display: flex; justify-content: flex-end; margin-top: 20px;">
          <el-popconfirm confirm-button-text="确认" cancel-button-text="取消" title="确认收货？" @confirm="showComment = true">
            <template #reference>
              <el-button type="primary" class="button" size="large">确认收货</el-button>
            </template>
          </el-popconfirm>
          <el-dialog v-model="showComment" title="请添加对卖家的评论" width="30%" >
            <el-input v-model="comment" placeholder="请输入评论内容" />
            <div style="display:flex;justify-content: end;padding-top: 10px;" :modal="false">
              <el-button type="primary" class=“button” size=“large” @click="confirmReceive(index)">确认</el-button>
            </div>
          </el-dialog>
          <el-button type="success" class="button" size="large" @click="show = true">发送消息</el-button>
          <el-dialog v-model="show" title="向卖家发送消息" width="30%" >
            <el-input v-model="msg" placeholder="请输入消息内容" />
            <div style="display:flex;justify-content: end;padding-top: 10px;">
              <el-button type="primary" class="button" size=“large” @click="sendMsg(index)">确认</el-button>
            </div>
          </el-dialog>
        </div>
        <el-divider></el-divider>
      </div>
    </transition-group>
  </el-container>
</template>
  
<script>
import { ElMessage } from "element-plus"
export default {
  name: "BoughtView",

  data() {
    return {
      show: false,
      showComment: false,
      msg: "",
      comment: "",
      items: [],
      loading: true,
    }
  },
  methods: {
    toFixed2(str) {
      let num = Number(str);
      return isNaN(num) ? str : num.toFixed(2);
    },
    confirmReceive(index) {
      if (this.comment === "") {
        ElMessage({ message: "评论不能为空", type: "error" })
        return;
      }
      this.$http.post("/api/confirm", {
        item_id: this.items[index].id,
        content: this.comment
      }).then().catch(error => {
        ElMessage({ message: error, type: "error" })
      })
      this.showComment = false;
      this.comment = "";
      ElMessage({ message: "确认收货成功", type: "success" })
      this.items.splice(index, 1);
    },
    sendMsg(index) {
      if (this.msg === "") {
        ElMessage({ message: "消息内容不能为空", type: "error" })
        return;
      }
      this.$http.post("/api/sendMsg", {
        item_id: this.items[index].id,
        content: this.msg,
        from_which: 0
      }).then().catch(error => {
        ElMessage({ message: error, type: "error" })
      })
      this.show = false;
      this.msg = "";
      ElMessage({ message: "发送消息成功", type: "success" })
    }
  },
  mounted() {
    this.$http.post('/api/getbought', {
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