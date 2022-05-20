import Vue from "vue";
import VueRouter from "vue-router";
// import HomeView from "../views/HomeView.vue";
import upload from '../components/upload.vue'
import Login from '../components/login.vue'
import download from '../components/download.vue'

Vue.use(VueRouter);

const routes = [
  {
    path : '/',
    name : Login,
    component : Login
  } ,
  {
    path : '/upload',
    name : upload,
    component : upload
  } ,
  {
    path : '/download',
    name : download,
    component : download
  } 
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
}); 

export default router;
