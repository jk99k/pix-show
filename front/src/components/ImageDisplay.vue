<template>
  <div>
    <transition name="slide-fade">
      <img v-if="showImage" :src="image" alt="Server Image" :key="currentIndex">
    </transition> 
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'

const image = ref('') // 画像のURLを格納するリファレンス
let currentIndex = 0; // 現在の画像のインデックス
const showImage = ref(false); // 画像を表示するかどうかのフラグ
const interval = 5000; // 画像を切り替える間隔

// サーバーから画像を取得して表示する関数
const fetchAndDisplayImage = () => {
  try {
    // サーバーから画像のURLを取得するためのリクエストを送信
    fetch('http://127.0.0.1:8000')
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch image');
        }
        // レスポンスから JSON データを取得
        return response.json();
      })
      .then(data => {
        // JSON データから次の画像の URL を取得してセット
        const nextImageUrl = data.files[currentIndex];
        image.value = `http://localhost:8000/uploads/${nextImageUrl}`;
        // 次の画像のインデックスを更新する
        currentIndex = (currentIndex + 1) % data.files.length;
      })
      .catch(error => {
        console.error('Error fetching image:', error);
      });
  } catch (error) {
    console.error('Error fetching image:', error);
  }
}

// 監視: imageの変更を監視し、新しい画像が読み込まれた後に古い画像を表示する
watch(image, () => {
  showImage.value = true;
  setTimeout(() => {
    showImage.value = false;
  }, interval - 750);
})

// コンポーネントがマウントされたときに画像を取得して表示する
onMounted(() => {
  fetchAndDisplayImage();
  // 8秒ごとに次の画像を取得して表示する
  setInterval(fetchAndDisplayImage, interval);
})
</script>

<style>
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

