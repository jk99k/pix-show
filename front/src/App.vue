<template>
  <!-- ぞのはここにページのレイアウトを書く -->
  <div>
    <header>
      <h1>PixShow</h1>
      <p>Please</p>
      <a href="UploadButton.vue">upload</a> <!-- 山代のUploadButton.vueはここ? -->
      <p>an image.</p>
    </header>

    <div class="image-container">
      <!-- 1段目 -->
      <div class="image-upper">
        <img
          src="https://img.freepik.com/free-photo/black-man-angry-expression_1194-2570.jpg"
          alt="Left Image Description"
        />
        <img
          src="https://img.freepik.com/free-photo/black-man-angry-expression_1194-2570.jpg"
          alt="Right Image Description"
        />
      </div>
    </div>

    <div class="image-container">
      <!-- 2段目 -->
      <div class="image-middle">
        <img
          src="https://img.freepik.com/free-photo/black-man-angry-expression_1194-2570.jpg"
          alt="Left Image Description"
        />
        <img
          src="https://img.freepik.com/free-photo/black-man-angry-expression_1194-2570.jpg"
          alt="Center Image Description"
        />
        <img
          src="https://img.freepik.com/free-photo/black-man-angry-expression_1194-2570.jpg"
          alt="Right Image Description"
        />
      </div>
    </div>

    <div class="image-container">
      <!-- 3段目 -->
      <div class="image-lower">
        <img
          src="https://img.freepik.com/free-photo/black-man-angry-expression_1194-2570.jpg"
          alt="Left Image Description"
        />
        <img
          src="https://img.freepik.com/free-photo/black-man-angry-expression_1194-2570.jpg"
          alt="Right Image Description"
        />
      </div>
    </div>
    <UploadButton />
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
body {
  background-color: #000000;
  text-align: center;
}

header {
  background-color: #272727;
  color: #fff;
  padding: 5px;
  text-align: center;
  p,
  a {
    display: inline;
  }
  a {
    color: #fc7bef;
  }
}

img {
  width: 240px;
  height: 240px;
  object-fit: cover;
  object-position: center;
  border-radius: 100%;
  transition: transform 0.3s; /* 変形のアニメーション効果を追加 */
}
.image-container {
  display: flex;
  justify-content: center;
  overflow-x: auto; /* 横方向のスクロールを有効にする */
  white-space: nowrap;
}

.image-upper img,
.image-middle img,
.image-lower img {
  margin: 0 24px;
  margin-top: 24px;
  margin-bottom: 24px;
}

/* 画像にマウスが触れたときの変形 */
img:hover {
  transform: scale(1.2); /* 画像を1.2倍に拡大 */
}
</style>
