<template>
    <button @click="handleClick" class="cool-button">Click me</button>
</template>
  
<script>
  export default {
    methods: {
      handleClick() {
        console.log('Button clicked!');
      }
    }
  }
</script>
  
<style>
  .cool-button {
    background-color: green;
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    transition-duration: 0.4s;
    cursor: pointer;
    border-radius: 8px;
  }
  
  .cool-button:hover {
    background-color: #45a049; /* Darker Green */
  }
</style>
  