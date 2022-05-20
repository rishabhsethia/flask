<template>
    <html>
        <head>

        </head>
        <body>
            <div class="Container jumbotron header text-center h1">
                User DashBoard
            </div>
            <div class="container">
                <div class="row center">
                    <div class="col-sm-12 text-center header3">
                        <a href="http://localhost:8080/upload">Upload Images</a>
                    </div> 
                </div> 
            </div>
                <div class="row">
                    <div class="col-sm-11">
                    <div class="col-sm-6 col-md-4 col-lg-3 border" v-for="(url,index) in blobUrlList" v-bind:key="index">
                    <figure>
                        <img v-bind:src="url" alt="url" title="imges">                        
                    </figure>
                    </div>
                    </div>
                </div> 
        </body>
    </html>
</template>


<script>
import axios from 'axios'
export default {
        name : 'download',
        
        data (){
            return {
                blobUrlList : []
            }
        },
        methods : {            
            getResponse(){
                //todo buid the path to this download api
                const path  = 'http://localhost:5000/downloadImage';
                axios.get(path)
                .then((res) =>{
                    this.blobUrlList.push(...res.data)
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