<template>
    <div>
        <div class="jumbotron header">This is Uploading Service</div>
        
            <form @submit.prevent="uploadfile" class="form-group center" method="post" enctype="multipart/form-data">
                <input @change="getFileName" type="file" name="photos" class="form-control-file" multiple />
                <input type="submit" name="submit Form" id="" />
                <!-- <button class="btn btn-primary" name="photos" @click="uploadfile" >Upload File</button> -->
            </form>
            
        
    </div>

    
</template>

<script>
import axios from 'axios'
export default {
        name : 'Upload',
        
        data (){
            return {
                msg : "Hello this is shark",
                files : []
            }
        },
        methods : {
            getFileName(event){
                this.files.splice(0,this.files.length)
                this.files.push(...event.target.files);
            },
            uploadfile(){
                const path  = 'http://localhost:5000/uploadImage';
                var formdata = new FormData();
                this.files.forEach(file => {
                    formdata.append("photos", file, file.name)
                });
                axios.post(path,formdata)
                .then((res)=>{
                    return res;
                })
                .catch((err)=>{
                    return err;
                })
            },
            getResponse(){
                const path  = 'http://localhost:5000/uploadImageService';
                axios.get(path)
                .then((res) =>{
                    console.log(res.data);
                    this.msg = res.data;
                })
                .catch((err) => {
                    console.log(err)
                })
            }
        },
            created(){
                this.getResponse();
            }
    }

</script>