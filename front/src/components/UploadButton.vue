<template>
  <label v-if="!value" class="upload-content-space user-photo default">
      <input ref="file" class="file-button" type="file" @change="upload" />
      Upload
  </label>

  <div>
      <label class="upload-content-space user-photo">
          <input ref="file" class="file-button" type="file" @change="upload" />
          <img class="user-photo-image" :src="value" />
      </label>
  </div>
</template>
  
<script>
import API_URL from '../url';
  export default {
    name: 'UploadButton',
    props: {
        value: {
            type: String,
            default: ''
        }
    },

    methods: {
    //   handleClick() {
    //     console.log('Button clicked!');
    //   }

        async upload(event) {//ボタンを押すとchange eventを拾ってuproad methodが呼ばれる→event情報から取得したfile情報を取得・checkFile methodに渡してチェックする
            const files = event.target.files || event.dataTransfer.files;
            const file = files[0];

            if (this.checkFile(file)) {
                const picture = await this.getBase64(file);
                this.$emit('input', picture);

                // フォームデータを作成
                const formData = new FormData();
                formData.append('files', file); // 'image' はサーバー側でファイルを受け取るためのキー名

                // サーバーにフォームデータを送信
                try {
                    const response = await fetch(`${API_URL}`, 
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
        getBase64(file){//checkfileでfileデータが問題ないとされた時、ここでFileReaderのインスタンスメソッドを利用してエンコードをする
            return new Promise((resolve, reject) => {
                const reader = new FileReader()
                reader.readAsDataURL(file)
                reader.onload = () => resolve(reader.result)
                reader.onerror = error => reject(error)
            })
        },
        checkFile(file){//ファイルのサイズが5MBより大きいか小さいかで処理を分ける
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
  
<style scoped>
.user-photo {
  cursor: pointer;
  outline: none;
}

.user-photo.default {
  align-items: center;
  background-color: #0074fb;
  border: 1px solid #0051b0;
  border-radius: 2px;
  box-sizing: border-box;
  display: inline-flex;
  font-weight: 600;
  justify-content: center;
  letter-spacing: 0.3px;
  color: #fff;
  height: 4rem;
  padding: 0 1.6rem;
  max-width: 177px;
}

.user-photo.default:hover {
  background-color: #4c9dfc;
}

.user-photo.default:active {
  background-color: #0051b0;
}

.user-photo-image {
  max-width: 85px;
  display: block;
}

.user-photo-image:hover {
  opacity: 0.8;
}

.file-button {
  display: none;
}

.uploaded {
  align-items: center;
  display: flex;
}
</style>
  