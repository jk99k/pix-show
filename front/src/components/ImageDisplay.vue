<template>
    <img :src="image" alt="">
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  
  const image = ref('') // 画像のURLを格納するリファレンス
  
  // サーバーから画像を取得する関数
  const fetchImage = () => {
    const imageUrl = 'http://127.0.0.1:8000/uploads/082_Original.jpg' // 画像のURLを指定
    image.value = imageUrl // 画像のURLをセット
  }
  
  // コンポーネントがマウントされたときに画像を取得する
  onMounted(() => {
    fetchImage();
  })
  </script>
  