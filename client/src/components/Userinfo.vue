<template>
    <div style="display: flex; justify-content: center; padding-top: 10vh; height: 100vh;">
        <el-card style="width: 70vw;height: 18vw;">
            <el-descriptions direction="vertical" :column="4" :size="size" border>
                <el-descriptions-item label="账号">{{ userinfo.username }}</el-descriptions-item>
                <el-descriptions-item label="电话号码">{{ userinfo.phonenum }}</el-descriptions-item>
                <el-descriptions-item label="邮箱" :span="2">{{ userinfo.email }}</el-descriptions-item>
                <el-descriptions-item label="所在校区">{{ userinfo.campus }}</el-descriptions-item>
                <el-descriptions-item label="详细地址">{{ userinfo.address }}</el-descriptions-item>
                <el-descriptions-item label="账户余额">{{ toFixed2(userinfo.money) }}</el-descriptions-item>
            </el-descriptions>
            <div style="padding-top: 30px;">
                <el-button type="primary" class=“button” size=“large” style="align-items:end"
                    @click="modifyphonenum = true">修改电话号码</el-button>
                <el-button type="primary" class=“button” size=“large” style="align-items:end"
                    @click="modifyemail = true">修改邮箱</el-button>
                <el-button type="primary" class=“button” size=“large” style="align-items:end"
                    @click="modifycampus = true">修改所在校区</el-button>
                <el-button type="primary" class=“button” size=“large” style="align-items:end"
                    @click="modifyaddress = true">修改详细地址</el-button>
                <el-button type="primary" class=“button” size=“large” style="align-items:end"
                    @click="modifypassword = true">修改密码</el-button>
                <el-button type="primary" class=“button” size=“large” style="align-items:end"
                    @click="modifymoney = true">充值账户余额</el-button>
            </div>
        </el-card>
    </div>
    <el-dialog v-model="modifyphonenum" title="修改电话号码" width="30%">
        <el-input v-model="input" placeholder="请输入新的电话号码" />
        <div style="display:flex;justify-content: end;padding-top: 10px;">
            <el-button type="primary" class=“button” size=“large” @click="modify('phonenum')">确认修改</el-button>
        </div>
    </el-dialog>
    <el-dialog v-model="modifyemail" title="修改邮箱" width="30%">
        <el-input v-model="input" placeholder="请输入新的邮箱" />
        <div style="display:flex;justify-content: end;padding-top: 10px;">
            <el-button type="primary" class=“button” size=“large” @click="modify('email')">确认修改</el-button>
        </div>
    </el-dialog>
    <el-dialog v-model="modifymoney" title="充值账户余额" width="30%">
        <el-input v-model="input" placeholder="请输入要充值的数额" />
        <div style="display:flex;justify-content: end;padding-top: 10px;">
            <el-button type="primary" class=“button” size=“large” @click="modify('money')">确认充值</el-button>
        </div>
    </el-dialog>
    <el-dialog v-model="modifycampus" title="修改所在校区" width="30%">
        <el-input v-model="input" placeholder="请输入所在校区" />
        <div style="display:flex;justify-content: end;padding-top: 10px;">
            <el-button type="primary" class=“button” size=“large” @click="modify('campus')">确认修改</el-button>
        </div>
    </el-dialog>
    <el-dialog v-model="modifyaddress" title="修改详细地址" width="30%">
        <el-input v-model="input" placeholder="请输入新的地址" />
        <div style="display:flex;justify-content: end;padding-top: 10px;">
            <el-button type="primary" class=“button” size=“large” @click="modify('address')">确认修改</el-button>
        </div>
    </el-dialog>
    <el-dialog v-model="modifypassword" title="修改密码" width="30%">
        <el-input v-model="oldPassword" type="password" placeholder="请输入旧密码" />
        <el-input v-model="input" type="password" placeholder="请输入新的密码" style="padding-top: 10px;" />
        <el-input v-model="confirm" type="password" placeholder="确认新的密码" style="padding-top: 10px;" />
        <div style="display:flex;justify-content: end;padding-top: 10px;">
            <el-button type="primary" class=“button” size=“large” @click="modify('password')">确认修改</el-button>
        </div>
    </el-dialog>
</template>
<script>
import { ElMessage } from 'element-plus';
export default {
    name: "userInfo",
    data() {
        return {
            userinfo: {
                username: "faqfaq",
                phonenum: "13586012465",
                email: "2654133250@qq.com",
                campus: "学院路校区",
                address: "大运村",
                money: 114.54545
            },
            modifyphonenum: false,
            modifypassword: false,
            modifyemail: false,
            modifycampus: false,
            modifyaddress: false,
            modifymoney: false,
            input: "",
            confirm: "",
            oldPassword: ""
        }
    },
    methods: {
        toFixed2(str) {
            let num = Number(str);
            return isNaN(num) ? str : num.toFixed(2);
        },
        modify(which) {
            if (which === "password") {
                if (this.input != this.confirm) {
                    ElMessage({ message: "确认密码与新密码不一致", type: "error" });
                    return;
                }
                this.$http.post("/api/modifypassword", {
                    user_id: this.$store.getters.status.userid,
                    old_pw: this.oldPassword,
                    new_pw: this.input
                }).then(response => {
                    if (response.data.success === true) {
                        ElMessage({ message: "修改成功", type: "success" })
                    }
                    else {
                        ElMessage({ message: "修改失败，请确认旧密码是否正确", type: "error" })
                    }
                }).catch(error => {
                    ElMessage({ message: error, type: "error" })
                    return;
                });
            }
            else {
                if (which === "phonenum") {
                    this.userinfo.phonenum = this.input;
                    this.modifyphonenum = false;
                }
                else if (which === "email") {
                    this.userinfo.email = this.input;
                    this.modifyemail = false;
                }
                else if (which === "campus") {
                    this.userinfo.campus = this.input;
                    this.modifycampus = false;
                }
                else if (which === "address") {
                    this.userinfo.address = this.input;
                    this.modifyaddress = false;
                }
                else if (which === "money") {
                    var num = parseFloat(this.input)
                    if (isNaN(num)) {
                        ElMessage({ message: "请输入正确的数额", type: "error" })
                    }
                    else {
                        this.userinfo.money = parseFloat(this.userinfo.money) + num;
                        this.modifymoney = false;
                        this.input = this.userinfo.money
                    }
                }
                this.$http.post("/api/modifyinfo", {
                    user_id: this.$store.getters.status.userid,
                    modify_which: which,
                    modify_content: this.input
                }).then().catch(error => {
                    ElMessage({ message: error, type: "error" })
                    return;
                });
                ElMessage({ message: "修改成功", type: "success" })
            }
            this.input = "";
            this.confirm = "";
            this.oldPassword = "";
        }
    },
    mounted() {
        this.$http.post('/api/getuserinfo', {
            user_id: this.$store.getters.status.userid,
        }).then(response => {
            this.userinfo = response.data.userinfo
        }).catch(error => {
            ElMessage({ message: error, type: "error" })
        })
    }
}
</script>
<style></style>