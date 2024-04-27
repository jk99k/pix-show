<template>
    <img :src="image" alt="">
</template>

<script>
import { ref, defineComponent, onMounted } from 'vue'

export default  defineComponent({
    setup() {
        // refでリアクティブにして値を更新されると反映
        let image = ref('')
    
        onMounted(async () => {
            // サーバーから非同期で画像URLを取得
            image.value = await getImage()
        })
    
        return {
            image
        }
    }
})
</script>

<style>

</style>