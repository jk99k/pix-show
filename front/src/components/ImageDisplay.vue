<template>
    <div>
      <!-- 画像を表示する -->
      <img :src="image" alt="Server Image">
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  
  const image = ref('') // 画像のURLを格納するリファレンス
  
  // サーバーから画像を取得する関数
  const fetchImage = () => {
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
            console.log(data)
          // JSON データから画像の URL を取得してセット
          const imageUrl = data.files[1];
          image.value = `http://localhost:8000/uploads/${imageUrl}`;
        })
        .catch(error => {
          console.error('Error fetching image:', error);
        });
    } catch (error) {
      console.error('Error fetching image:', error);
    }
  }
  
  // コンポーネントがマウントされたときに画像を取得する
  onMounted(() => {
    fetchImage();
  })
  </script>
  