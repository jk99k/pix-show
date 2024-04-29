<template>
    <!-- <button @click="handleClick" class="cool-button">Click me</button> -->

    <label v-if="!value" class="upload-content-space user-photo default">
        <input ref="file" class="file-button" type="file" @change="upload" />
        Do Upload
    </label>

    <div>
        <label class="upload-content-space user-photo">
            <input ref="file" class="file-button" type="file" @change="upload" />
            <img class="user-photo-image" :src="value" />
        </label>
    </div>
</template>
  
<script>
  export default {
    name: 'UploadButton',
    props: {
        value: {
            type: String,
            default: NonNullable
        }
    },
    methods: {
    //   handleClick() {
    //     console.log('Button clicked!');
    //   }

        async upload(event) {
            const files = event.target.files || event.dataTransfer.files;
            const file = files[0];

            if (this.checkFile(file)) {
                const picture = await this.getBase64(file);

                // フォームデータを作成
                const formData = new FormData();
                formData.append('image', file); // 'image' はサーバー側でファイルを受け取るためのキー名

                // サーバーにフォームデータを送信
                try {
                    const response = await fetch('/upload', 
                    {
                        method: 'POST',
                        body: formData
                    });

                    if (!response.ok) {
                        throw new Error('Upload failed');
                    }

                    // アップロードが成功した場合、サーバーから返された画像の URL を取得して親コンポーネントに渡す
                    const imageURL = await response.text();
                    this.$emit('input', imageURL);
                } catch (error) {
                    console.error('Upload error:', error);
                }
            }
        },
        getBase64(file){
            return new Promise((resolve, reject) => {
                const reader = new FileReader()
                reader.readAsDataURL(file)
                reader.onload = () => resolve(reader.result)
                reader.onerror = error => reject(error)
            })
        },
        checkFile(file){
            let result = true
            const SIZE_LIMIT = 5000000
            
            if(!file){
                result = false
            }

            if(file.type !== 'image/jpeg' && file.type !== 'image/png'){
                result = false
            }

            if(file.size > SIZE_LIMIT){
                result = false
            }
            return result
        }
    }
  }
</script>
  
<style>
  .cool-button {
/*     
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
    */

    border-radius: 39px;
    background: #D9D9D9;
    width: 221px;
    height: 225px;
  }
  
  .cool-button:hover {
    background-color: #45a049; /* Darker Green */
  }
</style>
  