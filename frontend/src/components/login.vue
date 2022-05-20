<template>
<html>
    <body>
    <div class="jumbotron center">
        <h1 class="header center" style="text-align:center;color:#6c6565">Login Page</h1>   
        <form @submit.prevent="login" class="container col-sm-4 center border padding" style="background:white; padding:10px">

            <div class="form-group" >
                <label for="exampleInputEmail1">Email address</label>
                <input v-model="email" type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
                <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">Password</label>
                <input v-model="password" type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
            </div>            
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
    </body>
</html>
</template>

<script>
import axios from 'axios'
export default {
        name : 'login',
        
        data (){
            return {
                email : "",
                password : ""
            }
        },
        methods : {
            login(event){
                const path  = 'http://localhost:5000/login'; 
                let userDetail = {
                    username : this.email,
                    password : this.password
                }               
                axios.post(path, new Blob([JSON.stringify(userDetail)], { type: 'application/json'}))
                .then((res)=>{
                    window.location = res.data == 'True' ? "\download" : window.location
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
            
        }
    }

</script>