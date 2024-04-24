<template>
  <!-- ぞのはここにページのレイアウトを書く -->
  <div>
    <header>
      <div class="menu-button">&#9776;</div>
      <h1>PixShow</h1>
      <UploadButton/>
    </header>
    <!--https://img.freepik.com/free-photo/black-man-angry-expression_1194-2570.jpg-->
    <div class="content">
      <img
        src="https://i.daily.jp/gossip/2018/12/20/Images/f_11919224.jpg"
        alt="Image Description"
      />
    </div>
  </div>
</template>

<script>
import UploadButton from "./components/UploadButton.vue";

export default {
  name: "App",
  components: {
    UploadButton,
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
        background-color: #272727;
        color: #fff;
        text-align: center;
        padding: 1%;
        display: flex;
        justify-content: space-between;
        align-items: center;
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
        display: flex;
        justify-content: center; /* コンテナ要素を横方向に中央揃え */
        align-items: center; /* コンテナ要素を垂直方向に中央揃え */
        height: calc(100vh - 100px); /* ヘッダーを除いた部分の高さ */
      }

      img {
        width: 100%;
        height: 100%;
        object-fit: contain;
        object-position: center;
      }
</style>
