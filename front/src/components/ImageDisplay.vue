<template>
    <div>
      <!-- 画像を表示する -->
      <img :src="image" alt="Server Image">
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  
  const image = ref('') // 画像のURLを格納するリファレンス
  let currentIndex = 0; // 現在の画像のインデックス
  
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
  
  // コンポーネントがマウントされたときに画像を取得して表示する
  onMounted(() => {
    fetchAndDisplayImage();
    // 5秒ごとに次の画像を取得して表示する
    setInterval(fetchAndDisplayImage, 5000);
  })
  </script>
  