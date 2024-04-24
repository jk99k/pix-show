<template>
    <button @click="handleClick">
        Click me
    </button>
</template>
  
<script>
    export default {
        methods: {
            handleClick() {
            // ボタンがクリックされたときの処理を記述する
            console.log('Button clicked!');
            }
        }
    }
</script>
  
<style>
  /* ボタンのスタイルを記述する */
  button {
    background-color: yellowgreen;
    color: purple;
    padding: 10px 20px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
  }
</style>
  