<template>
  <!-- ぞのはここにページのレイアウトを書く -->
  <div>
    <header>
      <div class="menu-button">&#9776;</div>      <!-- '&#9776;' ハンバーガーアイコン -->
      <h1>PixShow</h1>
      <UploadButton/>
    </header>
    <!--https://img.freepik.com/free-photo/black-man-angry-expression_1194-2570.jpg-->
    <div class="content">
      <ImageDisplay/>
    </div>
  </div>
</template>

<script>
import ImageDisplay from "./components/ImageDisplay.vue";
import UploadButton from "./components/UploadButton.vue";

export default {
  name: "App",
  components: {
    UploadButton,
    ImageDisplay,
},
};
</script>

<style>
body,
html {
  overflow: hidden;
  background-color: #05294f;
  text-align: center;
  margin: 0;
  padding: 0;
}

header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: #272727;
  color: #fff;
  text-align: center;
  padding: 1%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 1000;
}

.menu-button {
  font-size: 28px;
  cursor: pointer;
  margin-left: 1%;
}

.upload-button {
  background-color: #ffffff;
  color: #000000;
  border: none;
  padding: 6px 9px;
  border-radius: 5px;
  cursor: pointer;
  margin-right: 1%;
}

.upload-button:hover {
  background-color: #bdbdbd;
  color: #000000;
}

.content {
  margin-top: 60px; /* ヘッダーの高さ */
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 60px); /* 画面の高さからヘッダーの高さを引いた値 */
}

</style>
