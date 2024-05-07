<template>
  <div>
    <transition name="slide-fade">
      <img class="display-image" v-if="showImage" :src="image" alt="Server Image" :key="currentIndex">
    </transition> 
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'

const image = ref('') // 画像のURLを格納するリファレンス
let currentIndex = 0; // 現在の画像のインデックス
const showImage = ref(false); // 画像を表示するかどうかのフラグ
const interval = 8000; // 画像を切り替える間隔
const images = ref([]); // 画像の配列

// コンポーネントがマウントされたときに画像を取得して表示する
onMounted(() => {
  // サーバーから画像の配列を取得するためのリクエストを送信
  fetch('http://127.0.0.1:8000')
    .then(response => {
      if (!response.ok) {
        throw new Error('Failed to fetch images');
      }
      // レスポンスから JSON データを取得
      return response.json();
    })
    .then(data => {
      // 画像の配列を更新
      images.value = data.files.map(file => `http://localhost:8000/uploads/${file}`);
      // 最初の画像を表示
      image.value = images.value[currentIndex];
      // 8秒ごとに次の画像を表示
      setInterval(() => {
        currentIndex = (currentIndex + 1) % images.value.length;
        image.value = images.value[currentIndex];
      }, interval);
    })
    .catch(error => {
      console.error('Error fetching images:', error);
    });
})

// 監視: imageの変更を監視し、新しい画像が読み込まれた後に古い画像を表示する
watch(image, () => {
  showImage.value = true;
  setTimeout(() => {
    showImage.value = false;
  }, interval - 750);
})
</script>

<style>
.display-image {
  max-width: 100%;
  max-height: calc(100% - 60px); /* 画像の高さを画面の高さからヘッダーの高さを引いた値に制限 */
  object-fit: contain;
  object-position: center;
}

.slide-fade-enter-active {
  transition: opacity 0.5s ease-out, transform 0.5s ease-out;
}

.slide-fade-leave-active {
  transition: opacity 0.5s ease-out, transform 0.5s ease-out;
}

.slide-fade-enter-from, .slide-fade-leave-to {
  opacity: 0;
  transform: translateX(-20px);
}
</style>
