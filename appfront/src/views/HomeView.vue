<template>
  <div class="home">
    <el-row display="margin-top: 10px">
      <el-input
        v-model="input"
        placeholder="请输入书名"
        style="
          display: inline-table;
          width: 30%;
          float: left;
          margin-right: 10px;
        "
      >
      </el-input>
      <el-button
        type="primary"
        @click="addBook()"
        style="float: left; margin: 1px"
      >
        新增
      </el-button>
    </el-row>
    <el-row>
      <el-table :data="bookList" style="width: 100%; margin-top: 10px" border>
        <el-table-column prop="id" label="编号" min-width="100" align="center">
          <template scope="scope">{{ scope.row.pk }}</template>
        </el-table-column>
        <el-table-column
          prop="book_name"
          label="书名"
          min-width="100"
          align="center"
        >
          <template scope="scope">{{ scope.row.fields.book_name }}</template>
        </el-table-column>
        <el-table-column
          prop="add_time"
          label="添加时间"
          min-width="100"
          align="center"
        >
          <template scope="scope">{{
            formatTime(scope.row.fields.add_time)
          }}</template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
import axios from "axios";
axios.defaults.baseURL = "http://localhost:8000/api";
axios.defaults.headers.post["Content-Type"] = "application/json";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "home",
  data() {
    return {
      input: "",
      bookList: [],
    };
  },
  mounted: function () {
    this.showBooks();
  },
  methods: {
    addBook() {
      console.log(this.input);
      axios.get("add_book?book_name=" + this.input).then((response) => {
        console.log(response);
        let res = response.data;
        if (res["error_num"] === 0) {
          this.showBooks();
        } else {
          this.$message.error("新增书籍失败，请重试");
        }
        this.input = "";
      });
    },
    showBooks() {
      console.log("showBooks");
      axios.get("show_books").then((response) => {
        let res = response.data;
        console.log(res);
        if (res["error_num"] === 0) {
          this.bookList = res["list"];
        } else {
          this.$message.error("获取书籍列表失败，请重试");
          console.log(res["msg"]);
        }
      });
    },
    formatTime(origin) {
      let timestamp = Date.parse(origin);
      let date = new Date(timestamp);
      return (
        date.getFullYear() +
        "-" +
        (date.getMonth() + 1) +
        "-" +
        date.getDate() +
        " " +
        date.getHours() +
        ":" +
        date.getMinutes() +
        ":" +
        date.getSeconds()
      );
    },
  },
};
</script>

<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
